# Career data paths

Copy `config.example.yaml` to `config.local.yaml` and edit `career.root`.
The local file contains private settings and must not be committed.
For AI-assisted Profile initialization, only career.root needs changing when the
default folder names fit. See policies/profile-building.md (relative to the repo
root). A root alone does not configure Google authorization or search preferences.

`root` is an absolute path. All other paths are relative to `root`, or may
be absolute paths when the data is stored elsewhere. Use ordinary filesystem
paths, not Obsidian URLs. Filesystem access must be authorized separately.

| Key | Purpose |
| --- | --- |
| `profile` | Verified candidate facts in Markdown |
| `source_documents` | Original CVs, Word/PDF files and other source material |
| `project_evidence` | Reviewed project evidence summaries with source references |
| `applications` | Per-application CV and cover-letter files |
| `application_tracker` | Application status table in Markdown |

Source documents are retained as evidence, not automatically treated as verified
facts. Project repositories remain at their original locations.

## Search settings

The `search` section of config.local.yaml replaces the old search_terms.yaml.
All fields are required; config.example.yaml supplies a complete example:

| Key | Purpose |
| --- | --- |
| `keywords` | Non-empty list of job search terms |
| `location` | Search location |
| `sites` | Non-empty list of site names supported by JobSpy |
| `hours_old` | Positive integer; listing age filter in hours |
| `results_wanted` | Positive integer; requested results per keyword |
| `country_indeed` | Indeed country name supported by JobSpy |
| `linkedin_fetch_description` | Boolean; fetch LinkedIn descriptions |

## Site values

For the pinned `python-jobspy==1.1.82`, use these exact lowercase identifiers.
Choose a subset; listing every site does not improve coverage in every country.

| Value | Service | Region / limitations |
| --- | --- | --- |
| `linkedin` | LinkedIn | Global; uses `location` |
| `indeed` | Indeed | Multiple countries; uses `country_indeed` and `location` |
| `glassdoor` | Glassdoor | Supported country domains, including Ireland; uses `country_indeed` and `location` |
| `zip_recruiter` | ZipRecruiter | US and Canada |
| `bayt` | Bayt | Location coverage depends on the board; e.g. Dubai, UAE or Saudi Arabia |
| `naukri` | Naukri | India |
| `bdjobs` | BDJobs | Bangladesh |
| `google` | Google Jobs | Recognized by the pinned library, but not usable in this pipeline: it does not expose `google_search_term`; current upstream also reports Google Jobs unavailable |

Example: `sites: [linkedin, indeed, glassdoor]`. The default remains LinkedIn and
Indeed; no additional site was enabled automatically. Supported identifiers do
not guarantee successful scraping or consistent filter support. No live board
availability was tested for this documentation change.

The list was checked against the installed 1.1.82 `Site` enum and scraper mapping.
[Upstream documentation](https://github.com/speedyapply/JobSpy/blob/main/README.md)
explains geographic coverage and current service limitations. Newer upstream
versions include `hellowork`, but this project's pinned version does not; do not
add it without upgrading and verifying compatibility.

Your old keywords were migrated to private local configuration. The public
example uses generic keywords. Search configuration is validated before any
search request; invalid or missing configuration fails with setup guidance.

## Private presentation preferences

`preferences_path` is optional (null disables it). Copy preferences.example.md to
Git-ignored config/preferences.local.md, or choose another private file. Paths are
absolute or relative to the repo root. AI reads it at the start of every workflow;
new conversations can reuse Profile organization, language and writing preferences.

## Google Sheets setup

Set `google_sheets.spreadsheet` to the full Google Sheet URL or its ID,
`worksheet` to the exact tab name and `credentials_path` to your service-account
JSON file. Credential paths are absolute (recommended outside repo/vault) or
relative to repo root; `~` is expanded. Do not put credential contents in YAML.
For legacy installations only, an empty spreadsheet plus explicit spreadsheet_name
opens by name; URL/ID avoids ambiguous titles.

Follow the [complete Google setup walkthrough](../README.md#google-sheets-setup-first-time)
for Cloud project selection, API enablement, service-account/key creation, Sheet
sharing, read-only connection checks, preview and troubleshooting. The walkthrough
is maintained in the main README only.

## Runtime state and synchronization

Search and synchronization now read local settings; Career paths and preferences
are consumed by AI workflow and evaluation fingerprinting. Sync supports updates
by job_id, preserves additional manual columns, and refuses incompatible headers
rather than overwriting them. Empty worksheets may be initialized. Processed
state changes only after remote success. Only one writer/run at a time is supported.

Private data/job_history.csv retains observed JDs for reassessment. Input and score
hashes in data/*context.json prevent stale scores from being synchronized. Follow
policies/workflow.md for prepare/evaluate/seal/preview/sync order. Historical
processed jobs with no surviving JD cannot be reconstructed automatically.
