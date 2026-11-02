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

## Integration status

AI skills read this configuration directly to locate Career data. Python scripts
still do not load it; a shared validated runtime loader is future work. Search,
Google Sheets and credential settings remain in their existing locations until
that integration is implemented. Missing configuration/data/access must be
reported rather than falling back to the removed candidate directory.
