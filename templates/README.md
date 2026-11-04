# CV template and Obsidian stylesheet

This is an optional, reusable presentation preset. It contains no candidate data.
Writing and evidence standards remain in `../policies/`; personal choices belong
in the ignored `../policies/preferences.md`.

## Files and responsibilities

| File | Responsibility |
| --- | --- |
| `CV.md` | Editable Markdown structure with placeholders and semantic CSS classes |
| `resume.css` | Obsidian Reading view and print styling for that structure |
| `../policies/cv-writing-and-review.md` | Evidence-based writing, revision scope and ATS limitations |
| `../policies/application-pdf-generation.md` | PDF fidelity, export and verification |
| `../policies/preferences.md` (private, optional) | Selected template and personal presentation overrides |

Employer requirements and explicit instructions take precedence, followed by
private preferences and then these defaults. Neither a format nor a theme
guarantees ATS acceptance. Do not put names, contact details, GPA values or
candidate-specific employment exceptions in these public files.

## Included defaults

- Target-role headline below the name; contacts in selectable body text.
- `SUMMARY`, `PROFESSIONAL EXPERIENCE`, `TECHNICAL SKILLS`, `SELECTED PROJECTS`
  and `EDUCATION` headings. Omit irrelevant sections or adapt names to the content.
- Bold job title and right-aligned dates, then company and location in normal weight.
- Direct-action bullets; skill-category labels remain available in Technical Skills.
- Inline `[GitHub](URL)` beside the project name. Role/context and a short italic
  technology list share a paragraph. Project dates are optional, not prefilled.
- Institution first, dates right, then degree, classification and optional GPA.
  Use the supported original GPA scale; remove absent fields and separators.
- Times New Roman with fallback fonts, black text, dark blue underlined links,
  and A4 print margins. These are configurable theme defaults, not writing rules.

The Markdown uses `<p>` and `<span>` only where needed for alignment and metadata.
Maintain normal source-text order; do not align with repeated spaces or tables.
The CSS allows wrapping. `.resume-new-page` is available for a deliberate manual
page break, but the template does not force every CV's skills section onto page two.

## Install in Obsidian

1. In the intended vault, open **Settings → Appearance → CSS snippets → Open
   snippets folder**. Do not assume a machine-specific vault location.
2. Copy `resume.css` into that folder, normally `<vault>/.obsidian/snippets/`.
   Inspect or back up any existing file before replacing it.
3. Enable the `resume` snippet in Appearance settings.
4. Use `CV.md` as a starting structure in the appropriate application folder.
   Replace placeholders with supported facts and preserve `cssclasses: [resume]`.
5. Preview in Reading view, then export using Obsidian's PDF export. Check the
   actual PDF for page count, wrapping, links and text order.

The CSS is scoped to `resume` notes, except for the `@page` paper/margin rule:
Obsidian may apply that rule to other PDF exports while the snippet is enabled.
Disable the snippet when exporting unrelated notes if those settings are unwanted.
Reading view is not an exact A4 pagination preview. Content changes can change
page count; never assume two pages without checking the exported file.

## Updating the style

The repo stylesheet and the installed snippet are separate copies. Changes here
do not automatically update a vault, and vault edits do not update the repo.
When synchronization is requested, compare both copies, preserve unrelated local
customizations, and copy only the approved changes. Editing CSS does not authorize
rewriting CV content or changing the user's Obsidian theme/settings.
