#!/usr/bin/env python3
"""Import Norbert's completed XLSX worksheet and compare its literal readings.

Only Python's standard library is needed. The XLSX stays outside the repository:
its text, formulas, cached readings and cell references are retained in sources/.
"""
import argparse
import csv
import difflib
import hashlib
import json
import posixpath
import re
import zipfile
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
LINE_IDS = [f'P{p}-R{r:02}' for p, count in enumerate((6, 21, 21, 4), 1)
            for r in range(1, count + 1)]


def read_xlsx(path):
    """Read cell text and cached formula values without evaluating formulas."""
    with zipfile.ZipFile(path) as archive:
        strings = []
        if 'xl/sharedStrings.xml' in archive.namelist():
            strings = [''.join(t.text or '' for t in si.iterfind('.//m:t', NS))
                       for si in ET.fromstring(archive.read('xl/sharedStrings.xml'))]
        relations = {r.attrib['Id']: r.attrib['Target'] for r in
                     ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))}
        result = {}
        for sheet in ET.fromstring(archive.read('xl/workbook.xml')).findall('m:sheets/m:sheet', NS):
            target = relations[sheet.attrib['{' + NS['r'] + '}id']]
            target = target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/' + target)
            cells = {}
            for c in ET.fromstring(archive.read(target)).findall('.//m:sheetData/m:row/m:c', NS):
                value = c.find('m:v', NS)
                value = value.text if value is not None else ''
                kind = c.get('t')
                if kind == 's':
                    value = strings[int(value)]
                elif kind == 'inlineStr':
                    value = ''.join(t.text or '' for t in c.findall('.//m:t', NS))
                formula = c.find('m:f', NS)
                if value or formula is not None:
                    cells[c.attrib['r']] = {'value': value or '', 'type': kind or 'n',
                                            'formula': '=' + formula.text if formula is not None else ''}
            result[sheet.attrib['name']] = cells
    return result


def code_text(value):
    if not re.fullmatch(r'[0-9]{1,4}', value):
        raise ValueError('Invalid worksheet code: ' + repr(value))
    return value.zfill(3)


def extract(sheets):
    import audit
    readings, groups, annotations = [], [], []
    for sheet, table, note_col in [('clavis prima', 'prima', 'D'), ('clavis 2da', 'secunda', 'C')]:
        cells = sheets[sheet]
        for address, cell in cells.items():
            if not re.fullmatch(r'A[0-9]+', address) or not cell['value'].isdigit():
                continue
            row = address[1:]
            code = code_text(cell['value'])
            if len(code) != audit.width(code[0], table):
                raise ValueError(f'Invalid {table} code at {address}: {code}')
            value = cells.get('B' + row, {}).get('value', '')
            if not value.strip():
                raise ValueError(f'Missing reading at {sheet}!B{row}')
            readings.append({'table': table, 'code': code, 'value': value,
                             'worksheet': sheet, 'code_cell': address, 'value_cell': 'B' + row,
                             'notes_cell': note_col + row,
                             'notes': cells.get(note_col + row, {}).get('value', ''),
                             'occurrences': cells.get('C' + row, {}).get('value', '') if table == 'prima' else ''})
    identities = {(r['table'], r['code']) for r in readings}
    if len(identities) != len(readings):
        raise ValueError('Duplicate worksheet key entry')
    cells = sheets['decryption']
    used = set()
    for line, row in zip(LINE_IDS, range(2, 258, 5)):
        block = []
        for address, cell in cells.items():
            match = re.fullmatch(r'([A-Z]+)' + str(row), address)
            if not match or not cell['value'].isdigit():
                continue
            col = match[1]
            state_cell, reading_cell = col + str(row + 1), col + str(row + 2)
            state = cells.get(state_cell, {}).get('value')
            if state not in ('1', '2'):
                raise ValueError('Missing worksheet table state at ' + state_cell)
            cached = cells.get(reading_cell, {})
            code = code_text(cell['value'])
            table = 'prima' if state == '1' else 'secunda'
            if len(code) != audit.width(code[0], table):
                raise ValueError('Invalid grouped code at ' + address)
            block.append({'line': line, 'worksheet_row': str(row), 'code_cell': address,
                          'table_cell': state_cell, 'reading_cell': reading_cell,
                          'table': table, 'code': code, 'cached_reading': cached.get('value', ''),
                          'formula': cached.get('formula', '')})
            used.update((address, state_cell, reading_cell))
        if not block:
            raise ValueError('Missing decryption block at row ' + str(row))
        # Worksheet XML order is not guaranteed to be column order.
        def column_number(record):
            n = 0
            for ch in re.match('[A-Z]+', record['code_cell'])[0]:
                n = n * 26 + ord(ch) - ord('A') + 1
            return n
        groups.extend(sorted(block, key=column_number))
    for address, cell in cells.items():
        if address not in used and not cell['formula'] and cell['value']:
            annotations.append({'worksheet': 'decryption', 'cell': address, 'text': cell['value']})
    if any((g['table'], g['code']) not in identities for g in groups):
        raise ValueError('Grouped ciphertext references a missing worksheet key entry')
    return readings, groups, annotations


def write_csv(path, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def load_sources(root=ROOT):
    def read(name):
        with (root / 'sources' / name).open(newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    meta = json.loads((root / 'sources/norbert_workbook.json').read_text(encoding='utf-8'))
    return meta, read('norbert_key.csv'), read('norbert_decryption.csv'), read('norbert_notes.csv')


def classify(value):
    controls = {'-': ('null', 'NULL', '', ''), 'Comma': ('punctuation', 'COMMA', '', 'comma'),
                'punctum': ('punctuation', 'FULL_STOP', '', 'period'),
                'media nota': ('punctuation', 'SEMICOLON', '', 'semicolon'),
                'indic. clav. 2dam': ('switch', 'SWITCH_SECUNDA', 'secunda', ''),
                'indic. clav. 1Mam': ('switch', 'SWITCH_PRIMA', 'prima', '')}
    return controls.get(value.strip(), ('lexical', value.strip(), '', ''))


def merge_key(readings, retrieved, entries):
    old = {(e['table'], e['code']): e for e in entries}
    for row in readings:
        identity = row['table'], row['code']
        previous = old.get(identity, {})
        kind, value, target, punctuation = classify(row['value'])
        note = row['notes'].strip()
        uncertain = ('?' in value or '[' in value or
                     any(term in note.lower() for term in ('uncertain', 'unsure', 'illegible', 'first entry')))
        partial = not uncertain and bool(note) and any(term in note.lower() for term in ('can’t read', "can't read"))
        same_confirmed = (previous.get('value') == value and previous.get('review_status') == 'source_read'
                          and previous.get('human_confirmed', '').startswith('Yes') and not partial)
        probability = 'Low' if uncertain else previous['probability'] if same_confirmed else 'Moderate'
        credit = ('Partial — Norbert' if uncertain or partial else 'Yes — Norbert')
        detail = note or ('prior human confidence retained' if probability == 'High' else 'confidence not stated')
        credit += ' (completed worksheet; ' + detail + ')'
        if same_confirmed and 'Robert' in previous['human_confirmed']:
            credit = re.match(r'Yes — Robert[^;]*', previous['human_confirmed'])[0] + '; ' + credit
        old[identity] = {'table': row['table'], 'code': row['code'], 'value': value, 'kind': kind,
                         'review_status': 'provisional' if uncertain else 'source_read',
                         'probability': probability, 'human_confirmed': credit,
                         'source': f"Norbert worksheet ({retrieved}), '{row['worksheet']}'!{row['value_cell']}",
                         'target': target, 'punctuation_kind': punctuation}
    return sorted(old.values(), key=lambda e: (e['table'], int(e['code'])))


def worksheet_trace(groups, keys):
    import audit
    stream = ''.join(g['code'] for g in groups)
    locations = [(g['code_cell'], offset + 1) for g in groups for offset in range(len(g['code']))]
    trace = audit.scan(stream, locations, 0, 'prima', audit.source_controls(keys))
    return trace, locations


def comparison(entries, keys, root=ROOT):
    import audit
    meta, readings, groups, annotations = load_sources(root)
    source_keys = {(r['table'], r['code']): r for r in readings}
    if len(source_keys) != len(readings):
        raise ValueError('Duplicate imported key entry')
    trace, sheet_locations = worksheet_trace(groups, keys)
    continuous = (trace['stop']['reason'] == 'end_of_stream' and len(trace['units']) == len(groups)
                  and all((u['table'], u['code']) == (g['table'], g['code'])
                          for u, g in zip(trace['units'], groups)))
    mismatches = [r for r in readings if (r['table'], r['code']) not in keys or
                  classify(r['value']) != tuple(keys[r['table'], r['code']][field]
                                               for field in ('kind', 'value', 'target', 'punctuation_kind'))]
    provisional = [r for r in readings if keys.get((r['table'], r['code']), {}).get('review_status') == 'provisional']
    table_counts = {t: sum(r['table'] == t for r in readings) for t in ('prima', 'secunda')}
    switches = sum(bool(u['indicator_target']) for u in trace['units'])
    blocks = len({g['line'] for g in groups})
    lines = ['# Norbert worksheet comparison', '',
             f"Source: Norbert’s completed worksheet, retrieved {meta['retrieved_date']}. "
             f"Workbook SHA-256: `{meta['sha256']}`. Text-only snapshots are in [sources](../sources).", '',
             f"Imported **{len(readings)} key readings** ({table_counts['prima']} Prima, {table_counts['secunda']} Secunda) "
             f"and **{len(groups)} cipher groups** in {blocks} worksheet blocks. "
             f"**{len(mismatches)} key differences** from the imported source; "
             f"**{len(provisional)} provisional key readings** retain explicit uncertainty.", '',
             'Worksheet groups are replayed from Prima using the repository’s length and switch rules. ' +
             (f'All {len(groups)} groups and {switches} table transitions agree with the worksheet’s stated tables.' if continuous else
              'The grouped replay disagrees with the worksheet; review the group table below.'), '',
             '**This is a replay of Norbert’s grouped transcription.** The reviewed manuscript transcription in '
             '[ciphertext.txt](../ciphertext.txt) still differs. The conservative manuscript replay and its stopping '
             'points remain in [historical_reading.md](historical_reading.md). Group framing does not verify '
             'handwriting, expand word endings or authenticate the interlinear prose.', '',
             'Codes retain leading zeros. `-`, `Comma`, `punctum`, `media nota` and the two `indic. clav.` '
             'entries map to existing null, punctuation and switch operations. Other values retain their literal '
             'alternatives. Cached workbook results are recorded as cached values, not newly evaluated formulas.', '',
             'Worksheet block labels follow manuscript page order. A block may include the end of a code printed '
             'on the next physical row. Email interlinear line breaks are independent of these block labels.', '',
             '## Worksheet annotations', '', '| Cell | Norbert’s note |', '| --- | --- |']
    for note in annotations:
        lines.append('| ' + note['cell'] + ' | ' + audit.cell(note['text']) + ' |')
    lines += ['', 'The `028` and `8835` notes describe proposed corrections to enciphering. Both actual groups '
              'remain in the imported stream. The green `3333,7768` correction is already present in the '
              'repository. `771?` and the isolated `?` remain source notes.', '',
              '## Differences in the digit streams', '',
              'The table aligns the projected manuscript stream with the workbook stream using character '
              'sequence matching. It lists candidate changes, including unresolved source signs (`#`), '
              'without changing the manuscript transcription. Coordinates are one-based characters after '
              'the row label, or one-based digits within a worksheet code cell. Insertions are shown before '
              'the given manuscript coordinate. Repeated digits can make an edit boundary ambiguous.', '']
    manuscript_rows = [line.split('\t', 1) for line in (root / 'ciphertext.txt').read_text().splitlines()]
    raw, raw_locations = audit.project(manuscript_rows)
    stream = ''.join(g['code'] for g in groups)
    edits = [op for op in difflib.SequenceMatcher(None, raw, stream, autojunk=False).get_opcodes() if op[0] != 'equal']
    lines += [f'{len(edits)} candidate edit spans. Manuscript projection: {len(raw)} characters; '
              f'worksheet: {len(stream)} digits.', '',
              '| Operation | Manuscript start | Manuscript digits/signs | Worksheet start | Worksheet digits |',
              '| --- | --- | --- | --- | --- |']
    for tag, i, j, a, b in edits:
        left = ':'.join(map(str, raw_locations[i])) if i < len(raw_locations) else 'end'
        right = ':'.join(map(str, sheet_locations[a])) if a < len(sheet_locations) else 'end'
        lines.append(f'| {tag} | {left} | `{raw[i:j] or "∅"}` | {right} | `{stream[a:b] or "∅"}` |')
    lines += ['', '## Literal group comparison', '',
              '“Agrees” compares the imported key with the literal lookup. “Provisional” preserves uncertainty '
              'in a source reading. Missing or different cached values are called out separately. '
              'These labels are not a prose accuracy score.', '',
              '| Block | Code cell | Table | Code | Worksheet cached reading | Repository reading / operation | Status |',
              '| --- | --- | --- | --- | --- | --- | --- |']
    for group in groups:
        identity = group['table'], group['code']
        entry = keys.get(identity)
        source = source_keys.get(identity)
        status = 'Missing key' if entry is None else 'Key differs' if source is None or classify(source['value']) != tuple(
            entry[field] for field in ('kind', 'value', 'target', 'punctuation_kind')) else (
            'Provisional' if entry['review_status'] == 'provisional' else 'Agrees')
        if source is not None and group['cached_reading'].strip() != source['value'].strip():
            status += '; cached value differs' if group['cached_reading'] else '; no cached value'
        values = [group['line'], group['code_cell'], group['table'], '`' + group['code'] + '`',
                  group['cached_reading'] or '[no cached value]', audit.render_entry(entry) or '[missing]', status]
        lines.append('| ' + ' | '.join(audit.cell(v) for v in values) + ' |')
    lines += ['', '## Interlinear reading', '',
              'Norbert’s supplied email text, including page breaks, uncertainty and `[ciphertext: …]` '
              'annotations, is preserved in [norbert_interlinear.txt](../sources/norbert_interlinear.txt). '
              '[READING.md](../READING.md) uses the new reading and identified ciphertext corrections in '
              'the editorial edition. It still requires phrase-by-phrase alignment.']
    return '\n'.join(lines) + '\n'


def main():
    import audit
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workbook', type=Path, help='Downloaded Norbert worksheet XLSX')
    parser.add_argument('--retrieved', default=date.today().isoformat(), help='Retrieval date (YYYY-MM-DD)')
    args = parser.parse_args()
    date.fromisoformat(args.retrieved)
    readings, groups, annotations = extract(read_xlsx(args.workbook))
    entries, _ = audit.load_key()
    updated = merge_key(readings, args.retrieved, entries)
    # Validate the merged key and replay in a disposable directory before replacing repository data.
    import tempfile
    with tempfile.TemporaryDirectory() as folder:
        candidate = Path(folder)
        write_csv(candidate / 'working_key.csv', updated)
        _, keys = audit.load_key(candidate)
        trace, _ = worksheet_trace(groups, keys)
        if trace['stop']['reason'] != 'end_of_stream' or [(u['table'], u['code']) for u in trace['units']] != [
                (g['table'], g['code']) for g in groups]:
            raise ValueError('Worksheet table states do not match continuous replay')
    source_dir = ROOT / 'sources'
    source_dir.mkdir(exist_ok=True)
    write_csv(source_dir / 'norbert_key.csv', readings)
    write_csv(source_dir / 'norbert_decryption.csv', groups)
    write_csv(source_dir / 'norbert_notes.csv', annotations)
    metadata = {'source_filename': "Starhemberg - Norbert's worksheet.xlsx",
                'retrieved_date': args.retrieved, 'sha256': hashlib.sha256(args.workbook.read_bytes()).hexdigest(),
                'key_entries': len(readings), 'cipher_groups': len(groups), 'worksheet_blocks': len(LINE_IDS),
                'interlinear_source': 'Norbert email supplied by Robert in the 4 October 2026 update',
                'images_included': False}
    (source_dir / 'norbert_workbook.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    write_csv(ROOT / 'working_key.csv', updated)
    print(f'Imported {len(readings)} key readings and {len(groups)} groups. Run python3 audit.py --build.')


if __name__ == '__main__':
    main()
