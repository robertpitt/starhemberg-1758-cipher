#!/usr/bin/env python3
"""Test direct applicability of DECODE 1695/1698 without changing the cipher.

This is a deliberately permissive syntax exclusion test, not a decoder.
Acceptance is not evidence of a decipherment. Rejection excludes direct use
under the stated assumptions; it cannot exclude an undocumented transformation.
Only the certain P1/P2 transcription is tested. Standard library, Python 3.9+.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED_CIPHER_HASH = '66e550b75db3d7e7dc1b41cb724c5628885ce4cb66535f49acb49c09e96bcedc'


def edges(digits, i, internal_nulls=True):
    """Return all permissive token edges at a digit boundary.

    Superset of the photographed inventory: any ordinary pair whose first
    digit is neither 3 nor 8 (even unlisted pairs); any 31xxx, plus 30000;
    any 8xx and 900; standalone 8. Optional 8s inside an ordinary pair are
    also allowed. No null may interrupt the four-digit payload after 3.
    The table state is deliberately unrestricted: both tables share the
    code shapes, and any putative 8xx switch is already admitted.
    """
    if i >= len(digits):
        return []
    result = []
    first = digits[i]
    if first == '8':
        result.append((i + 1, 'null', '8'))
        if i + 3 <= len(digits):
            result.append((i + 3, 'special', digits[i:i + 3]))
    elif first == '3':
        code = digits[i:i + 5]
        if len(code) == 5 and (code == '30000' or code.startswith('31')):
            result.append((i + 5, 'long', code))
    else:
        if i + 2 <= len(digits):
            result.append((i + 2, 'pair', digits[i:i + 2]))
        if internal_nulls:
            j = i + 1
            while j < len(digits) and digits[j] == '8':
                j += 1
            if j > i + 1 and j < len(digits):
                result.append((j + 1, 'pair_with_internal_nulls', first + digits[j]))
        if digits[i:i + 3] == '900':
            result.append((i + 3, 'special', '900'))
    return result


def explore(digits, internal_nulls=True):
    """DAG reachability explores all paths; stores one witness per endpoint."""
    if not digits or any(c not in '0123456789' for c in digits):
        raise ValueError('Expected a nonempty ASCII digit stream')
    reached = {0}
    parents = {}
    dead_ends = []
    for i in range(len(digits)):
        if i not in reached:
            continue
        choices = edges(digits, i, internal_nulls)
        if not choices:
            dead_ends.append(i)
        for end, kind, code in choices:
            if end not in reached:
                reached.add(end)
                parents[end] = (i, kind, code)
    furthest = max(reached)
    path = []
    p = furthest
    while p:
        start, kind, code = parents[p]
        path.append({'start_digit_0based': start, 'end_digit_exclusive': p,
                     'kind': kind, 'code': code, 'surface': digits[start:p]})
        p = start
    return {'complete_path': len(digits) in reached,
            'digit_count': len(digits), 'furthest_digit_boundary': furthest,
            'dead_end_offsets': dead_ends, 'witness_to_furthest': path[::-1]}


def source_projection():
    raw = (ROOT / 'ciphertext.txt').read_bytes()
    actual_hash = hashlib.sha256(raw).hexdigest()
    if actual_hash != EXPECTED_CIPHER_HASH:
        raise ValueError('Ciphertext changed; review the source before rerunning this comparison')
    digits, locations = [], []
    for line in raw.decode('utf-8').splitlines():
        row, text = line.split(maxsplit=1)
        if not row.startswith(('P1-', 'P2-')):
            continue
        for column, char in enumerate(text, 1):
            if char in '0123456789':
                digits.append(char)
                locations.append({'row': row, 'source_character_1based': column})
            elif char not in ',. ':
                raise ValueError(f'Unexpected uncertain/non-numeric source character at {row}:{column}')
    return ''.join(digits), locations, actual_hash


def report():
    digits, locations, actual_hash = source_projection()
    variants = {}
    for name, internal in [('boundary_nulls', False), ('also_internal_nulls', True)]:
        result = explore(digits, internal)
        result['dead_ends'] = [
            {'digit_offset_0based': i, **locations[i],
             'required_five_digit_code': digits[i:i + 5],
             'reason': '3 at a unit boundary requires a long entry absent from the photographed code range'}
            for i in result.pop('dead_end_offsets')]
        if result['furthest_digit_boundary'] < len(digits):
            result['furthest_stop'] = locations[result['furthest_digit_boundary']]
        variants[name] = result

    # Manually read from R1697 I7483 P2, worked example, first cipher row.
    example_tokens = ['8', '31126', '8', '31397', '31338', '8', '31281',
                      '8', '832', '8', '31405']
    example = ''.join(example_tokens)
    cursor = 0
    for token in example_tokens:
        end = cursor + len(token)
        if not any(e == end and code == token for e, kind, code in edges(example, cursor)):
            raise AssertionError('Historical worked-example token path rejected')
        cursor = end
    if not explore(example)['complete_path']:
        raise AssertionError('Historical worked example rejected')

    return {
        'question': 'Can the photographed DECODE 1695/1698 codebook be applied directly to this ciphertext?',
        'result': 'direct_application_rejected' if all(not v['complete_path'] for v in variants.values()) else 'not_excluded',
        'ciphertext_sha256': actual_hash,
        'scope': 'P1 and P2; punctuation ignored and rows joined; no uncertain digits selected, no digits repaired',
        'test_kind': 'permissive syntax exclusion, not full decryption',
        'historical_example': {
            'source': 'R1697 I7483 P2, first cipher row',
            'tokens': example_tokens, 'expected_path_accepted': True,
            'independently_checked_prima_entries': {'31126': 'in', '31281': 'von'},
            'limitation': 'Tokenization control only; not a verified transcription of every plaintext entry'},
        'opening_comparison': {
            'forced_first_code': '20',
            'prima_value': 'Seine Excell[enz] (title; abbreviation expanded)',
            'secunda_value': 'aus',
            'letter_interlinear_opening': 'woferne',
            'sources': ['R1698 I7484 P1, first numeric column, 20',
                        'R1698 I7486 P3, first numeric column, 20',
                        'R1695 I7477 P8, Prima numeric column, 20',
                        '1758 letter, first cipher line and its interlinear reading']},
        'variants': variants,
        'limits': ['Does not exclude an undocumented recoding, a different key, or source corrections.',
                   'Does not authenticate all entries of the existing working key.',
                   'Historical table values and range observations remain human-reviewed source evidence.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', action='store_true')
    args = parser.parse_args()
    path = ROOT / 'output' / 'historical_codebook_check.json'
    payload = (json.dumps(report(), ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    if args.build:
        path.write_bytes(payload)
        print('Built output/historical_codebook_check.json')
    elif not path.exists() or path.read_bytes() != payload:
        raise SystemExit('Historical codebook report missing or stale; run with --build after review')
    else:
        print('Verified historical codebook comparison: direct application rejected under the documented assumptions')


if __name__ == '__main__':
    main()
