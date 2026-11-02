# Configuration

Copy `config.example.yaml` to `config.local.yaml` and fill in your settings.
`config.local.yaml` is private and Git-ignored. Career setup needs only a root;
job search and Sheet synchronization need their respective sections too.

## Fields

| Field | Definition | Example / default |
| --- | --- | --- |
| `career.root` | Absolute path to your Career folder. All Career filenames below are fixed by the project. | `/absolute/path/to/01 Career` |
| `search.keywords` | Non-empty list of job search terms. Each term runs a search. | `[data analyst, analytics engineer]` |
| `search.location` | Location sent to the job boards. | `Dublin, Ireland` |
| `search.sites` | Non-empty list of job board identifiers; see supported values below. | `[linkedin, indeed]` |
| `search.hours_old` | Listing age filter in hours; positive integer. | `6` |
| `search.results_wanted` | Requested results per keyword; positive integer, not a guaranteed count. | `100` |
| `search.country_indeed` | Country name used by Indeed and Glassdoor. | `Ireland` |
| `search.linkedin_fetch_description` | Whether to fetch LinkedIn job descriptions. | `true` |
| `google_sheets.spreadsheet_name` | Exact, unique spreadsheet title shared with the service account. | `AI Job Monitor` |
| `google_sheets.worksheet` | Exact tab name inside that Sheet, including capitalization and spaces. | `Jobs` |

Search fields are all required when running the crawler. Supported `sites` values
for pinned JobSpy 1.1.82:

| Value | Coverage |
| --- | --- |
| `linkedin` | Global; uses `location` |
| `indeed` | Multiple countries; uses `country_indeed` |
| `glassdoor` | Supported country domains, including Ireland; uses `country_indeed` |
| `zip_recruiter` | US and Canada |
| `bayt` | Coverage depends on the board, e.g. Middle East locations |
| `naukri` | India |
| `bdjobs` | Bangladesh |

`google` is not usable in this pipeline. Board availability and filter support
can vary. Save your own service-account JSON as `google-service-account.json` at
the repository root (Git-ignored). Its location is fixed; no path setting is needed.
Never put the key contents in config or include it in a shared ZIP. Follow the [six-step credential setup](../README.md#google-sheets-setup-first-time).
No connector login is needed. Existing spreadsheet URL/ID configurations remain
compatible, but the public example uses a spreadsheet name for simpler setup.

Personal presentation preferences are optional and live at the fixed, Git-ignored
`policies/preferences.md` path, outside config. No preferences path field is needed.

## Career files and folders

These paths are fixed relative to `career.root`; users do not configure them.

| Path | Purpose / who creates it |
| --- | --- |
| `Source Documents/` | Required input folder. The AI can create the empty folder; users put original CVs and other source documents here. |
| `Source Documents/Projects.md` | Optional user input listing project links, one per line. Only needed when supplying projects; see the short README example. |
| `Candidate Profile.md` | AI writes approved personal facts and reviewed project evidence here after content approval. |
| `applications.md` | AI creates/updates the application tracker when authorized. |
| `applications/Company Name/YYYY-MM-DD - Job Title/` | AI creates application folders when saving requested documents. Date is preparation start; submission date is recorded in the tracker. |
| `…/CV.md`, `…/Cover Letter.md` | AI-generated application documents when requested. |
| `…/CV.pdf` | Exported only when requested/needed. |

Use lowercase `applications` exactly. Project evidence stays inside Candidate
Profile.md. Existing files are preserved; old custom paths are no longer used and
are not automatically migrated. Filesystem permissions are separate from config.

## Working files in the repository

These private files are created as the pipeline runs; users do not fill them in.

| Path | Purpose |
| --- | --- |
| `data/raw_jobs.csv` | Crawler search results. |
| `data/job_history.csv` | Retained job descriptions for later reassessment. |
| `data/pending_jobs.csv` | Jobs waiting for AI evaluation. |
| `data/scored_jobs.csv` | AI evaluation output. |
| `data/evaluation_context.json`, `data/scored_context.json` | Queue/input fingerprints and sealed score hash used for validation. |
| `data/processed_job_ids.json`, `data/last_synced_context.json` | Processed IDs and evaluation context recorded after successful synchronization. |

The execution and evidence rules live in [career-workflow.md](../policies/career-workflow.md).

## Evaluation states and refresh

The fixed evaluation CSV/Sheet columns remain unchanged. For a usable JD, score
is an integer 0–100 with its matching recommendation. For missing/insufficient JD,
match_score is blank, recommendation is exactly `未評分／待補 JD`, and summary
explains how to provide the full JD. This is not a rejection. Known title/company/
URL stay visible. AI determines substantive JD completeness; Python validates the
structural contract and rejects numeric scores when no JD text exists locally.

Synchronized history is not automatically requeued on Profile/policy edits. New,
changed-JD and explicitly revisited jobs use current data/rules. Unfinished output
is invalidated by Profile/scoring/evidence changes; formatting/email preferences
are excluded. Processed IDs mean already synchronized, including unscored listings.
