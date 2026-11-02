import sys
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import prepare_evaluation as ctx
from schema import PENDING_COLUMNS


class FreshnessTests(unittest.TestCase):
    def test_changed_profile_requeues_and_old_scores_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); data = root / 'data'; data.mkdir()
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
                pd.DataFrame([{'job_id': 'site:1'}]).to_csv(data/'scored_jobs.csv', index=False)
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

    def test_seal_rejects_incomplete_queue(self):
        with tempfile.TemporaryDirectory() as folder:
            d = Path(folder)
            import hashlib
            # Bind the prepared queue so this test reaches coverage validation.
            (d/'evaluation_context.json').write_text('{"fingerprint":"current"}')
            (d/'pending_jobs.csv').write_text('job_id\na\nb\n')
            (d/'scored_jobs.csv').write_text('job_id\na\n')
            (d/'evaluation_context.json').write_text(json.dumps({'fingerprint':'current','queue_sha256':hashlib.sha256((d/'pending_jobs.csv').read_bytes()).hexdigest()}))
            with patch.multiple(ctx, DATA=d, CONTEXT=d/'evaluation_context.json', SEALED=d/'sealed.json'), patch.object(ctx, 'fingerprint', return_value='current'):
                with self.assertRaises(ValueError): ctx.seal()
                self.assertFalse((d/'sealed.json').exists())
