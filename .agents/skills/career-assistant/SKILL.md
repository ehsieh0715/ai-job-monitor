---
name: career-assistant
description: Use when initializing or updating a Candidate Profile from source documents or project repository links, evaluating jobs, discussing fit or experience, preparing or reviewing a CV or cover letter, exporting application Markdown to PDF, or assessing a pending batch of jobs with this repository.
---

# Career assistant

Resolve all references below from the repository root. Read `config/README.md`
for local configuration, start with `policies/workflow.md`, and always apply
`policies/evidence.md`.
Career configuration requires only `career.root`; resolve every generated path
from the fixed layout in `policies/workflow.md`. For Profile building, read original inputs only through
`Source Documents/` and its optional `Projects.md` links. Explicit user-designated
review/export files are allowed under evidence.md; do not scan around them. Keep reviewed project
evidence in `Candidate Profile.md`. The tracker is root `applications.md`, and
documents belong under lowercase `applications/`. Never ask users to configure
individual Career paths or silently migrate legacy files.

Read only the additional policies relevant to the request:

| Request | Policies |
| --- | --- |
| Initialize/merge source documents into Candidate Profile | `policies/profile.md` |
| Review Projects.md links or refresh a project section | `policies/projects.md` |
| Pasted JD / evaluate / job fit / pending batch | `policies/evaluation.md` |
| Prepare or revise CV | `policies/evaluation.md`, `policies/cv.md` |
| Review an existing CV | `policies/cv.md`; add `policies/evaluation.md` when assessing fit |
| Email draft | `policies/email.md` |
| PDF / convert Markdown / colour | `policies/pdf.md` |
| Cover letter or whether one helps | `policies/evaluation.md`, `policies/cover-letter.md` |

Policies own all standards, workflow steps and output contracts. Follow them
rather than maintaining copies here.
