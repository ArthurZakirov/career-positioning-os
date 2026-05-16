---
name: context-to-capability-framework
description: Explain or apply a general operating model that turns messy requests and unfamiliar domains into reusable, adopted capabilities through clarification, context engineering, reuse, composition, hardening, and adoption.
---

# Context-to-Capability Framework Skill

## Use this when

Use this skill to describe or apply a repeatable work model for:

- automation initiatives
- AI-agent projects
- developer-productivity systems
- internal tools
- operational workflows
- onboarding systems
- technical writing
- problem-solving case studies
- cross-domain ramp-up stories

## Core principle

The goal is not just to solve one task.

The goal is to turn messy context into reusable capability:

```text
messy request → clarified problem → reusable system → adopted outcome
```

## The framework

### 1. Decode the request behind the request

People often describe the first solution that comes to mind. Do not take the surface request as the real problem too quickly.

Use:

- active listening
- mirroring
- labeling emotions/frustrations
- restating the request in your own words
- looking for business risk, deadline, fear, manual pain, or hidden constraint
- direct exposure to the manual work
- operational data to validate where friction actually is

Goal:

```text
avoid solving the stated task while missing the real need
```

### 2. Context-engineer the problem

Assemble relevant context from:

- conversations
- docs
- tickets
- data
- code
- previous attempts
- constraints
- examples of the manual workflow

Then turn it into a form humans and AI tools can reason over.

Possible outputs:

- structured brief
- markdown context pack
- diagrams
- ticket analysis
- codebase map
- data dashboard
- problem statement
- decision memo

### 3. Find what already works

Before building, search for existing partial solutions.

Look for:

- the person who knows the problem best
- existing internal tools
- products
- methods
- experts
- books
- frameworks
- GitHub repos
- forum threads
- docs
- prior attempts

Principle:

```text
Most problems are not new. Someone has likely spent more time solving a version of it than you have.
```

### 4. Compose the solution

This solves the current instance.

Compose the right mix of:

- existing tools
- deterministic code
- APIs
- AI agents
- CLIs
- dashboards
- diagrams
- documentation
- SOPs
- human workflow changes

Do not force everything into AI or code. Choose the mechanism the outcome requires.

### 5. Harden the learning

This is different from composing the solution.

- Compose = solve this case.
- Harden = make the next similar case faster.

After the rabbit hole is solved, capture the discovered path as reusable capability.

Good hardening artifacts:

- agent skill
- script
- setup automation
- debugging procedure
- reusable prompt/context pack
- markdown playbook
- small internal tool
- checklist
- test harness

Example:

```text
Fixing one broken pipeline solves the current issue.
Creating an agent skill for debugging that pipeline class makes the next similar issue faster.
```

### 6. Make the solution land

A solution is not done when it technically works.

It lands when people understand it, trust it, use it, and can see the result.

Use:

- belief-creating demos
- diagrams
- flowcharts
- onboarding
- documentation
- workshops
- KPIs
- dashboards
- storytelling
- Pyramid Principle structure
- problem-first communication

Do not lead with the technology. Start with the problem the listener already cares about.

## Short framework line

```text
Decode the request behind the request → context-engineer the problem → find what already works → compose the solution → harden the learning → make it land.
```

## Application prompt

When applying the framework to a new project, ask:

```markdown
1. What surface request did the user/stakeholder give?
2. What deeper risk, deadline, bottleneck, or desire might be behind it?
3. What context exists: conversations, docs, tickets, data, code, previous attempts?
4. Who or what may already know part of the answer?
5. What mix of code, AI, tools, docs, dashboards, and human workflow is needed?
6. What learning should be hardened so the next similar case is faster?
7. How will the solution land: demo, onboarding, dashboard, KPI story, or leadership narrative?
```

## Quality bar

A strong output distinguishes clearly between:

- solving the current problem
- hardening the learning for future problems
- making the solution adopted and visible
