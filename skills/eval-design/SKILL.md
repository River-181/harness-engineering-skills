---
name: eval-design
description: Use when a project needs proof that agent outputs remain useful, grounded, safe, and maintainable over time. Creates organization-specific evals: golden cases, rubrics, failure modes, regression schedule, cross-agent normal-form comparison, and safety gates.
argument-hint: "[capability-or-project]"
---
# Evaluation Design

## Use when

- Need AI quality metrics
- Need regression tests
- Need compare outputs across models
- Need judge/client confidence

## Do not use when

- No AI or variable output exists and user only needs static docs

## Inputs to inspect

- Agent loop
- PRD
- Risk register
- Known failure modes
- Example inputs/outputs

## Files to create or update

- `docs/10_eval-plan.md`
- `evals/golden-cases.md`
- `evals/rubric.md`
- `evals/failure-modes.md`

## Operating sequence

1. Define eval objective.
2. Write golden cases with expected judgment/action.
3. Define must-include and must-not-include constraints.
4. Create human review rubric.
5. Create failure modes and mitigations.
6. Define pass/warn/fail thresholds.
7. Add regression cadence.
8. For model convergence, compare artifacts against normal-form rubric.

## Eval Types

- **Trigger eval:** Does the right skill activate?
- **Shape eval:** Did required files/sections appear?
- **Grounding eval:** Are claims tied to evidence?
- **Action safety eval:** Does the agent escalate/approve correctly?
- **Normal-form eval:** Do outputs from different models converge structurally?
- **Regression eval:** Does quality degrade after changes?

## Golden Case Format

```markdown
| ID | Scenario | Input | Expected Judgment | Expected Action | Must Include | Must Not Include | Risk Level |
```

## Quality gates

- No metric is “accuracy” without definition.
- High-risk scenarios include fail-closed cases.
- Eval plan can be rerun by maintainers.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:eval-design

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
