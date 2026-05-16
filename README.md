# Career Positioning OS

Most career materials are written backwards: you start with a resume, LinkedIn profile, or portfolio page, then try to remember which stories prove the claim.

Career Positioning OS starts from the source of truth instead:

```text
private work evidence
  -> structured achievement packet
  -> sanitized public abstraction
  -> resume, LinkedIn, portfolio, recruiter, or interview artifact
```

The goal is to make career positioning repeatable without leaking private details, overclaiming, or rewriting the same story from scratch for every surface.

## What It Helps With

- Structure messy work evidence before writing public copy.
- Preserve metrics, caveats, proof sources, and status distinctions.
- Keep private evidence separate from public methodology.
- Draft long-form project stories with a reusable narrative pattern.
- Use the same achievement source for multiple later outputs.

This repo contains public-safe methodology and skills. Your real evidence belongs in a private repo.

## Install

Install the skills for Codex with `skills.sh`:

```bash
npx skills add https://github.com/ArthurZakirov/career-positioning-os --skill '*' -a codex -g -y
```

List available skills first:

```bash
npx skills add https://github.com/ArthurZakirov/career-positioning-os --list
```

For local development from a cloned repo, link skills into Claude Code, `.agents`, and Codex skill directories:

```bash
./scripts/setup-local-links.sh
```

Existing non-symlink paths are left untouched unless `--force` is used.

## Use

Start by turning a real achievement into a private achievement packet using the schema. Keep the packet private.

Then use the installed skill when you want a long-form narrative:

```text
Use article-leverage-story to turn this achievement packet into a confidentiality-safe article draft.
```

The current public skill is optimized for story-driven articles and case-study narratives. It is not meant to be the final tool for resume bullets, compact LinkedIn bullets, or recruiter DMs.

## Keep Private Data Out

Do not put real raw notes, employer details, internal links, private metrics, target jobs, applications, compensation, or review strategy in this repo.

Use fictional examples here. Keep real evidence in a private repo, then publish only reviewed and sanitized outputs.

## Example

See the dummy achievement examples for the packet shape:

```bash
cat examples/dummy-achievements.yaml
```
