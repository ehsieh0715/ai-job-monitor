# AI Job Monitor

Three features, one shared Candidate Profile:

- **Candidate Profile:** turn your CVs, documents and project links into maintained facts.
- **Job Search & Evaluation:** find jobs, assess fit and update your Google Sheet.
- **CV & Cover Letter:** prepare applications from verified experience, then export when needed.

The scoring, evidence and writing principles live in Markdown policies. Describe what you need in ordinary language, and the assistant follows the relevant rules, without a long prompt to paste each time. See the [policy reference](#reference) to understand or adjust them.

**Requirements:** an AI assistant with local file access and terminal execution. Python handles job search and Google Sheets sync; AI handles evaluation and writing. An ordinary text-only chat cannot run this workflow. Start from [AGENTS.md](AGENTS.md).

## Candidate Profile
Ask your AI assistant:

> Help me set up this project and create my Candidate Profile. Check the project
> instructions and tell me what configuration or permissions are missing before
> making changes or running anything.

The assistant follows
[candidate-profile-generation.md](policies/candidate-profile-generation.md).

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

Keep your filenames. For GitHub projects, paste URLs into `Projects.md`; no project
download or role form is required. AI inspects accessible README/code/tests and
asks about actual contributions. A link alone is not proof of your authorship.

Review the proposed Markdown and approve it to create/update
`Candidate Profile.md` under your Career root. Facts, per-project capabilities,
achievements, limitations and sources stay in this one file. Originals remain intact.

New experience is proposed for approval before updating the Profile. Reusable
writing feedback can be remembered in private `policies/preferences.md` when you
ask; ideas/plans never become completed achievements.

## Job Search & Evaluation

### Set up once

After your Profile is ready:

1. Install Python dependencies below.
2. Set keywords, location, sites and time range in `config/config.local.yaml`.
3. Create your Google credential, share your Sheet and fill in its name/tab below.

The [configuration reference](config/README.md) lists fields and supported job
boards. You can ask the assistant to check setup and guide you through missing steps.

<details>
<summary>Install Python dependencies</summary>

Run from the repo root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

On Windows use `.venv\Scripts\python.exe` instead of `.venv/bin/python`.

</details>

#### Google Sheets setup (first time)

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

### Try your first search

> Check my job-search and Google Sheets setup and help me complete anything
> missing. Once ready, run one search, evaluate new jobs against my latest Profile
> and sync recommendations to my configured Sheet. I authorize this one-time
> Sheet update; preserve manual columns. Do not create a recurring schedule yet.

Each run follows [career-workflow.md](policies/career-workflow.md) and
[job-fit-evaluation.md](policies/job-fit-evaluation.md): search → evaluate → validate
→ sync. Previously processed jobs are not automatically reassessed. Paste a JD
later to revisit a role using your latest Profile and rules.

Listings without a usable JD appear as **Not assessed / JD needed**, with a blank
score and their link. Paste the full JD to assess them.

### Schedule future searches

After a successful trial, ask, for example:

> Set up job searches for this project every day at 09:00 and 18:00, timezone
> Europe/Dublin. Follow the project's scheduled workflow. I authorize recurring
> updates to recommendation fields in my configured Sheet; preserve manual columns.
> Notify me about meaningful changes, failures or required input. Confirm the
> actual schedule created, or explain how to set it up if scheduling is unavailable.

Choose your own times and timezone. The scheduler needs an AI-capable runner with
access to this repo, Career files, Python, network and the Google credential.
Cloning alone creates no schedule; check the assistant's setup confirmation.

**Running locally? Keep your computer on, awake and online, with the scheduler/
runner active.** Missed runs depend on the scheduler. For unattended execution on
another machine, that runner needs its own file access and credentials.

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

Paste a JD and ask:

> Evaluate this job against my Candidate Profile.

AI uses the same [fit standard](policies/job-fit-evaluation.md) as scheduled
searches. It asks material questions at any recommendation level, proposes Profile
corrections for approval and reassesses. If confirmed gaps make applying low-value,
it explains why. Evaluation alone does not create application documents.

When ready to proceed, ask, for example:

> Create a CV and cover letter for this application and save them as Markdown.

You can also request an application email, any document individually, or an
in-chat draft without saving. Each document follows its own writing policy below.

Files go under:

```text
01 Career/
├── Candidate Profile.md
├── applications.md
└── applications/Company Name/YYYY-MM-DD - Job Title/
    ├── CV_Name_Position.md
    ├── CoverLetter_Name_Position.md       # When needed
    └── ApplicationEmail_Name_Position.md  # When requested
```

The folder date is preparation start, not submission date. Submitted files are
preserved. No email or application is sent automatically.

To export, ask:

> Convert /path/CV_Name_Position.md to PDF with purple accents, preserving the source text.

Formal filenames follow [workflow naming rules](policies/career-workflow.md#application-filenames);
Markdown and PDF share the same basename. PDF-capable tools are
required; this repo does not yet include a standalone exporter. AI must disclose
missing tools/checks rather than claim successful conversion.

## Reference

Users start here; AI reads policies as needed. You only need to edit policies to
change shared behavior, not for ordinary use.

| Policy | Purpose |
| --- | --- |
| [Policy guide](policies/README.md) | Reading entry point and policy ownership |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Repo maintenance and policy-writing conventions |
| [career-workflow.md](policies/career-workflow.md) | Workflow routing, fixed paths and interactive scope |
| [scheduled-search-workflow.md](policies/scheduled-search-workflow.md) | Schedule setup, pipeline execution and Google sync |
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
