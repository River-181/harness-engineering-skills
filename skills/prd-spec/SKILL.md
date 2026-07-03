---
name: prd-spec
description: Use when moving from framing to buildable scope. Creates PRD, MVP proposal, and implementation-ready feature specs traced to CPS, users, scenarios, acceptance criteria, demoability, and risk controls.
argument-hint: "[product-or-feature]"
---
# PRD and Feature Specification

## Use when

- Need MVP proposal or feature specification
- Features need acceptance criteria
- Submission documents need consistent content

## Do not use when

- No CPS exists; use cps-framing first

## Inputs to inspect

- CPS
- Surface map
- Principles/definitions
- Domain model
- Existing feature list

## Files to create or update

- `docs/06_prd.md`
- `docs/08_feature-spec.md`
- Updates to `docs/09_flow.md` and `docs/11_change-log.md` if scope changes

## Operating sequence

1. Trace each feature to a problem and user job.
2. Classify MVP vs future scope.
3. Write acceptance criteria per feature.
4. Specify inputs, outputs, UI behavior, backend behavior, agent behavior.
5. Attach validation rules and error states.
6. Mark demoable features.
7. Record scope changes.

## Feature Acceptance Bar

A feature is implementation-ready only when it has:

- user and job,
- trigger,
- input/output,
- UI behavior or API behavior,
- agent behavior if AI-driven,
- validation/error states,
- audit events if high-risk,
- objective acceptance criteria,
- demo evidence.

## Traceability Table

```markdown
| Feature | Problem Trace | User | MVP? | Demo Step | Eval Case | Risk Control |
```

## Quality gates

- No feature exists without problem trace.
- No AI feature exists without agent behavior and eval case.
- No high-risk feature lacks control.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:prd-spec

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
