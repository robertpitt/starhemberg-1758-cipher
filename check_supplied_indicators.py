#!/usr/bin/env python3
"""Locate reviewed R1588 indicator and lexical codes without decoding the cipher."""
import argparse
import hashlib
import json
import re
from pathlib import Path

from audit import INPUT_SHA256, source_runs

ROOT = Path(__file__).resolve().parent


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


def report():
    for name, expected in INPUT_SHA256.items():
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != expected:
            raise ValueError('Unreviewed input change: ' + name)
    review_bytes = (ROOT / 'supplied_indicator_review.json').read_bytes()
    review = json.loads(review_bytes)
    colleague_bytes = (ROOT / 'satoshi_codebook_review.json').read_bytes()
    colleague_review = json.loads(colleague_bytes)
    rows = [line.split('\t', 1) for line in (ROOT / 'ciphertext.txt').read_text().splitlines()]
    by_id = dict(rows)
    stream, locations = project(rows)
    written = {}
    for row, raw in rows:
        for run in source_runs(raw):
            if run['surface'].isdigit():
                written[((row, run['start'] + 1), (row, run['end']))] = run['surface']
    candidates = [('worked_example_to_2', '025')]
    for item in review['reviews']:
        if item['id'] in ('B', 'C'):
            origin = 'table_heading_to_' + ('1' if item['id'] == 'B' else '2')
            candidates.extend((origin, code) for code in item['confirmed_codes'])
            candidates.extend((origin, code) for code in item['uncertain_codes'])
        elif item['id'] in ('E', 'F', 'G'):
            candidates.append(('lexical_' + item['context'] + '_' + item['confirmed_root'], item['code']))
    candidates.extend(('colleague_' + item['comparison_status'], item['code'])
                      for item in colleague_review['entries'])
    results = []
    for origin, code in candidates:
        pattern = ''.join('[0-9]' if ch == '?' else re.escape(ch) for ch in code)
        hits = []
        for match in re.finditer('(?=(' + pattern + '))', stream):
            start = match.start()
            found = match.group(1)
            first, last = locations[start], locations[start + len(found) - 1]
            same_row = first[0] == last[0]
            exact = written.get((first, last)) == found
            hits.append({
                'observed_digits': found,
                'start': {'row': first[0], 'character': first[1]},
                'end': {'row': last[0], 'character': last[1]},
                'exact_written_run': exact,
                'crosses_row': not same_row,
                'source_excerpt': (by_id[first[0]][first[1]-1:last[1]] if same_row else
                                   by_id[first[0]][first[1]-1:] + ' ↵ ' + by_id[last[0]][:last[1]]),
            })
        results.append({'origin': origin, 'reviewed_pattern': code,
                        'human_confirmed_complete_code': '?' not in code and not origin.startswith('colleague_'),
                        'substring_hits': len(hits),
                        'exact_written_run_hits': sum(hit['exact_written_run'] for hit in hits),
                        'hits': hits})
    return {
        'status': 'SEARCH_ONLY_NOT_DECIPHERMENT',
        'review_sha256': hashlib.sha256(review_bytes).hexdigest(),
        'colleague_review_sha256': hashlib.sha256(colleague_bytes).hexdigest(),
        'input_sha256': INPUT_SHA256,
        'method': 'Search all rows in order, ignoring separators and physical boundaries. Uncertain digit groups and G signs are barriers; uncertain separators are ignored. Preserve leading zeros. An observed comma boundary is not proof of a cipher-unit boundary.',
        'uncertain_code_policy': '?347 is a wildcard search only; matching digits do not resolve the manuscript reading.',
        'results': results,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', action='store_true', help='Write the search result')
    args = parser.parse_args()
    assert project([('x', '01[2|3]4<G1>5[,?]06')])[0] == '01#4#506'
    data = report()
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    target = ROOT / 'output' / 'supplied_indicator_search.json'
    if args.build:
        target.write_text(rendered)
    elif not target.exists() or target.read_text() != rendered:
        raise SystemExit('Search output missing or stale; use --build after review.')
    print(json.dumps({
        'status': data['status'],
        'candidates': [{key: item[key] for key in ('origin', 'reviewed_pattern',
                        'substring_hits', 'exact_written_run_hits')} for item in data['results']],
    }, indent=2))
