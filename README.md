# AI Job Monitor

Three features, one shared Candidate Profile:

- **Candidate Profile:** turn your CVs, documents and project links into maintained facts.
- **Job Search & Evaluation:** find jobs, assess fit and update your Google Sheet.
- **CV & Cover Letter:** prepare applications from verified experience, then export when needed.

Open this repo in an AI assistant with local file/terminal access. It should read
[AGENTS.md](AGENTS.md) and the single career-assistant skill. A normal chat without
those tools cannot operate your local files simply from a path. No Google connector
is required: Python searches/synchronizes; AI evaluates and writes application text.

## What do I type?

| Say | What happens |
| --- | --- |
| `profile` | Read your sources, propose a Profile, save after your approval |
| `search` | Search with your settings, evaluate and sync recommendations to your Sheet |
| `search preview` | Search/evaluate and preview without changing your Sheet |
| Paste a JD, or `evaluate` + JD | Assess fit, clarify important questions, then draft for recommended jobs |
| `evaluate only` + JD | Assess without application drafts |
| `cv`, `cover letter`, `email` | Draft for the current identified application |
| `save` | Save the agreed documents and application record |
| `pdf /path/CV.md purple` | Format exact source text as PDF if export tools are available |

No policy names or long prompts are needed. The AI reads the relevant rules each
run. It must report missing setup/access rather than pretend an action succeeded.

## Candidate Profile

**First-time setup:** copy `config/config.example.yaml` to
`config/config.local.yaml`. Set `career.root` to your absolute Career folder.
Other Career paths are fixed; no Google setup is needed for this feature.

Put your existing files in:

```text
01 Career/
└── Source Documents/
    ├── ...your CVs, cover letters, Word/PDF files and career notes
    └── Projects.md       # Optional: one project/repo URL per line
```

Keep your filenames. For GitHub projects, paste URLs into Projects.md; no project
download or role form is required. AI inspects accessible README/code/tests and
asks about actual contributions. A link alone is not proof of your authorship.

Say **`profile`**. Review the proposed Markdown and approve it to create/update
`Candidate Profile.md` under your Career root. Facts, per-project capabilities,
achievements, limitations and sources stay in this one file. Originals remain intact.

New experience is proposed for approval before updating the Profile. Reusable
writing feedback can be remembered in private `policies/preferences.md` when you
ask; ideas/plans never become completed achievements.

## Job Search & Evaluation

**One-time setup:**

1. Install Python dependencies below.
2. Edit `search` in config.local.yaml: keywords, location, sites and time range.
3. Fill google_sheets.spreadsheet_name and worksheet; create credentials below.

[Configuration reference](config/README.md) lists fields and supported job boards.
Choose a unique spreadsheet title to avoid ambiguity. Your config/key are Git-ignored.

<details>
<summary>Install Python dependencies</summary>

Run from the repo root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

On Windows use `.venv\Scripts\python.exe` instead of `.venv/bin/python`.

</details>

### Google Sheets setup (first time)

<details>
<summary>Create your Google service-account credential in six steps</summary>

1. Open [Google Cloud Console](https://console.cloud.google.com/); select/create
   a project, e.g. `my-job-monitor`.
2. In **APIs & Services → Library**, enable **Google Sheets API** and **Google Drive API**.
3. In **IAM & Admin → Service Accounts → Create service account**, name it
   `job-monitor-sync`. Leave optional project-role/user grants empty and finish.
4. Open **Keys → Add key → Create new key → JSON → Create**. Rename the downloaded
   file `google-service-account.json` and put it at this repo's root beside README.md.
5. Create/open your uniquely named Sheet with a dedicated empty `Jobs` tab. Share
   it with the service account email (`client_email` in the JSON) as **Editor**.
   Public link sharing is unnecessary.
6. In config.local.yaml set, for example:

```yaml
google_sheets:
  spreadsheet_name: AI Job Monitor
  worksheet: Jobs
```

No credential path field is needed. The JSON is the program's Google login, not
a server; Python runs on your computer/runner. Never commit/paste the private key
or include it in a shared ZIP; each person needs their own key. If organization
policy prevents keys, ask your administrator.

Official help: [enable APIs](https://developers.google.com/workspace/guides/enable-apis),
[create keys](https://docs.cloud.google.com/iam/docs/keys-create-delete),
[gspread authentication](https://docs.gspread.org/en/latest/oauth2.html).

</details>

Then say **`search`**. AI reads your latest Profile and runs the steps for you.
Results update existing job IDs and preserve your manual columns. Empty/incompatible
sheet handling and validation are automatic; errors stop the run.

**No usable JD?** The listing is still shown as **未評分／待補 JD**, with a blank
score and its link. This is not 0 or Skip. Paste the full JD later and say `evaluate`.
Profile/scoring changes do not automatically rescore your entire history; manually
revisited jobs use the latest Profile/rules. Changed job requirements can trigger
reassessment. PDF colours/email wording do not affect scores.

**Recurring searches:** after one successful end-to-end trial, choose frequency/
run times and timezone in your AI scheduler (or ask AI to create the task if supported).
Select this repo as the working directory and authorize recurring Sheet updates.
Task instruction: follow `policies/career-workflow.md` in scheduled mode. The runner
needs the current local files, Python, network and JSON key; cloning alone creates
no schedule. Unchanged runs stay quiet; meaningful changes/errors/questions are reported.

<details>
<summary>Manual operation and troubleshooting</summary>

The AI normally handles these steps; no need to memorize the commands:

```sh
.venv/bin/python src/main.py
.venv/bin/python src/prepare_evaluation.py
# AI now evaluates all pending rows and writes data/scored_jobs.csv.
.venv/bin/python src/prepare_evaluation.py --seal
.venv/bin/python src/sync_scores_to_sheet.py --dry-run
.venv/bin/python src/sync_scores_to_sheet.py
```

`--seal` checks that every row has valid output and still matches current scoring
inputs. `--dry-run` reads Google and previews without writes. Calling main.py alone
only searches; it does not perform AI evaluation. Only one run/writer at a time.

Sheet not found: check title and sharing with client_email. Tab not found: check
worksheet spelling. Missing key: put google-service-account.json at repo root.
Stale evaluation: ask AI to reevaluate the current unfinished batch; do not bypass
checks. Live access must be verified in your environment, not inferred from tests.

</details>

## CV & Cover Letter

Paste a JD or say **`evaluate`** for an identifiable job. AI applies the same fit
standard as batch search. For recommended roles it asks at most three consolidated
material questions, proposes Profile corrections for approval, and reassesses.
If still recommended it supplies CV, useful cover-letter and application-email
drafts. `evaluate only` stops before drafts. Batch searches never draft documents.

Say **`save`** when ready. Files go under:

```text
01 Career/
├── Candidate Profile.md
├── applications.md
└── applications/Company Name/YYYY-MM-DD - Job Title/
    ├── CV.md
    ├── Cover Letter.md       # When needed
    └── Application Email.md  # When requested
```

The folder date is preparation start, not submission date. Submitted files are
preserved. No email or application is sent automatically.

Say **`pdf /path/CV.md [colour]`** to export without rewriting. Default filenames:
`CV_Name_Position.pdf` / `CoverLetter_Name_Position.pdf`. PDF-capable tools are
required; this repo does not yet include a standalone exporter. AI must disclose
missing tools/checks rather than claim successful conversion.

## Reference

Users start here; AI reads policies as needed. You only need to edit policies to
change shared behavior, not for ordinary use.

| Policy | Purpose |
| --- | --- |
| [career-workflow.md](policies/career-workflow.md) | Commands, stages, scheduled runs |
| [candidate-evidence-standards.md](policies/candidate-evidence-standards.md) | Facts, approval, remembered preferences |
| [candidate-profile-generation.md](policies/candidate-profile-generation.md) | Consolidate source documents |
| [project-evidence-evaluation.md](policies/project-evidence-evaluation.md) | Review project capabilities/contributions |
| [job-fit-evaluation.md](policies/job-fit-evaluation.md) | Common scoring and missing-JD handling |
| [cv-writing-and-review.md](policies/cv-writing-and-review.md) | CV writing and quality |
| [cover-letter-writing.md](policies/cover-letter-writing.md) | Cover letters |
| [application-email-writing.md](policies/application-email-writing.md) | Email drafts |
| [application-pdf-generation.md](policies/application-pdf-generation.md) | PDF layout, filenames and checks |

Keep personal files, local config, preferences, generated data and keys private.
Git-ignore does not remove historical commits: audit history before publishing.
