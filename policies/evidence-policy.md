# Evidence policy

Version: 1.0. Applies to every assessment and application document.

## Sources and access

Read `config/config.local.yaml` (see `config/README.md`). Resolve `career.root`
as an absolute path; other career paths are relative to it unless absolute.
Missing configuration, files or permission: identify the exact missing path;
do not guess a fallback or silently use another person's data. Configuration
is not permission. AI skills read this configuration directly; Python integration
is tracked separately in the README.

Read the configured Candidate Profile first, then only relevant Project Evidence
summaries. Consult Source Documents or original code when a material claim needs
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

When the user confirms an actual experience, update the relevant Profile section
or Project Evidence summary within authorized scope, retaining context, limits
and source (including user confirmation when that is the source). Do not append
raw conversation as verified facts. Uncertain answers remain open questions.
Reassess afterward and explain any changed judgment. If a necessary write is not
permitted, report it; do not claim the shared profile was updated.

## Language and preferences

Default analysis: Traditional Chinese; CV/letter wording: professional English.
User preferences can change language, length, tone and section order. Shared
rule changes must apply to batch and conversational evaluation together; style
preferences never relax factual boundaries. Keep personal facts out of policies.
