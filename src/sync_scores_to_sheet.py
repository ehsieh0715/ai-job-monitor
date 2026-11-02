"""Idempotent score upsert; preserve user columns and refuse incompatible sheets."""
import argparse
import json
import math

import pandas as pd
from gspread.utils import rowcol_to_a1
from configuration import REPO_ROOT
from google_sheets import get_worksheet
from schema import PENDING_COLUMNS, SCORED_COLUMNS

SCORED_JOBS_PATH = REPO_ROOT / 'data/scored_jobs.csv'
PENDING_JOBS_PATH = REPO_ROOT / 'data/pending_jobs.csv'
PROCESSED_IDS_PATH = REPO_ROOT / 'data/processed_job_ids.json'


def clean_value(value):
    return '' if value is None or (isinstance(value, float) and math.isnan(value)) else value


def plan_sync(values, records):
    """Pure validation/planning, no network or local state writes."""
    header = values[0] if values else SCORED_COLUMNS.copy()
    if not header or len(set(header)) != len(header) or not set(SCORED_COLUMNS) <= set(header):
        raise ValueError('Incompatible Sheet header; use an empty worksheet or required named columns')
    idx = header.index('job_id')
    existing = {}
    for number, row in enumerate(values[1:], 2):
        id = str(row[idx]).strip() if idx < len(row) else ''
        if id:
            if id in existing:
                raise ValueError('Duplicate job_id in Sheet')
            existing[id] = (number, row + [''] * (len(header) - len(row)))
    updates, appends, seen = [], [], set()
    for record in records:
        if not set(SCORED_COLUMNS) <= set(record):
            raise ValueError('Missing required scored columns')
        record = {k: clean_value(v) for k, v in record.items()}
        id = str(record['job_id']).strip()
        if not id or id in seen:
            raise ValueError('Missing/duplicate job_id in scored data')
        seen.add(id)
        try:
            score = float(record['match_score'])
        except (ValueError, TypeError):
            raise ValueError('Invalid match_score') from None
        if not math.isfinite(score) or not score.is_integer() or not 0 <= score <= 100:
            raise ValueError('match_score must be an integer 0–100')
        label = 'Strong Apply' if score >= 85 else 'Apply' if score >= 70 else 'Consider' if score >= 55 else 'Skip'
        if record['recommendation'] != label:
            raise ValueError('Score/recommendation disagreement')
        if id in existing:
            number, old = existing[id]
            # Only patch owned cells, so manual columns/formulas are untouched.
            for col, name in enumerate(header, 1):
                if name in SCORED_COLUMNS and str(old[col - 1]) != str(record[name]):
                    updates.append({'range': rowcol_to_a1(number, col), 'values': [[record[name]]]})
        else:
            appends.append([record.get(name, '') if name in SCORED_COLUMNS else '' for name in header])
    return {'initialize': not values, 'updates': updates, 'appends': appends, 'ids': seen}


def sync_scores(dry_run=False):
    if not SCORED_JOBS_PATH.exists():
        raise FileNotFoundError(f'Missing scored data: {SCORED_JOBS_PATH}')
    scored = pd.read_csv(SCORED_JOBS_PATH, dtype=str, keep_default_na=False)
    if scored.empty:
        print('No scored jobs to sync.')
        return
    from prepare_evaluation import verify_seal, COMPLETED
    context = verify_seal()
    worksheet = get_worksheet()
    plan = plan_sync(worksheet.get_all_values(), scored.to_dict('records'))
    print(f"Sync plan: {len(plan['updates'])} changed cells; {len(plan['appends'])} new rows.")
    if dry_run:
        return
    if plan['initialize']:
        worksheet.update(range_name='A1:K1', values=[SCORED_COLUMNS], value_input_option='RAW')
    if plan['updates']:
        worksheet.batch_update(plan['updates'], value_input_option='RAW')
    if plan['appends']:
        worksheet.append_rows(plan['appends'], value_input_option='RAW')
    # Mark processed only after every remote operation succeeded. Retrying is safe
    # for a single writer: the next plan reconciles successful remote writes.
    processed = set(json.loads(PROCESSED_IDS_PATH.read_text())) if PROCESSED_IDS_PATH.exists() else set()
    processed.update(plan['ids'])
    PROCESSED_IDS_PATH.write_text(json.dumps(sorted(processed), indent=2))
    if PENDING_JOBS_PATH.exists():
        pending = pd.read_csv(PENDING_JOBS_PATH, dtype=str, keep_default_na=False)
        pending = pending[~pending['job_id'].isin(plan['ids'])]
        pending[PENDING_COLUMNS].to_csv(PENDING_JOBS_PATH, index=False)
    COMPLETED.write_text(json.dumps(context, indent=2))
    print('Scores synchronized.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true', help='Read Sheet and plan without any writes')
    sync_scores(parser.parse_args().dry_run)
