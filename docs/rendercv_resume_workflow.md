# RenderCV Resume Workflow

Career Positioning OS should not reimplement resume rendering. It should prepare the career signal, then hand the document mechanics to RenderCV.

## Install RenderCV Skill

RenderCV publishes an external agent skill:

```bash
npx skills add rendercv/rendercv-skill
```

For Codex:

```bash
npx skills add rendercv/rendercv-skill --skill rendercv -a codex -g -y
```

The external skill is named `rendercv`.

## Responsibility Split

Career Positioning OS:

- structures private achievement evidence
- selects the right stories and proof
- compresses bullets for reader fit
- checks public/private boundary risks
- prepares resume-ready content

RenderCV:

- owns the YAML schema
- owns themes, layouts, locales, and typography
- renders PDF, HTML, PNG, and Markdown outputs
- validates RenderCV-specific document structure

## Recommended Loop

1. Build or update private achievement packets outside this public repo.
2. Use `impact-bullets` and `compression-and-iteration` to create resume-ready bullet content.
3. Use `rendercv-resume-handoff` to prepare the handoff.
4. Use external `rendercv` skill to create or edit the RenderCV YAML file.
5. Render the PDF with RenderCV.
6. Review the PDF for factual accuracy, positioning, and visual quality.

## Handoff Prompt

```text
Use rendercv to turn this Career Positioning OS resume content into a RenderCV YAML file and render the resume PDF. Preserve factual claims, metrics, and role boundaries. Do not invent missing dates, employers, technologies, or credentials.
```

## Boundary

Do not vendor RenderCV schema docs or rendering code into this repo. Link to the external skill and install it where needed.
