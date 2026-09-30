#!/usr/bin/env python3
"""Validate the working key and reproduce the review table and partial replay."""
import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PUNCTUATION = {'comma': ',', 'period': '.', 'semicolon': ';',
               'question': '?', 'parenthesis': '[parenthesis]'}


def width(first, table):
    if table not in ('prima', 'secunda') or first not in '0123456789':
        raise ValueError('Invalid table or leading digit')
    return 3 if first == '0' or (int(first) % 2 == 0) == (table == 'prima') else 4

def scan(stream, locations, start, table, controls):
    units = []
    cursor = start
    while cursor < len(stream):
        if stream[cursor] == '#':
            return {'units': units, 'stop': {'reason': 'uncertain_source', 'location': locations[cursor]}}
        size = width(stream[cursor], table)
        code = stream[cursor:cursor + size]
        reason = ('incomplete_group' if len(code) != size else
                  'uncertain_source' if '#' in code else
                  'unverified_four_digit_form' if size == 4 and code[0] != code[1] else None)
        if reason:
            return {'units': units, 'stop': {'reason': reason, 'table': table,
                    'candidate': code, 'location': locations[cursor]}}
        target = controls[table].get(code)
        units.append({'table': table, 'code': code, 'start': locations[cursor],
                      'end': locations[cursor + size - 1], 'indicator_target': target})
        if target:
            table = target
        cursor += size
    return {'units': units, 'stop': {'reason': 'end_of_stream'}}

def project(rows):
    digits, locations = [], []
    for row, raw in rows:
        for match in re.finditer(r'\[,\?\]|\[[^\]]*\]|<G\d>|[0-9]', raw):
            token = match.group()
            if token == '[,?]':
                continue
            digits.append(token if token.isdigit() else '#')
            locations.append((row, match.start() + 1))
    return ''.join(digits), locations

def source_controls(keys):
    controls = {'prima': {}, 'secunda': {}}
    for (table, code), entry in keys.items():
        if entry['kind'] == 'switch' and entry['review_status'] == 'source_read':
            controls[table][code] = entry['target']
    return controls

def render_entry(entry):
    if entry is None:
        return None
    if entry['review_status'] != 'source_read':
        return '[provisional: ' + entry['value'] + ']'
    kind = entry['kind']
    if kind == 'null':
        return '∅'
    if kind == 'switch':
        return '→ ' + entry['target']
    if kind == 'punctuation':
        return PUNCTUATION[entry['punctuation_kind']]
    if kind == 'cancellation':
        return '[CADATUR: scope unresolved]'
    return entry['value']


def load_key(root=ROOT):
    with (root / 'working_key.csv').open(newline='', encoding='utf-8') as f:
        entries = list(csv.DictReader(f))
    keys, identities = {}, set()
    for e in entries:
        identity = e['table'], e['code']
        if identity in identities or e['table'] not in ('prima', 'secunda') or not re.fullmatch(r'[0-9]{3,4}', e['code']):
            raise ValueError('Duplicate or invalid code: ' + str(identity))
        identities.add(identity)
        if e['probability'] not in ('High', 'Moderate', 'Low', 'Unassessed') or not e['value'] or not e['human_confirmed']:
            raise ValueError('Missing value or review information: ' + str(identity))
        if e['review_status'] == 'supplied_guess':
            if e['kind'] != 'unknown' or e['target'] or e['probability'] != 'Unassessed':
                raise ValueError('Supplied guess cannot operate as a source entry')
            continue
        if e['review_status'] not in ('source_read', 'provisional') or len(e['code']) != width(e['code'][0], e['table']):
            raise ValueError('Invalid source status or length: ' + str(identity))
        if e['kind'] not in ('lexical', 'null', 'switch', 'punctuation', 'cancellation') or not e['source']:
            raise ValueError('Missing source or invalid kind: ' + str(identity))
        if e['kind'] == 'switch' and e['target'] != {'prima': 'secunda', 'secunda': 'prima'}[e['table']]:
            raise ValueError('Invalid switch target')
        if e['kind'] == 'punctuation' and e['punctuation_kind'] not in PUNCTUATION:
            raise ValueError('Invalid punctuation')
        if e['review_status'] == 'provisional' and e['probability'] != 'Low':
            raise ValueError('Provisional reading must remain low confidence')
        keys[identity] = e
    return entries, keys


def replay(keys, root=ROOT):
    rows = [line.split('\t', 1) for line in (root / 'ciphertext.txt').read_text().splitlines()]
    expected = [f'P{p}-R{r:02}' for p, count in enumerate((6, 21, 21, 4), 1) for r in range(1, count + 1)]
    if [row[0] for row in rows] != expected or any(len(row) != 2 for row in rows):
        raise ValueError('Ciphertext must retain its 52 labelled rows in order')
    stream, locations = project(rows)
    traces = {}
    for name, start in [('opening', 0), ('transition_probe', locations.index(('P3-R02', 50)))]:
        trace = scan(stream, locations, start, 'prima', source_controls(keys))
        for unit in trace['units']:
            unit['reading'] = render_entry(keys.get((unit['table'], unit['code'])))
        traces[name] = trace
    return traces


def cell(value):
    return value.replace('|', '\\|').replace('\n', ' ')


def review_table(entries):
    lines = ['# Key review table', '',
             'Probability is qualitative, not a measured percentage. High confirms only the stated reading, '
             'not every alternative or its use in the letter. Partial and illegible readings are not fully confirmed.', '',
             'Norbert’s manuscript readings in both tables retain his notation and explicit uncertainty. '
             'See [EVIDENCE.md](../EVIDENCE.md) for corrections and source conflicts. Supplied guesses are excluded from the replay.', '',
             '| Table | Code | Value | Probability | Human confirmed |',
             '| --- | --- | --- | --- | --- |']
    priority = {'Low': 0, 'Unassessed': 0, 'Moderate': 1, 'High': 2}
    for e in sorted(entries, key=lambda e: (priority[e['probability']], e['table'], int(e['code']))):
        value = e['value'] + (' (supplied guess; source unconfirmed)' if e['review_status'] == 'supplied_guess' else '')
        cells = [e['table'].title(), '`' + e['code'] + '`', value, e['probability'], e['human_confirmed']]
        lines.append('| ' + ' | '.join(cell(c) for c in cells) + ' |')
    return '\n'.join(lines) + '\n'


def literal_reading(traces):
    lines = ['# Historical-key replay', '',
             '**R1588/R1589 is identified; the full decipherment remains incomplete.** '
             'Coordinates are one-based characters after each row label in [ciphertext.txt](../ciphertext.txt). '
             'Unknown entries stay unknown; supplied guesses never fill gaps.', '']
    for name, trace in traces.items():
        assumption = ('Instruction-prescribed Prima at the start; no paragraph reset inferred.' if name == 'opening' else
                      'Independent Prima start at P3-R02:50; this does not resume the stopped opening trace.')
        lines += ['## ' + name.replace('_', ' ').title(), '', assumption, '',
                  '| Source start | Table | Code | Source reading / operation |', '| --- | --- | --- | --- |']
        for u in trace['units']:
            reading = cell(u['reading'] or '[key entry not yet transcribed]')
            lines.append(f"| {u['start'][0]}:{u['start'][1]} | {u['table']} | `{u['code']}` | {reading} |")
        stop = trace['stop']
        location = ':'.join(map(str, stop.get('location', [])))
        lines += ['', f"**Stop:** {stop['reason']}; `{stop.get('candidate', '')}` at {location}.", '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', action='store_true', help='Regenerate the two Markdown outputs after reviewed key changes')
    args = parser.parse_args()
    entries, keys = load_key()
    traces = replay(keys)
    outputs = {'output/key_review_table.md': review_table(entries),
               'output/historical_reading.md': literal_reading(traces)}
    for name, content in outputs.items():
        target = ROOT / name
        if args.build:
            target.parent.mkdir(exist_ok=True)
            target.write_text(content, encoding='utf-8')
        elif not target.exists() or target.read_text() != content:
            raise SystemExit(name + ' is missing or stale; review changes, then run with --build')
    print(f'{len(keys)} source entries; {len(entries)} review rows; both outputs consistent.')
    print('Opening: ' + str(len(traces['opening']['units'])) + ' groups. Full decipherment remains incomplete.')


if __name__ == '__main__':
    main()
