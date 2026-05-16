---
name: linkedin-content-validation
description: Use when drafting, saving, formatting, validating, or repairing LinkedIn profile and content assets in this repository, including headlines, About sections, Experience descriptions, project copy, posts, articles, and LinkedIn image specs.
---

# LinkedIn Content Validation

Use this skill after any LinkedIn/profile-content drafting skill produces copy or visual specs.

## Workflow

1. Save generated text under `content/` as Markdown with YAML frontmatter.
2. Save generated image specs under `content/` or `assets/` as YAML.
3. Run the formatter.
4. Run the validator.
5. If validation fails, repair the draft using the exact machine-readable error.
6. Repeat until validation passes.

## Markdown Contract

Every LinkedIn Markdown file must use frontmatter:

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

## Commands

```bash
python3 scripts/format_linkedin_text.py --write content
python3 scripts/format_linkedin_text.py --check content
python3 scripts/validate_linkedin_assets.py content
python3 scripts/validate_linkedin_assets.py content --config config/linkedin_limits.yaml
```

## Repair Priorities

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

Do not remove blank lines just to fit a character limit. If `count_mode` is `non_newline_unicode_codepoints`, shorten actual words instead.
