"""Behavioral checks for conservative replay; run python3 -m unittest -v."""
import itertools
import unittest
import decode
import analyze_boundaries as boundaries


class ReplayTests(unittest.TestCase):
    def rows(self, *texts):
        return [{'id':f'P1-R{i:02}', 'text':text} for i,text in enumerate(texts,1)]

    def replay(self, rows, main=None, second=None, plans=None):
        return decode.replay(rows, {'main':main or {},'second':second or {}},plans or [])

    def candidates(self, segments):
        return [s for s in segments if s['kind']=='decoded_candidate']

    def plan(self, start, end, codes, row='P1-R01'):
        return {'id':'example','start':{'row':row,'character':start},
                'end':{'row':row,'character':end},'table':'second','codes':codes,
                'basis':'Test fixture'}

    def test_unseparated_row_join_retains_exact_source(self):
        source,segments=self.replay(self.rows('5','521,'),main={'5521':'Marechal'})
        unit=self.candidates(segments)[0]['units'][0]
        self.assertEqual(unit['code'],'5521')
        self.assertEqual(unit['source'],'5\n521')
        self.assertEqual(unit['end'],{'row':'P1-R02','character':3})
        self.assertEqual(''.join(s['source'] for s in segments),source.text)

    def test_row_break_does_not_require_joining_a_unit(self):
        _,segments=self.replay(self.rows('437','040'),main={'437':'er','040':'wie'})
        self.assertEqual([u['code'] for u in self.candidates(segments)[0]['units']],['437','040'])

    def test_recorded_separator_prevents_automatic_join(self):
        _,segments=self.replay(self.rows('5,','521'),main={'5521':'Marechal'})
        self.assertFalse(self.candidates(segments))

    def test_whole_parse_overrides_greedy_prefix(self):
        _,segments=self.replay(self.rows('7775'),main={'777':'lich','7775':'ge / gen'})
        self.assertEqual(self.candidates(segments)[0]['literal'],'ge / gen')

    def test_two_full_segmentations_remain_ambiguous(self):
        _,segments=self.replay(self.rows('1234567'),main={'123':'a','4567':'b','1234':'c','567':'d'})
        self.assertEqual(segments[0]['kind'],'ambiguous')
        self.assertEqual(segments[0]['full_parse_count'],2)

    def test_shared_code_does_not_select_a_table(self):
        _,segments=self.replay(self.rows('066'),main={'066':'sein'},second={'066':'vor'})
        self.assertEqual(segments[0]['kind'],'ambiguous')
        self.assertEqual(segments[0]['full_parse_count'],2)

    def test_partial_known_suffix_is_not_silently_resynchronized(self):
        _,segments=self.replay(self.rows('9123'),main={'123':'word'})
        self.assertEqual(segments[0]['kind'],'unresolved')
        self.assertEqual(segments[0]['source'],'9123')

    def test_explicit_name_span_records_crossed_comma(self):
        text='1015,33005714,771,336'
        values={'101':'ab','533':'be','005':'de','714':'ber','771':'ni','336':'s'}
        _,segments=self.replay(self.rows(text),second=values,
                plans=[self.plan(1,len(text),list(values))])
        segment=segments[0]
        self.assertEqual(segment['literal'],'abbedebernis')
        self.assertEqual(segment['marks'][0]['at_code_boundary'],False)
        self.assertEqual(segment['units'][1]['source'],'5,33')
        self.assertEqual(segment['table_selection'],'explicit_span_hypothesis')

    def test_digit_alternatives_and_glyphs_are_not_deleted(self):
        text='1[2|3]4<G1>567'
        source,segments=self.replay(self.rows(text),main={'124':'x','567':'y'})
        self.assertEqual(''.join(s['source'] for s in segments),text)
        self.assertEqual([s['source'] for s in segments if s['kind']=='uncertain_digits'],['[2|3]'])
        self.assertEqual([s['source'] for s in segments if s['kind']=='glyph'],['<G1>'])
        self.assertEqual([s['literal'] for s in self.candidates(segments)],['y'])
        with self.assertRaisesRegex(ValueError,'uncertain digits or glyphs'):
            self.replay(self.rows(text),second={'124':'x','567':'y'},
                        plans=[self.plan(1,len(text),['124','567'])])

    def test_uncertain_separator_is_not_automatically_removed(self):
        _,segments=self.replay(self.rows('1[,?]23'),main={'123':'x'})
        self.assertFalse(self.candidates(segments))
        _,segments=self.replay(self.rows('1[,?]23'),second={'123':'x'},
                              plans=[self.plan(1,7,['123'])])
        self.assertEqual(segments[0]['literal'],'x')
        self.assertEqual(segments[0]['marks'][0]['kind'],'uncertain_separator')

    def test_explicit_span_must_match_digits(self):
        with self.assertRaisesRegex(ValueError,'exact source digits'):
            self.replay(self.rows('123'),second={'124':'x'},plans=[self.plan(1,3,['124'])])

    def test_overlapping_spans_fail(self):
        a=self.plan(1,3,['123'])
        b=dict(self.plan(2,4,['234']),id='other')
        with self.assertRaisesRegex(ValueError,'Overlapping'):
            self.replay(self.rows('1234'),second={'123':'a','234':'b'},plans=[a,b])

    def test_invalid_or_duplicate_span_fails(self):
        a=self.plan(1,3,['123'])
        with self.assertRaisesRegex(ValueError,'Duplicate'):
            self.replay(self.rows('123'),second={'123':'a'},plans=[a,a])
        with self.assertRaisesRegex(ValueError,'Invalid source coordinate'):
            self.replay(self.rows('123'),second={'123':'a'},plans=[self.plan(0,3,['123'])])

    def test_unknown_value_is_not_a_null(self):
        _,segments=self.replay(self.rows('409'),main={'409':'?'})
        self.assertEqual(segments[0]['literal'],'?')
        self.assertTrue(segments[0]['units'][0]['qualified_value'])

    def test_partial_anchor_keeps_both_residual_fragments(self):
        text='91238'
        _,segments=self.replay(self.rows(text),second={'123':'word'},plans=[self.plan(2,4,['123'])])
        self.assertEqual([(s['kind'],s['source']) for s in segments],
                         [('unresolved','9'),('decoded_candidate','123'),('unresolved','8')])

    def test_empty_or_unrecognized_source_cannot_hide_text(self):
        source,segments=self.replay(self.rows(''))
        self.assertEqual(segments,[])
        with self.assertRaisesRegex(ValueError,'Unrecognized source'):
            self.replay(self.rows('123!'),main={'123':'word'})


class ParseTests(unittest.TestCase):
    def test_dynamic_parse_count_matches_exhaustive_enumeration(self):
        keys={'1':'a','11':'b','2':'c'}
        def brute(text):
            if not text:return 1
            return sum(brute(text[len(k):]) for k in keys if text.startswith(k))
        for width in range(1,8):
            for chars in itertools.product('12',repeat=width):
                text=''.join(chars)
                self.assertEqual(boundaries.parses(text,keys)['full_parse_count'],brute(text))

    def test_frozen_data_accounting_and_conditional_anchors(self):
        import json
        reports=decode.make_reports()
        result=json.loads(reports['output/decoding.json'])
        _,rows=boundaries.load()
        self.assertEqual(''.join(s['source'] for s in result['segments']),
                         '\n'.join(r['text'] for r in rows))
        self.assertFalse(result['summary']['complete_decipherment'])
        self.assertFalse(result['summary']['global_switch_rule_established'])
        self.assertEqual(result['summary']['cross_row_units'],12)
        self.assertEqual(result['summary']['source_separators_inside_candidate_units'],3)
        checks={v['id']:v for v in result['validation']}
        self.assertEqual(checks['second_bernis']['matches'][0]['literal'],'abbedebernis')
        self.assertEqual(checks['second_bernis']['comparison'],'editorial_difference')
        self.assertEqual(checks['bezahlung']['comparison'],'editorial_difference')
        self.assertEqual(checks['stainville']['comparison'],'qualified_key_value')


if __name__=='__main__':
    unittest.main()
