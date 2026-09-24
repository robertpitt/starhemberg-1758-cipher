#!/usr/bin/env python3
"""Audit the supplied CSV and reproduce a source-preserving concordance.

No key recovery, source correction, table-switch inference, or grammatical
expansion occurs. Python 3.9+, standard library only. Run with --build to
regenerate all reports; without arguments, compare reports and check input hashes.
The integrated audit also verifies the conditional replay and boundary analysis.
"""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
KEY_PATH = ROOT / 'working_key.csv'
CIPHER_PATH = ROOT / 'ciphertext.txt'
INPUT_SHA256 = {'ciphertext.txt': '66e550b75db3d7e7dc1b41cb724c5628885ce4cb66535f49acb49c09e96bcedc', 'working_key.csv': '9e815ceb11d9f48e76345349a9640c1423e825e516c301f2acb043ccad0fd63a'}


def json_bytes(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def source_runs(text):
    """Split only observed commas/dots outside uncertainty brackets.

    Each output retains its literal surface and zero-based character span.
    Whitespace only trims the outside of a run. No physical line join occurs.
    A doubtful [,?] separator stays inside its run.
    """
    depth = 0
    left = 0
    pieces = []
    previous_mark = 'row_start'
    for i, ch in enumerate(text):
        if ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
            if depth < 0:
                raise ValueError('Unbalanced source brackets')
        elif ch in ',.' and depth == 0:
            raw = text[left:i]
            s = left + len(raw) - len(raw.lstrip())
            e = i - (len(raw) - len(raw.rstrip()))
            if s < e:
                pieces.append(dict(surface=text[s:e], start=s, end=e,
                                   left=previous_mark, right=ch))
            left, previous_mark = i + 1, ch
    if depth:
        raise ValueError('Unbalanced source brackets')
    raw = text[left:]
    s = left + len(raw) - len(raw.lstrip())
    e = len(text) - (len(raw) - len(raw.rstrip()))
    if s < e:
        pieces.append(dict(surface=text[s:e], start=s, end=e,
                           left=previous_mark, right='row_end'))
    return pieces


def literal_digit_projection(rows, page):
    """Search-only projection: no digit alternatives are selected.

    Uncertain numerals/G glyphs are barriers (#); punctuation is skipped.
    Physical source characters remain linked to each projected character.
    This projection is NOT a cipher parse or an edited source transcription.
    """
    chars, locs = [], []
    for row in rows:
        if row['manuscript_page'] != page:
            continue
        for m in re.finditer(r'\[,\?\]|\[[^\]]*\]|<G\d>|[0-9]', row['text']):
            val = m.group()
            if val == '[,?]':
                continue
            chars.append(val if val.isdigit() else '#')
            locs.append({'row': row['id'], 'source_character': m.start()+1})
    return ''.join(chars), locs


def find_literal(rows, page, needle):
    stream, locs = literal_digit_projection(rows, page)
    hits = []
    start = 0
    while True:
        p = stream.find(needle, start)
        if p < 0:
            break
        hits.append({'start': locs[p], 'end': locs[p+len(needle)-1]})
        start = p + 1
    return hits


def find_written(rows, codes, allowed_rows=None):
    out = []
    for row in rows:
        if allowed_rows and row['id'] not in allowed_rows:
            continue
        runs = source_runs(row['text'])
        forms = [r['surface'] for r in runs]
        for i in range(len(forms)-len(codes)+1):
            if forms[i:i+len(codes)] == codes:
                out.append({'row': row['id'], 'written_run_start': i+1,
                            'source_character_start': runs[i]['start']+1,
                            'source_character_end': runs[i+len(codes)-1]['end']})
    return out


def make_reports():
    with KEY_PATH.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != ['table','group','value','occurrences','confidence']:
            raise ValueError('Unexpected CSV schema')
        entries = list(reader)
    keys = {}
    for e in entries:
        ck = (e['table'], e['group'])
        if ck in keys:
            raise ValueError('Duplicate table/group: ' + repr(ck))
        if e['table'] not in ('main','second') or not re.fullmatch('[0-9]+',e['group']):
            raise ValueError('Invalid table or code')
        if e['confidence'] not in ('high','medium','low'):
            raise ValueError('Unexpected confidence label')
        if int(e['occurrences']) < 1:
            raise ValueError('Invalid supplied occurrence annotation')
        keys[ck] = e
    rows = []
    for line in CIPHER_PATH.read_text(encoding='utf-8').splitlines():
        match = re.fullmatch(r'(P([1-4])-R([0-9]{2}))\t(.+)', line)
        if not match:
            raise ValueError('Invalid ciphertext row: ' + repr(line))
        row_id, page, number, source = match.groups()
        rows.append(dict(id=row_id, manuscript_page=int(page), row=int(number),
                         text=source, status=('human_transcription' if int(page) <= 2
                                             else 'draft_or_partly_reviewed')))
    assert len(rows) == 52
    assert len({r['id'] for r in rows}) == len(rows)
    assert source_runs('05,293,1127,1158,3391.')[0]['surface'] == '05'
    assert [x['surface'] for x in source_runs('1[,?]2,03.')] == ['1[,?]2','03']
    assert [x['surface'] for x in source_runs('04<G1>,<G2><G3><G4>,4')] == ['04<G1>','<G2><G3><G4>','4']

    stats = {
        'entry_count': len(entries),
        'table_counts': dict(collections.Counter(e['table'] for e in entries)),
        'confidence_counts_as_supplied': dict(collections.Counter(e['confidence'] for e in entries)),
        'unique_decimal_forms': len({e['group'] for e in entries}),
        'duplicate_table_group_rows': 0,
        'explicit_unknown_entries': [e for e in entries if e['value'].strip() == '?'],
        'table_specific_collisions': [],
        'qualifications': [
            'Confidence labels and occurrence counts are supplied annotations, not independently authenticated here.',
            'Slash alternatives, parentheses and question marks are preserved verbatim.',
            'Code strings retain leading zeros; table identity is mandatory.',
            'The CSV contains mappings but no explicit segmentation or switching instructions.'
        ]
    }
    main = {e['group'] for e in entries if e['table']=='main'}
    sec = {e['group'] for e in entries if e['table']=='second'}
    for code in sorted(main & sec):
        stats['table_specific_collisions'].append({
            'code': code, 'main': keys['main',code]['value'],
            'second': keys['second',code]['value']})
    assert stats['entry_count'] == 277
    assert stats['table_counts'] == {'main':229,'second':48}
    assert stats['confidence_counts_as_supplied'] == {'medium':96,'high':97,'low':84}

    specifications = [
        dict(id='K23-01', table='main', codes=['448','049','1127','832','405'],
             expected=['vor','st','el','ung','machen'], rows=['P1-R04'],
             note='Literal vorstelungmachen; conventional spelling adds a second l. No en between ung and machen.'),
        dict(id='K23-02', table='main', codes=['049','1127','832'],
             expected=['st','el','ung'], rows=['P1-R04','P1-R06'],
             note='Repeated within-word sequence stelung; orthographic normalization is separate.'),
        dict(id='K23-03', table='main', codes=['217','1165','1104'],
             expected=['mi','li','ta'], rows=['P2-R01','P2-R10'],
             note='Repeated military-word stem, not an independently positioned complete phrase.'),
        dict(id='K23-04', table='main', codes=['219','9931','645'],
             expected=['ab','be','de'], rows=['P2-R13','P2-R19'],
             note='Literal abbe de before spacing, accents and capitalization.'),
        dict(id='K23-05', table='main', codes=['219','9931','645','1146','473','226'],
             expected=['ab','be','de','ber','ni','s'], rows=['P2-R19'],
             note='Exact abbedebernis before spacing, accents and capitalization.'),
        dict(id='K23-06', table='main', codes=['868','5537','1113','5519'],
             expected=['grafen','Brühl','und','dem'], rows=['P2-R14'],
             note='Supplied labels for grafen Bruehl und dem at this source location.'),
        dict(id='K23-07', table='second', codes=['533','005','714','771'],
             expected=['be','de','ber','ni'], search_page=3, min_hits=2,
             note='Two exact digit matches in the draft transcription. Subdivision and second-table use are explicit assumptions; do not supply the following s automatically.'),
        dict(id='K23-08', table='second', codes=['533','195','396'],
             expected=['be','zahl','ung'], search_page=3, min_hits=1,
             note='Confirms the supplied code-value combination. The raw match in the draft transcription crosses written-group divisions; it does not independently settle the location of the supplied textual correction.')
    ]
    checks = []
    for s in specifications:
        vals = [keys[s['table'],c]['value'] for c in s['codes']]
        assert vals == s['expected'], s['id']
        rec = dict(s)
        rec['literal_concatenation'] = ''.join(vals)
        rec['supplied_confidence'] = [keys[s['table'],c]['confidence'] for c in s['codes']]
        rec['status'] = 'mechanical lookup/source-location check; not independent historical key recovery'
        if 'rows' in s:
            hits = find_written(rows, s['codes'], s['rows'])
            assert {h['row'] for h in hits} == set(s['rows']), s['id']
            rec['source_match_kind'] = 'adjacent exact written runs in human-transcribed pages'
        else:
            hits = find_literal(rows,s['search_page'],''.join(s['codes']))
            assert len(hits) >= s['min_hits'], s['id']
            rec['source_match_kind'] = 'literal digits in draft source; proposed internal code boundaries'
        rec['source_matches'] = hits
        checks.append(rec)

    # A two-table concordance: no table is automatically selected by page.
    concordance=[]
    counts=collections.defaultdict(collections.Counter)
    rawmd=['# Main-table lookup of the human-transcribed pages\n',
      'This is a lookup overlay, NOT a complete decipherment. No long written group is subdivided, no line break joined, no code silently omitted.',
      'Each CSV value is reproduced verbatim, including alternatives and uncertainty. `UNLISTED` and `?` are not nulls.\n']
    for row in rows:
        rr = source_runs(row['text'])
        rendered=[]
        for no,run in enumerate(rr,1):
            g=run['surface']
            m=keys.get(('main',g)); b=keys.get(('second',g))
            concordance.append(dict(row=row['id'],written_run=no,source_surface=g,
                source_character_start=run['start']+1,source_character_end=run['end'],
                left_boundary=run['left'],right_boundary=run['right'],
                source_status=row['status'],
                main_value=m['value'] if m else 'UNLISTED',
                main_confidence=m['confidence'] if m else '',
                second_value=b['value'] if b else 'UNLISTED',
                second_confidence=b['confidence'] if b else ''))
            if row['manuscript_page'] <= 2:
                c=counts['P1-P2']; c['written_run_occurrences']+=1
                if m:
                    c['listed_occurrences']+=1
                    c['literal_unknown' if m['value']=='?' else 'nonplaceholder_occurrences']+=1
                else:c['unlisted_occurrences']+=1
                value=m['value'] if m else 'UNLISTED'
                rendered.append(f'`{g}` → **{value}**')
        if row['manuscript_page'] <=2:
            rawmd+=['\n## '+row['id']+'\n','```text\n'+row['text']+'\n```\n',
                    ' · '.join(rendered)+'\n']
    stats['exact_run_lookup_counts']=dict(counts['P1-P2'])
    stats['lookup_count_warning']='Written runs include edge fragments, uncertain/long forms, and editorial runs. This is not a decipherment coverage percentage.'

    out={
        'output/key_inventory.json':json_bytes(stats),
        'output/selected_checks.json':json_bytes(checks),
        'output/human_pages_literal_overlay.md':('\n'.join(rawmd).rstrip()+'\n').encode('utf-8')
    }
    buf=io.StringIO(newline=''); writer=csv.DictWriter(buf,fieldnames=list(concordance[0]),delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(concordance)
    out['output/all_rows_dual_table_concordance.tsv']=buf.getvalue().encode('utf-8')
    km=['# Supplied key inventory\n','All values, counts and confidence labels below are supplied, not inferred by this audit.\n']
    for table in ('main','second'):
        km += ['\n## '+table+'\n','| Group | Value as supplied | Occurrences as supplied | Confidence as supplied |','|---|---|---:|---|']
        for e in entries:
            if e['table']==table:
                km.append('| `{group}` | {value} | {occurrences} | {confidence} |'.format(**{k:v.replace('|','\\|') for k,v in e.items()}))
    out['output/supplied_key_inventory.md']=('\n'.join(km)+'\n').encode('utf-8')
    return out,stats,checks


def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--build',action='store_true');args=ap.parse_args()
    for relative_path, expected_hash in INPUT_SHA256.items():
        actual_hash = hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            raise ValueError('Input checksum mismatch: ' + relative_path)
    out,stats,checks=make_reports()
    import analyze_boundaries
    import decode
    out['output/boundary_analysis.json'] = json_bytes(analyze_boundaries.make_report())
    out.update(decode.make_reports())
    replay_summary = json.loads(out['output/decoding.json'])['summary']
    for rel,content in out.items():
        path=ROOT/rel
        if args.build:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(content)
        elif not path.exists() or path.read_bytes()!=content:
            raise ValueError('Missing or stale report: '+rel)
    print(json.dumps({'status':'PASS','entries':stats['entry_count'],'tables':stats['table_counts'],
                      'source_rows':52,'selected_checks':len(checks),'verified_reports':len(out),
                      'reading_checks':replay_summary['selected_literal_checks'],
                      'complete_decipherment':replay_summary['complete_decipherment'],
                      'exact_written_run_counts':stats['exact_run_lookup_counts'],
                      'limitation':'Lookup and source accounting only; no switch rules, whole-letter decoding, or historical authentication established.'},indent=2))


if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,AssertionError,OSError) as e:
        print('AUDIT FAILED:',repr(e),file=sys.stderr);sys.exit(1)
