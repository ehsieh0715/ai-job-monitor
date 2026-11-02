# Application document export

A request such as `pdf /path/CV.md colour purple` or `convert to pdf` with an
unambiguous current source activates this policy. This is a tool-assisted export
procedure, not a claim that this repo includes a standalone PDF converter.
Require a PDF-capable runtime; if unavailable report what is missing, not a fake
output. Read the exact specified Markdown, not an older draft from memory.

## Source fidelity

Export is formatting only. Preserve all visible words, punctuation, dates and
ordering; do not silently proofread, rewrite headings, add missing business-letter
fields or remove content to fit pages. Markdown syntax is not visible text; render
links with the source's visible label and clickable target. Flag typos separately.
If the Markdown is not suitable (ambiguous tables, missing letter fields), propose
an edit before changing it; never make factual changes during conversion.

## Layout

Use A4, a clean single-column flow, ordinary selectable text, standard headings
already present in the source, round bullets/hyphens and an embedded standard
font such as Liberation Sans or Arial. No text boxes, icons, photos, graphic skill
bars or tables for layout. Keep contact details in the main text at page 1 top,
not running headers/footers. If the source places contacts elsewhere, fidelity
takes precedence: propose relocation and obtain approval rather than move text
silently or claim the preferred layout passed. Disable discretionary ligatures where the renderer
supports it and verify extracted characters rather than assuming font settings work.
Minimum margins 12 mm; normal readable type and balanced line spacing.
CV target maximum two pages, letter one page unless employer/user specifies otherwise.
Keep a job/project/education entry together when it fits on a page. If an entry
cannot fit, or length and readability conflict, stop and ask about shortening or
relaxing pagination. Never shrink to unreadable text or rewrite to meet page count.
Formal letter fields must match the source, not guessed contacts/dates.

## Colour

Use an explicitly requested colour or confirmed private preference. Without either,
use black headings and charcoal body, white background. Resolve `same as last time`
only from saved preferences or an identifiable previous artifact; otherwise ask.
Accent is limited to name, headings, dates, category labels and subtle divider rules;
body remains #222222 or #1A1A1A. Compute accent contrast against white, minimum
4.5:1 (aim 7:1); if requested colour fails, propose a darker alternative. Do not
silently substitute it or impose a universal favourite colour. Persist agreed
colour choices under evidence.md's personal-preference rule.

## Naming and destination

Default exported names are `CV_Name_Position.pdf` and
`CoverLetter_Name_Position.pdf`. Resolve Name from the confirmed candidate name,
Position from the current JD/application; ask if missing or ambiguous. Replace
whitespace runs with underscores and remove path separators/control/unsafe filename
characters. Keep readable Unicode letters. Never interpret values as filesystem
paths. An explicit safe filename overrides the default. Set PDF metadata Title to
the output basename. Export next to the source by default or an explicitly requested
destination; do not move originals. Never overwrite a submitted/existing different
version: use a separate version suffix or ask where ambiguous.

## Verification and delivery

Use available PDF creation tools, then extract visible text with two independent
methods (e.g. pdftotext and pypdf) and compare against rendered source text,
normalizing only whitespace/line breaks and Markdown presentation syntax. Preserve
punctuation/character order; fix encoding/ligature errors. Inspect rendered page
images for clipping, page breaks, margins and reading order; check count, links,
embedded fonts and metadata. Do not promise every ATS will accept a PDF.
If a required check is unavailable, disclose it and do not claim complete validation.

Deliver the actual PDF link, with a short factual note: colour/contrast if used,
page count, text-check methods, any unmet checks or source typos. Do not claim a
file was generated based only on this policy. Do not send/submit documents.
