import unittest

from check_r1588_framing import scan
from check_supplied_indicators import project


class FramingChecks(unittest.TestCase):
    controls = {'prima': {'412': 'secunda'}, 'secunda': {'2215': 'prima'}}

    def test_control_crosses_row_and_changes_next_group_length(self):
        stream, locations = project([('a', '1158,41'), ('b', '2,533,2215,448')])
        result = scan(stream, locations, 0, 'prima', self.controls)
        self.assertEqual([(u['table'], u['code']) for u in result['units']],
                         [('prima', '1158'), ('prima', '412'), ('secunda', '533'),
                          ('secunda', '2215'), ('prima', '448')])
        self.assertEqual(result['units'][1]['start'], ('a', 6))
        self.assertEqual(result['units'][1]['end'], ('b', 1))
        self.assertEqual(result['stop']['reason'], 'end_of_stream')

    def test_no_join_through_uncertain_digit(self):
        stream, locations = project([('a', '1158,4[1|2]2,533')])
        result = scan(stream, locations, 0, 'prima', self.controls)
        self.assertEqual([u['code'] for u in result['units']], ['1158'])
        self.assertEqual(result['stop']['reason'], 'uncertain_source')

    def test_unverified_form_is_not_repaired_or_skipped(self):
        stream, locations = project([('a', '768,5512,020')])
        result = scan(stream, locations, 0, 'prima', self.controls)
        self.assertEqual(result['units'], [])
        self.assertEqual(result['stop']['candidate'], '7685')
        self.assertEqual(result['stop']['reason'], 'unverified_four_digit_form')


if __name__ == '__main__':
    unittest.main()
