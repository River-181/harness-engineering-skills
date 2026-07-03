---
name: risk-compliance
description: Use for regulated, financial, customer-facing, enterprise, or high-risk workflows that need reviewable engineering controls. Creates operational risk, privacy, security, compliance, approval, audit, copyright, hallucination, explainability, and responsibility controls. Not legal advice.
argument-hint: "[workflow-or-domain]"
---
# Risk and Compliance Harness

## Use when

- Personal/sensitive/regulated data is involved
- Customer-facing action exists
- External model/API boundary exists
- Compliance/audit questions are likely

## Do not use when

- Pure internal toy example with no risk and user asked for lightweight flow

## Inputs to inspect

- Architecture
- Agent loop
- Data rules
- Feature spec
- Known policies or laws from user

## Files to create or update

- Risk section in `docs/06_prd.md`
- Security boundary in `docs/07_architecture.md`
- Failure handling in `docs/09_flow.md`
- Risk cases in `docs/10_eval-plan.md`
- `rules/compliance-rules.md` and `rules/data-rules.md`

## Operating sequence

1. Classify data types.
2. Identify high-risk actions.
3. Identify external model/API boundaries.
4. Define approval gates.
5. Define audit events.
6. Define fail-closed triggers.
7. Define mitigations for privacy/security/copyright/hallucination/explainability/responsibility.
8. Assign owner and residual risk.
9. Add limitations to handoff.

## Approval Gate Schema

```markdown
| Action | Risk Level | Required Reviewer | Evidence Required | Can Auto-Execute? | Audit Event |
```

## Fail-Closed Triggers

- Missing permission.
- Missing evidence.
- Policy ambiguity.
- PII boundary uncertainty.
- Conflicting sources.
- Low confidence on high-risk action.
- External API/license uncertainty.

## Quality gates

- High-risk customer action cannot be complete without approval + audit + fallback.
- Legal conclusions are not invented; uncertain law is marked for review.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:risk-compliance

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
