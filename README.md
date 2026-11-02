# AI Job Monitor

Search for jobs, assess application value and prepare evidence-based applications
using your own Career Markdown folder. No web interface is required.

## Shared standards

| File | Purpose |
| --- | --- |
| [Evidence policy](policies/evidence-policy.md) | Facts, sources, contributions, questions and profile updates |
| [Job evaluation](policies/job-evaluation.md) | One scoring standard for batch results and any pasted JD |
| [Resume writing](policies/resume-writing.md) | Compose a job-specific CV from verified evidence |
| [Resume review](policies/resume-review.md) | Check claims, relevance and document quality |
| [Cover letter writing](policies/cover-letter-writing.md) | Value, narrative, writing and attachment standards |

`.agents/skills/career-assistant/SKILL.md` is the single entry point. It selects
the relevant policy files; all standards and workflow details live in policies.
The policies consolidate the earlier ai-job-monitor evaluation rules and
career-application playbook/writing guidance. They replace the old requirement to
select exactly one base CV: a Master CV or existing CV is not required. Initial
and deep assessments use the same score; newly confirmed evidence can change it
with an explanation. Personal facts belong outside this repo.

## Configure your own data

Copy `config/config.example.yaml` to `config/config.local.yaml`, set your Career
root, and grant the assistant necessary filesystem access. See
[configuration](config/README.md). Keep the local file and credentials private.
A configured path does not grant access. Suggested external layout:

```text
01 Career/
  Candidate Profile.md
  Source Documents/       # Original CV, Word/PDF and other source materials
  Project Evidence/       # Reviewed summaries, sources, limitations and commit
  Applications/
    Applications.md       # Existing application tracker
    Company Name/
      YYYY-MM-DD - Job Title/
        CV.md
        CV.pdf             # When exported
        Cover Letter.md    # Only when useful/requested
```

Folder date means preparation start; the tracker records actual submission date.
Preserve submitted versions. Do not copy entire project repositories into Career.
Do not commit profiles, source documents, generated applications or credentials.

## AI conversation workflow

Use an assistant that can read local files and this repo's skills. For example:

- “Use career-assistant to assess this JD.” A pasted JD needs no Sheet entry.
- “I actually implemented this; here is my contribution.” Confirmed evidence can
  update the shared Profile and change the assessment.
- “Proceed with a CV for this role.” Compose relevant evidence under the writing
  rules, then save when authorized. A letter is optional.

Language defaults are Traditional Chinese analysis and English application text;
users can change presentation preferences without weakening evidence rules.
Skills are instructions for an assistant, not a built-in LLM evaluation service.

## Current Python pipeline and limits

Install dependencies from `requirements.txt` in a virtual environment.
Run `python src/main.py` to search into local `data/` CSVs. The career-assistant skill in batch evaluation mode
can produce `data/scored_jobs.csv`; `python src/sync_scores_to_sheet.py` then
synchronizes scores. This requires network access and valid Google credentials.

Career paths are currently read directly by AI skills, not by Python scripts.
Search parameters are loaded from the private configuration (see
[configuration](config/README.md)). Google Sheet name/worksheet/credential path
remain in `src/google_sheets.py`.
The Python pipeline is therefore **not yet fully configurable for another user**.
Sync currently appends new IDs and may overwrite the header; verify a compatible
sheet before running. Updating existing assessments/fully configurable sync are
future implementation work. No scheduler is installed by this change.

## Before sharing publicly

The working tree and Git history need a separate personal-data/secret audit.
Moving files out of the repo does not remove historical copies. Do not publish or
rewrite history until the audit and a history-handling plan have been reviewed.
