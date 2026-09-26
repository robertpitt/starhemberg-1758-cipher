import copy
import json
import unittest

from decode_historical import (ROOT, apply_amendments, generate, render_entry,
                               render_edition, source_controls, validate_key)


class HistoricalReplayChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = json.loads((ROOT / 'historical_key.json').read_text())
        cls.keys = validate_key(cls.document)
        cls.files, cls.report = generate()

    def test_review_changes_only_the_authorized_span(self):
        original = [line.split('\t', 1) for line in (ROOT / 'ciphertext.txt').read_text().splitlines()]
        snapshot = copy.deepcopy(original)
        amendments = json.loads((ROOT / 'ciphertext_emendations.json').read_text())['amendments']
        reviewed = apply_amendments(original, amendments)
        self.assertEqual(original, snapshot)
        changed = [(a[0], a[1], b[1]) for a, b in zip(original, reviewed) if a != b]
        self.assertEqual(len(changed), 1)
        self.assertEqual(changed[0][0], 'P3-R02')
        self.assertTrue(changed[0][2].endswith('1158,412,929,2215,112'))
        self.assertEqual(dict(reviewed)['P1-R05'], dict(original)['P1-R05'])

    def test_amendments_cannot_be_reapplied_or_overlap(self):
        amendment = dict(id='test', status='human_confirmed', row='a', start=2,
                         end=4, original='234', replacement='99')
        with self.assertRaises(ValueError):
            apply_amendments([['a', '1995']], [amendment])
        with self.assertRaises(ValueError):
            apply_amendments([['a', '12345']], [amendment, amendment])
        amendment['status'] = 'suggested'
        with self.assertRaises(ValueError):
            apply_amendments([['a', '12345']], [amendment])

    def test_reviewed_transition_returns_to_prima(self):
        trace = self.report['traces']['transition_probe']
        self.assertEqual([(u['table'], u['code']) for u in trace['units']],
                         [('prima', '1158'), ('prima', '412'), ('secunda', '929'),
                          ('secunda', '2215'), ('prima', '1121'), ('prima', '221')])
        self.assertEqual(trace['units'][3]['reading'], '→ prima')
        self.assertEqual(trace['stop']['candidate'], '5394')
        self.assertEqual(trace['units'][4]['end'], ('P3-R03', 1))

    def test_no_repair_or_supplied_value_fills_a_source_gap(self):
        trace = self.report['traces']['opening']
        self.assertEqual(trace['stop']['candidate'], '7685')
        self.assertEqual(trace['stop']['location'], ('P1-R05', 43))
        # The supplied CSV says 1115=ten; the source has not been authenticated.
        entry = next(u for u in trace['units'] if u['code'] == '1115')
        self.assertIsNone(entry['reading'])
        self.assertEqual(entry['review_status'], 'missing')
        self.assertFalse(self.report['complete_decipherment'])

    def test_provisional_indicator_does_not_change_state(self):
        keys = copy.deepcopy(self.keys)
        keys[('prima', '412')]['review_status'] = 'provisional'
        self.assertNotIn('412', source_controls(keys)['prima'])
        self.assertIn('2215', source_controls(keys)['secunda'])
        self.assertTrue(render_entry(keys[('prima', '412')]).startswith('[provisional:'))

    def test_bad_control_or_crop_is_rejected(self):
        for field, value in [('target', 'third'), ('crop_box_xyxy', [-1, 0, 20, 20])]:
            document = copy.deepcopy(self.document)
            entry = next(e for e in document['entries'] if e['kind'] == 'switch')
            entry[field] = value
            with self.assertRaises(ValueError):
                validate_key(document)

    def test_generated_artifacts_are_current(self):
        for name, expected in self.files.items():
            with self.subTest(name=name):
                self.assertEqual((ROOT / name).read_text(), expected)

    def test_worked_example_retains_duplicate_and_switch(self):
        result = json.loads(self.files['output/r1588_example_check.json'])
        self.assertEqual(result['trace']['stop']['reason'], 'end_of_stream')
        units = result['trace']['units']
        self.assertEqual(sum(u['code'] == '240' for u in units), 2)
        switch = next(i for i, u in enumerate(units) if u['code'] == '477')
        self.assertEqual(units[switch]['indicator_target'], 'secunda')
        self.assertTrue(all(u['table'] == 'secunda' for u in units[switch + 1:]))
        self.assertEqual(result['continuous_vs_annotated_differences'][0]['continuous_codes'], ['240'])

    def test_partial_human_readings_remain_provisional(self):
        for code, reading in [('1121', 'C - C[r|k]'), ('210', 'Wum[b|g]')]:
            entry = self.keys[('prima', code)]
            self.assertEqual(entry['value'], reading)
            self.assertEqual(entry['human_review']['transcription'], reading)
            self.assertEqual(entry['review_status'], 'provisional')
            units = [u for trace in self.report['traces'].values() for u in trace['units']]
            unit = next(u for u in units if u['table'] == 'prima' and u['code'] == code)
            self.assertEqual(unit['reading'], '[provisional: ' + reading + ']')

    def test_translation_requires_review_after_key_or_status_change(self):
        edition = json.loads((ROOT / 'reading_edition.json').read_text())
        for field, value in [('reading', 'anderes'), ('review_status', 'provisional')]:
            traces = copy.deepcopy(self.report['traces'])
            unit = next(u for u in traces['opening']['units'] if u['code'] == '405')
            unit[field] = value
            with self.assertRaisesRegex(ValueError, 'Review translation'):
                render_edition(edition, traces)


if __name__ == '__main__':
    unittest.main()
