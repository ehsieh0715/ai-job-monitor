import sys
import json
import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import prepare_evaluation as ctx
from schema import PENDING_COLUMNS


def scoring_files(root):
    directory = root / 'policies'
    directory.mkdir(exist_ok=True)
    for name in ['candidate-evidence-standards.md', 'job-fit-evaluation.md']:
        (directory / name).write_text('Initial scoring rule')


class FreshnessTests(unittest.TestCase):
    def test_changed_profile_invalidates_unfinished_scores(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); scoring_files(root); data = root / 'data'; data.mkdir()
            career = root / 'career'; career.mkdir()
            profile = career / 'Candidate Profile.md'; profile.write_text('confirmed SQL')
            row = {k: '' for k in PENDING_COLUMNS}; row.update(job_id='site:1', description='SQL')
            pd.DataFrame([row]).to_csv(data/'job_history.csv', index=False)
            pd.DataFrame([dict(row, description='SQL latest')]).to_csv(data/'raw_jobs.csv', index=False)
            with patch.multiple(ctx, REPO_ROOT=root, DATA=data, CONTEXT=data/'evaluation_context.json',
                                SEALED=data/'scored_context.json', COMPLETED=data/'last_synced_context.json',
                                HISTORY=data/'job_history.csv'), patch.object(ctx, 'load_config', return_value={'career': {'root': str(career)}}):
                ctx.prepare()
                self.assertEqual(len(pd.read_csv(data/'pending_jobs.csv')), 1)
                self.assertEqual(pd.read_csv(data/'pending_jobs.csv').iloc[0]['description'], 'SQL latest')
                pd.DataFrame([dict(row,match_score='75',recommendation='Apply',match_summary='SQL evidence')]).drop(columns=['description']).to_csv(data/'scored_jobs.csv', index=False)
                ctx.seal(); completed = ctx.verify_seal()
                queue = data/'pending_jobs.csv'
                unchanged = queue.read_bytes()
                queue.write_text(queue.read_text().replace('SQL', 'changed JD'))
                with self.assertRaises(ValueError): ctx.verify_seal()
                queue.write_bytes(unchanged)
                (data/'last_synced_context.json').write_text(json.dumps(completed))
                profile.write_text('confirmed SQL and Python')
                with self.assertRaises((ValueError, FileNotFoundError)): ctx.verify_seal()
                ctx.prepare()
                with self.assertRaises((ValueError, FileNotFoundError)): ctx.verify_seal()
                ctx.seal(); ctx.verify_seal()
                (data/'scored_jobs.csv').write_text('job_id\nsite:2\n')
                with self.assertRaises((ValueError, FileNotFoundError)): ctx.verify_seal()

    def test_changes_do_not_requeue_synced_history(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);scoring_files(root); data=root/'data';data.mkdir();career=root/'career';career.mkdir()
            profile=career/'Candidate Profile.md';profile.write_text('New confirmed profile')
            (data/'job_history.csv').write_text(','.join(PENDING_COLUMNS)+'\nsite:1,,,,,,,,SQL\n')
            (data/'processed_job_ids.json').write_text('["site:1"]')
            with patch.multiple(ctx,REPO_ROOT=root,DATA=data,CONTEXT=data/'context.json',SEALED=data/'seal.json',HISTORY=data/'job_history.csv'), patch.object(ctx,'load_config',return_value={'career':{'root':str(career)}}):
                ctx.prepare()
                self.assertTrue(pd.read_csv(data/'pending_jobs.csv').empty)
                profile.write_text('Another update')
                ctx.prepare()
                self.assertTrue(pd.read_csv(data/'pending_jobs.csv').empty)

    def test_only_scoring_policies_change_fingerprint(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);scoring_files(root);(root/'Candidate Profile.md').write_text('verified');policies=root/'policies';policies.mkdir(exist_ok=True)
            with patch.object(ctx,'REPO_ROOT',root),patch.object(ctx,'load_config',return_value={'career':{'root':str(root)}}):
                baseline=ctx.fingerprint()
                (policies/'application-pdf-generation.md').write_text('purple')
                (policies/'application-email-writing.md').write_text('concise')
                self.assertEqual(ctx.fingerprint(),baseline)
                (policies/'job-fit-evaluation.md').write_text('weights')
                self.assertNotEqual(ctx.fingerprint(),baseline)

    def test_seal_rejects_id_only_and_scores_without_jd(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            row={c:'' for c in PENDING_COLUMNS};row['job_id']='site:1'
            pending=root/'pending_jobs.csv';pd.DataFrame([row]).to_csv(pending,index=False)
            context=root/'context.json';context.write_text(json.dumps({'fingerprint':'current','queue_sha256':hashlib.sha256(pending.read_bytes()).hexdigest()}))
            with patch.multiple(ctx,DATA=root,CONTEXT=context,SEALED=root/'seal.json'),patch.object(ctx,'fingerprint',return_value='current'):
                pd.DataFrame([{'job_id':'site:1'}]).to_csv(root/'scored_jobs.csv',index=False)
                with self.assertRaises(ValueError):ctx.seal()
                result={k:v for k,v in row.items() if k!='description'}
                result.update(match_score='75',recommendation='Apply',match_summary='unsupported')
                pd.DataFrame([result]).to_csv(root/'scored_jobs.csv',index=False)
                with self.assertRaises(ValueError):ctx.seal()
                from evaluation_validation import NEEDS_JD
                result.update(match_score='',recommendation=NEEDS_JD,match_summary='Full JD needed.')
                pd.DataFrame([result]).to_csv(root/'scored_jobs.csv',index=False)
                ctx.seal()
                self.assertTrue((root/'seal.json').exists())

    def test_manual_jd_correction_wins_over_old_raw_snapshot(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);scoring_files(root);data=root/'data';data.mkdir()
            (root/'Candidate Profile.md').write_text('verified')
            row={c:'' for c in PENDING_COLUMNS};row.update(job_id='site:1',description='old scraped JD')
            pd.DataFrame([row]).to_csv(data/'raw_jobs.csv',index=False)
            row['description']='new user-supplied JD'
            pd.DataFrame([row]).to_csv(data/'pending_jobs.csv',index=False)
            with patch.multiple(ctx,REPO_ROOT=root,DATA=data,CONTEXT=data/'context.json',SEALED=data/'seal.json',HISTORY=data/'job_history.csv'),patch.object(ctx,'load_config',return_value={'career':{'root':str(root)}}):
                ctx.prepare()
            self.assertEqual(pd.read_csv(data/'pending_jobs.csv').iloc[0]['description'],'new user-supplied JD')

    def test_missing_scoring_policy_blocks_preparation(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);scoring_files(root);(root/'Candidate Profile.md').write_text('verified')
            (root/'policies/job-fit-evaluation.md').unlink()
            with patch.object(ctx,'REPO_ROOT',root),patch.object(ctx,'load_config',return_value={'career':{'root':str(root)}}):
                with self.assertRaisesRegex(FileNotFoundError,'job-fit-evaluation.md'):ctx.fingerprint()
