# Scheduled AI-run prompt

Use this as the task instruction in an AI scheduler with local execution, file
and network access. Replace the repo path and select your own interval/timezone
in the scheduler. This file neither creates a schedule nor supplies credentials.
The machine/execution environment must be available for runs; do not assume your
local Career folder exists in a cloud environment or another machine.

> Work in `/absolute/path/to/ai-job-monitor`. Follow
> `.agents/skills/career-assistant/SKILL.md` and `policies/workflow.md` in scheduled
> mode. Read the current private config, preferences, Candidate Profile and relevant
> evidence. Search, prepare the evaluation queue, evaluate all rows under the shared
> policy, seal, preview and synchronize to my configured Google Sheet. I authorize
> recurring updates to that sheet's owned recommendation fields. Preserve manual
> columns. Stop on failure or unavailable access; do not guess credentials or
> experience. Do not overlap runs, draft application documents or submit jobs.
> Stay quiet when nothing meaningful changes. Notify me about meaningful new or
> changed recommendations, failures, or questions requiring my answer.

For a new conversation without skill auto-discovery, explicitly ask it to read the
same entrypoint and workflow. A chat without local/connected tools cannot execute
this merely by receiving the prompt; use a suitable environment first.
