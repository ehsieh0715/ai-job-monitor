import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from schema import SCORED_COLUMNS
from evaluation_validation import validate_evaluations, NEEDS_JD


def record():
    r={c:'' for c in SCORED_COLUMNS}
    r.update(job_id='site:1', match_score='75', recommendation='Apply', match_summary='SQL evidence; domain gap.')
    return r


class ValidationTests(unittest.TestCase):
    def test_id_only_is_not_validated(self):
        with self.assertRaises(ValueError): validate_evaluations([{'job_id':'site:1'}])

    def test_missing_jd_has_no_numeric_score(self):
        r=record();r.update(match_score='',recommendation=NEEDS_JD,match_summary='JD needed; paste the full description.')
        self.assertEqual(validate_evaluations([r])[0]['match_score'],'')
        r['match_score']='0'
        with self.assertRaises(ValueError):validate_evaluations([r])

    def test_bad_summary_score_or_label_rejected(self):
        for changes in [{'match_summary':''},{'match_score':'NaN'},{'match_score':'75.5'},
                        {'match_score':True},{'recommendation':'Skip'},{'job_id':' site:1 '}]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                validate_evaluations([dict(record(),**changes)])

    def test_valid_scored_and_duplicate_ids(self):
        self.assertEqual(validate_evaluations([record()])[0]['recommendation'],'Apply')
        with self.assertRaises(ValueError):validate_evaluations([record(),record()])
