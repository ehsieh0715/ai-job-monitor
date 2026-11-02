import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from schema import SCORED_COLUMNS
from sync_scores_to_sheet import plan_sync


def job(id='site:1', score=75):
    row = {c: '' for c in SCORED_COLUMNS}
    row.update(job_id=id, match_score=score, recommendation='Apply', title='=unsafe', match_summary='Verified evidence and gap')
    return row


class SheetSyncTests(unittest.TestCase):
    def test_updates_existing_keeps_extra_fields_and_column_order(self):
        header = ['Note'] + list(reversed(SCORED_COLUMNS))
        old = job(score=70)
        values = [header, ['keep'] + [str(old[c]) for c in reversed(SCORED_COLUMNS)]]
        plan = plan_sync(values, [job()])
        self.assertEqual(len(plan['updates']), 1)
        self.assertTrue(all(not item['range'].startswith('A') for item in plan['updates']))
        self.assertEqual(plan['appends'], [])

    def test_new_and_identical_retry(self):
        row = job()
        self.assertEqual(len(plan_sync([], [row])['appends']), 1)
        values = [SCORED_COLUMNS, [str(row[c]) for c in SCORED_COLUMNS]]
        p = plan_sync(values, [row])
        self.assertEqual(p['updates'], [])
        self.assertEqual(p['appends'], [])

    def test_incompatible_header_fails(self):
        with self.assertRaises(ValueError):
            plan_sync([['Company', 'Status']], [job()])

    def test_duplicate_or_bad_scores_fail(self):
        for rows in [[job(), job()], [job(score=110)], [dict(job(), recommendation='Skip')]]:
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                plan_sync([], rows)

    def test_duplicate_remote_ids_fail(self):
        row = [str(job()[c]) for c in SCORED_COLUMNS]
        with self.assertRaises(ValueError):
            plan_sync([SCORED_COLUMNS, row, row], [job()])


if __name__ == '__main__':
    unittest.main()

class SyncExecutionTests(unittest.TestCase):
    def test_dry_run_and_remote_failure_do_not_mark_processed(self):
        import tempfile
        import pandas as pd
        import sync_scores_to_sheet as sync
        from unittest.mock import patch, MagicMock
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            scores = root/'scored.csv'; pd.DataFrame([job()]).to_csv(scores, index=False)
            pending = root/'pending.csv'
            from schema import PENDING_COLUMNS
            pd.DataFrame([{c: 'site:1' if c == 'job_id' else '' for c in PENDING_COLUMNS}]).to_csv(pending,index=False)
            before = pending.read_bytes()
            ws = MagicMock(); ws.get_all_values.return_value = []
            with patch.multiple(sync, SCORED_JOBS_PATH=scores, PENDING_JOBS_PATH=pending,
                                PROCESSED_IDS_PATH=root/'processed.json'), patch.object(sync,'get_worksheet',return_value=ws), patch('prepare_evaluation.verify_seal',return_value={'fingerprint':'test'}), patch('prepare_evaluation.COMPLETED',root/'completed.json'):
                sync.sync_scores(dry_run=True)
                ws.update.assert_not_called(); ws.append_rows.assert_not_called()
                self.assertFalse((root/'processed.json').exists())
                ws.append_rows.side_effect = RuntimeError('network failure')
                with self.assertRaises(RuntimeError): sync.sync_scores()
                self.assertEqual(pending.read_bytes(),before)
                self.assertFalse((root/'processed.json').exists())
                ws.append_rows.side_effect = None
                sync.sync_scores()
                self.assertTrue((root/'processed.json').exists())
                self.assertTrue((root/'completed.json').exists())
                self.assertTrue(pd.read_csv(pending).empty)
                self.assertEqual(ws.append_rows.call_args.kwargs['value_input_option'],'RAW')

class MissingJDTests(unittest.TestCase):
    def test_missing_jd_clears_old_score_and_is_idempotent(self):
        from evaluation_validation import NEEDS_JD
        old=job();new=dict(old,match_score='',recommendation=NEEDS_JD,match_summary='請貼上 JD 後重新評估')
        before=[SCORED_COLUMNS,[str(old[c]) for c in SCORED_COLUMNS]]
        plan=plan_sync(before,[new])
        self.assertIn({'range':'I2','values':[['']]},plan['updates'])
        after=[SCORED_COLUMNS,[str(new[c]) for c in SCORED_COLUMNS]]
        self.assertEqual(plan_sync(after,[new])['updates'],[])
