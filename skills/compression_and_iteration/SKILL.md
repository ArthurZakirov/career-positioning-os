---
name: compression-and-iteration
description: Compress bios, profile sections, bullets, posts, and visual prompts to strict character limits while preserving hook, proof, mechanism, reader benefit, and CTA.
---

# Compression & Iteration Skill

## Use this when

Use this skill when copy is over a character limit or feels too dense.

Common limits:

- LinkedIn headline
- LinkedIn About section
- LinkedIn Experience description
- GitHub bio
- resume one-page constraints
- social posts
- image prompt text limits

## Core principle

Compression should not remove the reason to read.

Protect these elements:

1. hook
2. proof
3. unusual contrast
4. mechanism
5. reader benefit
6. CTA

Cut everything else first.

## Step 1 — Count and classify

Identify:

- current character count
- target character count
- required reduction
- highest-signal sentences
- low-signal/redundant sections

## Step 2 — Protect the spine

For a bio/profile, protect:

```text
proof → unusual starting point → curiosity question → mechanism → reader benefit → CTA
```

For resume bullets, protect:

```text
metric → outcome → mechanism → scope
```

For visual prompts, protect:

```text
layout → emotional contrast → mechanism → aspect ratio → text constraints
```

## Step 3 — Cut in the right order

Cut in this order:

1. filler phrases
2. repeated words
3. unnecessary adjectives
4. long setup explanations
5. redundant examples
6. overly detailed starting-point descriptions
7. secondary tools in long tech-stack lists
8. less measurable claims
9. optional CTA modifiers

Do not cut first:

- numbers
- timeframes
- before/after metrics
- strong mechanism phrases
- reader-benefit line
- proof of adoption

## Common compression replacements

```text
"in order to" → "to"
"the reason why" → "why"
"was able to" → "could" or direct verb
"helped to secure" → "helped secure"
"a very high amount of" → "high"
"the people closest to the work" → "operators/users"
"with the goal of" → "to"
"made it possible for" → "enabled"
"used operational data to see the bigger picture" → "used operational data"
```

## Compressing the starting-point gap

Bad:

```text
Before this role, most of my coding experience came from many different internships where I mainly wrote Jupyter notebooks and scripts, and I had little experience with Java, AWS, Databricks, Spark, CI/CD, production testing, and large legacy services.
```

Better:

```text
Before this, my coding was mostly ML notebooks and scripts. I had to ramp up on production engineering, cloud, CI/CD, testing, and legacy services almost from scratch.
```

## Compressing mechanisms

Verbose:

```text
I use active listening, operational data, and direct manual exposure to uncover the real bottleneck, risk, deadline, or hidden constraint.
```

Shorter:

```text
Use active listening, data, and hands-on exposure to uncover the real bottleneck, risk, or constraint.
```

## Compression output format

Return:

```markdown
## Current estimate
- Characters: [count]
- Limit: [limit]
- Need to cut: [number]

## Revised version
[text]

## What I cut
- [cut]
- [cut]

## What I protected
- [protected]
- [protected]
```

## Iteration rules

When revising based on feedback:

- Preserve the user's underlying conceptual correction, not just the surface wording.
- If the user rejects a phrase, infer the principle behind the rejection.
- Do not reintroduce previously rejected claims.
- Distinguish between factual correction and style preference.
- Keep a compact list of protected phrases.

## Quality bar

A compressed version is successful if:

- it fits the limit
- the hook still works
- proof remains specific
- the mechanism remains distinct
- the reader benefit remains clear
- no factual nuance was reversed
