# AI Job Monitor

Turn your own career documents into a maintained Candidate Profile, evaluate jobs
against one evidence standard, and prepare job-specific CVs and cover letters.
Personal documents live in your external Career folder (an Obsidian vault works
well). The repository supplies code, shared policies and one AI skill entry point.

## 1. Create your Profile first

Clone this repo and open it in an AI coding assistant with local file access.
Create a Career folder and place your original CVs, Word/PDF files, experience
notes or old candidate JSON in `Source Documents/`:

```text
01 Career/
  Source Documents/
    ...your original files
```

Copy `config/config.example.yaml` to `config/config.local.yaml`. For Profile
initialization, only change `career.root`; keep the other Career paths at their
defaults unless your files are elsewhere. Grant read access to the sources and
write access to the intended Profile. Setting a path does not grant permission.

Ask in ordinary language, for example:

> Use career-assistant. My Career root is `/absolute/path/to/01 Career`.
> Read Source Documents and build/update Candidate Profile.md there, following
> policies/profile-building.md. Preserve my original files and existing confirmed
> facts; flag conflicts and ask about important missing evidence.

You may also supply the root in conversation and ask the assistant to create the
private configuration using the example. This initial request authorizes writing
the Profile/configuration within granted access, not searching or uploading data.
No Master CV or existing Profile is required. Initialization needs an AI assistant
and document-reading capabilities; running Python alone does not generate it.

The assistant reads available materials, consolidates evidence and saves a
Markdown Profile. Unknown claims stay marked; it does not turn every CV assertion
or README feature into verified experience. Subsequent confirmed experience updates
this same Profile rather than another JSON database. Original sources stay intact.

The old project's exact Profile-generation prompt was not found in the reviewed
project documents or Git history; profile-building.md defines the new repeatable
workflow. It carries forward the old JSON's summary, roles, experience, skills,
projects, education, constraints, tailoring boundaries and conflict information.

## 2. Evaluate a job in the same conversation

Paste any complete JD and say “評估這份工作”. It need not appear in a Sheet or CSV.
The assistant reads the Profile and relevant evidence, gives a common score and
recommendation, and asks about experience that could materially change the result.
Unknowns receive no assumed credit; a changed judgment includes its reason.
If the Profile is incomplete, the assessment is provisional rather than invented.

## 3. Search and synchronize recommendations

Edit `search` in config.local.yaml: keywords, location, sites and time range.
See [configuration](config/README.md) for all supported site identifiers/limits.
Install Python dependencies in a virtual environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python src/main.py
```

Search writes local pending jobs. Ask career-assistant to evaluate the pending
batch under policies/job-evaluation.md; it produces `data/scored_jobs.csv`.
Then, with a correctly configured Sheet and credentials, run:

```sh
.venv/bin/python src/sync_scores_to_sheet.py
```

**Current limit:** Google Sheet name/worksheet/credential path still live in
`src/google_sheets.py`; they are not yet externalized. The sync appends new IDs
and may overwrite the header. Verify a compatible sheet before using it. Career
paths are read directly by the AI; Python loads the private search configuration.
This is not yet a fully automatic clone-and-run setup. A root path alone is enough
for Profile initialization, not for Google authorization, custom searches or sync.
No LLM API evaluation service or scheduler is installed by this workflow.

## 4. Prepare an application after deciding to proceed

Say “Proceed with a CV for this role”. The assistant composes relevant verified
Profile/project evidence under the writing rules; no single base CV is required.
A cover letter is optional. Save/export files when requested or already authorized:

```text
01 Career/
  Candidate Profile.md
  Source Documents/
  Project Evidence/          # Reviewed project summaries; repositories stay in place
  Applications/
    Applications.md          # Existing application tracker
    Company Name/
      YYYY-MM-DD - Job Title/
        CV.md
        CV.pdf               # When exported
        Cover Letter.md      # When useful/requested
```

Folder date is preparation start; actual submission date is in the tracker.
Preserve submitted versions. No separate JD, analysis or progress notes are created
by default. Existing full notes need not be split or moved into this layout.

## Where to change behavior

[career-assistant](.agents/skills/career-assistant/SKILL.md) is the sole skill
entry point; it selects the references below without duplicating their rules.

| Policy | Purpose |
| --- | --- |
| [Profile building](policies/profile-building.md) | Initialize/merge documents into the configured Profile |
| [Evidence](policies/evidence-policy.md) | Sources, claim boundaries, questions and updates |
| [Job evaluation](policies/job-evaluation.md) | Same scoring standard for manual JDs and batches |
| [Resume writing](policies/resume-writing.md) | Select and compose relevant factual content |
| [Resume review](policies/resume-review.md) | Check evidence, relevance and quality |
| [Cover letter](policies/cover-letter-writing.md) | Value, narrative and writing standards |

Presentation preferences can change language, tone, length and order; they cannot
relax evidence standards. Defaults: Traditional Chinese analysis, English CV/letter.
The earlier ai-job-monitor and career-application rules are consolidated here.

## Privacy and sharing

Keep config.local.yaml, profiles, raw documents, applications, cache and credentials
private. This repo's Git history still needs a personal-data/secret audit; moving
files out does not remove historical copies. Do not publish or rewrite history
until the audit and handling plan have been reviewed.
