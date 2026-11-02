# Candidate Evidence Standards

Version: 1.2. Applies to every assessment and application document.

## Sources and access

Read `config/config.local.yaml` (see `config/README.md`). Resolve `career.root`
as an absolute path. It is the only configurable Career path. Use the fixed
layout in career-workflow.md; legacy per-file path overrides are not supported.
Missing configuration, files or permission: identify the exact missing path;
do not guess a fallback or silently use another person's data. Configuration
is not permission. AI skills and Python path resolution use this same layout.
Read optional local `policies/preferences.md` for presentation preferences;
current task instructions take precedence. Preferences never override evidence
rules or change scoring standards.

For an explicit review/revision/export request, the user-designated individual
file may be read outside Source Documents; this permits no surrounding-directory
scan and does not make it an authoritative Profile source. Respect filesystem
access and distinguish source fidelity from factual verification.

Read `<career.root>/Candidate Profile.md` first, including relevant project
sections. Consult originals only in `<career.root>/Source Documents/` or project
links recorded in its Projects.md when a material claim needs
verification. An incomplete profile calls for source review or questions, not an
assumption that the candidate has no experience. CVs are presentations of facts,
not authoritative facts; repetition across files adds no evidence strength.

## Claim boundaries

Label evidence as professional (direct or adjacent), portfolio/project,
academic, learning/mentioned-only, or planned/in progress. Employment does not
by itself establish production use. A completed academic implementation can
show technical capability without becoming commercial experience.

Preserve actual employer, dates, contract/part-time status and underlying title.
A functional title clarification is allowed only when documented responsibilities
support it; never invent a promotion or replace the contractual title.
Do not penalize a different historical title when the actual work transfers.

Use only verified skills, responsibilities, scale, metrics and outcomes. Separate
individual contributions from team/repository capabilities; code existence alone
does not establish personal authorship. Do not equate a tutorial, planned feature,
prototype or named technology with completed implementation or production ownership.
A paused deployment may still have completed verified functionality; state both
implementation and current operating status accurately.

For project summaries record implemented functions, candidate contribution,
verified results, limitations, source paths/URLs, inspected files, inspected commit
and review date. Inspect relevant code, tests/configuration and documentation,
not README alone. Mark uninspected claims as unverified. Keep repositories in
place. Reuse summaries; inspect changes when the source commit changes or a
specific claim requires deeper review. Never invent a checked commit.

## Questions and updates

Missing evidence is unverified, not a confirmed absence. Award no assumed credit.
In conversation ask focused questions only where answers could materially change
fit: context, owned action, completion, scope/result and supporting source.
Do not repeatedly ask facts already recorded. In unattended runs mark pending
questions without guessing answers or blocking the entire batch.

When the user supplies experience, first prepare a source-linked proposed edit to
Candidate Profile.md (including project sections), with context, limits and
confirmation provenance.
Present exact target paths and additions/replacements/removals for approval.
Answering factual questions is not permission to write. A general build/update
request is permission to inspect and propose, not to save unseen Markdown content.
After explicit approval of the displayed edit, apply only that approved scope;
do not ask again for unchanged already-approved content. Uncertain claims remain
questions. If further changes are discovered, propose them separately.

This gate applies to initial Profile generation and later updates. It does not
change separately authorized CV/letter/tracker or pipeline writes. Filesystem
permission is still required. Until approval, keep the proposal in conversation,
not an unapproved draft file; distinguish hypothetical/pending evidence from the
saved Profile in any provisional discussion. Never let unattended runs update
the Candidate Profile or treat unapproved new claims as established evidence.
Reassess confirmed saved changes and explain changed judgments. If blocked, report
it rather than claiming an update. Project review follows project-evidence-evaluation.md.

## Personal preferences and shared rules

Personal language, tone and formatting choices belong in Git-ignored
`policies/preferences.md`, not shared policies. If absent, follow the current
request, document audience and employer requirements; ask only when necessary.
Do not assume a specific user's language for people who clone this project.
Shared rule changes apply equally to batch and conversational evaluation.
Style preferences never relax factual boundaries or establish candidate facts.

When a user requests that corrections/preferences be remembered (including standing
permission to remember future feedback), merge confirmed reusable language, tone,
formatting and workflow presentation choices into policies/preferences.md within
filesystem access. Group by topic, update superseded choices and avoid raw-chat
logs or duplicate bullets; a later explicit correction supersedes the old choice.
Report the saved change briefly. One-job instructions stay local unless reusable
intent is clear; ask about ambiguity. Facts require the separate Profile content
approval gate. Ideas/plans never become achievements. Never save passwords, keys
or guessed preferences. User preferences cannot relax shared evidence/scoring rules.
