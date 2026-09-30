"""Guard the reviewed data and conservative replay during future updates."""
import hashlib
import unittest
import audit


class ReviewedDataTests(unittest.TestCase):
    def setUp(self):
        self.entries, self.keys = audit.load_key()

    def test_reviewed_ciphertext_and_key_coverage(self):
        self.assertEqual(hashlib.sha256((audit.ROOT / 'ciphertext.txt').read_bytes()).hexdigest(),
                         "9538a568567976c0cf93a2fff29ef4317a6eed60160f662a2c40f7b83c284e64")
        self.assertEqual((len(self.keys), len(self.entries)), (322, 384))
        self.assertEqual(sum('Norbert' in e['human_confirmed'] for e in self.entries), 122)

    def test_human_readings_and_uncertainty(self):
        self.assertEqual(self.keys['prima', '210']['value'], 'würde -n')
        self.assertEqual(self.keys['prima', '049']['review_status'], 'provisional')
        self.assertIn('illegible', self.keys['prima', '049']['human_confirmed'])
        self.assertIn('Partial', self.keys['prima', '1118']['human_confirmed'])
        self.assertEqual(self.keys['prima', '1121']['value'], 'C - C[r|k]')
        self.assertEqual(self.keys['prima', '025']['punctuation_kind'], 'comma')

    def test_norbert_followup_and_explicit_uncertainty(self):
        for code, value in [('400', 'sey -e/-n -d'), ('1115', 'te -r/-n ; t'), ('621', 'davon')]:
            self.assertEqual(self.keys['prima', code]['value'], value)
            self.assertEqual(self.keys['prima', code]['probability'], 'High')
        for code in ('248', '5512'):
            self.assertEqual(self.keys['prima', code]['review_status'], 'provisional')
            self.assertEqual(self.keys['prima', code]['probability'], 'Low')
            self.assertIn('Partial', self.keys['prima', code]['human_confirmed'])
        self.assertEqual(self.keys['prima', '629']['value'], 'aufdaß')
        row = dict(line.split('\t', 1) for line in (audit.ROOT / 'ciphertext.txt').read_text().splitlines())['P1-R03']
        self.assertEqual(row[20:23], '621')
        opening = audit.replay(self.keys)['opening']['units']
        unit = next(u for u in opening if u['start'] == ('P1-R03', 21))
        self.assertEqual((unit['code'], unit['reading']), ('621', 'davon'))

    def test_guesses_and_provisional_switches_do_not_drive_replay(self):
        self.assertNotIn(('prima', '008'), self.keys)
        self.assertNotIn('3347', audit.source_controls(self.keys)['prima'])
        self.assertNotIn('2215', audit.source_controls(self.keys)['secunda'])
        self.assertEqual(audit.source_controls(self.keys)['secunda']['018'], 'prima')

    def test_opening_stops_without_repair(self):
        opening = audit.replay(self.keys)['opening']
        self.assertEqual(len(opening['units']), 90)
        self.assertEqual(sum(len(u['code']) for u in opening['units']), 307)
        self.assertEqual(opening['stop']['candidate'], '3540')
        self.assertEqual(opening['stop']['location'], ('P2-R01', 5))
        self.assertEqual(next(u['reading'] for u in opening['units'] if u['code'] == '004'), 's ; ss')

    def test_latest_norbert_corrections_take_priority(self):
        row = dict(line.split('\t', 1) for line in (audit.ROOT / 'ciphertext.txt').read_text().splitlines())['P1-R05']
        self.assertIn('643,3333,7768,5512', row)
        self.assertNotIn('3337,768', row)
        for code, value in [('011', 'habe -n'), ('028', 'p ; pp'), ('613', 'le -t/-n -s'),
                            ('442', 'kei -t -e -n'), ('3395', 'is ; Corsi -ca')]:
            self.assertEqual(self.keys['prima', code]['value'], value)
            self.assertEqual(self.keys['prima', code]['probability'], 'High')
        for code in ('005', '3337'):
            self.assertEqual(self.keys['prima', code]['review_status'], 'provisional')
            self.assertIn('Partial', self.keys['prima', code]['human_confirmed'])

    def test_norbert_secunda_reading_keeps_state_across_rows(self):
        trace = audit.replay(self.keys)['transition_probe']
        self.assertEqual([(u['table'], u['code']) for u in trace['units']],
                         [('prima', '1158'), ('prima', '412'), ('secunda', '929'),
                          ('secunda', '2215'), ('secunda', '112'), ('secunda', '122'),
                          ('secunda', '153'), ('secunda', '946'), ('secunda', '557')])
        self.assertEqual([u['reading'] for u in trace['units'][2:8]],
                         ['gra', 'f', 'sta', 'in', 'vil', 'l(e)'])
        self.assertEqual(trace['units'][5]['start'], ('P3-R03', 1))
        self.assertEqual(trace['stop']['candidate'], '6388')
        self.assertEqual(trace['stop']['location'], ('P3-R03', 16))

    def test_secunda_reviews_do_not_require_img_marker(self):
        secunda = [e for e in self.entries if e['table'] == 'secunda' and 'Norbert' in e['human_confirmed']]
        self.assertEqual(len(secunda), 48)
        self.assertEqual(sum(e['probability'] == 'High' for e in secunda), 20)
        self.assertEqual(sum(e['probability'] == 'Moderate' for e in secunda), 27)
        self.assertEqual(self.keys['secunda', '2259']['review_status'], 'provisional')
        for code, value in [('141', 'wor'), ('353', 'und'), ('732', 'von'), ('2215', 'f')]:
            self.assertEqual(self.keys['secunda', code]['value'], value)
            self.assertEqual(self.keys['secunda', code]['kind'], 'lexical')

    def test_uncertain_digits_are_barriers(self):
        stream, locations = audit.project([('row', '01[2|3]4<G1>5[,?]06')])
        self.assertEqual(stream, '01#4#506')
        trace = audit.scan(stream, locations, 0, 'prima', audit.source_controls(self.keys))
        self.assertEqual(trace['units'], [])
        self.assertEqual(trace['stop']['reason'], 'uncertain_source')

    def test_outputs_are_current(self):
        self.assertEqual((audit.ROOT / 'output/key_review_table.md').read_text(), audit.review_table(self.entries))
        self.assertEqual((audit.ROOT / 'output/historical_reading.md').read_text(), audit.literal_reading(audit.replay(self.keys)))


if __name__ == '__main__':
    unittest.main()
