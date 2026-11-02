import sys
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from job_history import merge_jobs
from schema import PENDING_COLUMNS
import search_jobs


class HistoryTests(unittest.TestCase):
    def test_empty_description_does_not_erase_retained_jd(self):
        old = pd.DataFrame([{'job_id':'site:1','description':'Full SQL JD','title':'Old'}])
        new = pd.DataFrame([{'job_id':'site:1','description':'','title':'New'}])
        row = merge_jobs(old,new).iloc[0]
        self.assertEqual(row['description'],'Full SQL JD')
        self.assertEqual(row['title'],'New')

    def test_changed_processed_job_requeued(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); (root/'data').mkdir()
            row={c:'' for c in PENDING_COLUMNS};row.update(job_id='site:1',description='old')
            pd.DataFrame([row]).to_csv(root/'data/job_history.csv',index=False)
            pending = root/'pending.csv'; pd.DataFrame(columns=PENDING_COLUMNS).to_csv(pending,index=False)
            processed = root/'processed.json';processed.write_text(json.dumps(['site:1']))
            observed=pd.DataFrame([dict(row,site='site',id='1',description='new')])
            with patch.multiple(search_jobs,REPO_ROOT=root,PENDING_JOBS_PATH=pending,PROCESSED_IDS_PATH=processed):
                search_jobs.update_pending_jobs(observed)
            saved=pd.read_csv(pending)
            self.assertEqual(len(saved),1)
            self.assertEqual(saved.iloc[0]['description'],'new')
            pd.DataFrame(columns=PENDING_COLUMNS).to_csv(pending,index=False)
            observed['description'] = float('nan')
            with patch.multiple(search_jobs,REPO_ROOT=root,PENDING_JOBS_PATH=pending,PROCESSED_IDS_PATH=processed):
                search_jobs.update_pending_jobs(observed)
            self.assertTrue(pd.read_csv(pending).empty)
