# Candidate Profile Generation

Version: 1.3.

## Setup

- For initialization, a user-supplied absolute Career root is sufficient; missing Profile/config is expected. Use the fixed layout and migration safeguards in `career-workflow.md`.
- **Root conflict:** ask before switching to an explicit root that differs from config; do not mix candidate data.
- **Config creation:** preserve existing settings and copy missing fields from the public example, without inventing preferences.
- Inventory only `Source Documents/`, without following external symlinks. If missing/empty, create an authorized empty source folder and explain where to put inputs; do not substitute another source directory or scan the vault/computer.
- Resolve file URLs to local paths; report inaccessible, scanned or unreadable content and extraction limits. Do not claim remote access or a Python conversion workflow.
- Do not clone whole projects, move originals or create synchronized source copies by default.

## Consolidate

1. Read an existing Profile; merge verified additions, notes and source pointers rather than reset it.
2. Read relevant Markdown/text/JSON/Word/PDF inputs. Legacy `candidate_profile.json` is input, not a second maintained database; CV variants are not independent corroboration.
3. Extract dates, context, actions, personal contribution, skills, results and limits. Keep source pointers per claim group; exact metrics need traceable support. A resume assertion is not implementation or authorship proof.
4. Preserve confirmed facts over unverified older claims. Put uncertain titles/dates/metrics in Open Questions; ask high-impact questions without blocking initialization on every unknown.
5. Review optional `Source Documents/Projects.md` under `project-evidence-evaluation.md`; plain URLs suffice. Reuse existing project evidence and propose one section per stable project identity.
6. Display proposed content and exact destination/changes; use the evidence policy's approval gate. After approval check lost facts, duplicates, unsupported claims and credentials; report saved sections and access limits.

## Profile sections

- **Summary & Target Roles:** factual overview; distinguish stated targets from suggestions.
- **Work Experience:** employer, title, dates, employment type and location, owned work, results, technologies and limits.
- **Projects:** context, contributions, implementation, results, limits, sources and reviewed commit.
- **Skills & Evidence:** capability, evidence type, depth and supporting work or projects.
- **Education & Certifications:** supported qualification, dates and status.
- **Constraints & Preferences:** location, permission, availability and stated interests; mark unknowns.
- **Claim Boundaries:** factual clarifications and wording risks specific to this candidate.
- **Open Questions & Conflicts:** unresolved claims and sources, never established capability.
- **Source Review:** source paths, review date, inspected revisions and limits of extraction or verification; no credentials or full source dumps. Review date does not prove every source is current.

## Save and reuse

- Omit empty subsections. Retain evidence for multiple job directions, not a finished CV or every raw document; link fuller sources when needed.
- Keep reviewed project evidence inside Profile. No separate Project Evidence directory, per-project summaries, parallel JSON, progress/index notes or unapproved draft files.
- Choose language from current instructions/private preferences, otherwise audience; preserve original titles/technical terms for accuracy.
- Create the root and source scaffold only with access; never create an empty Profile in place of approved content. Application folders/tracker are created only when their authorized stage needs them.
- Later updates use the evidence approval gate. Incomplete Profile supports provisional evaluation, not invented experience.
- **After saving:** report the Profile path and offer the README's first-search workflow in ordinary language.
- **Next action:** do not search, sync, draft or submit merely because Profile was saved; require authorization for that stage.
- Scheduling is optional after a successful trial; timing, timezone, environment and recurring writes remain the user's choices.
