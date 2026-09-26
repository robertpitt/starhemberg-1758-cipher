#!/usr/bin/env python3
"""Replay supported local segmentations without inventing switching rules.

Python 3.9+, standard library only. By default check the saved reports; --build
regenerates them. Untabled runs are candidates in both supplied tables. Only
explicit, source-located hypotheses may cross recorded separators. Every source
character is preserved in the accounting, including uncertain digits and glyphs.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import unicodedata

import analyze_boundaries as boundaries
import audit

ROOT = Path(__file__).resolve().parent
EVENT = re.compile(r'[0-9]+|\[[^\]]*\]|<G[0-9]+>|[,\.]|\s+')


class Source:
    def __init__(self, rows):
        self.rows = rows
        self.text = '\n'.join(row['text'] for row in rows)
        self.starts = []
        self.by_id = {}
        offset = 0
        for row in rows:
            self.starts.append(offset)
            self.by_id[row['id']] = (offset, len(row['text']))
            offset += len(row['text']) + 1

    def location(self, offset):
        index = bisect_right(self.starts, offset) - 1
        return {'row': self.rows[index]['id'], 'character': offset-self.starts[index]+1}

    def offset(self, location):
        start, length = self.by_id[location['row']]
        char = location['character']
        if not isinstance(char, int) or not 1 <= char <= length:
            raise ValueError('Invalid source coordinate: ' + repr(location))
        return start + char - 1


def events(text):
    result, end = [], 0
    for m in EVENT.finditer(text):
        if m.start() != end:
            raise ValueError('Unrecognized source characters: '+repr(text[end:m.start()]))
        result.append(m)
        end = m.end()
    if end != len(text):
        raise ValueError('Unrecognized source characters: '+repr(text[end:]))
    return result


def marked_value(value):
    return value == '?' or any(symbol in value for symbol in ('/', '?', '('))


def materialize(source, start, end, table, codes, keys, metadata, selection):
    raw = source.text[start:end]
    matches = events(raw)
    # This is the only code path that may cross separators, and its caller must
    # supply an explicitly located hypothesis or an unseparated numeric block.
    if any(m.group().startswith('<') or (m.group().startswith('[') and m.group() != '[,?]')
           for m in matches):
        raise ValueError('Cannot decode through uncertain digits or glyphs')
    digits = [(start+m.start()+i, char) for m in matches if m.group().isdigit()
              for i, char in enumerate(m.group())]
    if ''.join(c for _, c in digits) != ''.join(codes):
        raise ValueError('Hypothesis codes do not match the exact source digits')
    units, consumed = [], 0
    cuts = set()
    for code in codes:
        if code not in keys[table]:
            raise ValueError('Unlisted hypothesis code: '+table+':'+code)
        positions = [p for p, _ in digits[consumed:consumed+len(code)]]
        if len(positions) != len(code):
            raise ValueError('Incomplete unit')
        value = keys[table][code]
        units.append({'table':table, 'code':code, 'value':value,
            'start':source.location(positions[0]), 'end':source.location(positions[-1]),
            'source':source.text[positions[0]:positions[-1]+1],
            'supplied_confidence':metadata.get((table, code), {}).get('confidence'),
            'qualified_value':marked_value(value)})
        consumed += len(code)
        cuts.add(consumed)
    if consumed != len(digits):
        raise ValueError('Unaccounted digits')
    marks, digit_offset = [], 0
    for m in matches:
        token = m.group()
        if token.isdigit():
            digit_offset += len(token)
        elif token in (',', '.', '[,?]') or '\n' in token:
            marks.append({'source':token, 'at':source.location(start+m.start()),
                'digit_offset':digit_offset, 'at_code_boundary':digit_offset in cuts,
                'kind':('row_break' if '\n' in token else 'uncertain_separator'
                        if token == '[,?]' else 'separator')})
    return {'kind':'decoded_candidate', 'table_selection':selection, 'table':table,
            'units':units, 'literal':''.join(u['value'] for u in units), 'marks':marks}


def replay(rows, keys, hypotheses, metadata=None):
    """Partition the entire source exactly once; never skip failed parses."""
    metadata = metadata or {}
    source = Source(rows)
    located, identifiers = [], set()
    for hypothesis in hypotheses:
        if hypothesis['id'] in identifiers:
            raise ValueError('Duplicate hypothesis ID')
        identifiers.add(hypothesis['id'])
        start = source.offset(hypothesis['start'])
        end = source.offset(hypothesis['end']) + 1
        if start >= end or hypothesis['table'] not in keys:
            raise ValueError('Invalid hypothesis span/table')
        if not source.text[start].isdigit() or not source.text[end-1].isdigit():
            raise ValueError('Hypothesis endpoints must be literal digits')
        located.append((start,end,hypothesis))
    located.sort(key=lambda item:item[0])
    if any(left[1] > right[0] for left,right in zip(located,located[1:])):
        raise ValueError('Overlapping hypotheses')
    segments = []

    def emit(start,end,record):
        segments.append(dict(record, id=f'S{len(segments)+1:04}',
            offset_start=start, offset_end=end, start=source.location(start),
            end=source.location(end-1), source=source.text[start:end]))

    def numeric(start,end):
        raw = source.text[start:end]
        digits = ''.join(c for c in raw if c.isdigit())
        candidates = {t:boundaries.parses(digits,d) for t,d in keys.items()}
        total = sum(p['full_parse_count'] for p in candidates.values())
        if total == 1:
            table = next(t for t,p in candidates.items() if p['full_parse_count'])
            codes = candidates[table]['examples'][0]['codes']
            emit(start,end,materialize(source,start,end,table,codes,keys,metadata,
                                      'unique_among_supplied_tables'))
        else:
            emit(start,end,{'kind':'ambiguous' if total else 'unresolved',
                'candidate_parses':candidates, 'full_parse_count':total})

    def unanchored(start,end):
        pending = None
        for m in events(source.text[start:end]):
            a,b = start+m.start(),start+m.end()
            token = m.group()
            if token.isdigit() or (token.isspace() and pending is not None):
                if pending is None:
                    pending = a
                continue
            if pending is not None:
                numeric(pending,a)
                pending = None
            kind = ('source_mark' if token in (',','.','[,?]') else
                    'uncertain_digits' if token.startswith('[') else
                    'glyph' if token.startswith('<') else 'layout')
            emit(a,b,{'kind':kind})
        if pending is not None:
            numeric(pending,end)

    cursor = 0
    for start,end,hypothesis in located:
        unanchored(cursor,start)
        record = materialize(source,start,end,hypothesis['table'],hypothesis['codes'],
                             keys,metadata,'explicit_span_hypothesis')
        record['hypothesis'] = hypothesis
        emit(start,end,record)
        cursor = end
    unanchored(cursor,len(source.text))
    if ''.join(s['source'] for s in segments) != source.text:
        raise ValueError('Source accounting failed')
    if any(a['offset_end'] != b['offset_start'] for a,b in zip(segments,segments[1:])):
        raise ValueError('Gap or overlap in source accounting')
    return source, segments


def normalize(text):
    # Comparison only: never used to select a segmentation or alter output.
    folded = unicodedata.normalize('NFKD',text.casefold())
    return ''.join(c for c in folded if c.isalpha() and not unicodedata.combining(c))


def validate_readings(segments, edition):
    german = edition.split('## German\n',1)[1].split('## English',1)[0]
    tests = [
        ('vorstellung','main',['448','049','1127','832','405'],'P1-R04',
         ['vor','st','el','ung','machen'],'Vorstellungen machen',
         'The supplied correction is Vorstellung machen; literal stelung also lacks the conventional second l.'),
        ('marechal','main',['5521'],'P1-R04',['Marechal'],'Marechal',
         'Joins the final 5 of P1-R04 to the opening 521 of P1-R05.'),
        ('military_stem','main',['217','1165','1104'],'P2-R01',['mi','li','ta'],'militarischen',
         'Only the milita stem is checked; the whole word is not established by these three units.'),
        ('main_bernis','main',['219','9931','645','1146','473','226'],'P2-R19',
         ['ab','be','de','ber','ni','s'],'Abbé de Bernis','Case, spacing and accents are editorial.'),
        ('grafen_bruehl','main',['868','5537','1113','5519'],'P2-R14',
         ['grafen','Brühl','und','dem'],'Grafen Brühl und dem','Literal values match after case and spacing normalization.'),
        ('stainville','second',['112','122','153','946'],'P3-R02',
         ['sta','in','vil','l(e)'],'Stainville','The last entry retains its supplied optional e; table choice is a local hypothesis.'),
        ('second_bernis','second',['101','533','005','714','771','336'],'P3-R11',
         ['ab','be','de','ber','ni','s'],'Abbé Bernis','The supplied prose omits de at the noted occurrence; this candidate restores it and crosses the recorded comma inside 533. Its full prose alignment is not independently established.'),
        ('bezahlung','second',['533','195','396'],'P3-R18',['be','zahl','ung'],'Zahlung',
         'The correction notes supply Bezahlung. Matching digits alone do not settle which prose occurrence they annotate.')]
    # Gaps, uncertain signs, and ambiguous choices are hard barriers for this
    # validation; recorded separators/layout alone may lie between checked units.
    units = []
    for segment in segments:
        if segment['kind']=='decoded_candidate':
            units.extend(segment['units'])
        elif segment['kind'] not in ('source_mark','layout'):
            units.append(None)
    results = []
    for label,table,codes,row,expected,phrase,note in tests:
        matches=[]
        for i in range(len(units)-len(codes)+1):
            candidate=units[i:i+len(codes)]
            if (all(u is not None for u in candidate) and
                [(u['table'],u['code']) for u in candidate]==[(table,c) for c in codes] and
                candidate[0]['start']['row']==row):
                values=[u['value'] for u in candidate]
                matches.append({'start':candidate[0]['start'],'end':candidate[-1]['end'],
                                'values':values,'literal':''.join(values)})
        if not matches or any(m['values']!=expected for m in matches):
            raise ValueError('Literal decoding regression: '+label)
        if phrase not in german:
            raise ValueError('Reference phrase absent from German edition: '+phrase)
        literal=''.join(expected)
        if any(marked_value(v) for v in expected):
            status='qualified_key_value'
        elif normalize(literal)==normalize(phrase):
            status='matches_after_case_spacing_and_accent_normalization'
        elif normalize(phrase).startswith(normalize(literal)):
            status='stem_only'
        else:
            status='editorial_difference'
        results.append({'id':label,'literal_check':'PASS','table':table,'codes':codes,
            'matches':matches,'reference_phrase':phrase,'comparison':status,'note':note,
            'comparison_scope':'Selected phrase/stem present in supplied edition; not a full occurrence alignment.'})
    return results


def summarize(segments, validation):
    counts=collections.Counter(s['kind'] for s in segments)
    literal_digits=collections.Counter()
    for segment in segments:
        # Bracketed digit alternatives are symbols, not selected literal digits.
        if segment['kind']!='uncertain_digits':
            literal_digits[segment['kind']] += sum(c.isdigit() for c in segment['source']) if segment['kind']!='glyph' else 0
    units=[u for s in segments if s['kind']=='decoded_candidate' for u in s['units']]
    return {'software_checks':'PASS', 'complete_decipherment':False,
        'global_switch_rule_established':False,'source_characters_accounted_for':True,
        'segment_counts':dict(sorted(counts.items())),
        'literal_digit_accounting':dict(sorted(literal_digits.items())),
        'candidate_units':len(units),
        'candidate_units_by_table':dict(collections.Counter(u['table'] for u in units)),
        'units_with_qualified_values':sum(u['qualified_value'] for u in units),
        'units_with_question_mark_value':sum(u['value']=='?' for u in units),
        'cross_row_units':sum(u['start']['row']!=u['end']['row'] for u in units),
        'source_separators_inside_candidate_units':sum(
            not m['at_code_boundary'] and m['kind']=='separator'
            for s in segments if s['kind']=='decoded_candidate' for m in s['marks']),
        'selected_literal_checks':len(validation),
        'selected_reference_comparisons':dict(collections.Counter(v['comparison'] for v in validation)),
        'warning':'Counts describe conditional lookup and source accounting, not independently verified decipherment coverage.'}


def place(location):
    return f"{location['row']}:{location['character']}"


def make_reports():
    keys,rows=boundaries.load()
    with (ROOT/'working_key.csv').open(encoding='utf-8-sig',newline='') as f:
        metadata={(e['table'],e['group']):e for e in csv.DictReader(f)}
    plan=json.loads((ROOT/'decoding_spans.json').read_text(encoding='utf-8'))
    edition=(ROOT/'input/supplied_reading.md').read_text(encoding='utf-8')
    source,segments=replay(rows,keys,plan['spans'],metadata)
    validation=validate_readings(segments,edition)
    summary=summarize(segments,validation)
    report={'inputs':dict(audit.INPUT_SHA256,**{
                name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                for name in ('decoding_spans.json','input/supplied_reading.md')}),
            'policy':[
                'All readings are conditional on the supplied incomplete key.',
                'Without an explicit span, recorded separators and uncertain signs are boundaries; unseparated row breaks may be crossed.',
                'Every complete known-entry parse is considered in both tables; only a unique candidate is expanded.',
                'Table-exclusive dictionary membership is a candidate selection rule, not an inferred historical switch.',
                'Explicit spans may split written runs and cross recorded separators; their source locations and marks are retained.',
                'No plaintext fills gaps, chooses table states, or resolves key alternatives.',
                'The entire source, including punctuation, uncertainty and glyphs, is accounted for exactly once.'],
            'summary':summary,'validation':validation,'segments':segments}
    lines=['# Conditional literal decoding','',
        '**This remains a partial reading. No general table-switching rule is implemented.**',
        'The supplied edition is in [input/supplied_reading.md](../input/supplied_reading.md). It is not inserted into this output.',
        'Tables on ordinary runs are unique dictionary candidates, not historically verified states. Five explicit second-table spans are local hypotheses.',
        'Values retain spelling, alternatives and `?`. `UNRESOLVED`, `AMBIGUOUS`, `UNCERTAIN`, and `GLYPH` markers consume the indicated source; nothing is dropped.',
        'Segments spanning physical rows appear at their starting row; their full endpoints are in [decoding.json](decoding.json). Source commas separate runs but are not emitted as plaintext punctuation. Encoded comma values remain visible.','']
    render=collections.defaultdict(list)
    for s in segments:
        kind=s['kind']
        if kind=='decoded_candidate':
            label=s['table']+(' hypothesis' if s['table_selection']=='explicit_span_hypothesis' else ' candidate')
            text=' / '.join(u['value'] for u in s['units'])
            render[s['start']['row']].append(f"{{{label}: {text}}}")
        elif kind in ('unresolved','ambiguous','uncertain_digits','glyph'):
            label={'unresolved':'UNRESOLVED','ambiguous':'AMBIGUOUS','uncertain_digits':'UNCERTAIN','glyph':'GLYPH'}[kind]
            raw=s['source'].replace('\n',' ↵ ')
            render[s['start']['row']].append(f"[{label} {s['id']}: {raw}]")
    for row in rows:
        lines += ['## '+row['id'],'','```text',' · '.join(render[row['id']]) or '(accounted for in the preceding span)','```','']
    review=['# Reading validation and unresolved inventory','',
        '**Software checks pass; a full readable decipherment is not established.**',
        'These checks compare selected literal outputs with phrases or stems in the supplied German. They are not independent recovery tests and do not align the entire letter.','',
        '| Check | Literal result | Supplied German reference | Comparison |',
        '| --- | --- | --- | --- |']
    for v in validation:
        literal=v['matches'][0]['literal'].replace('|','\\|')
        review.append(f"| {v['id']} | `{literal}` | {v['reference_phrase']} | {v['comparison']} |")
    review += ['']+[f"- **{v['id']}:** {v['note']}" for v in validation]
    review += ['','## Accounting','',f"- Candidate units: {summary['candidate_units']} (conditional, not a coverage score).",
        f"- Cross-row units: {summary['cross_row_units']}.",
        f"- Qualified value occurrences: {summary['units_with_qualified_values']}; literal `?` occurrences: {summary['units_with_question_mark_value']}.",
        f"- Unresolved numeric spans: {summary['segment_counts'].get('unresolved',0)}; ambiguous spans: {summary['segment_counts'].get('ambiguous',0)}.",
        f"- Uncertain digit groups: {summary['segment_counts'].get('uncertain_digits',0)}; G glyphs: {summary['segment_counts'].get('glyph',0)}.",
        '- Every source character is preserved in the JSON ledger.','',
        '## Work queue: unresolved or ambiguous spans','',
        'A zero dictionary parse may reflect missing entries, a wrong grouping assumption, a transcription issue, or unknown control rules. It does not establish which explanation is correct.','',
        '| ID | Location | Source | Status |','| --- | --- | --- | --- |']
    for s in segments:
        if s['kind'] in ('unresolved','ambiguous','uncertain_digits','glyph'):
            raw=s['source'].replace('\n',' ↵ ').replace('|','\\|')
            review.append(f"| {s['id']} | {place(s['start'])}–{place(s['end'])} | `{raw}` | {s['kind']} |")
    return {'output/decoding.json':audit.json_bytes(report),
            'output/decoded_reading.md':('\n'.join(lines).rstrip()+'\n').encode('utf-8'),
            'output/reading_validation.md':('\n'.join(review).rstrip()+'\n').encode('utf-8')}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build',action='store_true')
    args=parser.parse_args()
    outputs=make_reports()
    for relative,content in outputs.items():
        path=ROOT/relative
        if args.build:
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(content)
        elif not path.exists() or path.read_bytes()!=content:
            raise ValueError('Missing or stale report: '+relative)
    print(json.dumps(json.loads(outputs['output/decoding.json'])['summary'],indent=2))


if __name__=='__main__':
    main()
