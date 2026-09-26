"""Checks for the source-linked exclusion test, including historical controls."""
import unittest

from check_historical_codebook import edges, explore, report


class HistoricalCodebookTests(unittest.TestCase):
    def test_historical_worked_example(self):
        self.assertTrue(report()['historical_example']['expected_path_accepted'])

    def test_nulls_must_not_interrupt_long_payload(self):
        self.assertEqual(edges('31888', 0), [(5, 'long', '31888')])
        self.assertFalse(explore('3881126')['complete_path'])

    def test_three_in_second_pair_position_is_not_an_indicator(self):
        self.assertTrue(explore('2331126')['complete_path'])

    def test_optional_nulls_inside_pair_are_explored(self):
        self.assertTrue(explore('2884', True)['complete_path'])
        self.assertFalse(explore('2884', False)['complete_path'])

    def test_special_eight_code_and_null_paths_are_both_available(self):
        self.assertEqual(edges('876', 0), [(1, 'null', '8'), (3, 'special', '876')])
        self.assertTrue(explore('899')['complete_path'])
        self.assertTrue(explore('900')['complete_path'])

    def test_no_dropped_digit_resynchronization(self):
        self.assertFalse(explore('33236')['complete_path'])
        self.assertFalse(explore('2033236')['complete_path'])

    def test_source_fails_both_permissive_variants(self):
        result = report()
        self.assertEqual(result['result'], 'direct_application_rejected')
        for variant in result['variants'].values():
            self.assertEqual(variant['digit_count'], 1341)
            self.assertEqual(variant['furthest_digit_boundary'], 117)
            self.assertEqual(variant['furthest_stop'],
                             {'row': 'P1-R03', 'source_character_1based': 17})


if __name__ == '__main__':
    unittest.main()
