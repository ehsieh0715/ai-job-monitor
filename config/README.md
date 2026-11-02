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
| `google_sheets.spreadsheet` | Destination Google Sheet URL or ID. | `https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit` |
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
can vary. No Google account credentials belong in this YAML: the intended Sheet
workflow uses the connected Google Drive account with Sheets read/write access.
**Connector sync integration is pending; the existing Python sync command still
requires a service-account key.** See [current status and setup](../README.md#google-sheets-setup-first-time).

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

The execution and evidence rules live in [workflow.md](../policies/workflow.md).
