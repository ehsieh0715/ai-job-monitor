---
name: evaluate-jobs
description: Use when evaluating searched jobs or any manually supplied JD, including roles outside Google Sheets, before deciding whether to prepare an application.
---

# Evaluate jobs

From the repository root read `policies/evidence-policy.md` and
`policies/job-evaluation.md`. They own all evidence and scoring rules.
Read `config/config.local.yaml` directly and resolve configured Career paths as
specified in `config/README.md`; use the profile and relevant summaries, not the
removed candidate directory. Missing configuration/data/access must be reported.

## Conversation

Accept a complete pasted JD without requiring a URL, CSV entry or Sheet row.
Return the common score/recommendation, strongest evidence, material gap and
application value. Ask focused questions for material unknown experience and
label the current assessment provisional. Confirmed facts update the authorized
shared Profile/evidence source before reassessment; explain changes from earlier
judgments. Do not draft a CV/letter until the user confirms proceeding or requests
that document. Use tailor-resume / write-cover-letter then.

## Unattended batch

Read every row of `data/pending_jobs.csv`; use stored description first. Preserve
separate job IDs across sites even when substantive assessment can be reused.
Apply the same policy; record pending questions, eligibility/JD uncertainty and
provisional status in match_summary without assuming answers or updating Profile.

Create/replace only `data/scored_jobs.csv` with these exact columns:

```text
job_id,found_at,site,title,company,location,search_term,job_url,match_score,recommendation,match_summary
```

Preserve the first eight fields from pending input, excluding description. Scores
are integers 0–100 with the policy's four allowed labels. Traditional Chinese
summary normally uses 2–4 sentences and includes relevant uncertainty and policy
version. Do not change pending rows, source documents, tracker, processed IDs or
Google Sheets; synchronization is a separate action.

Validate one output row per input row, preserved job IDs/metadata, no extra jobs,
exact column order, valid score/label agreement, required uncertainty disclosures
and supported claims. Report total, counts per recommendation and counts with
incomplete JD, pending evidence, eligibility or structural gaps; do not dump all
job text. Invalid/ambiguous input identifiers must be reported, not silently lost.
