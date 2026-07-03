---
name: architecture
description: Use after PRD/domain model and before implementation. Designs system architecture, component boundaries, dataflow, integration points, security boundaries, logging, audit, failure handling, and demo-vs-production separation.
argument-hint: "[system-or-feature]"
---
# Architecture and Dataflow

## Use when

- Need buildable architecture
- Need dataflow/security boundary
- External API/model usage must be documented
- Demo shortcuts must be separated from production

## Do not use when

- No domain model exists; run domain-model first unless user asks for rough sketch

## Inputs to inspect

- Domain model
- PRD
- Feature spec
- Data rules
- Existing repo stack

## Files to create or update

- `docs/07_architecture.md`
- Updates to `rules/data-rules.md`, `rules/agent-rules.md`, `rules/compliance-rules.md`

## Operating sequence

1. Identify runtime components.
2. Assign responsibilities and ownership.
3. Describe dataflow and trust boundaries.
4. List external services with data sent/received, license, constraints, fallback.
5. Define storage, retention, logging, audit.
6. Define failure modes and fallbacks.
7. Separate demo-mode mocks from production architecture.

## Required Architecture Views

1. Component view.
2. Dataflow view.
3. Agent execution view.
4. Security/trust boundary view.
5. Audit/logging view.
6. Failure/fallback view.

## External Boundary Rule

No external model/API/service may appear without:

- purpose,
- data sent,
- data received,
- permission basis or constraint,
- fallback,
- audit/log event.

## Quality gates

- No “black box AI” component.
- Data leaving the system is explicitly described.
- Demo mocks are labeled.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:architecture

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
