"""Check source fidelity, table transitions and conservative worksheet imports."""
import tempfile
import unittest
import zipfile
from pathlib import Path

import audit
import norbert


class NorbertImportTests(unittest.TestCase):
    def setUp(self):
        self.meta, self.readings, self.groups, self.notes = norbert.load_sources()
        self.entries, self.keys = audit.load_key()

    def test_all_imported_values_match_the_key(self):
        self.assertEqual((len(self.readings), len(self.groups), len(self.notes)), (445, 779, 7))
        for reading in self.readings:
            entry = self.keys[reading['table'], reading['code']]
            self.assertEqual(norbert.classify(reading['value']),
                             tuple(entry[f] for f in ('kind', 'value', 'target', 'punctuation_kind')),
                             reading['value_cell'])
            self.assertIn(reading['value_cell'], entry['source'])
        source_keys = {(r['table'], r['code']): r for r in self.readings}
        for group in self.groups:
            self.assertEqual(group['cached_reading'].strip(),
                             source_keys[group['table'], group['code']]['value'].strip(), group['code_cell'])
            self.assertTrue(group['formula'].startswith('=IF('), group['reading_cell'])

    def test_complete_group_replay_agrees_with_source_states(self):
        trace, _ = norbert.worksheet_trace(self.groups, self.keys)
        self.assertEqual(trace['stop']['reason'], 'end_of_stream')
        self.assertEqual([(u['table'], u['code']) for u in trace['units']],
                         [(g['table'], g['code']) for g in self.groups])
        switches = [(u['start'][0], u['indicator_target']) for u in trace['units'] if u['indicator_target']]
        self.assertEqual(switches, [('M142', 'secunda'), ('G232', 'prima')])
        # The finished worksheet corrects the older 2215/f + 112/sta name probe.
        name = [g for g in self.groups if g['code_cell'] in ('N142', 'O142', 'P142', 'A147', 'B147', 'C147')]
        self.assertEqual([g['code'] for g in name], ['929', '2275', '112', '122', '153', '946'])

    def test_notes_and_enciphering_errors_are_not_silent_repairs(self):
        groups = {g['code_cell']: g for g in self.groups}
        notes = {n['cell']: n['text'] for n in self.notes}
        self.assertEqual(groups['N7']['code'], '028')
        self.assertEqual(groups['D157']['code'], '8835')
        self.assertIn('038', notes['P8'])
        self.assertIn('8833', notes['R157'])
        self.assertEqual(self.keys['secunda', '8835']['value'], 'Erz -haus')
        self.assertEqual(self.keys['prima', '5512']['review_status'], 'provisional')
        self.assertIn('unsure', self.keys['prima', '5512']['human_confirmed'])
        self.assertEqual(self.keys['secunda', '050']['review_status'], 'provisional')
        self.assertIn('fold', self.keys['secunda', '050']['human_confirmed'])

    def test_import_is_idempotent_and_retains_other_reviewers(self):
        updated = norbert.merge_key(self.readings, self.meta['retrieved_date'], self.entries)
        self.assertEqual(updated, self.entries)
        for identity in [('prima', '025'), ('prima', '412'), ('secunda', '018')]:
            self.assertIn('Robert', self.keys[identity]['human_confirmed'])
            self.assertIn('Norbert', self.keys[identity]['human_confirmed'])

    def test_comparison_is_current(self):
        expected = norbert.comparison(self.entries, self.keys)
        self.assertTrue((audit.ROOT / 'output/norbert_comparison.md').read_text() == expected)

    def test_interlinear_corrections_and_uncertainty_are_preserved(self):
        text = (audit.ROOT / 'sources/norbert_interlinear.txt').read_text()
        self.assertEqual([line for line in text.splitlines() if line.startswith('(') and line.endswith('/4)')],
                         ['(1/4)', '(2/4)', '(3/4)', '(4/4)'])
        for phrase in ('[ciphertext: Herr]', '[ciphertext: Belle-Isle]', 'ehestens(?)',
                       '[ciphertext: worvon dieser Ministre mir]', '[ciphertext: damit]',
                       '[ciphertext correctly: soubisische]'):
            self.assertIn(phrase, text)

    def test_xlsx_reader_preserves_cached_values_without_evaluation(self):
        ns = norbert.NS['m']
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'fixture.xlsx'
            with zipfile.ZipFile(path, 'w') as archive:
                archive.writestr('xl/workbook.xml', f'<workbook xmlns="{ns}" xmlns:r="{norbert.NS["r"]}">'
                                 '<sheets><sheet name="test" r:id="rId1"/></sheets></workbook>')
                archive.writestr('xl/_rels/workbook.xml.rels', '<Relationships>'
                                 '<Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
                archive.writestr('xl/sharedStrings.xml', f'<sst xmlns="{ns}"><si><t>005</t></si></sst>')
                archive.writestr('xl/worksheets/sheet1.xml', f'<worksheet xmlns="{ns}"><sheetData><row r="1">'
                                 '<c r="A1" t="s"><v>0</v></c><c r="B1" t="str"><f>1+1</f><v>cached text</v></c>'
                                 '<c r="C1" t="inlineStr"><is><t>Brühl</t></is></c></row></sheetData></worksheet>')
            cells = norbert.read_xlsx(path)['test']
        self.assertEqual(cells['A1']['value'], '005')
        self.assertEqual(cells['B1']['formula'], '=1+1')
        self.assertEqual(cells['B1']['value'], 'cached text')
        self.assertEqual(cells['C1']['value'], 'Brühl')


if __name__ == '__main__':
    unittest.main()
