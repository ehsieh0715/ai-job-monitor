---
name: evaluate-jobs
description: Evaluate pending job opportunities against the candidate profile, score application value, identify realistic skill gaps, and produce scored_jobs.csv with Traditional Chinese recommendations.
---

# Evaluate Jobs

Evaluate pending job opportunities against the candidate's verified experience and determine whether each opportunity is worth spending time tailoring a resume and applying for.

## Required Inputs

Read:

- `candidate/candidate_profile.json`
- `data/pending_jobs.csv`

Use `candidate/candidate_profile.json` as the factual source for candidate experience, skills, projects, education, and evidence strength.

`data/pending_jobs.csv` contains:

- `job_id`
- `found_at`
- `site`
- `title`
- `company`
- `location`
- `search_term`
- `job_url`
- `description`

Evaluate every job currently listed in `data/pending_jobs.csv`.

## Job Description Source

Use the local `description` column in `data/pending_jobs.csv` as the primary source for job requirements.

Do not browse LinkedIn or Indeed when a non-empty and reasonably complete local description is available.

Only use `job_url` as a fallback when:

- `description` is empty;
- `description` is clearly incomplete;
- the stored content does not contain enough information to make a reasonable assessment.

If the complete JD still cannot be obtained:

- evaluate cautiously using available title, company, location, and context;
- do not invent requirements;
- explicitly state in the Traditional Chinese summary that the完整 JD 無法取得.

## Primary Evaluation Goal

The score should answer:

> How worthwhile is it for this candidate to spend time tailoring the resume and applying?

Do not evaluate jobs purely by keyword overlap.

The objective is to help prioritize applications and avoid spending time tailoring resumes for jobs where the underlying mismatch cannot realistically be solved.

## Candidate Evidence Rules

Use the candidate profile as the factual source of candidate experience.

Do not invent:

- skills;
- years of experience;
- production experience;
- responsibilities;
- achievements;
- project ownership;
- technologies;
- certifications.

Distinguish carefully between:

- `professional` evidence;
- `project` evidence;
- `academic` evidence;
- `mentioned` or mentioned-only technologies.

Professional evidence should generally receive the strongest weight.

Portfolio projects are valid evidence of demonstrated capabilities, especially for technical tools and concepts.

However, project experience must not be represented as equivalent to years of professional production experience.

Academic experience can support understanding and foundational capability but must not be represented as commercial experience.

Repeated evidence across multiple resume versions must not artificially increase evidence strength.

## Role Title Handling

Do not penalize the candidate simply because a previous job title differs from the target job title.

Evaluate actual responsibilities and demonstrated capabilities.

For example, responsibilities performed under `Data & Growth Manager` may provide legitimate evidence for:

- Data Analyst;
- Analytics Engineer;
- Data Engineer;
- Business Analyst;
- Data Governance;
- BI-related roles;

when the actual responsibilities support the target position.

Use role-title tailoring guidance from the candidate profile where appropriate.

Do not fabricate employment titles or imply a promotion or contractual title that did not occur.

## Scoring

Use:

- 85–100: `Strong Apply`
- 70–84: `Apply`
- 55–69: `Consider`
- 0–54: `Skip`

`match_score` should represent application priority and expected value of spending time tailoring the resume.

Do not calculate the score by mechanically counting matching technologies.

## Evaluation Priorities

Give strong weight to:

- relevant professional responsibilities;
- transferable experience;
- demonstrated technical capabilities;
- relevant portfolio projects;
- analytics experience;
- data engineering experience;
- business analysis experience;
- stakeholder and cross-functional collaboration;
- data quality;
- data governance;
- reporting and BI;
- experimentation;
- product analytics;
- business analytics;
- SQL and data modelling;
- demonstrated ability to learn adjacent technologies.

Consider the overall shape of the candidate's experience rather than requiring an exact historical job-title match.

## Overqualification

Do not penalize overqualification by default.

A role being somewhat junior should not reduce the score unless there is a concrete reason that applying would be inappropriate or unlikely to make sense.

The primary concern is whether the candidate is underqualified in ways that materially reduce application value.

## Experience and Seniority Requirements

Treat years-of-experience requirements carefully.

If a role asks for substantially more experience than the candidate can demonstrate, such as:

- 7+ years;
- 8+ years;
- 10+ years;
- extensive senior leadership;
- substantial people-management experience;
- senior architecture ownership;

determine whether this appears to be:

1. a strict requirement;
2. a preferred qualification;
3. recruiter wish-list language.

Do not automatically reject a job because one preferred experience number is higher.

If the seniority or experience requirement appears fundamental to the role, treat it as a meaningful structural gap.

Explain clearly in `match_summary` when required seniority or years of experience are the primary reason for lowering the score.

Do not recommend spending significant time rewriting the resume to compensate for an experience gap that cannot realistically be fixed.

## Quickly Learnable Skills

When a job requires a skill or concept the candidate currently lacks, determine whether useful evidence could realistically be created within approximately one focused day.

Possible quick improvements include:

- learning core concepts of a tool;
- completing a small practical exercise;
- extending an existing portfolio project;
- adding a small demonstrable implementation;
- learning relevant terminology;
- adding meaningful project documentation;
- creating a small proof of concept.

Recommend quick improvement only when the work would create genuine evidence or materially improve interview readiness.

Do not recommend simply adding unsupported keywords to the resume.

When appropriate, explicitly identify:

`可快速補強：`

and explain the specific action.

For example:

「可快速補強：目前缺少 Microsoft Fabric 的實作證據，但可考慮用現有 analytics engineering project 做一個小型 Fabric implementation，建立可展示的實作證據。」

Do not recommend a one-day project when the JD clearly expects substantial commercial or production experience with that technology.

## Structural Gaps

Structural gaps include requirements that cannot realistically be solved through one-day learning or resume tailoring.

Examples:

- 7+ years of required experience;
- extensive production experience;
- several years of people management;
- mandatory professional certification;
- deep industry-specific experience;
- senior architecture ownership;
- substantial commercial experience with a technology;
- significant leadership responsibility.

Identify these clearly.

Do not suggest artificial resume changes to hide structural gaps.

The summary should explain when such a gap makes resume tailoring low-value.

## Mentioned-Only Technologies

Technologies classified in the candidate profile as mentioned-only must not be represented as demonstrated hands-on experience.

If the target job explicitly requires one of these technologies:

1. identify the gap;
2. determine how important it is to the role;
3. determine whether a small project could provide meaningful evidence;
4. mention a quick improvement only when realistic.

If the technology is not relevant to the target job, do not mention or emphasize it.

Never convert familiarity into professional experience.

## Project Evidence

Use relevant portfolio projects strategically when evaluating fit.

A project can demonstrate:

- technical capability;
- conceptual understanding;
- implementation experience;
- learning ability;
- related tooling experience.

It cannot automatically demonstrate:

- commercial production experience;
- enterprise-scale ownership;
- years of professional experience.

For collaborative projects, respect candidate contribution boundaries recorded in the candidate profile.

Do not attribute repository-wide work to the candidate when individual ownership is unclear.

## Resume-Tailoring Value

Explicitly consider whether tailoring the resume is worth the candidate's time.

A high score generally means:

- underlying experience already matches reasonably well;
- the candidate has credible evidence for core responsibilities;
- gaps are manageable;
- tailoring could materially improve positioning;
- applying is worthwhile.

A medium score may mean:

- several relevant capabilities exist;
- one or more meaningful gaps remain;
- the application may still be reasonable;
- substantial resume rewriting may have limited value.

A low score generally means:

- important requirements are structurally missing;
- seniority is substantially mismatched;
- core domain expertise is absent;
- rewriting wording would not materially solve the mismatch;
- time is probably better spent on another application.

Do not recommend unnecessary resume changes merely to mirror JD wording.

When the candidate already has the necessary evidence, prefer recommending targeted wording changes over creating unnecessary new projects.

## Traditional Chinese Assessment Requirement

`match_summary` MUST be written in Traditional Chinese.

Do not use Simplified Chinese.

Keep technical terms, technologies, product names, and commonly used job terminology in English when clearer.

Examples include:

- dbt
- Power BI
- Microsoft Fabric
- Python
- SQL
- Azure
- stakeholder management
- data modelling
- ETL
- CI/CD

Do not translate technical terminology unnaturally.

## Match Summary Content

The summary should normally explain:

1. why the role matches;
2. the strongest relevant candidate evidence;
3. the most important gap;
4. whether the gap is:
   - already manageable;
   - quickly learnable;
   - or structurally difficult to overcome;
5. whether resume tailoring is worth the time;
6. when relevant, what specifically should be emphasized or quickly strengthened.

Keep the assessment concise but sufficiently informative for application decisions.

Usually use approximately 2–4 sentences.

### Strong match example

「匹配度高。現有 Data Engineering、SQL、dbt 與 data quality 經驗可直接對應主要職責，相關 portfolio 也提供足夠的技術證據。Microsoft Fabric 目前缺乏實作證據，但屬於可快速補強項目，可考慮用現有 analytics engineering project 延伸一個小型 Fabric implementation。值得針對此職缺調整履歷並投遞。」

### Structural gap example

「核心 Data Analyst 能力符合，包含 SQL、dashboard、stakeholder collaboration 與 business analysis。主要差距是職缺明確要求 7+ 年相關商業經驗，屬於短期無法補足的年資差距。修改履歷無法實質解決此問題，因此不建議投入大量時間客製履歷。」

### Minimal tailoring example

「職責與既有經驗高度吻合，主要差異集中在工具名稱，沒有明顯結構性缺口。建議投遞，履歷只需針對 JD 調整既有 bullet wording 與相關 project 排序，不需要另外建立 project。」

### Quick improvement example

「整體 Analytics Engineer 職責與既有 SQL、dbt、data modelling 及 data quality project 高度相關。主要缺口是 JD 要求 Airflow，目前只有 familiarity-level evidence。可快速補強：若 Airflow 屬於核心要求，可在現有 pipeline project 加入簡單 DAG 作為實作證據；完成後再於履歷中準確呈現。」

## Output

Create:

`data/scored_jobs.csv`

Preserve these columns from `pending_jobs.csv`:

- `job_id`
- `found_at`
- `site`
- `title`
- `company`
- `location`
- `search_term`
- `job_url`

Do NOT copy `description` into the output.

Add exactly:

- `match_score`
- `recommendation`
- `match_summary`

The final column order must be:

1. `job_id`
2. `found_at`
3. `site`
4. `title`
5. `company`
6. `location`
7. `search_term`
8. `job_url`
9. `match_score`
10. `recommendation`
11. `match_summary`

`match_score` must be an integer from 0 to 100.

`recommendation` must be exactly one of:

- `Strong Apply`
- `Apply`
- `Consider`
- `Skip`

Do not add additional columns unless explicitly requested.

## Processing Rules

Evaluate every row currently present in `data/pending_jobs.csv`.

If duplicate listings for the same underlying role appear across Indeed and LinkedIn, evaluate each CSV row so downstream job IDs remain intact.

You may reuse the same substantive evaluation when the descriptions clearly represent the same position.

Use the locally stored job description whenever available.

Do not repeatedly browse job URLs when local descriptions contain sufficient evidence.

## Files That Must Not Be Modified

Do not modify:

- `data/pending_jobs.csv`
- `candidate/candidate_profile.json`
- source resumes
- project source materials
- Google Sheets
- `processed_job_ids.json`

Only create or replace:

`data/scored_jobs.csv`

## Final Validation

Before finishing:

1. confirm every pending job has exactly one output row;
2. confirm every `job_id` from pending jobs is preserved;
3. confirm no extra jobs were introduced;
4. confirm every `match_score` is an integer between 0 and 100;
5. confirm every `recommendation` uses an allowed value;
6. confirm every `match_summary` is written in Traditional Chinese;
7. confirm `description` is not included in `scored_jobs.csv`;
8. confirm no candidate experience was fabricated.

## Completion Summary

After writing `data/scored_jobs.csv`, report:

- total jobs evaluated;
- Strong Apply count;
- Apply count;
- Consider count;
- Skip count;
- jobs where complete JD information was unavailable;
- jobs with realistic one-day skill improvements;
- jobs primarily downgraded because of seniority or experience requirements.

Do not print all individual evaluations in the terminal unless requested.
The CSV is the primary output.