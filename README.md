# AI Job Monitor

Use this project for three things:

1. **Build a Candidate Profile** from your CVs, experience notes and project links.
2. **Find and evaluate jobs** against that Profile using shared scoring rules, with
   a Google Sheet as the recommendation destination and an AI scheduler for repeat runs.
3. **Prepare tailored CVs and cover letters** by selecting verified experience
   from the Profile for a new or previously reviewed job.

Start with setup and your Profile, test one search/evaluation cycle, then schedule
repeat runs or bring a specific job to discuss.

Python handles searching and Google Sheet synchronization; the AI handles Profile
building, evaluation and application writing. No Google connector is required.

## 1. Set up and build your Profile

### Copy the configuration

Clone this repository and open it in an AI coding assistant with access to local
files and terminal commands. From the repository folder, run:

```sh
cp config/config.example.yaml config/config.local.yaml
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

On Windows, copy the file using your file manager and use
`.venv\Scripts\python.exe` in place of `.venv/bin/python`.

Edit `config/config.local.yaml`. Keep its search fields and change them to match
your target roles and location. Set your Career folder and Sheet destination:

```yaml
career:
  root: /absolute/path/to/01 Career

# Keep and edit the search section from the example.

google_sheets:
  spreadsheet_name: AI Job Monitor
  worksheet: Jobs
```

This snippet shows only the folder and Sheet settings; the copied file contains
all required search fields. See [field definitions](config/README.md#fields).
Career setup needs only `root`; other Career filenames are fixed by the project.
Use the exact spreadsheet title and tab name; avoid duplicate spreadsheet titles
in the service account's shared files. No Sheet link is needed. Keep config private.

### Google Sheets setup (first time)

Python needs a Google identity to write your private Sheet. Each user creates
one service account and downloads its JSON key once. This does not rent a server;
Python runs on your own computer or runner.

<details>
<summary>Expand: create your Google credential in six steps</summary>

1. Open [Google Cloud Console](https://console.cloud.google.com/). Select or create
   a project, for example `my-job-monitor`.
2. In **APIs & Services → Library**, enable **Google Sheets API** and
   **Google Drive API** in that project.
3. Open **IAM & Admin → Service Accounts → Create service account**. Name it
   `job-monitor-sync`. Leave optional project roles/user-access grants empty and
   finish; it does not need project Owner or Editor to edit a shared Sheet.
4. Open the account's **Keys → Add key → Create new key → JSON → Create**.
   Google downloads the credential. Rename it to `google-service-account.json`
   and save it at this repository's root, beside README.md. It is Git-ignored.
   Never paste its private key
   into chat or commit the JSON. If organization policy blocks keys, ask your admin.
5. Create/open a uniquely named Google Sheet, e.g. **AI Job Monitor**, with an
   empty **Jobs** tab. **Share** the Sheet with the service account email shown on
   its page (also `client_email` in the JSON), granting **Editor**. Public link
   sharing is unnecessary.
6. Fill `google_sheets.spreadsheet_name` and `worksheet` in
   config/config.local.yaml as shown above. No credential-path setting is needed.
   Do not include the JSON if you manually zip/share this folder; each user needs
   their own key. Git-ignore does not remove previously tracked credentials.

Google's [API guide](https://developers.google.com/workspace/guides/enable-apis),
[key guide](https://docs.cloud.google.com/iam/docs/keys-create-delete) and
[gspread authentication guide](https://docs.gspread.org/en/latest/oauth2.html)
provide more detail if the console labels differ.

</details>

After installing dependencies, check read access from the repo root:

```sh
.venv/bin/python -c 'import sys; sys.path.insert(0, "src"); from google_sheets import get_worksheet; get_worksheet().row_values(1); print("Sheet read access OK")'
```

This only reads; it needs network access and does not prove write permission.
If the Sheet cannot be found, check its exact name and sharing with client_email;
if the tab cannot be found, check its tab name. Use your own credentials.

### Add your source documents

Create the folder you set as `career.root`, with a `Source Documents` folder inside:

```text
01 Career/
└── Source Documents/
    ├── ...your existing CVs, cover letters and career documents
    └── Projects.md            # Optional project links
```

Put any existing CV versions, cover letters, work/education records, achievement
notes and other career materials here. Keep your own filenames; no specific CV
or notes file is required. Markdown, Word and PDF documents can be used when the
assistant has the tools to read them.

The AI consolidates these sources into one proposed `Candidate Profile.md`, asks
about important uncertainties, and saves it after your approval. This is the input
folder it reads; it does not scan your entire vault or computer.

If you have projects, create `Source Documents/Projects.md` with one project or
repository link per line:

```text
https://github.com/YOUR_USERNAME/PROJECT_ONE
https://github.com/YOUR_USERNAME/PROJECT_TWO
```

Skip that file if you have no projects. The AI reviews accessible sources and
asks about your actual contribution; a link alone does not establish authorship
or grant access to a private repository.

### Ask the AI to build your Profile

Say `profile`. The AI reads your configured Source Documents and project links,
asks material questions and proposes Candidate Profile.md for approval.

Review the proposal and answer the important questions. Once you approve the
content, the AI saves **`Candidate Profile.md`** directly under your Career root.
This is the Profile used for later job evaluations and application documents.

Expect a Markdown document with sections such as:

```markdown
# Candidate Profile
## Summary & Target Roles
## Work Experience
## Projects
### Project Name
## Skills & Evidence
## Education & Certifications
## Constraints & Preferences
## Claim Boundaries
## Open Questions & Conflicts
## Source Review
```

Empty sections can be omitted. Experience and projects include verified actions,
results, sources and limitations. Unresolved claims stay marked as questions.
Project evidence is embedded in this Profile, without a separate summary folder.

As you use the project, the full Career structure will look like this:

```text
01 Career/
├── Source Documents/                         # Your inputs
│   ├── ...your CVs, cover letters and other career materials
│   └── Projects.md                           # Optional project links
├── Candidate Profile.md                      # Approved facts and project evidence
├── applications.md                           # Application tracking table
└── applications/
    └── Company Name/
        └── YYYY-MM-DD - Job Title/
            ├── CV.md
            ├── CV.pdf                        # When exported
            └── Cover Letter.md               # When requested
```

The AI creates output files and application folders as the authorized work needs
them. Folder dates are preparation dates; actual submission dates belong in
`applications.md`. Existing or submitted documents are preserved.

Optional language/style choices go in Git-ignored `policies/preferences.md`, e.g.
“Analysis: Traditional Chinese; CV: English.” No config field is needed. Without
this file, the AI follows the current request and document audience.

## 2. Test one run, then set up recurring searches

### Choose what to search

In the existing `search` section of `config/config.local.yaml`, set your keywords,
location, job boards, listing age and requested result count. For example, change
`keywords` to `[data analyst, analytics engineer]` and `location` to your target
city. [Configuration](config/README.md) explains every field and supported board.

### Run once in the current chat

After your Profile has been approved and saved, paste:

> Follow career-assistant and `policies/workflow.md`. Use my local configuration
> and latest Candidate Profile to run one job search, prepare the pending queue,
> evaluate every pending job under `policies/evaluation.md`, and seal the scores.
> Show a concise summary of recommendations and unresolved evidence questions.
> Preview with `src/sync_scores_to_sheet.py --dry-run`, then synchronize my
> configured Sheet with Python. Preserve manual columns and stop on errors.

The sequence is **Python search → AI evaluation → Python validation and sync**.
After AI creates the scored CSV, the commands are:

```sh
.venv/bin/python src/prepare_evaluation.py --seal
.venv/bin/python src/sync_scores_to_sheet.py --dry-run
.venv/bin/python src/sync_scores_to_sheet.py
```

The AI follows policies/workflow.md, including preparing the queue before scoring.
Empty queues need no upload. Test a complete run before scheduling, and run one
writer at a time. Python main.py alone searches but does not perform AI evaluation.

### Schedule recurring searches

After a successful end-to-end trial, choose your frequency/run times and timezone
in your AI environment's scheduling interface. Set this repository as the working
directory and use this short task instruction:

> Follow `.agents/skills/career-assistant/SKILL.md` and the scheduled-run procedure
> in `policies/workflow.md`. Search, evaluate and sync to my configured Sheet.

You may ask the AI to create the task if scheduling tools are available. Authorize
recurring Sheet updates when setting it up; the execution rules stay in the policy.
The scheduled environment needs Python, current Career files, network access and
its own access to the private JSON key. A connected Google app is not required.

## 3. Evaluate a job and prepare application documents

Paste a JD, or type `evaluate` with a JD or identifiable retained job. The AI uses
your latest Profile and shared scoring rules automatically; no policy names needed.

For recommended jobs, it asks only material questions (at most three consolidated
questions per round), proposes Profile corrections for your approval and reassesses.
If still recommended, it directly provides CV, useful cover-letter and application-
email drafts. Say `evaluate only` if you want assessment without drafting. Batch/
scheduled runs never generate application documents. Ask to save the package when
ready; nothing is submitted or emailed automatically.

Short commands:

- `evaluate` + JD: assess and follow the recommended-job flow.
- `cv`, `cover letter`, `email`: draft for the current identified application.
- `save`: save the agreed package within the fixed application structure.
- `pdf /path/CV.md purple`: format the exact Markdown as PDF, without rewriting.

PDF defaults: `CV_Name_Position.pdf` / `CoverLetter_Name_Position.pdf`, single
column, A4, restrained readable colour, text and visual checks. Conversion requires
available PDF tools; no standalone PDF exporter is included in this repo yet.

To remember reusable corrections, ask once: “Remember my future writing feedback.”
The AI merges confirmed preferences into private policies/preferences.md. Facts
still require approval before Profile updates; ideas are not recorded as achievements.

## Reference

[Configuration](config/README.md) explains user settings. Policies use short names:

| Policy | Purpose |
| --- | --- |
| [workflow.md](policies/workflow.md) | Short commands, stages and scheduled runs |
| [evidence.md](policies/evidence.md) | Facts, approval and remembered preferences |
| [profile.md](policies/profile.md) | Build/update Candidate Profile |
| [projects.md](policies/projects.md) | Review project links and contributions |
| [evaluation.md](policies/evaluation.md) | Common job-fit scoring |
| [cv.md](policies/cv.md) | CV writing and review |
| [cover-letter.md](policies/cover-letter.md) | Cover letter writing |
| [email.md](policies/email.md) | Application email drafts |
| [pdf.md](policies/pdf.md) | PDF formatting, naming and checks |

Keep local config, personal preferences, source documents, Profile, application
files and pipeline data private. Removing a tracked file does not remove older
copies from Git history; review history before sharing or publishing this repo.
