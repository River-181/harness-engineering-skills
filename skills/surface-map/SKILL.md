---
name: surface-map
description: Use when a vague product may require multiple apps, consoles, portals, dashboards, APIs, actors, permissions, or action boundaries. Decomposes a product into user-facing and operator-facing software surfaces by actor, job, permission, data access, action authority, and risk.
argument-hint: "[product-context]"
---
# Product Surface Decomposition

## Use when

- One “app” actually has multiple actors
- Demo combines user/admin/reviewer flows
- Permissions or risk differ by user group

## Do not use when

- Single actor, single workflow, no permission distinction

## Inputs to inspect

- CPS
- PRD draft
- User roles
- Workflow notes

## Files to create or update

- Product Surfaces section in `docs/06_prd.md`
- Flow updates in `docs/09_flow.md`
- Permission notes for `docs/05_domain-model.md`

## Operating sequence

1. List all explicit and implied actors.
2. For each actor, list job-to-be-done, data access, actions, and risk.
3. Split surfaces when permissions, risk, or workflow differ.
4. Mark MVP vs future surfaces.
5. Identify cross-surface handoffs and approval points.
6. Flag demo simplifications separately.

## Surface Split Test

Split into separate surfaces when any answer differs materially:

- Who uses it?
- What data can they see?
- What can they change or execute?
- Who approves the action?
- What audit trail is needed?
- What would be dangerous if exposed to the wrong actor?

## Output Table

```markdown
| Surface | User | Job | Core Screens | Data Access | Actions | Risks | MVP? |
```

## Quality gates

- Customer and admin powers are not mixed without an explicit demo-mode label.
- Every high-risk action belongs to an internal/reviewer/approval surface.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:surface-map

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
