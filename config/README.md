# Career data paths

Copy `config.example.yaml` to `config.local.yaml` and edit `career.root`.
The local file contains private settings and must not be committed.

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

Your old keywords were migrated to private local configuration. The public
example uses generic keywords. Search configuration is validated before any
search request; invalid or missing configuration fails with setup guidance.

## Integration status

AI skills read Career configuration directly; the Python search pipeline now
loads `search` from config.local.yaml independently of the working directory.
Career permissions still require separate authorization. Google Sheets and
credential settings remain in src/google_sheets.py pending their integration.
