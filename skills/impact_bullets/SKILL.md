---
name: impact-bullets
description: Convert raw work history into measurable resume and LinkedIn experience bullets with outcomes, scope, mechanisms, tech stack, and credibility signals under character limits.
---

# Impact Bullets Skill

## Use this when

Use this skill to create or revise:

- resume bullets
- LinkedIn Experience bullets
- project-impact bullets
- performance-review summaries
- portfolio case-study proof points

## Core principle

A bullet should prove value, not merely list responsibilities.

Strong bullet formula:

```text
Action + measurable result + context/constraint + mechanism + business/user impact
```

Not every bullet needs all parts, but the strongest bullets include several.

## Step 1 — Extract raw material

From the user's notes, extract:

- outcome achieved
- metric or scale
- time period
- starting constraint
- technical mechanism
- tools/tech stack
- audience/users affected
- business risk or deadline
- adoption evidence
- seniority/visibility signals

Do not invent metrics or tools.

## Step 2 — Choose bullet type

Use a mix of bullet types.

### Outcome bullet

Focuses on business result.

```text
• Helped secure [business-critical outcome] by [action] in [timeframe], after [constraint].
```

### Leverage bullet

Shows before/after prioritization or efficiency.

```text
• Shifted [roadmap/process] from [before metric] to [after metric] — [ratio] more leverage — by [mechanism].
```

### Production system bullet

Shows real deployment and stack.

```text
• Built and deployed [system] with [tech stack], automating [workflow steps].
```

### Adoption bullet

Shows the work landed with users.

```text
• Equipped [number/type of users] with [capability] through [workshops/onboarding/docs/tools].
```

### Scope-expansion bullet

Shows responsibility beyond role.

```text
• Became a technical contact for [stakeholders] on [topics], supporting [decisions/outcomes].
```

### Ramp-up bullet

Shows learning speed.

```text
• Exceeded [expected level/timeframe] in [domain] despite [starting constraint], contributing to [critical effort].
```

## Step 3 — Add tech stack without bloating

Tech stack should support credibility, not drown the bullet.

Good:

```text
• Built and deployed [system] with LangChain, Pydantic, Databricks, Delta Lake, and MLflow, automating [workflow].
```

Too much:

```text
• Built with Tool A, Tool B, Tool C, Tool D, Tool E, Tool F, Tool G, Tool H, Tool I, Tool J...
```

For long stacks, add a final line:

```text
Tech stack: Python, Java, Databricks, Delta Lake, MLflow, AWS, Docker, Jira API, Slack API.
```

## Step 4 — Avoid internal jargon

Translate internal names into external language.

Examples:

- internal request channel → operational request channel
- team-specific acronym → manual operational workflow
- service name → legacy Java service
- internal ticket code → automation roadmap item

Keep private/company-specific details out unless the user explicitly wants them included.

## Step 5 — Tune for platform

### Resume

More formal, achievement-oriented, concise.

### LinkedIn Experience

Can be slightly more narrative and include adoption/visibility signals.

### Performance review

Can include more context, constraints, and leadership appreciation.

## Character-limit compression order

When over limit, cut in this order:

1. adjectives and filler
2. repeated tech stack mentions
3. excessive internal context
4. secondary examples
5. redundant bullets
6. less measurable claims

Protect:

- strongest metrics
- business-critical outcomes
- deployed/adopted evidence
- senior stakeholder signals
- unique mechanisms

## Strong verbs

Use:

- built
- deployed
- shifted
- secured
- automated
- equipped
- reduced
- maintained
- enabled
- analyzed
- visualized
- onboarded
- contributed
- converted
- hardened
- scaled

Avoid:

- helped with
- worked on
- involved in
- participated in
- responsible for

Use “helped” only when the user wants careful attribution or did not own the whole outcome.

## Output format

Return:

```markdown
## Full version
[bullets]

## LinkedIn version under [limit]
[bullets]

## Resume version
[bullets]

## Notes / assumptions
- [items that need user verification]
```

## Quality bar

Every bullet should answer at least two of:

- What changed?
- How much?
- How fast?
- For whom?
- Under what constraint?
- Using what mechanism?
- Why did it matter?
