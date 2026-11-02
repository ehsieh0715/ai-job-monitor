# Build and update Candidate Profile

Version: 1.0. Apply `evidence-policy.md`; this file owns profile initialization.
This is an AI-assisted document workflow, not a Python conversion command.

## Input and destination

A user-supplied absolute Career root is sufficient to start profile initialization.
For initialization only, a missing local configuration or Profile is expected:
these bootstrap rules replace the existing-file prerequisite in evidence-policy.md.
Use the supplied root/defaults and create the requested files within authorized
access; still stop for unavailable source data or filesystem permission.
Use explicit paths if supplied; otherwise use these paths relative to that root:
`Candidate Profile.md`, `Source Documents/`, `Project Evidence/`,
`Applications/`, `Applications/Applications.md`.
Use `config/config.local.yaml` when already configured; if an explicit root differs,
ask whether to switch rather than silently reading/mixing two people's data.
When initializing configuration, preserve existing search/other settings; copy
missing fields from the public example, but never invent personal preferences.

A request to initialize/build and save a Profile authorizes that destination
write within granted filesystem access, not unrestricted vault edits. Report the
exact path needing access if blocked. Local file paths are not web URLs; resolve
a provided file URL to a local path before using it. Do not invent remote access.

Inventory only the configured Source Documents subtree, without following symlinks
outside it. If missing/empty, explain where to put files or request an explicit
alternative source directory. Do not recursively scan the entire vault/computer,
clone repositories, move originals or create synchronized copies.

## Consolidation

1. Read an existing Profile before changing it. Preserve verified user additions,
   full notes and source pointers; merge rather than reset or blindly append.
2. Inventory relevant Markdown/text/JSON, CV Word/PDF and other documents. Read
   legacy candidate_profile.json as input, not a second database to maintain.
   DOCX/PDF versions of one CV and repeated claims are not independent evidence.
   Use appropriate document-reading tools; flag scanned/unreadable files and
   extraction limits. Never claim to have read unavailable content.
3. Extract stable facts and candidate-owned actions with dates, context, skills,
   results, evidence type and limits. Retain a source pointer per experience,
   project or claim group; exact metrics require traceable support. A raw CV's
   assertion is a source claim, not automatic proof of implementation/authorship.
4. Reconcile conflicts explicitly. Preserve existing confirmed facts over an
   unverified older claim; uncertain dates/titles/metrics go in Open Questions,
   not silently into factual sections. Ask focused high-impact questions and
   save the rest as unresolved; initialization need not wait for every detail.
5. Read existing project summaries first. If technical depth is needed, inspect
   authorized relevant code/tests/config and documentation at the original local
   path or accessible repository URL. README-only claims remain unverified.
   Never invent an inspected commit or personal contribution. Detailed reviewed
   summaries may go in Project Evidence when authorized; include concise project
   evidence in the Profile even if no separate summary is needed.
6. Save one coherent Markdown Profile at the configured destination. Review
   against the source inventory and existing Profile for lost facts, unsupported
   claims, duplicates and leaked credentials. Report destination, sources reviewed,
   unreadable/skipped materials and important pending questions; do not create
   separate progress logs, source indexes or a parallel JSON profile.

## Profile shape

Use these sections as a compact consistent structure, omitting empty subsections:

- **Summary & Target Roles:** factual overview; distinguish stated targets from
  suggested directions. Do not invent preferences or motivation.
- **Work Experience:** employer, actual title, dates, employment type/location;
  responsibilities, owned contributions, achievements, technologies and limits.
- **Projects:** professional/portfolio/academic context, completion/operating
  status, candidate contribution, verified functions/results, source links and
  inspected commit if actually reviewed.
- **Skills & Evidence:** capability, evidence type and relevant experience/project
  reference, depth and boundaries; learning is not implementation.
- **Education & Certifications:** exact supported qualification, dates/status.
- **Constraints & Preferences:** verified location, work permission, availability,
  role interests and writing preferences, with unknowns marked rather than assumed.
- **Claim Boundaries:** allowed factual title clarifications, limitations and
  important wording risks. Do not import candidate-specific rules into repo policies.
- **Open Questions & Conflicts:** unresolved claims with sources; never score
  them as established capability.
- **Source Review:** compact embedded record of paths, review date, extraction or
  verification limits and project commits where applicable. No credentials or
  full source dumps. A review date is not proof that every source is current.

Keep enough concrete evidence to support assessments and multiple CV directions,
not a finished resume or a copy of every raw document. Link to full sources when
needed. Profile language follows the user's preference (default Traditional
Chinese analysis, preserving titles/technical terms); later CV wording is English.

## Ongoing use

After generation, the Profile is the maintained shared factual entry point;
raw documents remain references. Follow evidence-policy.md for later confirmed
experience updates and do not re-read all originals on every assessment. An
incomplete Profile supports only provisional evaluations until material questions
are resolved. Requesting initialization does not authorize job searches, Sheet
writes, application drafting or submission. Those use their respective policies
and separate search/Google settings.
