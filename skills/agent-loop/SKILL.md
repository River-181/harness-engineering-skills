---
name: agent-loop
description: Use when designing AI Agent product capabilities, competition judging evidence, or production agent safety. Creates judgment → action → verification/improvement loops with retrieval, rule checks, approval, logging, and feedback.
argument-hint: "[agent-capability]"
---
# AI Agent Loop Design

## Use when

- Need to show AI Agent, not chatbot
- Need judgment/action/verification loop
- Need reviewer approval/audit/feedback design

## Do not use when

- Feature contains no AI judgment or action selection

## Inputs to inspect

- Flow
- Feature spec
- Architecture
- Risk rules
- Eval plan

## Files to create or update

- `docs/09_flow.md`
- Agent sections in `docs/08_feature-spec.md`
- `docs/10_eval-plan.md`
- `rules/agent-rules.md`

## Operating sequence

1. Identify each agent capability.
2. Define trigger and inputs.
3. Define context gathering/retrieval.
4. Define judgment output and confidence.
5. Define possible actions and forbidden actions.
6. Define verification checks.
7. Define approval/escalation.
8. Define audit events and feedback.
9. Add golden cases.

## Agent Capability Card

```markdown
### Agent Capability: <Name>
| Field | Content |
|---|---|
| Trigger | |
| Inputs | |
| Context Sources | |
| Judgment | |
| Possible Actions | |
| Forbidden Actions | |
| Verification | |
| Approval Needed? | |
| Audit Events | |
| Failure Modes | |
| Eval Cases | |
```

## Judgment Output Contract

An agent judgment must include:

- classification/status/risk/priority,
- evidence used,
- uncertainty or confidence,
- recommended action,
- reason not to act if blocked.

## Quality gates

- Generation without verification is incomplete.
- High-risk action without human approval is blocked.
- Every loop has eval cases.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:agent-loop

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
