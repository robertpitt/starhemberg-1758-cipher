#!/usr/bin/env python3
"""Test source-read R1588 lengths; stop at uncertainty or unverified code form."""
import argparse
import hashlib
import json
from pathlib import Path

from audit import INPUT_SHA256
from check_supplied_indicators import project

ROOT = Path(__file__).resolve().parent


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


def report():
    for name, expected in INPUT_SHA256.items():
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != expected:
            raise ValueError('Input changed: ' + name)
    rules = (ROOT / 'r1588_source_rules.json').read_bytes()
    review_bytes = (ROOT / 'supplied_indicator_review.json').read_bytes()
    review = json.loads(review_bytes)
    controls = {'prima': {}, 'secunda': {}}
    for item in review['reviews']:
        if item['id'] == 'B':
            controls['secunda'].update((code, 'prima') for code in item['confirmed_codes'])
        elif item['id'] == 'C':
            controls['prima'].update((code, 'secunda') for code in item['confirmed_codes'])
    rows = [line.split('\t', 1) for line in (ROOT / 'ciphertext.txt').read_text().splitlines()]
    stream, locations = project(rows)
    local_start = locations.index(('P3-R02', 50))
    return {'status': 'PARTIAL_FRAMING_DIAGNOSTIC_NOT_DECIPHERMENT',
            'input_sha256': INPUT_SHA256,
            'rules_sha256': hashlib.sha256(rules).hexdigest(),
            'indicator_review_sha256': hashlib.sha256(review_bytes).hexdigest(),
            'policy': 'Ignore recorded separators and physical row breaks; preserve digit locations. Start Prima. Stop before uncertain digits or a four-digit group without a repeated initial. The latter is a numerical-table consistency safeguard, not a separately transcribed prohibition in clause 1. Do not repair or resume automatically. Paragraph boundaries are not encoded; no inferred resets. Indicator recognition does not validate sentence-boundary eligibility.',
            'from_opening': scan(stream, locations, 0, 'prima', controls),
            'local_probe': {'assumption': 'Independent probe at known 1158, assuming Prima; not a continuation of the stopped opening scan.',
                            **scan(stream, locations, local_start, 'prima', controls)}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', action='store_true')
    args = parser.parse_args()
    data = report()
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    output = ROOT / 'output' / 'r1588_framing_check.json'
    if args.build:
        output.write_text(rendered)
    elif not output.exists() or output.read_text() != rendered:
        raise SystemExit('Missing or stale output; review then use --build.')
    print(json.dumps({key: {'units': len(data[key]['units']), 'stop': data[key]['stop']}
                      for key in ('from_opening', 'local_probe')}, indent=2))
