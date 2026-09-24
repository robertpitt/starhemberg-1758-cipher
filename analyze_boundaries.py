#!/usr/bin/env python3
"""Reproduce conditional segmentation and table-location evidence.

Standard library only. Never alters inputs, chooses uncertain digits, treats
unknowns as nulls, or uses plaintext to score a parse. --build writes the report;
otherwise verifies its exact bytes. All parses are relative to the supplied,
incomplete dictionary, not an authenticated historical codebook.
"""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import json
import re
from pathlib import Path
import audit

ROOT = Path(__file__).resolve().parent
REPORT = ROOT / 'output/boundary_analysis.json'


def parses(text, keys):
    """Count every full dictionary parse; retain at most three examples."""
    if not re.fullmatch(r'[0-9]+', text):
        return {'status': 'not_evaluated_nonliteral_digits'}
    count = [0] * (len(text) + 1)
    examples = [[] for _ in count]
    count[-1] = 1
    examples[-1] = [[]]
    widths = sorted({len(k) for k in keys})
    for start in range(len(text) - 1, -1, -1):
        for width in widths:
            end = start + width
            code = text[start:end]
            if end <= len(text) and code in keys:
                count[start] += count[end]
                for tail in examples[end]:
                    if len(examples[start]) < 3:
                        examples[start].append([code] + tail)
    return {'status': 'evaluated', 'full_parse_count': count[0],
            'examples': [{'codes': p, 'values': [keys[k] for k in p]}
                         for p in examples[0]]}


def load():
    for name, expected in audit.INPUT_SHA256.items():
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != expected:
            raise ValueError('Input checksum mismatch: ' + name)
    keys = {t: {} for t in ('main', 'second')}
    with (ROOT / 'working_key.csv').open(encoding='utf-8-sig', newline='') as f:
        for entry in csv.DictReader(f):
            keys[entry['table']][entry['group']] = entry['value']
    rows = []
    for line in (ROOT / 'ciphertext.txt').read_text(encoding='utf-8').splitlines():
        rid, text = line.split('\t')
        rows.append({'id': rid, 'text': text, 'runs': audit.source_runs(text)})
    return keys, rows


def projection(rows):
    """Ignore separators for search only; record every ignored mark and row break.

    Numeric uncertainties and G signs are barriers. No alternative is chosen.
    Positions are one-based source character coordinates, including markup.
    """
    stream, locations, gaps = [], [], collections.defaultdict(list)
    for index, row in enumerate(rows):
        for m in re.finditer(r'\[[^\]]*\]|<G\d>|[0-9]|[,\.]', row['text']):
            token = m.group()
            location = {'row': row['id'], 'character': m.start() + 1}
            if token in (',', '.', '[,?]'):
                gaps[len(stream)].append(dict(location, kind={
                    ',': 'comma', '.': 'period', '[,?]': 'uncertain_separator'}[token]))
            else:
                stream.append(token if token.isdigit() else '#')
                locations.append(location)
        if index + 1 < len(rows):
            gaps[len(stream)].append({'kind': 'row_break', 'after': row['id'],
                                      'before': rows[index + 1]['id']})
    return ''.join(stream), locations, gaps


def trace(start, codes, locations, gaps):
    stop = start + sum(map(len, codes))
    ends, offset = [], start
    for code in codes:
        offset += len(code)
        ends.append(offset)
    cuts = set(ends[:-1])
    boundary_events = []
    for offset in sorted(gaps):
        if start < offset < stop:
            for gap in gaps[offset]:
                boundary_events.append(dict(gap, digit_offset=offset-start,
                    at_proposed_code_boundary=offset in cuts))
    return {'start': locations[start], 'end': locations[stop-1],
            'source_events_inside_span': boundary_events,
            'proposed_boundaries_without_recorded_event': [
                {'after': locations[cut-1], 'before': locations[cut]}
                for cut in ends[:-1] if not gaps.get(cut)]}


def make_report():
    keys, rows = load()
    inventory = {}
    for table, dictionary in keys.items():
        conflicts = [{'short': a, 'long': b} for a in sorted(dictionary)
                     for b in sorted(dictionary) if a != b and b.startswith(a)]
        pattern = (r'(?:[02468][0-9]{2}|(?:11|33|55|77|99)[0-9]{2})'
                   if table == 'main' else
                   r'(?:[013579][0-9]{2}|(?:22|44|66|88)[0-9]{2})')
        inventory[table] = {
            'entries': len(dictionary),
            'length_counts': dict(sorted(collections.Counter(map(len, dictionary)).items())),
            'all_four_digit_entries_begin_with_a_doubled_digit': all(
                k[0] == k[1] for k in dictionary if len(k) == 4),
            'prefix_conflicts': conflicts,
            'prefix_free': not conflicts,
            'descriptive_shape_regex': pattern,
            'shape_exceptions': [{'code': k, 'value': v} for k, v in dictionary.items()
                                 if not re.fullmatch(pattern, k)]}
    long_runs, row_counts = [], []
    for row in rows:
        forms = [r['surface'] for r in row['runs']]
        row_counts.append({'row': row['id'], 'written_runs': len(forms),
            'exact_main_only': sum(f in keys['main'] and f not in keys['second'] for f in forms),
            'exact_second_only': sum(f in keys['second'] and f not in keys['main'] for f in forms),
            'exact_both': sum(f in keys['main'] and f in keys['second'] for f in forms),
            'literal_numeric_runs_longer_than_four': sum(
                f.isdigit() and len(f) > 4 for f in forms)})
        for n, run in enumerate(row['runs'], 1):
            text = run['surface']
            if text.isdigit() and len(text) > 4:
                long_runs.append({'row': row['id'], 'run': n, 'source': text,
                    'start_character': run['start']+1, 'end_character': run['end'],
                    'parses': {t: parses(text, d) for t, d in keys.items()}})
    joins = []
    for left, right in zip(rows, rows[1:]):
        a, b = left['runs'][-1], right['runs'][0]
        if a['right'] != 'row_end':
            continue
        joins.append({'left_row': left['id'], 'right_row': right['id'],
            'left_fragment': a['surface'], 'right_fragment': b['surface'],
            'join_digit_offset': len(a['surface']) if a['surface'].isdigit() else None,
            'parses': {t: parses(a['surface'] + b['surface'], d) for t, d in keys.items()}})
    stream, locations, gaps = projection(rows)
    # Exhaustive maximal spans containing >=4 consecutive known second-table
    # entries. Prefix freedom makes the forward parse deterministic from each
    # digit offset. Overlapping, non-contained spans are retained.
    assert inventory['second']['prefix_free']
    candidates = []
    for start in range(len(stream)):
        offset, codes = start, []
        while offset < len(stream):
            options = [stream[offset:offset+n] for n in (3, 4)
                       if offset+n <= len(stream) and stream[offset:offset+n] in keys['second']]
            assert len(options) <= 1
            if not options:
                break
            code = options[0]
            codes.append(code)
            offset += len(code)
        if len(codes) >= 4:
            candidates.append((start, offset, codes))
    maximal = [(a, b, codes) for a, b, codes in candidates if not any(
        c <= a and d >= b and (c, d) != (a, b) for c, d, _ in candidates)]
    second_spans = [dict(trace(a, p, locations, gaps), codes=p,
        values=[keys['second'][c] for c in p],
        alternative_main_parses=parses(stream[a:b], keys['main'])) for a, b, p in maximal]
    # Explicit source/key examples for transition bounds, not inferred switches.
    anchor_specs = [
        ('main_before_second_region', 'main', ['233','1118','831','802','5568','1155'], 'P3-R02'),
        ('bezahlung', 'second', ['533','195','396'], 'P3-R18'),
        ('main_return_run', 'main', ['7779','054','437','248'], 'P3-R21'),
        ('main_after_return', 'main', ['022','1113','1144','5536','022','223','7727'], 'P4-R02')]
    anchors = []
    for label, table, codes, expected_row in anchor_specs:
        needle = ''.join(codes)
        matches = []
        for match in re.finditer('(?=' + needle + ')', stream):
            if locations[match.start()]['row'] == expected_row:
                matches.append(trace(match.start(), codes, locations, gaps))
        assert matches, label
        anchors.append({'label': label, 'table': table, 'codes': codes,
            'values': [keys[table][c] for c in codes], 'matches': matches,
            'other_table_full_parses': parses(needle, keys['second' if table == 'main' else 'main'])})
    return {'input_sha256': audit.INPUT_SHA256,
        'scope': [
            'Facts are relative to the frozen transcription and supplied incomplete CSV.',
            'A unique complete dictionary parse does not prove a historical segmentation.',
            'No full dictionary parse does not refute a table: its key may be incomplete.',
            'Search spans ignore separators and row breaks only while recording them explicitly.',
            'Unknown digit alternatives and G signs are barriers, never deleted or assigned values.',
            'Maximal second-table spans use a declared minimum of four known entries; this is not a significance threshold.',
            'No exact switch location, switching instruction, or number of switches is inferred.'],
        'key_structure': inventory, 'row_inventory': row_counts,
        'long_numeric_runs': long_runs, 'unseparated_row_boundary_candidates': joins,
        'maximal_second_table_spans_at_least_four_entries': second_spans,
        'transition_anchors': anchors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', action='store_true')
    args = parser.parse_args()
    result = make_report()
    content = (json.dumps(result, ensure_ascii=False, indent=2)+'\n').encode('utf-8')
    if args.build:
        REPORT.parent.mkdir(exist_ok=True)
        REPORT.write_bytes(content)
    elif not REPORT.exists() or REPORT.read_bytes() != content:
        raise ValueError('Missing or stale report: output/boundary_analysis.json')
    print(json.dumps({'status': 'PASS', 'long_numeric_runs': len(result['long_numeric_runs']),
        'unseparated_row_boundaries': len(result['unseparated_row_boundary_candidates']),
        'maximal_second_table_spans': len(result['maximal_second_table_spans_at_least_four_entries'])}))


if __name__ == '__main__':
    main()
