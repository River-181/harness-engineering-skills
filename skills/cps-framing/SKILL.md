---
name: cps-framing
description: Use when the team needs a clear why, strategic narrative, problem definition, or scope boundary before PRD or implementation. Frames a product or feature using Context → Problem → Solution.
argument-hint: "[product-or-feature]"
---
# CPS Framing

## Use when

- User asks “what problem are we solving?”
- Proposal needs a concise narrative
- PRD feels like feature soup
- Presentation needs a persuasive opening

## Do not use when

- Problem framing is already approved and user wants implementation detail

## Inputs to inspect

- `docs/00_source-log.md`
- `docs/01_meeting-log.md`
- User-provided market/project context

## Files to create or update

- `docs/02_cps.md`
- Decision entries in `harness.yaml.decisions` for scope choices

## Operating sequence

1. Write context as concrete facts already true.
2. Write problem as actor + situation + pain/risk/cost.
3. Write solution as operating mechanism, not feature list.
4. Write non-solutions to prevent scope creep.
5. Write success evidence as observable metrics or demo evidence.
6. Create traceability from context to problem to solution.

## CPS Normal Form

```markdown
## Context
- What is true now?
- What workflow, market, system, data, policy, or user behavior creates the setting?

## Problem
- Who experiences pain?
- In what situation?
- What breaks, slows, costs, risks, or is missed?

## Solution
- What loop or mechanism resolves the problem?
- What does the system observe, decide, do, verify, and improve?

## Non-Solutions
- What will not be handled in MVP?

## Success Evidence
- What will judges, customers, or maintainers see?
```

## Quality gates

- Context is not generic trend prose.
- Problem is not a disguised solution.
- Solution names a loop/mechanism and can feed PRD features.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:cps-framing

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
