# Candidate Profile Generation

Version: 1.2. Apply `candidate-evidence-standards.md`; this file owns profile initialization.
This is an AI-assisted document workflow, not a Python conversion command.

## Input and destination

A user-supplied absolute Career root is sufficient to start profile initialization.
For initialization only, a missing local configuration or Profile is expected:
these bootstrap rules replace the existing-file prerequisite in candidate-evidence-standards.md.
Use the supplied root and fixed layout to inspect and propose content. Create Profile
only after approval under candidate-evidence-standards.md; still stop for unavailable sources
or filesystem permission.
Use the fixed paths relative to root: `Candidate Profile.md`, `Source Documents/`,
optional `Source Documents/Projects.md`, `applications.md` and `applications/`.
Only career.root is configurable; do not ask users to fill in individual paths.
Do not create a separate Project Evidence directory or summary files: reviewed
project evidence belongs in the Profile's Projects sections.
Use `config/config.local.yaml` when already configured; if an explicit root differs,
ask whether to switch rather than silently reading/mixing two people's data.
When initializing configuration, preserve existing search/other settings; copy
missing fields from the public example, but never invent personal preferences.

A build/update request authorizes inspection and a proposal, not writing unseen
Profile content (including project evidence). Apply candidate-evidence-standards.md's approval gate,
including initial creation. Local filesystem permission is separately required.
Resolve a file URL to its local path; do not invent remote access.

Inventory only `<career.root>/Source Documents/`, without following symlinks
outside it. This is the required source entry. If missing, create the empty folder
when authorized; if missing/empty, explain where the user must put source files.
Do not choose or request an alternative source directory. Do not recursively scan
the entire vault/computer, clone repositories, move originals or create synchronized
copies.

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
5. Read optional `<career.root>/Source Documents/Projects.md` and follow
   project-evidence-evaluation.md for each listed project. Plain URLs are sufficient.
   Read existing Profile project sections first, inspect relevant source when required, then
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
- **Projects:** one named subsection per project, using project-evidence-evaluation.md
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
needed. Choose Profile and document languages from the current request and local
policies/preferences.md when present; otherwise match the audience. Preserve
original titles and technical terms where needed for accuracy.

## Ongoing use

After generation, the Profile is the maintained shared factual entry point;
raw documents remain references. Follow candidate-evidence-standards.md for later confirmed
experience updates and do not re-read all originals on every assessment. An
incomplete Profile supports only provisional evaluations until material questions
are resolved. Requesting initialization does not authorize job searches, Sheet
writes, application drafting or submission. Those use their respective policies
and separate search/Google settings.

After saving an approved Profile, briefly report its path and offer the next
step: check search/Google setup, then run a user-authorized first search,
evaluation and Sheet sync under career-workflow.md. Point to README.md's
"Try your first search" example; do not require users to know
Python commands or policy names. Do not execute that step merely because the
Profile was saved. Mention scheduling only as an option after a successful trial;
frequency, timezone and recurring-write authorization remain the user's choice.

## Creation and legacy layout

Create the root/Source Documents scaffold only within authorized filesystem
access. Do not create an empty Profile as a substitute for an approved proposal.
Create applications/ subfolders and root applications.md when an authorized
application save/tracker update needs them, not during unrelated profile work.
If old path overrides, Applications/ or Project Evidence/ already exist, follow
the migration safeguards in career-workflow.md; never move or merge them silently.
