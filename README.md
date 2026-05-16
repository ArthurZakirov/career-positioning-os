# Career Positioning OS

Public-safe skills, schemas, and examples for turning private work evidence into market-facing career signal.

## Contents

- `schemas/achievement-packet.schema.json`: JSON Schema for structured achievement evidence.
- `examples/dummy-achievements.yaml`: fictional examples that show the shape without using private evidence.
- `docs/public-private-boundary.md`: rules for keeping real evidence out of the public repo.
- `skills/article-leverage-story/SKILL.md`: public-safe long-form story/article drafting skill.
- `.codex-plugin/plugin.json`: Codex plugin manifest.
- `.agents/plugins/marketplace.json`: Codex marketplace metadata.
- `.claude-plugin/`: Claude Code plugin metadata.
- `scripts/setup-local-links.sh`: local symlink setup for Claude Code, `.agents`, and Codex skill directories.

## Local Setup

Link the repo skills into local agent runtimes:

```bash
./scripts/setup-local-links.sh
```

The script links each skill directory into:

- `~/.claude/skills/`
- `~/.agents/skills/`
- `~/.codex/skills/`

Existing non-symlink paths are left untouched unless `--force` is used.

## Install With skills.sh

Install from GitHub:

```bash
npx skills add https://github.com/ArthurZakirov/career-positioning-os --list
npx skills add https://github.com/ArthurZakirov/career-positioning-os --skill '*' -a codex -g -y
```

## Boundary

This repo may contain methodology, templates, schemas, dummy examples, and reusable skills.

Private evidence belongs in a private repo, not here.

Use this flow:

```text
private raw notes
  -> private achievement packet
  -> sanitized public abstraction
  -> public artifact
```
