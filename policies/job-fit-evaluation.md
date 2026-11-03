# Job Fit Evaluation

Version: 1.4. Read with `candidate-evidence-standards.md`. The same standard applies to batch
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

## Screening before detailed assessment

Screen each job's substantive role description and mandatory requirements against
the current Profile first. This is not a title/keyword filter: check whether a
restriction is mandatory, preferred, flexible, or contradicted elsewhere in the JD.
Stop reading secondary duties, benefits, and improvement opportunities once a
decisive requirement makes applying low-value on the recorded evidence.

Examples include ten years of relevant commercial ownership against a clearly
shorter career without equivalent scope, required professional registration, or
required language proficiency unsupported by the Profile. A modest years gap,
senior title, missing preferred tool, or ambiguous wording such as "native-level"
is not alone a stop condition. Count actual transferable responsibilities; do not
convert project work into commercial years.

For confirmed failure, state the decisive requirement and stop. If a required
capability is not recorded, do not claim it is absent: stop provisionally with a
short condition, e.g. "German is required; no evidence is recorded. Reassess if
you have working proficiency." Do not investigate secondary gaps or ask routine
questions just to establish the absence of unrecorded experience. Continue when
existing evidence makes equivalence or a different interpretation plausible;
ask a focused question only to resolve that ambiguity. A user may explicitly
reopen any screened role for deeper assessment.

Early-stop roles still receive an evidence-based numeric score and `Skip` under
the existing CSV contract, not the missing-JD state. Use a compact weighted
assessment of 3–5 decisive groups totaling 100, including the decisive requirement
and strongest transferable evidence, rather than a full 5–8-group breakdown.
Do not invent requirements from unread details. If a screening adjustment is
needed to keep the score in the Skip band, explain the specific reason briefly.
An unverified gate is a provisional priority decision, not a verified legal or
qualification failure. Do not assign a fixed score to all early stops or invent
weights to obtain a label. Both routes retain the same evidence anchors and bands.

For roles not stopped by the screen, identify requirements from the JD before
comparing the candidate. Group roughly
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

Choose and classify the groups and weights from the JD before assigning evidence
scores or looking at an old recommendation. Keep independent capabilities
separate, but do not count dashboards, reporting, KPIs and analytics repeatedly
unless their responsibilities are genuinely distinct. Keep preferred exposure
separate from required/core capabilities; do not silently promote it to a gate.
Freeze this rubric for the assessment's inputs and use it for both batch and chat.

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
Use deterministic rounding: round the weighted total plus explicit adjustments
to the nearest integer, with exact halves rounded up. Derive the recommendation
from that number; never choose a label and then assign a number to match it.
Scores of 9–10 require a short reference explaining the additional direct depth,
ownership or outcomes beyond the 8 anchor. General praise or numerous matching
keywords is not evidence of exceptional depth.

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
When improvement advice is useful, use one rating: No project needed (default),
Optional improvement, High-value
project, or Priority project. Consider JD importance, recurring career value,
existing adjacent evidence, effort and interview-preparation alternatives.
Suggest at most one extension/project normally, with scope, value and timing;
never delay an application for an optional improvement.
For early-stop roles omit improvement plans, project suggestions and default
"No project needed" labels. Do not investigate closing structural gaps unless asked.

## Conversation, uncertainty and consistency

Use one validated assessment for the same job, substantive JD, Profile/evidence
and scoring policy, regardless of batch, chat, model, agent or summary length.
First retrieve its calculation record, not only its prior score or prose summary.
If inputs match and the record is supported and arithmetically valid, reuse its
rubric, scores and recommendation; do not independently improvise a new score
because the user pasted the JD into chat. Recalculate the stored arithmetic if
needed without changing the evidence judgments.

If no valid calculation record exists, assess from evidence without anchoring to
the old number, then compare with available prior output. A saved CSV, successful
sync or seal is not proof of an evidence-based assessment. Explain a discrepancy
as an unsupported prior result when its reasoning cannot be reconstructed; do
not invent a retrospective rubric to defend it or average conflicting scores.

Changes need an identifiable new JD requirement, new/corrected evidence, scoring
policy change, arithmetic correction or explicit correction of interpretation.
For a correction, identify the changed groups/weights/scores and why the prior
treatment was wrong. A different writing style or more detailed discussion is
not a valid reason. This record is a reusable priority judgment, not a claim
that a subjective integer is an objectively exact measure of employability.

## Compact calculation record

Retain private structured calculation records in `data/evaluation_audit.jsonl`,
separate from the unchanged CSV/Sheet columns and short user-facing summaries.
Use one compact record per job and input version: stable job identity, JD and
Profile/evidence/policy fingerprints, the selected requirement groups with
mandatory/core/preferred classification, weights, evidence scores and short
source references, any explicit adjustment and reason, total and recommendation.
Share batch-level provenance where possible. References and short factual reasons
are sufficient; do not generate long reasoning narratives or copy source documents.
Equivalent listings may share a substantive rubric while preserving their own IDs.

Check weights total 100, evidence scores lie within 0–10, arithmetic and rounding
match the final integer, adjustments have reasons, and the label matches the band.
Check evidence supports the judgments as well as the arithmetic. Reject category-
wide fixed-score fallbacks, title/keyword-only scoring and unexplained hand-entered
totals, including on early-stop roles. Summary shortening never authorizes those
shortcuts. A missing/inconsistent record must be resolved before claiming the
batch follows this policy or synchronizing it. Current `--seal` checks alone do
not enforce this calculation-record contract; perform these checks explicitly
until code supports it, and do not claim automatic enforcement already exists.

For roles proceeding beyond the screen, give a **provisional** score for material
unknown experience based only on known evidence, identify pending questions and
ask before finalizing, regardless of
the initial recommendation. In particular, ask about plausible unrecorded
experience that could turn Consider/Skip into Apply/Strong Apply; never assume
that experience exists or award hypothetical credit. Follow the shared evidence
policy for Profile proposals and approval. Batch runs use a concise reassessment
condition only where it could change the decision, not question lists. The
early-stop route does not require routine follow-up questions.

For a single JD lead with score/recommendation (a reasoned priority estimate,
not interview probability), up to three supported strengths, material concerns
and application value. Follow career-workflow.md for interactive request handling.
Keep the response concise; expose weights/evidence mapping when useful
or requested. Prioritize eligibility, mandatory gaps, core work, seniority, then
preferred familiarity. State policy version and Profile review date once in the
batch context/report, not in every row. For a single JD, disclose meaningful
uncertainty in plain language without stock version/date disclaimers; provide
provenance and weights when requested. A short reassessment condition is enough
to identify an early-stop result as provisional. Existing CSV fields remain unchanged.

When structural/non-waivable gaps make preparation low-value, say `reconsider
applying` and stop before document drafting. Give the strongest transferable
point if useful, decisive gap and at most one narrow reassessment condition.
Unknowns remain unknown; early stopping does not require resolving every unknown
or investigating improvement plans. It does not apply to ordinary stretches.
For drafting and its request and saving conditions, follow the
interactive contract in career-workflow.md; explicit user constraints take precedence.

## Unattended batch

Screen every row of `data/pending_jobs.csv`; use stored description first and
perform detailed assessment only when the screen is not decisive. Preserve
separate job IDs across sites even when substantive assessment can be reused.
Apply the same policy; retain decision-relevant eligibility/JD uncertainty through
short gap or reassessment wording, without assuming answers or updating Profile.
JD-insufficient rows use the unscored state above, not a provisional numeric score.

Create/replace `data/scored_jobs.csv` and retain its compact calculation records
as above; do not modify other workflow state during evaluation. Exact CSV columns:

```text
job_id,found_at,site,title,company,location,search_term,job_url,match_score,recommendation,match_summary
```

Preserve the first eight fields from pending input, excluding description. Scores
are integers 0–100 with the policy's four allowed labels for assessable JDs.
For `Not assessed / JD needed`, score must be blank and summary explains the missing JD
and how to supply it. These rows are synchronized so users can still inspect the
listing; processed means synchronized, not that a fit assessment was possible. Use the requested
summary language or local policies/preferences.md. Use 1–2 short sentences for
early-stop roles and normally 2 short sentences otherwise: strongest fit and
decisive gap, with at most one extra reassessment condition if material. Do not
append routine questions, version/Profile-date statements, generic work-permission
checks, "unverified experience receives no credit", or default project ratings.
Mention work permission only for a specific decision issue in the JD or known
circumstances. Common provenance and limitations belong in the batch report once.
Do not change pending rows, source documents, tracker, processed IDs or
Google Sheets; synchronization is a separate action.

Validate one output row per input row, preserved job IDs/metadata, no extra jobs,
exact column order, valid score/label agreement, required uncertainty disclosures
and supported claims. Report total, counts per recommendation and counts with
unscored/missing JD, pending evidence, eligibility or structural gaps; do not dump all
job text. Invalid/ambiguous input identifiers must be reported, not silently lost.

## Reassessment scope

Read the latest Profile and scoring/evidence policies for every new or explicitly
revisited job. Do not bulk re-score synchronized history merely because the Profile
or a policy changed. Reassess a historical role only when the user explicitly asks to revisit it
(for example, by pasting its JD for evaluation); explain changes from its earlier
assessment. Search never automatically requeues synchronized jobs, even if the
scraped JD has changed. Updating that existing Sheet row still needs sync authorization.
Unfinished output must be revalidated if its scoring inputs changed before upload.
PDF/email/style changes are not job-fit changes.
