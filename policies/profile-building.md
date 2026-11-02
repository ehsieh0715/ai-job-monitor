# Build and update Candidate Profile

Version: 1.1. Apply `evidence-policy.md`; this file owns profile initialization.
This is an AI-assisted document workflow, not a Python conversion command.

## Input and destination

A user-supplied absolute Career root is sufficient to start profile initialization.
For initialization only, a missing local configuration or Profile is expected:
these bootstrap rules replace the existing-file prerequisite in evidence-policy.md.
Use the supplied root/defaults to inspect and propose content. Create Profile
only after approval under evidence-policy.md; still stop for unavailable sources
or filesystem permission.
Use explicit paths if supplied; otherwise use these paths relative to that root:
`Candidate Profile.md`, `Source Documents/`, `Project Evidence/`,
`Applications/`, `Applications/Applications.md`.
Use `config/config.local.yaml` when already configured; if an explicit root differs,
ask whether to switch rather than silently reading/mixing two people's data.
When initializing configuration, preserve existing search/other settings; copy
missing fields from the public example, but never invent personal preferences.

A build/update request authorizes inspection and a proposal, not writing unseen
Profile/Project Evidence content. Apply evidence-policy.md's approval gate,
including initial creation. Local filesystem permission is separately required.
Resolve a file URL to its local path; do not invent remote access.

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
   propose the rest as unresolved; initialization need not wait for every detail.
5. Read Source Documents/Projects.md (relative to configured source_documents)
   and follow project-evidence.md for every listed repo. Plain URLs are sufficient.
   Read existing summaries first, inspect relevant source when required, then
   propose one Profile subsection per project; no automatic summary-file creation.
6. Present the proposed Markdown and precise destination/change list. Ask material
   questions and revise the proposal; write only after explicit approval of that
   content. Preserve other verified facts. Review for lost facts, duplicate projects,
   unsupported claims and credentials. Report written sections and source/access
   limits. No progress/index notes, parallel JSON or unapproved draft files.

## Profile shape

Use these sections as a compact consistent structure, omitting empty subsections:

- **Summary & Target Roles:** factual overview; distinguish stated targets from
  suggested directions. Do not invent preferences or motivation.
- **Work Experience:** employer, actual title, dates, employment type/location;
  responsibilities, owned contributions, achievements, technologies and limits.
- **Projects:** one named subsection per repository, using project-evidence.md
  for role/contribution, capabilities, achievements, limits, sources and commit.
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
