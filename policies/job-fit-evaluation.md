# Job Fit Evaluation

Version: 1.2. Read with `candidate-evidence-standards.md`. The same standard applies to batch
search results, pasted JDs and manually found jobs; neither Sheet membership nor
an existing CV is required. The score measures the value of preparing and applying.

## JD and requirements

Use a complete supplied/local JD first. Fetch an official source only for material
omissions; do not repeatedly browse complete local descriptions. If JD is absent
or too incomplete to identify substantive duties and requirements, do not assign
any numeric score or Apply/Skip advice. Use `Not assessed / JD needed`, leave match_score
blank, preserve the URL/company/title and explain that the user may paste the JD
for evaluation. A title or generic company description is not sufficient. Never
use 0/Skip as a missing-information placeholder. In conversation invite the user
to paste the JD; in batch continue the other jobs. Incomplete candidate evidence
with a sufficient JD is a different case: it can receive provisional assessment.

If a real JD is recovered from an official URL or supplied by the user for an
existing queued job, retain that text in the corresponding pending/history record
before preparing/sealing a fresh assessment. Do not alter a prepared queue and
then seal the old results; prepare again and evaluate the current queue. This is
source recovery, not permission to guess requirements or overwrite other jobs.
For public appointments inspect referenced official booklets/application packs
for citizenship, qualifications, post-qualification years, licences, vetting and
clearance. Unavailable eligibility is unverified, not a confirmed failure.

Identify requirements from the JD before comparing the candidate. Group roughly
5–8 material capabilities; classify each as explicit mandatory, core success
criterion, or preferred/wish-list. Ambiguous wording is not an automatic gate.
A repeated keyword is not an independent capability. Recognize a role-defining
cluster only when several specialized capabilities form the role's essential
foundation (e.g. clinical systems, integration standards and operational support).
Generic SQL/Python or project evidence cannot offset a missing specialized
foundation by receiving full credit for every component.

## Common score

Assign group weights totaling 100, normally in steps of 5, by importance to doing
the job. Score each group 0–10 using the strongest relevant verified evidence:

| Anchor | Evidence |
| --- | --- |
| 0 | No supporting evidence |
| 2 | Mentioned-only familiarity or weak adjacency |
| 4 | Relevant academic/training evidence or limited practical exercise |
| 6 | Directly relevant project implementation or meaningful adjacent professional work |
| 8 | Direct, substantial professional evidence |
| 10 | Exceptional direct professional depth, ownership, scope and results |

These are anchors, not automatic ceilings by background. Consider directness,
context, depth, scope, outcomes and materially relevant recency. A strong academic
implementation may warrant project-level technical credit. Specialized operational
groups normally warrant 2–4 for generic adjacent work, 4–6 for relevant projects,
and 7–10 only for direct/comparable professional operations. Explain exceptions.
Do not double-count the same capability or mistake an adjacent activity for the
exact requested activity (e.g. ticket coordination is not formal programme ownership).

`base score = sum(group score / 10 * group weight)`

Round the final score to an integer 0–100. Keep it close to the base; material
adjustments require a stated reason such as eligibility, structural seniority,
role-defining capability or genuinely equivalent transferable responsibility.
Do not tune a score merely to reach a preferred label.

| Final score | Recommendation |
| --- | --- |
| 85–100 | Strong Apply |
| 70–84 | Apply |
| 55–69 | Consider |
| 0–54 | Skip |

Verified failure of a non-waivable legal, language, licence, work-authorization
or similar gate means Skip; keep the final score in the Skip band and explain
the gate adjustment. A likely screening requirement reduces priority in proportion
to its importance; a missing preferred item does not automatically reject.
Strong Apply requires credible coverage of nearly all core/mandatory groups.
Unverified important eligibility, an unsupported role-defining requirement, or
multiple required capabilities supported only indirectly prevents Strong Apply;
reconsider the score consistently rather than emitting conflicting score/label.

## Gaps and investment

- **Manageable:** verified work substantially transfers; state the remaining context gap.
- **Quick improvement:** about one focused day could create genuine evidence or
  useful interview readiness. Do not credit future work before completion.
- **Structural:** cannot be solved by wording or one day: extensive relevant
  commercial experience, people management, deep domain operations or mandatory certification.

Judge years by actual relevant responsibilities and expected independence. A
modest gap is not automatic Skip; distinguish absolute eligibility, screening
risk and wish-list. Do not count unrelated work or projects as direct commercial
years. Do not penalize overqualification without a concrete reason. Mentoring
language can reduce expected depth, but does not automatically waive an essential
platform/domain foundation. Group material gaps; omit irrelevant missing tools.

Before suggesting a project, ask whether its correctly labelled evidence would
actually change viability or merely prepare for interviews. If the decisive
production/domain gap remains, it cannot materially raise the recommendation.
Use one rating: No project needed (default), Optional improvement, High-value
project, or Priority project. Consider JD importance, recurring career value,
existing adjacent evidence, effort and interview-preparation alternatives.
Suggest at most one extension/project normally, with scope, value and timing;
never delay an application for an optional improvement.

## Conversation, uncertainty and consistency

Show the same numeric score and recommendation for a manual JD. Initial and deep
assessment differ in detail, not standards. Recompute independently of old labels,
then compare with available prior results. Explain changes through new JD details,
confirmed evidence, corrected interpretation or policy version; do not change
judgment simply because the user selected the job.

For material unknown experience give a **provisional** score based only on known
evidence, identify pending questions and ask before finalizing, regardless of
the initial recommendation. In particular, ask about plausible unrecorded
experience that could turn Consider/Skip into Apply/Strong Apply; never assume
that experience exists or award hypothetical credit. Follow the shared evidence
policy for Profile proposals and approval. Batch runs record these questions and
the provisional limitation in the summary without blocking other jobs.

For a single JD lead with score/recommendation (a reasoned priority estimate,
not interview probability), up to three supported strengths, material concerns
and application value. Follow career-workflow.md for interactive request handling.
Keep the response concise; expose weights/evidence mapping when useful
or requested. Prioritize eligibility, mandatory gaps, core work, seniority, then
preferred familiarity. State policy version and whether provisional; record the
JD source and profile/evidence version or review date when available, never invent
versions. Existing CSV fields remain unchanged; put necessary context in summary.

When structural/non-waivable gaps make preparation low-value, say `reconsider
applying` and stop before document drafting. Give the strongest transferable
point, decisive gap, why wording cannot fix it and any narrow condition worth
checking. Resolve material unknowns before treating a gap as confirmed; this stop
rule must not suppress those questions. It does not apply to ordinary stretches.
For drafting and its request and saving conditions, follow the
interactive contract in career-workflow.md; explicit user constraints take precedence.

## Unattended batch

Read every row of `data/pending_jobs.csv`; use stored description first. Preserve
separate job IDs across sites even when substantive assessment can be reused.
Apply the same policy; record pending questions, eligibility/JD uncertainty and
provisional status in match_summary without assuming answers or updating Profile.
JD-insufficient rows use the unscored state above, not a provisional numeric score.

Create/replace only `data/scored_jobs.csv` with these exact columns:

```text
job_id,found_at,site,title,company,location,search_term,job_url,match_score,recommendation,match_summary
```

Preserve the first eight fields from pending input, excluding description. Scores
are integers 0–100 with the policy's four allowed labels for assessable JDs.
For `Not assessed / JD needed`, score must be blank and summary explains the missing JD
and how to supply it. These rows are synchronized so users can still inspect the
listing; processed means synchronized, not that a fit assessment was possible. Use the requested
summary language or local policies/preferences.md. The summary normally uses
2–4 sentences and includes relevant uncertainty and policy
version. Do not change pending rows, source documents, tracker, processed IDs or
Google Sheets; synchronization is a separate action.

Validate one output row per input row, preserved job IDs/metadata, no extra jobs,
exact column order, valid score/label agreement, required uncertainty disclosures
and supported claims. Report total, counts per recommendation and counts with
unscored/missing JD, pending evidence, eligibility or structural gaps; do not dump all
job text. Invalid/ambiguous input identifiers must be reported, not silently lost.

## Reassessment scope

Read the latest Profile and scoring/evidence policies for every new or explicitly
revisited job. Do not bulk re-score synchronized history merely because the Profile
or a policy changed. Reassess a historical role when the user identifies/pastes it
(or when a changed JD is actually observed); explain changes from its earlier
assessment. Updating that existing Sheet row still needs sync authorization.
Unfinished output must be revalidated if its scoring inputs changed before upload.
PDF/email/style changes are not job-fit changes.
