"""Merge newer observations without erasing retained nonempty source fields."""
import pandas as pd
from schema import PENDING_COLUMNS


def merge_jobs(*frames):
    records = {}
    for frame in frames:
        for row in frame.fillna('').to_dict('records'):
            id = str(row.get('job_id', ''))
            if not id:
                continue
            record = records.setdefault(id, {col: '' for col in PENDING_COLUMNS})
            for col in PENDING_COLUMNS:
                value = row.get(col, '')
                if str(value).strip():
                    record[col] = value
    return pd.DataFrame(list(records.values()), columns=PENDING_COLUMNS)
