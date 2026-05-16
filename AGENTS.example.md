# Career Positioning OS Agent Instructions

> Public-safe template. Do not put private career strategy, real employer details, applications, raw notes, or achievement packets in this repo.

## Purpose

Help users turn private work evidence into public-safe career artifacts through reusable methodology, schemas, examples, and skills.

## Boundaries

Public-safe:

- methodology
- templates
- schemas
- dummy examples
- reusable skills
- deterministic validators and formatting scripts

Private:

- real achievement packets
- raw notes
- employer details
- target job strategy
- applications
- compensation or review strategy

## Repository Status

This is a public methodology and skills repo. Keep examples fictional or sanitized, and keep real user evidence in a private repository.

## LinkedIn/Profile Assets

When drafting LinkedIn or profile content into files, use the relevant writing skill first, then use `linkedin-content-validation`.

Run:

```bash
python3 scripts/format_linkedin_text.py --write content
python3 scripts/format_linkedin_text.py --check content
python3 scripts/validate_linkedin_assets.py content
```

Do not remove blank lines just to satisfy a LinkedIn character limit when the configured count mode ignores newlines. Compress actual words instead.
