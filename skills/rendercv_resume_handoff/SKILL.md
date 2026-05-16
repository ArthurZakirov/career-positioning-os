---
name: rendercv-resume-handoff
description: Use when a user wants to turn Career Positioning OS resume content into a RenderCV YAML file, install or use the external RenderCV agent skill, or render a resume/CV PDF without reimplementing RenderCV's schema, CLI, themes, or PDF generation.
---

# RenderCV Resume Handoff

Use this skill when Career Positioning OS work reaches the point where resume content should become a deterministic CV/resume artifact.

## Principle

Do not reimplement RenderCV.

Career Positioning OS owns:

- achievement evidence structure
- positioning logic
- bullet/story compression
- audience fit
- public/private boundary checks

RenderCV owns:

- YAML resume schema
- theme and layout options
- rendering pipeline
- PDF/HTML/PNG/Markdown outputs
- typography and document mechanics

## External Skill

RenderCV publishes its own agent skill:

```bash
npx skills add rendercv/rendercv-skill
```

For Codex specifically:

```bash
npx skills add rendercv/rendercv-skill --skill rendercv -a codex -g -y
```

Use the external `rendercv` skill for RenderCV-specific schema, CLI, theme, and rendering details.

## Workflow

1. Use Career Positioning OS skills to select and compress the resume content.
2. Preserve the source achievement packet privately.
3. Produce public-safe bullet text and section content.
4. Hand off the selected content to the external `rendercv` skill.
5. Let the `rendercv` skill create or edit the YAML file.
6. Let RenderCV render the final PDF or other outputs.

## Handoff Prompt

Use this prompt when the external skill is installed:

```text
Use rendercv to turn this Career Positioning OS resume content into a RenderCV YAML file and render the resume PDF. Preserve factual claims, metrics, and role boundaries. Do not invent missing dates, employers, technologies, or credentials.
```

If the external skill is not available in the current session, tell the user to install it with:

```bash
npx skills add rendercv/rendercv-skill --skill rendercv -a codex -g -y
```

Then restart or reload the agent session if the runtime only discovers skills at startup.

## Guardrails

- Do not copy RenderCV schema documentation into this repo.
- Do not create a parallel RenderCV validator here.
- Do not guess RenderCV YAML fields when the external skill can provide the current schema.
- Do not remove Career Positioning OS evidence caveats just to make a resume look cleaner.
- Keep private source evidence outside this public repo.
