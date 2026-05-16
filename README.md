# Career Positioning OS

Most career materials are written as summaries of what happened.

That is not enough. Good positioning turns real achievements into persuasive representations: structured clearly enough for a busy executive, emotionally legible enough for a reader to care, and specific enough that the claim feels earned.

Career Positioning OS is a public-safe skill system for doing that with AI agents.

It starts from the source of truth:

```text
private work evidence
  -> structured achievement packet
  -> persuasive, sanitized representation
  -> resume, LinkedIn, portfolio, recruiter, or interview artifact
```

The skills encode reusable writing and persuasion principles: consulting-style top-down structure, narrative tension, SCQA, curiosity gaps, proof before claim, status-aware positioning, and direct-response copywriting patterns. The goal is to make achievement representation repeatable without leaking private details, overclaiming, or rewriting the same story from scratch for every surface.

## What It Helps With

- Structure messy work evidence before turning it into public persuasion.
- Preserve metrics, caveats, proof sources, and status distinctions so the writing stays credible.
- Keep private evidence separate from public methodology.
- Draft long-form project stories with narrative tension and reusable takeaways.
- Turn one achievement source into different persuasive views for different audiences.
- Keep the agent focused on representation principles instead of generic resume-writing advice.

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

Then use the installed skill when you want a persuasive long-form narrative:

```text
Use article-leverage-story to turn this achievement packet into a confidentiality-safe article draft.
```

The current public skill is optimized for story-driven articles and case-study narratives. It is not meant to be the final tool for resume bullets, compact LinkedIn bullets, or recruiter DMs.

The skill should help with the thinking behind the representation, not just the prose: what to lead with, what proof to reveal when, how to create contrast without arrogance, and how to extract the reusable operating principle from the story.

## Keep Private Data Out

Do not put real raw notes, employer details, internal links, private metrics, target jobs, applications, compensation, or review strategy in this repo.

Use fictional examples here. Keep real evidence in a private repo, then publish only reviewed and sanitized outputs.

## Example

See the dummy achievement examples for the packet shape:

```bash
cat examples/dummy-achievements.yaml
```
