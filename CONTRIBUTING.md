# Contributing

## Scope

- Keep career-task rules in `policies/`, personal choices in ignored `policies/preferences.md`, and presentation defaults in `templates/`.
- Read only the policies affected by a change. Ordinary career tasks do not need this guide.
- Keep private candidate files, generated applications, local configuration and credentials out of commits.

## Writing policies

- Use a descriptive title. Add one scope sentence only when the title leaves a meaningful ambiguity.
- Do not require Use when, Read with, Why or a callout at the top of every file.
- Keep one decision per bullet; keep its condition and consequence together.
- Split unrelated actions, not every sentence. Use short labels when they improve scanning.
- Use numbered steps for required sequences and tables for mappings or fixed specifications.
- Prefer natural wording to slash lists; preserve literal paths, commands, schemas and formulas.
- Explain a reason or include an example only for a boundary that is easy to misinterpret.
- Keep each rule in one owning file. References are lookups, not instructions to recursively reload every linked policy.
- Merge corrections into existing rules and remove superseded text. Avoid generic advice and discussion history.

## Reviewing changes

- Ask the user to resolve behavior conflicts; do not silently change authorization, scores or evidence standards during cleanup.
- Preserve scoring anchors, formulas, output contracts, source boundaries and approved action scope.
- Check links, representative edge cases and applicable tests. Tests alone do not prove an AI will interpret prose correctly.
- Preserve unrelated edits, staged state and submitted documents. Do not commit unless requested.
