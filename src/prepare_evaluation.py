"""Prepare a fresh evaluation queue; seal AI-produced scores before synchronization."""
import argparse
import hashlib
import json

import pandas as pd
from configuration import REPO_ROOT, load_config, load_career_paths
from schema import PENDING_COLUMNS, SCORED_COLUMNS
from job_history import merge_jobs
from evaluation_validation import validate_evaluations, NEEDS_JD

DATA = REPO_ROOT / 'data'
CONTEXT = DATA / 'evaluation_context.json'
SEALED = DATA / 'scored_context.json'
COMPLETED = DATA / 'last_synced_context.json'
HISTORY = DATA / 'job_history.csv'


def fingerprint():
    config = load_config()
    profile = load_career_paths(config=config)['profile']
    if not profile.is_file():
        raise FileNotFoundError(f'Initialize Profile first: {profile}')
    files = [profile] + [REPO_ROOT / 'policies' / name for name in
                         ('candidate-evidence-standards.md', 'job-fit-evaluation.md')]
    for required in files:
        if not required.is_file():
            raise FileNotFoundError(f'Missing scoring input: {required}')
    digest = hashlib.sha256()
    for p in files:
        digest.update(str(p).encode()); digest.update(p.read_bytes())
    return digest.hexdigest()


def prepare():
    current = fingerprint()
    DATA.mkdir(exist_ok=True)
    frames = []
    # Seed history from surviving legacy CSVs as well as the current search queue.
    for name in ['job_history.csv', 'raw_jobs.csv', 'pending_jobs.csv']:
        p = DATA / name
        if p.exists():
            df = pd.read_csv(p, dtype=str, keep_default_na=False)
            if 'job_id' not in df and {'site', 'id'} <= set(df):
                df['job_id'] = df['site'] + ':' + df['id']
            if 'job_id' in df:
                for col in PENDING_COLUMNS:
                    if col not in df:
                        df[col] = ''
                frames.append(df[PENDING_COLUMNS])
    history = merge_jobs(*frames)
    history.to_csv(HISTORY, index=False)
    # Queue new/changed jobs only. Profile/policy edits never requeue synced history.
    pending_path = DATA / 'pending_jobs.csv'
    queued_ids = set()
    if pending_path.exists():
        pending = pd.read_csv(pending_path, dtype=str, keep_default_na=False)
        queued_ids.update(pending['job_id'])
    processed_path = DATA / 'processed_job_ids.json'
    processed = set(json.loads(processed_path.read_text())) if processed_path.exists() else set()
    queued_ids.update(set(history['job_id']) - processed)
    history[history['job_id'].isin(queued_ids)].to_csv(pending_path, index=False)
    pending_path = DATA / 'pending_jobs.csv'
    if not pending_path.exists():
        pd.DataFrame(columns=PENDING_COLUMNS).to_csv(pending_path, index=False)
    SEALED.unlink(missing_ok=True)
    CONTEXT.write_text(json.dumps({'fingerprint': current, 'queue_sha256': hashlib.sha256(pending_path.read_bytes()).hexdigest()}, indent=2))
    print('Evaluate every pending row, then run prepare_evaluation.py --seal.')


def seal():
    context = json.loads(CONTEXT.read_text())
    if context['fingerprint'] != fingerprint() or context.get('queue_sha256') != hashlib.sha256((DATA / 'pending_jobs.csv').read_bytes()).hexdigest():
        raise ValueError('Profile/evidence/policies changed during evaluation; prepare and evaluate again')
    path = DATA / 'scored_jobs.csv'
    pending = pd.read_csv(DATA / 'pending_jobs.csv', dtype=str, keep_default_na=False)
    scores = pd.read_csv(path, dtype=str, keep_default_na=False)
    if list(scores.columns) != SCORED_COLUMNS:
        raise ValueError('Evaluation CSV must use the complete ordered schema')
    validate_evaluations(scores.to_dict('records'))
    from collections import Counter
    if Counter(pending['job_id']) != Counter(scores['job_id']):
        raise ValueError('Scored rows do not cover the prepared pending queue')
    source_by_id = pending.set_index('job_id', drop=False)
    for row in scores.to_dict('records'):
        source = source_by_id.loc[row['job_id']]
        if not str(source['description']).strip() and row['recommendation'] != NEEDS_JD:
            raise ValueError('No JD: use the unscored Needs JD state; do not invent a score')
        for col in PENDING_COLUMNS[:-1]:
            if str(row[col]) != str(source[col]):
                raise ValueError(f'Evaluation changed source metadata: {col}')
    context['scores_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    SEALED.write_text(json.dumps(context, indent=2))
    print('Sealed current scored output; no Sheet writes.')


def verify_seal():
    context = json.loads(SEALED.read_text())
    if context['fingerprint'] != fingerprint() or context.get('queue_sha256') != hashlib.sha256((DATA / 'pending_jobs.csv').read_bytes()).hexdigest() or context['scores_sha256'] != hashlib.sha256((DATA / 'scored_jobs.csv').read_bytes()).hexdigest():
        raise ValueError('Stale/unsealed scores; prepare, evaluate and seal again')
    return context


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seal', action='store_true')
    seal() if parser.parse_args().seal else prepare()
