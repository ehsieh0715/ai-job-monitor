"""Prepare a fresh evaluation queue; seal AI-produced scores before synchronization."""
import argparse
import hashlib
import json

import pandas as pd
from configuration import REPO_ROOT, load_config
from schema import PENDING_COLUMNS
from job_history import merge_jobs

DATA = REPO_ROOT / 'data'
CONTEXT = DATA / 'evaluation_context.json'
SEALED = DATA / 'scored_context.json'
COMPLETED = DATA / 'last_synced_context.json'
HISTORY = DATA / 'job_history.csv'


def fingerprint():
    config = load_config()
    career = config['career']
    from pathlib import Path
    root = Path(career['root']).expanduser()
    if not root.is_absolute():
        raise ValueError('career.root must be absolute')
    def career_path(key, default):
        p = Path(career.get(key, default)).expanduser()
        return p if p.is_absolute() else root / p
    profile = career_path('profile', 'Candidate Profile.md')
    if not profile.is_file():
        raise FileNotFoundError(f'Initialize Profile first: {profile}')
    files = [profile] + sorted((REPO_ROOT / 'policies').glob('*.md'))
    evidence = career_path('project_evidence', 'Project Evidence')
    if evidence.exists():
        files += sorted(evidence.rglob('*.md'))
    preferences = config.get('preferences_path')
    if preferences:
        p = Path(preferences).expanduser()
        p = p if p.is_absolute() else REPO_ROOT / p
        if not p.is_file():
            raise FileNotFoundError(f'Missing preferences: {p}')
        files.append(p)
    digest = hashlib.sha256()
    for p in files:
        digest.update(str(p).encode()); digest.update(p.read_bytes())
    return digest.hexdigest()


def prepare():
    current = fingerprint()
    DATA.mkdir(exist_ok=True)
    frames = []
    # Seed history from surviving legacy CSVs as well as the current search queue.
    for name in ['job_history.csv', 'pending_jobs.csv', 'raw_jobs.csv']:
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
    previous = json.loads(COMPLETED.read_text()).get('fingerprint') if COMPLETED.exists() else None
    pending_path = DATA / 'pending_jobs.csv'
    if pending_path.exists():
        pending = pd.read_csv(pending_path, dtype=str, keep_default_na=False)
        # Hydrate queued IDs from retained text; current raw observations won above.
        queued = history[history['job_id'].isin(pending['job_id'])]
        queued.to_csv(pending_path, index=False)
    if previous != current:
        history.to_csv(DATA / 'pending_jobs.csv', index=False)
        print(f'Profile/evidence/policy changed or first run: queued {len(history)} known jobs.')
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
    from collections import Counter
    if Counter(pending['job_id']) != Counter(scores['job_id']):
        raise ValueError('Scored rows do not cover the prepared pending queue')
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
