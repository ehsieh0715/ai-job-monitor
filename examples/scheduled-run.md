# Scheduled AI-run prompt

Use this as the task instruction in an AI scheduler with local execution, file
and network access plus connected Google Drive Sheets read/write tools. Replace the repo path and select your own interval/timezone
in the scheduler. This file neither creates a schedule nor connects a Google account.
The machine/execution environment must be available for runs; do not assume your
local Career folder exists in a cloud environment or another machine.

> Work in `/absolute/path/to/ai-job-monitor`. Follow
> `.agents/skills/career-assistant/SKILL.md` and `policies/workflow.md` in scheduled
> mode. Read optional local policies/preferences.md for presentation only.
> Read the current private config, Candidate Profile and relevant
> project sections inside root Candidate Profile.md. Resolve Career paths from
> workflow.md using only career.root; do not scan outside Source Documents for
> original inputs or create separate Project Evidence files. Search, prepare the
> evaluation queue, evaluate all rows under the shared policy and seal. Read the Sheet destination only from private config. Use the
> Google Drive connector synchronization contract, including Python validation
> and verified readback before local completion. If that integration is not yet
> implemented, stop after sealing and report it; do not use the legacy service-account
> command or mark pending jobs processed. I authorize
> recurring updates to that sheet's owned recommendation fields. Preserve manual
> columns. Stop on failure or unavailable access; do not guess credentials or
> experience. Do not overlap runs, draft application documents or submit jobs.
> Stay quiet when nothing meaningful changes. Notify me about meaningful new or
> changed recommendations, failures, or questions requiring my answer.

For a new conversation without skill auto-discovery, explicitly ask it to read the
same entrypoint and workflow. A chat without local/connected tools cannot execute
this merely by receiving the prompt; use a suitable environment first.

The connector synchronization integration is currently pending. This prompt is the
migration target, not a claim of working keyless scheduled synchronization. Verify
connector availability in the scheduled runner independently of this chat.
