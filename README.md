# AI Job Monitor

Three core features help you move from career evidence to a prepared application:

1. **Build and update your Candidate Profile** — consolidate your documents and
   confirmed experience into one Markdown profile at your chosen location.
2. **Find and evaluate jobs** — assess searched jobs or any pasted job description
   against your latest Profile using shared scoring rules, and sync recommendations
   to your Google Sheet. Recurring runs require a separately configured scheduler.
3. **Prepare CVs and cover letters** — discuss fit, clarify missing evidence and
   update your Profile, then generate or revise application documents after you
   confirm you want to proceed. Save them in your chosen application folder.

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
    Projects.md             # Optional: one GitHub repo URL per line
```

For GitHub projects, add plain repo links to `Source Documents/Projects.md`:

```text
https://github.com/YOUR_USERNAME/PROJECT_ONE
https://github.com/YOUR_USERNAME/PROJECT_TWO
```

Copy the [link-only example](examples/Projects.md) if useful. No project download,
role form or skill checklist is needed. The AI follows
[project-evidence.md](policies/project-evidence.md): read README and relevant code,
tests/config/docs, ask about unknown personal contributions, and propose a separate
Profile subsection for each project. Private repos require authorized access.
For later updates it compares inspected commits and proposes edits to that same
project section rather than adding duplicates. README-only access is labelled.

Copy `config/config.example.yaml` to `config/config.local.yaml`. For Profile
initialization, only change `career.root`; keep the other Career paths at their
defaults unless your files are elsewhere. Grant read access to the sources and
write access to the intended Profile. Setting a path does not grant permission.

Ask in ordinary language, for example:

> Use career-assistant. My Career root is `/absolute/path/to/01 Career`.
> Read Source Documents and build/update Candidate Profile.md there, following
> policies/profile-building.md. Preserve my original files and existing confirmed
> facts; flag conflicts and ask about important missing evidence. Show the proposed
> Markdown and wait for my approval before writing Profile or Project Evidence.

You may also supply the root in conversation and ask the assistant to create the
private configuration using the example. A Profile request starts inspection and
a proposal; only explicit approval of the displayed content authorizes saving
Profile/Project Evidence Markdown. Answering factual questions alone is not approval.
Configuration changes need their own requested/authorized scope; no searching or
uploading is implied.
No Master CV or existing Profile is required. Initialization needs an AI assistant
and document-reading capabilities; running Python alone does not generate it.

The assistant reads available materials, consolidates evidence, presents the
proposed Markdown Profile and saves it after your approval. Unknown claims stay marked; it does not turn every CV assertion
or README feature into verified experience. Subsequent experience is proposed and approved before updating
this same Profile rather than another JSON database. Original sources stay intact.

The old project's exact Profile-generation prompt was not found in the reviewed
project documents or Git history; profile-building.md defines the new repeatable
workflow. It carries forward the old JSON's summary, roles, experience, skills,
projects, education, constraints, tailoring boundaries and conflict information.

For lasting generation/style preferences, set `preferences_path` to a private
Markdown file; see [example](config/preferences.example.md). The assistant reads
it each time. Shared evidence requirements still apply.

## 2. Evaluate a job in the same conversation

Paste any complete JD and say “評估這份工作”. It need not appear in a Sheet or CSV.
The assistant reads the Profile and relevant evidence, gives a common score and
recommendation, and asks about experience that could materially change the result.
Any Profile/evidence edit is shown for approval before writing, even after you
answer those questions.
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

Search retains local JD history and queues new jobs. Run:

```sh
.venv/bin/python src/prepare_evaluation.py
```

Ask career-assistant to evaluate every pending row under the shared policy. After
it creates data/scored_jobs.csv, seal and preview:

```sh
.venv/bin/python src/prepare_evaluation.py --seal
.venv/bin/python src/sync_scores_to_sheet.py --dry-run
```

Configure your Sheet URL/ID, tab and service-account JSON path in config.local.yaml.
[Google setup instructions](#google-sheets-setup-first-time) cover enabling
APIs, creating credentials and sharing the Sheet. When ready/authorized, run:

```sh
.venv/bin/python src/sync_scores_to_sheet.py
```

Sync updates existing IDs and appends new ones, preserving custom columns. An
incompatible Sheet stops rather than having its header overwritten. Changes to
Profile/evidence/preferences/policies queue retained jobs for reevaluation; stale
or altered sealed scores cannot sync. Old jobs without retained descriptions
cannot be recovered automatically. Run only one writer at a time.

For recurring runs use the [scheduled AI prompt](examples/scheduled-run.md), with
your chosen scheduler, repo path, interval and timezone. It follows
[workflow.md](policies/workflow.md). Cloning does not install a scheduler or LLM
service. The runner needs access to the machine/files, Python, network and Google
credentials; calling main.py alone performs no AI evaluation. Empty queues stop
without uploading old scores. Actual board/Google access must be verified in your
own environment; offline tests do not establish successful live authentication.

## Google Sheets setup (first time)

This project's Python connector uses a **service account**, not an API-key string
or an OAuth desktop-client JSON. The code runs on your computer/chosen runner;
Google Cloud supplies the identity and API access, not a server for this pipeline.
Each user should create their own credentials and use their own Sheet.

### A. Select a Google Cloud project and enable APIs

1. Sign in to [Google Cloud Console](https://console.cloud.google.com/).
2. Open the project selector at the top. Select an existing project or choose
   **New project**, enter a name such as `job-monitor`, and create/select it.
3. Open **APIs & Services → Library**. Search for **Google Sheets API**, open it,
   and click **Enable**. If already enabled, leave it enabled.
4. Return to Library and enable **Google Drive API** in the same project.
5. Check **APIs & Services → Enabled APIs & services** for both entries.

Keep that project selected throughout setup. If controls are unavailable, ask the
project administrator for permission to enable services. See Google's
[API enablement guide](https://developers.google.com/workspace/guides/enable-apis).

### B. Create the service account

1. Open **IAM & Admin → Service Accounts** and click **Create service account**.
2. Enter a name such as `job-monitor-sync`, then **Create and continue**.
3. For this shared-Sheet workflow, leave optional project-role and user-access
   grants empty and finish. Do not grant project Owner/Editor just to edit a Sheet:
   file access is granted in step D.
4. Open the account and note its email, shaped like
   `job-monitor-sync@YOUR_PROJECT_ID.iam.gserviceaccount.com`.

You do not need an OAuth consent-screen setup or domain-wide delegation for this
explicitly shared-Sheet workflow. See Google's
[credential guide](https://developers.google.com/workspace/guides/create-credentials).

### C. Download and store a JSON key

1. In that service account, open **Keys → Add key → Create new key**.
2. Select **JSON**, click **Create**, and save the downloaded file.
3. Store it outside the repo and vault, for example:
   `/Users/YOUR_NAME/.config/ai-job-monitor/google-service-account.json` on macOS,
   or a private directory on your own OS. Use your actual path in step E.
4. Confirm locally that the JSON contains `"type": "service_account"` and a
   `client_email`. Do not paste the file or its private key into chat or Git.

If key creation is blocked by organization policy, ask your administrator about an
approved authentication method; the current connector expects a JSON key and
cannot bypass that policy. If you lose the downloaded key, create a replacement
and revoke the old one rather than expecting to download it again. See Google's
[key management guide](https://docs.cloud.google.com/iam/docs/keys-create-delete).

### D. Create and share your spreadsheet

1. Create/open your own Google Sheet. Add a dedicated, empty tab named `Jobs`
   (or choose another exact tab name).
2. Click **Share** and add the service account email from step B (also available
   as `client_email` in the JSON). Set its file permission to **Editor**.
3. Keep general link access restricted; public sharing is not required.
4. Copy the spreadsheet URL from the address bar, not merely its display name.

The service identity is separate from your personal Google login, so you must
share the file with it even when you own the Sheet. See
[gspread service-account authentication](https://docs.gspread.org/en/latest/oauth2.html).

### E. Fill your private configuration

If not already done, copy config/config.example.yaml to config/config.local.yaml.
Add/edit this section without deleting your Career and search settings:

```yaml
google_sheets:
  spreadsheet: "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit"
  worksheet: "Jobs"
  credentials_path: "/absolute/private/path/google-service-account.json"
```

The spreadsheet ID is the segment between `/d/` and `/edit`; either the full URL
or just that ID works. `worksheet` is the bottom tab name, not the document title;
the URL's `gid` does not select a tab for this connector. Credentials must exist
on the machine running the task. Do not commit config.local.yaml or the key.

### F. Check the connection without changing the Sheet

After installing dependencies, run this from the repository root (macOS/Linux):

```sh
.venv/bin/python -c 'import sys; sys.path.insert(0, "src"); from google_sheets import get_worksheet; get_worksheet().row_values(1); print("Google Sheet read access OK")'
```

On Windows, use `.venv\Scripts\python.exe` instead of `.venv/bin/python`.
This authenticates and reads the configured tab; it needs network access but no
Profile or scored CSV. It does not write cells or prove write permission.

### G. Preview and perform the first synchronization

Complete the search → prepare → AI evaluation → seal steps in section 3 first.
Then run:

```sh
.venv/bin/python src/sync_scores_to_sheet.py --dry-run
```

This reads the Sheet and validates the sealed evaluation; it writes neither
cells nor local processed state. Check the target and reported changes. To apply:

```sh
.venv/bin/python src/sync_scores_to_sheet.py
```

An empty tab receives the required header on this first write. Existing compatible
tabs are matched by column names; extra manual columns are preserved. Incompatible
headers stop the sync. Do not use your application tracker tab as the search tab.

### Troubleshooting

| Symptom | Check |
| --- | --- |
| Credential file not found | Use the real JSON path on this runner; expand/move it locally, not into the repo. |
| SpreadsheetNotFound / 404 | Confirm URL/ID and share that exact file with the JSON's client_email. |
| WorksheetNotFound | Create the tab; match spelling, spaces and capitalization in worksheet. |
| API disabled / SERVICE_DISABLED | Enable the named API in the project that owns the credential. |
| Permission denied / 403 | Check Editor file access, protected ranges and organization sharing restrictions. |
| Invalid grant / invalid JWT | Check key/account revocation and machine clock; replace credentials if necessary. |
| Incompatible Sheet header | Use a dedicated empty tab or the required columns from src/schema.py. |
| Missing/stale seal or changed queue | Prepare, reevaluate and seal current jobs; do not reuse an old scored CSV. |
| Key creation unavailable | Ask your organization administrator; do not disable policy as a workaround. |

Cloud Console labels can change; use the linked Google guides if the screens differ.
This setup enables Google access only. Recurring execution still needs the
[scheduler and available AI runner](examples/scheduled-run.md).

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
| [Workflow](policies/workflow.md) | Interactive stages and scheduled search/evaluate/sync |
| [Profile building](policies/profile-building.md) | Initialize/merge documents into the configured Profile |
| [Project evidence](policies/project-evidence.md) | Link-only repo input, source review and per-project approved updates |
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
