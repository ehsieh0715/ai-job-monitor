# Application PDF Generation

## Preserve text

- Read the exact specified source and require a PDF-capable runtime; do not assume the repo includes an exporter.

- Export changes presentation only. Preserve visible words, punctuation, dates and order; do not proofread, add fields or delete content to fit pages.
- Render Markdown links with their visible labels and clickable targets. Flag typos separately.
- If source structure or fields are unsuitable, propose an edit first. Preserve current approved text until authorized otherwise.

## Layout

- A4, single-column selectable text, existing standard headings, ordinary bullets and embedded standard font (for example Liberation Sans or Arial).
- **Containers:** no layout tables, text boxes, icons, photos or graphic skill bars.
- **Contacts:** keep them in page-one body, not running headers or footers. If relocation is needed, propose it before changing source order.
- Minimum margins 12 mm; readable type/spacing. CV at most two pages and letter one unless user/employer specifies otherwise.
- Keep an entry together when it fits. If length and readability conflict, ask about shortening or relaxed pagination; do not shrink unreadably or rewrite text.
- **Template:** preserve the selected headline and date alignment; right-aligned dates do not require a table.
- **Letter fields:** use source facts, never guessed contacts or dates.
- **Characters:** disable discretionary ligatures where supported and verify extracted text.
- **Obsidian:** verify pagination in the exported PDF, not Reading view. Leave unrelated themes, snippets and settings unchanged.

## Colour

- Use requested colour or confirmed private preference. Otherwise black headings, charcoal body and white background; resolve "same as last time" only from saved preferences/identified artifact.
- Limit accent to name, headings, dates, labels, links and subtle rules; body stays #222222 or #1A1A1A.
- Check contrast against white: at least 4.5:1, aim 7:1. Propose a darker alternative if needed; do not silently replace requested colour or impose a favourite.
- Visited/unvisited links use the selected colour and remain clickable/readable. Save agreed personal colour choices under evidence/preference rules.

## Save

- Default names: `CV_Name_Position.pdf` / `CoverLetter_Name_Position.pdf`; safe explicit names override defaults.
- **Filename inputs:** get name and position from confirmed facts or JD; ask if missing.
- **Filename safety:** replace whitespace with underscores and remove path separators, control and unsafe characters. Retain readable Unicode; never interpret values as paths.
- Metadata Title equals output basename. Save beside source unless a destination was requested; do not move originals or overwrite a different/submitted version.

## Verify and report

- Extract actual PDF text with two independent methods, such as pdftotext and pypdf. Compare with rendered source, normalizing only whitespace/line breaks/Markdown presentation, not punctuation or order.
- Inspect page images for clipping, breaks, margins and reading order; check page count, links, embedded fonts and metadata. Fix encoding/ligature issues without rewriting content.
- If a check/runtime is unavailable, state the limitation; do not claim full validation, a generated file or universal ATS acceptance.
- Deliver the actual PDF link, page count, text-check methods, relevant colour/contrast and unmet checks/source typos. Do not send/submit documents.
