# Job Fit Evaluation

Version: 1.5.

## JD completeness

- Use complete supplied/local JD text first; fetch official sources only for material omissions. Do not repeatedly browse a complete description.
- Without substantive duties/requirements, leave score blank and label `Not assessed / JD needed`; retain company/title/URL and request the JD. Never substitute 0/Skip for missing information.
- For an existing queued job, retain officially recovered JD text in its pending/history record before preparing/sealing fresh output. Do not seal old scores after changing inputs.
- For public appointments, inspect referenced official packs for citizenship, qualifications, post-qualification years, licences, vetting and clearance; unavailable eligibility remains unknown.

## Screen before detailed scoring

- Compare substantive mandatory requirements with current Profile. Distinguish mandatory, preferred, flexible and contradictory wording; do not screen by title/keywords alone.
- Stop provisionally when a decisive structural requirement makes preparation low-value. State the requirement and at most one narrow reassessment condition; unknown is not confirmed absence.
- A modest years gap, senior title, missing preferred tool or ambiguous "native-level" wording alone is not decisive. Continue and ask when transferable responsibility or another interpretation is plausible.
- Count actual relevant commercial responsibilities and independence, not unrelated work or projects as commercial years. Do not penalize overqualification without a concrete reason.
- **Early-stop scoring:** use 3–5 supported groups with weights totaling 100 and a Skip label. Explain adjustments; never use fixed fallback scores.
- **Early-stop scope:** omit secondary-gap investigation, routine questions, strengths lists and improvement plans. Reassess more deeply if the user requests it.

## Build the rubric

- Before evidence scoring or looking at an old recommendation, choose JD-based groups, classifications and weights. Freeze them for these inputs and reuse across chat/batch.
- For detailed assessment use roughly 5–8 groups; weights total 100, normally in steps of 5. Classify mandatory, core success criterion and preferred/wish-list separately.
- Do not count repeated reporting/dashboard/KPI terms as independent capabilities unless responsibilities differ. Do not promote preferred exposure into a gate.
- Recognize role-defining specialized clusters. Generic SQL or Python cannot offset a missing clinical or operational foundation by receiving full credit for every component.

## Evidence scores

| Score | Anchor |
| --- | --- |
| 0 | No supporting evidence |
| 2 | Mentioned-only familiarity or weak adjacency |
| 4 | Relevant academic/training evidence or limited practical exercise |
| 6 | Directly relevant project implementation or meaningful adjacent professional work |
| 8 | Direct, substantial professional evidence |
| 10 | Exceptional direct professional depth, ownership, scope and results |

- Anchors are not automatic ceilings. Consider directness, context, depth, scope, outcomes and materially relevant recency; strong academic implementation can earn project-level technical credit.
- Specialized operational groups normally warrant 2–4 for generic adjacency, 4–6 for relevant projects, and 7–10 for direct/comparable professional operations. Explain exceptions.
- Scores 9–10 need a short reference showing depth/ownership/results beyond 8. Numerous keywords or praise do not establish exceptional evidence.
- Do not double-count capabilities or equate adjacent activity with the required activity, such as ticket coordination with formal programme ownership.

## Calculate and recommend

- `base score = sum(group score / 10 * group weight)`.
- Keep final score close to base. State each material adjustment and reason, such as eligibility, structural seniority, role-defining gaps or genuinely equivalent responsibility.
- Round weighted total plus adjustments to nearest integer, exact halves up. Derive the label from the score; never tune the score to reach a preferred label.

| Final score | Recommendation |
| --- | --- |
| 85–100 | Strong Apply |
| 70–84 | Apply |
| 55–69 | Consider |
| 0–54 | Skip |

- Verified failure of a non-waivable legal, language, licence or work-authorization gate means Skip; explain an adjustment into the Skip band. An unverified gate is only a provisional priority decision.
- Likely screening requirements reduce priority proportionately; missing preferred items do not automatically reject.
- Strong Apply requires credible coverage of nearly all core and mandatory groups. Important unknown eligibility, an unsupported role-defining requirement or multiple indirectly supported required capabilities prevents it; keep the score and label consistent.
- The score estimates application priority, not interview probability or objectively exact employability.

## Questions and application value

- For non-screened interactive roles, give a provisional score based on known evidence and ask before finalizing material unknowns, even at Consider or Skip. Prioritize plausible unrecorded experience that could change the decision; award no hypothetical credit.
- Use the evidence approval gate for Profile proposals and workflow's limit of three consolidated questions per round. Reassess saved substantive changes; do not invent an approval step for unchanged Profile.
- Single-JD advice leads with a score and label, up to three supported advantages, material concerns and application value. Keep uncertainty plain; expose weights and provenance when useful or requested, not routine version disclaimers.
- Early-stop advice gives the decisive gap, optionally the strongest transferable point, and at most one reassessment condition. Say to reconsider applying when a structural or non-waivable gap makes preparation low-value; stop before drafting.
- Follow `career-workflow.md` for current or standing interactive drafting authorization. Neither a score nor batch execution grants new document-write scope.

## Gaps and preparation

- **Manageable:** verified work transfers substantially; identify the remaining context gap.
- **Quick improvement:** roughly one focused day can create useful evidence or interview readiness; give no credit before completion.
- **Structural:** cannot be solved by wording or a day of work, such as extensive commercial ownership, people management or required certification.
- Mentoring language can reduce expected independence, but does not waive an essential domain or platform foundation. Group material gaps and omit irrelevant missing tools.
- Before suggesting a project, check whether correctly labelled evidence would change viability or merely prepare for interviews. Do not imply it closes a decisive production or domain gap.
- **Improvement rating:** when useful choose No project needed (default), Optional improvement, High-value project, or Priority project.
- **Suggested work:** suggest at most one extension, stating scope, value and timing. Never delay applying for optional work.
- Early stops omit project suggestions and default improvement ratings.

## Consistency and calculation record

- Retrieve the calculation record, not just a prior score or summary. Reuse supported, arithmetically valid judgments for matching JD, Profile, evidence and policy inputs; recompute arithmetic if needed.
- If no valid record exists, assess independently of the old number, then compare. Do not reverse-engineer a rubric to defend unsupported history or average conflicting results; explain the discrepancy.
- Score changes require new or changed JD or substantive evidence, policy changes, arithmetic correction or corrected interpretation. Identify changed groups, scores or weights and why. Writing style and summary length alone are not causes.
- **Calculation record:** save job identity, input fingerprints, classified groups, weights, scores, source references, justified adjustments, total and label in private `data/evaluation_audit.jsonl`.
- **Provenance:** fingerprints cover the JD, Profile, evidence and policy. Share batch provenance where possible, but retain separate listing IDs for equivalent rubrics.
- Validate weights=100, scores=0–10, supported evidence, arithmetic, half-up rounding, justified adjustments and agreement between score and label. Reject category-wide fallbacks, title-only scoring and unexplained totals, including early stops.
- Missing or inconsistent records must be resolved before claiming compliance or syncing. `--seal` validates artifact structure and integrity, not evidence or this calculation contract; check these explicitly until code supports them.
- Keep references and reasons short, not full sources or long reasoning narratives. A subjective priority score is not a probability.

## Batch output

- Screen every `data/pending_jobs.csv` row, using stored JD first. Detail only non-screened roles; preserve separate site IDs and decision-relevant uncertainty without asking blocking questions or updating Profile.
- Replace only `data/scored_jobs.csv` and retain calculation records. Do not change pending rows, sources, tracker, processed IDs or Sheets; sync is separate.
- Use these exact columns:

```text
job_id,found_at,site,title,company,location,search_term,job_url,match_score,recommendation,match_summary
```

- Preserve the first eight input fields, excluding description. One row per input; no added or lost IDs. Report ambiguous identifiers rather than silently dropping them.
- Assessable scores are integer 0–100 with the four matching labels. Missing JD uses blank score, exact `Not assessed / JD needed`, and a summary explaining how to supply it; synchronized does not mean assessed.
- Use the requested language or private language preference. Early-stop summaries use 1–2 short sentences; others normally two: strongest fit and decisive concern, plus at most one decision-changing reassessment condition.
- Do not append routine questions, per-row policy versions or Profile dates, generic permission checks, stock evidence disclaimers or default project ratings. Mention work permission only for a specific issue.
- **Batch validation:** check columns, complete rows and IDs, preserved metadata, matching scores and labels, and uncertainty.
- **Batch report:** record common provenance once; report recommendation totals and counts for missing JD, pending evidence, eligibility and structural gaps. Do not dump JDs.

## Reassessment scope

- Read current Profile, scoring and evidence rules for new or explicitly revisited jobs. Do not bulk re-score synchronized history after Profile or policy edits or automatically requeue because a scrape changed.
- User-requested historical reassessment explains changes; Sheet updates still need sync authorization. Revalidate unfinished output after scoring-input changes. PDF, email or style changes alone do not change fit.
