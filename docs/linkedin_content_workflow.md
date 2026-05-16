# LinkedIn Content Workflow

Use this workflow when an agent drafts LinkedIn profile or content assets from the skills in this repository.

## Loop

1. Draft content using the relevant skill.
2. Save the draft to `content/<asset>.md` with YAML frontmatter.
3. Run the formatter.
4. Run the validator.
5. If validation fails, read the exact machine-readable error.
6. Revise the text.
7. Repeat until validation passes.

## Commands

```bash
python3 scripts/format_linkedin_text.py --write content
python3 scripts/format_linkedin_text.py --check content
python3 scripts/validate_linkedin_assets.py content
python3 scripts/validate_linkedin_assets.py content --config config/linkedin_limits.yaml
```

## Markdown Contract

Every generated LinkedIn text file under `content/` must use YAML frontmatter:

```markdown
---
platform: linkedin
section: about
---

Text body here.
```

Supported `section` values:

- `profile_headline`
- `about`
- `experience_description`
- `project_title`
- `project_description`
- `post`
- `comment`
- `article_title`
- `article_body`

The validator checks only the body, not the frontmatter.

## Repair Rules

Preserve:

1. quantified hook
2. reader benefit
3. proof metrics
4. mechanism/framework
5. CTA

Remove first:

1. filler words
2. repeated qualifiers
3. duplicated concepts
4. excessive internal details
5. weak adjectives
6. redundant setup

Do not remove blank lines just to fit the limit. If the configured count mode ignores newlines, shorten actual text instead.

## Why Blank Lines Matter

LinkedIn content is usually read on mobile. Blank lines prevent walls of text and improve scanning.

For sections configured with `non_newline_unicode_codepoints`, the validator ignores `\n` and `\r`. This means formatting should add breathing room, while compression should remove or tighten words.
