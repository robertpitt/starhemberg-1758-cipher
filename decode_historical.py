#!/usr/bin/env python3
"""Reproduce the source-key collation and strict historical-rule replay.

The supplied transcription/key stay frozen. Reviewed amendments create a
separate derived transcription. No old lexical guess fills a historical gap.
"""
import argparse
from collections import Counter
import csv
from difflib import SequenceMatcher
import hashlib
import json
from pathlib import Path

from audit import INPUT_SHA256
from check_r1588_framing import scan, width
from check_supplied_indicators import project

ROOT = Path(__file__).resolve().parent
PUNCTUATION = {'comma': ',', 'period': '.', 'semicolon': ';',
               'question': '?', 'parenthesis': '[parenthesis]'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def apply_amendments(rows, amendments):
    result = [list(row) for row in rows]
    by_id = dict(result)
    grouped = {}
    for item in amendments:
        if item['status'] != 'human_confirmed':
            raise ValueError('Unconfirmed amendment: ' + item['id'])
        row, start, end = item['row'], item['start'] - 1, item['end']
        if row not in by_id or not 0 <= start < end <= len(by_id[row]):
            raise ValueError('Invalid amendment coordinates')
        if by_id[row][start:end] != item['original']:
            raise ValueError('Amendment no longer matches original: ' + item['id'])
        grouped.setdefault(row, []).append(item)
    for row in result:
        items = sorted(grouped.get(row[0], []), key=lambda x: x['start'])
        if any(a['end'] >= b['start'] for a, b in zip(items, items[1:])):
            raise ValueError('Overlapping amendments')
        for item in reversed(items):
            row[1] = row[1][:item['start'] - 1] + item['replacement'] + row[1][item['end']:]
    return result


def validate_key(document):
    keys = {}
    sources = {x['file']: x for x in document['sources']}
    for entry in document['entries']:
        table, code = entry['table'], entry['code']
        identity = (table, code)
        if identity in keys or not code.isdigit() or len(code) != width(code[0], table):
            raise ValueError('Duplicate or malformed historical code: ' + str(identity))
        if entry['review_status'] not in ('source_read', 'provisional'):
            raise ValueError('Invalid review status')
        if entry['kind'] not in ('lexical', 'null', 'punctuation', 'switch', 'cancellation'):
            raise ValueError('Invalid entry kind')
        source = sources[entry['source_file']]
        x, y, xx, yy = entry['crop_box_xyxy']
        if not (0 <= x < xx <= source['size'][0] and 0 <= y < yy <= source['size'][1]):
            raise ValueError('Crop outside source: ' + str(identity))
        if entry['kind'] == 'switch' and entry['target'] == table:
            raise ValueError('Indicator points to its own table')
        if entry['kind'] == 'switch' and entry['target'] not in ('prima', 'secunda'):
            raise ValueError('Invalid indicator target')
        if entry['kind'] == 'punctuation' and entry['punctuation_kind'] not in PUNCTUATION:
            raise ValueError('Invalid punctuation kind')
        keys[identity] = entry
    return keys


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


def render_edition(edition, traces):
    lines = ['# German reading and English translation', '',
             '**Revised working edition — the complete letter is not yet validated as a continuous decipherment.**', '',
             edition['scope'], '',
             'This file is generated from `reading_edition.json` and the source-based replay. '
             'The supplied edition used by the legacy comparison is preserved in [input/supplied_reading.md](input/supplied_reading.md).', '',
             '## Source-aligned German and English extracts', '',
             'Literal entries below follow the current historical key. Normalized wording and translation are editorial interpretations; they do not fill gaps in the replay.', '']
    for excerpt in edition['excerpts']:
        units = traces[excerpt['trace']]['units']
        start = next(i for i, u in enumerate(units) if list(u['start']) == excerpt['start'])
        selected = units[start:start + len(excerpt['codes'])]
        if ([u['code'] for u in selected] != excerpt['codes'] or
                [u['reading'] for u in selected] != excerpt['expected_readings'] or
                any(u['review_status'] != 'source_read' for u in selected)):
            raise ValueError('Review translation after changed source reading: ' + excerpt['id'])
        lines += ['### ' + excerpt['id'].replace('_', ' ').title(), '',
                  f"Source: {excerpt['start'][0]}:{excerpt['start'][1]}; codes `{' / '.join(excerpt['codes'])}`.", '',
                  '**Literal:** ' + ' / '.join('{' + u['reading'] + '}' if ' / ' in u['reading'] else u['reading'] for u in selected), '',
                  '**German:** ' + excerpt['german'], '', '**English:** ' + excerpt['english'], '']
        if excerpt.get('note'):
            lines += [excerpt['note'], '']
    transition = traces['transition_probe']
    lines += ['### Corrected transition — wording unresolved', '',
              'This independent probe assumes Prima at P3-R02:50; it is not a continuation of the stopped opening trace.', '',
              '| Table | Code | Source reading / operation |', '| --- | --- | --- |']
    for unit in transition['units']:
        value = (unit['reading'] or '[untranscribed]').replace('|', '\\|')
        lines.append(f"| {unit['table']} | `{unit['code']}` | {value} |")
    lines += ['', '**German:** Graf ⟦1121: unsichere Buchstabenlesung, siehe Tabelle⟧ der ⟦Fortsetzung ungeklärt⟧.', '',
              '**English:** Count ⟦1121: uncertain letter reading, shown above⟧ ⟦der: the/who; syntax unresolved⟧ ⟦continuation unresolved⟧.', '',
              'No translation or name expansion is assigned to the uncertain letters. Controls are displayed as operations, not words.', '',
              '## German', '',
              '**Provisorischer Lesetext:** Der gesamte folgende Text bleibt eine redaktionelle Arbeitsfassung. Auch unmarkierte Wörter sind nicht durchgehend am historischen Schlüssel bestätigt. Die fortlaufende Prüfung stoppt derzeit bei P1-R05; einzelne frühere Wortlesungen sind ebenfalls offen.', '']
    for paragraph in edition['german_paragraphs']:
        lines += [paragraph, '']
    lines += ['## English', '',
              '**Provisional translation:** The whole text below translates the editorial working text, including its unverified passages. Unbracketed wording is not automatically authenticated. Continuous framing currently stops at P1-R05, with lexical gaps before that point.', '']
    for paragraph in edition['english_paragraphs']:
        lines += [paragraph, '']
    lines += ['## Reading decisions and unresolved passages', '']
    lines += ['- ' + note for note in edition['notes']]
    lines += ['', 'See the [full source replay](output/historical_reading.md), [key inventory](output/historical_key.md), and [remaining work](REMAINING_WORK.md).', '']
    return '\n'.join(lines)


def generate(root=ROOT):
    for name, expected in INPUT_SHA256.items():
        if sha(root / name) != expected:
            raise ValueError('Frozen input changed: ' + name)
    key_document = json.loads((root / 'historical_key.json').read_text())
    keys = validate_key(key_document)
    amendments = json.loads((root / 'ciphertext_emendations.json').read_text())
    original = [line.split('\t', 1) for line in (root / 'ciphertext.txt').read_text().splitlines()]
    rows = apply_amendments(original, amendments['amendments'])
    stream, locations = project(rows)
    controls = source_controls(keys)
    example = json.loads((root / 'r1588_worked_example.json').read_text())
    example_stream, example_locations = project(example['continuous_rows'])
    example_trace = scan(example_stream, example_locations, 0, 'prima', controls)
    example_codes = [unit['code'] for unit in example_trace['units']]
    differences = []
    for tag, a, b, c, d in SequenceMatcher(None, example_codes, example['annotated_codes']).get_opcodes():
        if tag != 'equal':
            differences.append({'operation': tag, 'continuous_group_index_1based': a + 1,
                                'continuous_codes': example_codes[a:b],
                                'annotated_codes': example['annotated_codes'][c:d]})
    example_missing = sorted({(u['table'], u['code']) for u in example_trace['units']
                              if (u['table'], u['code']) not in keys})
    example_provisional = sorted({(u['table'], u['code']) for u in example_trace['units']
                                  if (u['table'], u['code']) in keys and
                                  keys[(u['table'], u['code'])]['review_status'] != 'source_read'})
    example_result = {'status': 'FULL_FRAMING_WITH_SOURCE_DISCREPANCY_NOT_FULL_LEXICAL_VALIDATION',
                      'transcription_status': example['status'],
                      'trace': example_trace, 'continuous_vs_annotated_differences': differences,
                      'key_entries_missing': example_missing,
                      'key_entries_provisional': example_provisional, 'notes': example['notes']}
    traces = {}
    for name, index in [('opening', 0), ('transition_probe', locations.index(('P3-R02', 50)))]:
        trace = scan(stream, locations, index, 'prima', controls)
        for unit in trace['units']:
            entry = keys.get((unit['table'], unit['code']))
            unit['reading'] = render_entry(entry)
            unit['kind'] = entry['kind'] if entry else 'untranscribed_key_entry'
            unit['review_status'] = entry['review_status'] if entry else 'missing'
            unit['variants_complete'] = entry.get('variants_complete', False) if entry else False
        trace['assumption'] = ('Instruction-prescribed Prima at the start; no paragraph reset inferred.'
                               if name == 'opening' else
                               'Independent Prima start at P3-R02:50; this does not resume the stopped opening trace.')
        traces[name] = trace
    with (root / 'working_key.csv').open() as source:
        old = list(csv.DictReader(source))
    collation = []
    for item in old:
        table = {'main': 'prima', 'second': 'secunda'}[item['table']]
        code = item['group']
        entry = keys.get((table, code))
        status = ('source_transcribed' if entry and entry['review_status'] == 'source_read' else
                  'provisional_source_reading' if entry else
                  'incompatible_code_length' if len(code) != width(code[0], table) else
                  'needs_handwriting_review')
        row = {'table': table, 'code': code, 'supplied_value': item['value'], 'status': status,
               'source_value': entry['value'] if entry else None,
               'source_kind': entry['kind'] if entry else None}
        if entry:
            row.update(source_file=entry['source_file'], crop_box_xyxy=entry['crop_box_xyxy'])
        collation.append(row)
    counts = dict(Counter(x['status'] for x in collation))
    hashes = {name: sha(root / name) for name in
              ('historical_key.json', 'ciphertext_emendations.json', 'r1588_source_rules.json',
               'r1588_worked_example.json', 'reading_edition.json')}
    report = {'codebook_identification': 'established: R1588 / R1589',
              'status': 'PARTIAL_SOURCE_KEY_REPLAY', 'complete_decipherment': False,
              'input_sha256': INPUT_SHA256, 'source_sha256': hashes,
              'coordinate_system': 'Rows and characters refer to output/ciphertext_reviewed.txt. The exact original span and user transcription for each amendment are in ciphertext_emendations.json.',
              'policy': 'No supplied-key fallback, plaintext fitting, digit insertion, silent resynchronization, or guessed paragraph resets. Unknown lexical entries remain explicit. Non-repeated four-digit forms stop the diagnostic; cancellation scope is not inferred. Lexical readings are roots/alternatives, not a fluent edition.',
              'historical_entry_counts': dict(Counter(x['kind'] for x in keys.values())),
              'historical_review_counts': dict(Counter(x['review_status'] for x in keys.values())),
              'collation_counts': counts, 'traces': traces}
    inventory = {'status': 'EVERY_SUPPLIED_ENTRY_ACCOUNTED_FOR_NOT_EVERY_READING_RESOLVED',
                 'historical_key_sha256': hashes['historical_key.json'], 'counts': counts,
                 'entries': collation}
    md = ['# Historical-key replay', '',
          'Codebook: **R1588/R1589, identified**. The key transcription and full decipherment remain incomplete.', '',
          'Coordinates below refer to `ciphertext_reviewed.txt`; reviewed changes are recorded against the unchanged original in `ciphertext_emendations.json`.', '']
    for name, trace in traces.items():
        md += ['## ' + name.replace('_', ' ').title(), '', trace['assumption'], '',
               '| Source start | Table | Code | Source reading / operation |',
               '| --- | --- | --- | --- |']
        for unit in trace['units']:
            reading = (unit['reading'] or '[key entry not yet transcribed]').replace('|', '\\|')
            md.append(f"| {unit['start'][0]}:{unit['start'][1]} | {unit['table']} | `{unit['code']}` | {reading} |")
        md += ['', '**Stop:** `' + json.dumps(trace['stop'], ensure_ascii=False) + '`.', '']
    queue = ['# Key collation review queue', '',
             'Identification is settled. These are transcription or code-representation issues, not alternative-codebook hypotheses.', '',
             'A transcribed source entry is not a claim that every abbreviated alternative has been expanded or independently human-reviewed.', '',
             '| Table | Code | Supplied guess (not authority) | Outstanding issue |', '| --- | --- | --- | --- |']
    for row in collation:
        if row['status'] != 'source_transcribed':
            queue.append(f"| {row['table']} | `{row['code']}` | {row['supplied_value'].replace('|', '/')} | {row['status']} |")
    queue += ['', 'All source-transcribed comparisons, including changed meanings, appear in `key_collation.json`. Do not infer semantic agreement merely from the status `source_transcribed`.', '']
    missing = sorted({(u['table'], u['code']) for trace in traces.values()
                      for u in trace['units'] if u['review_status'] == 'missing'})
    queue += ['## Missing entries encountered in the current traces', '',
              'This list also includes codes absent from the supplied key. These traces stop early, so this is not an exhaustive inventory for the whole letter.', '']
    queue += [f'- {table}: `{code}`' for table, code in missing]
    queue.append('')
    queue += ['## Provisional entries in the historical key', '',
              'This includes entries absent from the supplied CSV. A partial human reading remains provisional until its letters and interpretation are resolved.', '',
              '| Table | Code | Provisional reading |', '| --- | --- | --- |']
    for (table, code), entry in sorted(keys.items()):
        if entry['review_status'] == 'provisional':
            value = entry['value'].replace('|', '\\|')
            queue.append(f'| {table} | `{code}` | {value} |')
    queue.append('')
    key_md = ['# Source key transcription', '', key_document['scope'], '',
              key_document['review_policy'], '',
              '| Table | Code | Reading / operation | Status | Source |',
              '| --- | --- | --- | --- | --- |']
    for (table, code), entry in sorted(keys.items()):
        value = render_entry(entry).replace('|', '\\|')
        key_md.append(f"| {table} | `{code}` | {value} | {entry['review_status']} | {entry['source_file']} |")
    key_md += ['', 'Exact crop coordinates, source hashes and alternative-reading notes are retained in `historical_key.json`. No image is distributed in this inventory.', '']
    example_md = ['# R1588 worked-example check', '',
                  'The complete continuous digit string frames under the recovered rules, starting in Prima and changing to Secunda at `477`. This is an assistant transcription, not a fully authenticated plaintext check.', '',
                  '| Table | Code | Key reading / operation |', '| --- | --- | --- |']
    for u in example_trace['units']:
        entry = keys.get((u['table'], u['code']))
        reading = render_entry(entry) or '[key entry not yet transcribed]'
        example_md.append(f"| {u['table']} | `{u['code']}` | {reading} |")
    example_md += ['', '**Stop:** `' + json.dumps(example_trace['stop']) + '`.', '',
                   '## Continuous string versus annotated breakdown', '',
                   'Differences are preserved, rather than corrected to make the example agree:', '',
                   '```json', json.dumps(differences, ensure_ascii=False, indent=2), '```', '']
    example_md += ['- ' + note for note in example['notes']]
    example_md += ['', 'The explicit annotation readings and source crop coordinates are in `r1588_worked_example.json`. Resolve provisional readings and compare all abbreviated alternatives with the annotations before claiming full independent validation. In particular, numerical `3372` appears to name a French minister, while the example annotation appears to name a French army; this remains an unresolved source reading or discrepancy.', '']
    render_json = lambda obj: json.dumps(obj, ensure_ascii=False, indent=2) + '\n'
    edition = json.loads((root / 'reading_edition.json').read_text())
    return {'READING.md': render_edition(edition, traces),
            'output/ciphertext_reviewed.txt': '\n'.join('\t'.join(row) for row in rows) + '\n',
            'output/historical_replay.json': render_json(report),
            'output/historical_reading.md': '\n'.join(md),
            'output/key_collation.json': render_json(inventory),
            'output/historical_key.md': '\n'.join(key_md),
            'output/r1588_example_check.json': render_json(example_result),
            'output/r1588_example_check.md': '\n'.join(example_md),
            'output/key_review_queue.md': '\n'.join(queue)}, report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', action='store_true')
    args = parser.parse_args()
    files, report = generate()
    for name, text in files.items():
        path = ROOT / name
        if args.build:
            path.write_text(text)
        elif not path.exists() or path.read_text() != text:
            raise SystemExit('Missing or stale report: ' + name)
    print(json.dumps({'status': report['status'], 'complete_decipherment': False,
                      'historical_entry_counts': report['historical_entry_counts'],
                      'collation_counts': report['collation_counts'],
                      'trace_stops': {name: trace['stop'] for name, trace in report['traces'].items()}}, indent=2))
