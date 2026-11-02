# AI Job Monitor

Three core features help you move from career evidence to a prepared application:

1. **Build and update your Candidate Profile** — consolidate your documents and
   confirmed experience into one Markdown profile under your chosen Career root.
2. **Find and evaluate jobs** — assess searched jobs or any pasted job description
   against your latest Profile using shared scoring rules, and sync recommendations
   to your Google Sheet. Recurring runs require a separately configured scheduler.
3. **Prepare CVs and cover letters** — discuss fit, clarify missing evidence and
   update your Profile, then generate or revise application documents after you
   confirm you want to proceed. Save them in the fixed application structure under that root.

Personal documents live in your external Career folder (an Obsidian vault works
well). The repository supplies code, shared policies and one AI skill entry point.

For first-time use, build your Candidate Profile. After that, choose job evaluation,
search or application preparation as needed; searching is not required to use a
JD you already have.

## Candidate Profile

Clone this repo and open it in an AI coding assistant with local file access.
Create a Career folder and place your original CVs, Word/PDF files, experience
notes or old candidate JSON in `Source Documents/`:

```text
01 Career/
  Source Documents/
    ...your original files
    Projects.md             # Optional: one project/repository URL per line
```

If you have projects to review, create `Source Documents/Projects.md` and put
one project/repository link per line, for example:

```text
https://github.com/YOUR_USERNAME/PROJECT_ONE
https://github.com/YOUR_USERNAME/PROJECT_TWO
```

This is your input link list, not a generated report. Skip it if you have no
projects. The AI reviews accessible sources, asks about your contributions and
proposes project sections inside Candidate Profile.md. No separate project report
folder is needed; [project-evidence.md](policies/project-evidence.md) defines the
review rules.

Copy `config/config.example.yaml` to `config/config.local.yaml`. For Profile
initialization, set only `career.root`; all other Career paths are fixed by the
project. `Source Documents/` is the required input entry. Grant read access to the sources and
write access to the intended Profile. Setting a path does not grant permission.

Ask in ordinary language, for example:

> Use career-assistant. My Career root is `/absolute/path/to/01 Career`.
> Read Source Documents and build/update Candidate Profile.md there, following
> policies/profile-building.md. Preserve my original files and existing confirmed
> facts; flag conflicts and ask about important missing evidence. Show the proposed
> Markdown and wait for my approval before writing Candidate Profile.md, including
> its project sections.

You can give the Career root in conversation and ask the AI assistant to configure
it for you. The assistant reviews your sources, asks about important uncertainties,
and shows the proposed Profile for approval before saving. Original files stay intact.

Optional personal language/style preferences go in local `policies/preferences.md`
(Git-ignored), e.g. “Analysis: Traditional Chinese; CV: English.” No config field
is needed. The AI reads it when present; explicit instructions for the current
task take precedence. A fresh clone does not contain your personal preferences.

## Job Search & Evaluation

### Evaluate a job in conversation

Paste any complete JD and say “評估這份工作”. It need not appear in a Sheet or CSV.
The assistant reads the Profile and relevant evidence, gives a common score and
recommendation, and asks about experience that could materially change the result.
Any Profile/evidence edit is shown for approval before writing, even after you
answer those questions.
Unknowns receive no assumed credit; a changed judgment includes its reason.
If the Profile is incomplete, the assessment is provisional rather than invented.

### Configure search and Google Sheets

Use `config/config.local.yaml` for your own settings (copy the example if needed):

| Setting | What to provide |
| --- | --- |
| `career.root` | Your Career folder; all internal paths are fixed |
| `search` | Keywords, location, sites, listing age and desired result count |
| `google_sheets.spreadsheet` | Your Google Sheet URL or ID |
| `google_sheets.worksheet` | Exact destination tab name |

See [configuration](config/README.md) for supported site values. Complete the
[one-time Google setup](#google-sheets-setup-first-time) below before syncing.
Keep personal settings private. The destination is configured only in this YAML;
do not repeat it in prompts or schedules.

### Ask AI to run it now

In an AI environment with local file/command and network access, ask:

> Follow career-assistant and policies/workflow.md. Use my local configuration
> and latest Candidate Profile to search jobs, evaluate every pending job, seal
> the results, preview changes and synchronize recommendations to my configured
> Google Sheet. Preserve manual columns and stop if required access is unavailable.

The intended flow is **Python search → pending CSV → AI evaluation → Python
validation → AI connector writes → verified local completion**. Python main.py
alone does not evaluate jobs or use the connector.

**Migration status:** this change documents the connector workflow; the current
Python synchronization command still uses a service account. Connector plan,
readback verification and local-completion integration remain to be implemented.
Do not treat connecting Drive as completing that migration. The first run
may require filesystem/network authorization; permissions are separate from paths.

### Schedule recurring runs

First complete a successful interactive run. Then choose either:

- **Ask the AI to create a schedule:** in an environment with scheduling tools,
  specify the repo path, frequency, timezone and permission to update the target
  Sheet. For example: “Create a recurring task every 6 hours, Europe/Dublin, for
  this repo. Use examples/scheduled-run.md and my private configuration.” The AI
  should report the created schedule; without a scheduling tool it must explain
  the limitation rather than claim it was created.
- **Create it yourself:** open your environment's Scheduled tasks/Automations
  interface, add a task, select the interval/timezone and use the
  [scheduled-run prompt](examples/scheduled-run.md), replacing its repo path.

A scheduled AI runner needs the same repo, private config, latest Profile,
Python dependencies, connected Google Drive tools, file permissions and network access as
an interactive run. A cloud task does not automatically have your local vault.
Do not overlap runs. Cron calling main.py only searches; it does not add AI scoring.
Cloning the repo does not itself install or activate a schedule. Tool availability
and account permissions depend on the execution environment. Connector-based
schedules must wait until the synchronization integration described below is implemented.

### Run the pipeline manually

<details>
<summary>Expand: Python commands and the AI evaluation handoff</summary>

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
it creates data/scored_jobs.csv, seal the current batch:

```sh
.venv/bin/python src/prepare_evaluation.py --seal
```

This checks queue coverage and binds the scores to the current inputs. It does not
write to Google Sheets or prove that the AI applied the scoring rules correctly.
The remaining connector handoff is specified in [workflow.md](policies/workflow.md).
Its programmatic planning, readback and completion integration is pending; no new
connector CLI command is available yet.

The existing `sync_scores_to_sheet.py` command (including `--dry-run`) still
requires service-account credentials. It is the legacy implementation, not the
keyless connector path. Do not run it expecting it to use the connected account.
Do not manually mark jobs processed just because a connector write was attempted.

Changes to Profile/project evidence/policies queue retained jobs for
reevaluation. Old jobs without retained descriptions cannot be recovered
automatically. Run only one writer at a time. Empty queues stop without uploading
old scores. Offline tests do not establish successful live Google access.

</details>

### Google Sheets setup (first time)

The connector workflow uses your connected Google account. It does not require
creating a Google Cloud project, service account or downloaded JSON key.
**The setup below configures the intended workflow; the synchronization integration
is still pending, as described above.**

1. Enable/connect the **Google Drive** connector in the AI environment used for
   this project. It must expose Google Sheets read and write tools, not only search.
2. Connect the Google account that has **Editor** access to the destination Sheet.
   Public link sharing is not required. Organization policies and protected ranges
   may still limit writes.
3. Create/open the destination Sheet and a dedicated tab, such as `Jobs`. Avoid
   using your application tracker tab for search recommendations.
4. Set the destination once in private `config/config.local.yaml`:

```yaml
google_sheets:
  spreadsheet: "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit"
  worksheet: "Jobs"
```

`spreadsheet` accepts the full URL or its ID. `worksheet` is the exact bottom-tab
name, including spaces and capitalization; a URL's `gid` does not override it.
Prompts and schedules refer to this configuration rather than carrying a second
copy of the destination. Keep the local configuration out of Git.

Before synchronization, the AI must read the configured spreadsheet metadata and
confirm the exact tab through the connector. A read proves read access only;
actual writes and readback are required to verify successful synchronization.

The planned handoff validates the sealed batch, previews changes, writes only
owned recommendation fields, reads back the affected data, and updates local
processed/pending state only after verification. It preserves manual columns,
rejects duplicate IDs and incompatible headers, and reconciles partial writes on
retry. See [the workflow contract](policies/workflow.md#connector-synchronization-contract-migration-target).

| Symptom | Check |
| --- | --- |
| Connector or Sheets write tools unavailable | Connect Google Drive in the actual interactive/scheduled execution environment; stop synchronization if tools remain unavailable. |
| File unavailable / permission denied | Check the configured URL/ID, connected account, Editor access, protected ranges and organization restrictions. |
| Destination tab missing | Create the tab and match its exact name in config. |
| Incompatible header or duplicate IDs | Resolve the conflict before writing; never overwrite unrelated data to bypass validation. |
| Missing/stale seal or changed queue | Prepare, reevaluate and seal current jobs. |
| Legacy command asks for a JSON key | It still uses the old Python transport; connector migration is not yet implemented. |

Existing service-account keys are not deleted by this documentation change.
Recurring execution also needs an available AI runner with local files and
connector tools; see [the scheduled-run requirements](examples/scheduled-run.md).

## CV & Cover Letter

Say “Proceed with a CV for this role”. The assistant composes relevant verified
Profile/project evidence under the writing rules; no single base CV is required.
A cover letter is optional. The project creates the following fixed structure as
needed within authorized scope. Users configure only the root, not these individual paths:

```text
01 Career/
  Candidate Profile.md
  Source Documents/
    Projects.md              # Optional project links; originals stay here
  applications.md            # Root-level application tracker
  applications/
    Company Name/
      YYYY-MM-DD - Job Title/
        CV.md
        CV.pdf               # When exported
        Cover Letter.md      # When useful/requested
```

Folder date is preparation start; actual submission date is in root applications.md.
Reviewed project evidence is embedded in Candidate Profile.md. The AI creates
application subfolders and the tracker when the authorized work needs them.
Use lowercase applications/ and applications.md exactly. Legacy custom paths and
old Applications/ or Project Evidence/ files are not migrated automatically; see
[configuration and migration](config/README.md#fixed-career-layout).
Preserve submitted versions. No separate JD, analysis or progress notes are created
by default. Existing full notes need not be split or moved into this layout.

## Where to change behavior

[career-assistant](.agents/skills/career-assistant/SKILL.md) is the sole skill
entry point; it selects the references below without duplicating their rules.

| Policy | Purpose |
| --- | --- |
| [Workflow](policies/workflow.md) | Interactive stages and scheduled search/evaluate/sync |
| [Profile building](policies/profile-building.md) | Initialize/merge documents into root Candidate Profile.md |
| [Project evidence](policies/project-evidence.md) | Link-only repo input, source review and per-project approved updates |
| [Evidence](policies/evidence-policy.md) | Sources, claim boundaries, questions and updates |
| [Job evaluation](policies/job-evaluation.md) | Same scoring standard for manual JDs and batches |
| [Resume writing](policies/resume-writing.md) | Select and compose relevant factual content |
| [Resume review](policies/resume-review.md) | Check evidence, relevance and quality |
| [Cover letter](policies/cover-letter-writing.md) | Value, narrative and writing standards |

Local `policies/preferences.md` can set language, tone, length and order; it cannot
relax shared evidence or scoring standards. Personal preferences are not published.
The earlier ai-job-monitor and career-application rules are consolidated here.

## Privacy and sharing

Keep config.local.yaml, profiles, raw documents, applications, cache and credentials
private. This repo's Git history still needs a personal-data/secret audit; moving
files out does not remove historical copies. Do not publish or rewrite history
until the audit and handling plan have been reviewed.
