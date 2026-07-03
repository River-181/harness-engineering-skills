---
name: domain-model
description: Use before architecture, database design, code generation, or AI Agent implementation. Builds an implementation-ready domain model with entities, relationships, states, transitions, events, permissions, and audit relationships.
argument-hint: "[domain-or-feature]"
---
# Domain Modeling

## Use when

- Need schema/API/UI state model
- Central object lifecycle is unclear
- Permissions or audit depend on state transitions

## Do not use when

- User only needs high-level narrative

## Inputs to inspect

- CPS
- Principles
- Definitions
- Feature scenarios

## Files to create or update

- `docs/05_domain-model.md`
- Updates to `rules/data-rules.md` and `rules/agent-rules.md`

## Operating sequence

1. Identify entities from definitions and workflows.
2. Map relationships and ownership.
3. Choose central lifecycle objects.
4. Define allowed and blocked transitions.
5. Define events and payload fields.
6. Define permissions by role and state.
7. Attach audit events to high-risk transitions.
8. Mark unknown fields as explicit open questions with owner.

## State Transition Contract

Every transition must specify:

- current state,
- next state,
- actor or system trigger,
- validation required,
- audit event,
- rollback or failure state.

## Event Naming

Use past-tense domain events:

- `CaseTriaged`
- `EvidenceCollected`
- `RecommendationValidated`
- `ActionApproved`
- `ActionRejected`

## Quality gates

- No state transition lacks actor/trigger.
- No high-risk transition lacks audit.
- Permissions are not “everyone can everything.”


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:domain-model

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
