# Scheduled Search, Evaluation and Sync

## Setup and scope

- **Runner requirements:** AI evaluation, repository and Career access, Python, network and the runner's own configured Google credentials.
- **Runner limits:** `main.py` only searches; cloud execution does not inherit local access or this chat's tools.
- Do not create/activate a schedule without authorized timing, timezone, execution environment and recurring-write scope. Before activation require a successful end-to-end trial and independently verify runner access.
- Use the current absolute repo path, configured Sheet and repo working directory. Saved tasks reference the career-assistant entrypoint and `policies/career-workflow.md`; every run rereads current rules, config and Profile.
- **Schedule creation:** use available tools when requested; ask only for missing material settings or authorization.
- **Schedule result:** report what was actually created. If tooling is unavailable, give manual guidance; do not install a scheduler or add an example file automatically.
- Use only configured Google destination and repo-root `google-service-account.json`; ignore retired credential overrides. Never print the key, search for another person's credentials or use connectors for pipeline sync.
- Allow only one pipeline/sync writer; do not overlap schedules.
- Unattended work cannot update Profile/preferences, draft CVs/letters, submit applications or invent experience. Interactive standing drafting permission does not apply.

## Run in order

1. Read current inputs and rules and verify stage access.
2. Run `.venv/bin/python src/main.py`. On search failure stop; never publish old scores as a new run.
3. Run `.venv/bin/python src/prepare_evaluation.py`. It prepares new or explicitly queued jobs and recovers retained JD. Profile/policy changes do not requeue synced history.
4. Evaluate the entire current queue under `job-fit-evaluation.md`, replacing scored output and validating calculation records. Empty queue ends successfully without sync. Unknowns remain provisional; missing JD remains unscored.
5. Run `.venv/bin/python src/prepare_evaluation.py --seal` only after current evaluation is complete. It checks required structure, IDs, metadata, scores, labels, summaries and input/output hashes, not substantive scoring quality or JD completeness.
6. Run `.venv/bin/python src/sync_scores_to_sheet.py --dry-run`. It authenticates and reads Google and previews the sealed batch; no remote writes or local-state changes.
7. With current or recurring write authorization, run the same sync command without `--dry-run`.

## Sync and recovery

- **Sheet updates:** update owned cells by job_id, append new jobs and preserve manual columns. Empty worksheets may initialize.
- **Stop conditions:** incompatible headers, duplicate IDs or invalid scores stop the run.
- Change local processed state only after successful remote API calls. Failed or partial writes stay pending; retries reread/replan rather than blindly append.
- A successful API response is the completion check. Independent post-write readback is not implemented; do not claim it occurred.
- Only Profile and scoring and evidence policies affect unfinished-score freshness, not presentation preferences. Revalidate stale unfinished output; do not silently rewrite synced history.
- Do not infer application status or remove rows because a job disappears from search.

## Report

- Keep successful or unchanged runs quiet unless periodic reports were requested.
- Notify meaningful new recommendations, changed judgments, failures or required action; include pending evidence questions for later conversation.
- Do not put credentials or full personal sources in logs.
