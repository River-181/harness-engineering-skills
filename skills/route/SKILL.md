---
name: route
description: Use when the user asks what to do next, gives messy product/enterprise AI/FDE/MVP/agent-delivery requirements, asks for a harness, or requests implementation before discovery artifacts exist. Routes the request into the right Harness Engineering lifecycle skill and artifact sequence.
argument-hint: "[task-or-project-context]"
---
# Harness Engineering Router

## Use when

- User asks “what should we do next?”
- User gives messy requirements and expects product output
- User asks for implementation but artifacts are missing
- User asks to make the project deterministic, reusable, maintainable, or handoff-ready

## Do not use when

- The user already named the exact skill to run and all inputs exist
- The request is a small one-off edit unrelated to harness artifacts

## Inputs to inspect

- `harness.yaml` if present
- `docs/` artifact inventory
- `rules/` and `evals/` inventory
- README, package files, open issues, or user-provided task

## Files to create or update

- A routing report
- Optionally update `harness.yaml.open_questions` and `harness.yaml.quality_gates` when gaps are discovered

## Operating sequence

1. Classify the project stage: discovery, MVP, pilot, production, handoff, or skillpack-maintenance.
2. Inventory required artifacts without assuming they exist.
3. Classify user intent: intake, framing, surfaces, definitions, domain, PRD, architecture, agent loop, code rules, eval, risk, demo, validation, or adapter.
4. Choose exactly one next skill unless user explicitly asks for a batch.
5. Name the first file to create or update.
6. State the stop condition before implementation.

## Routing Matrix

| Evidence | Recommended skill |
|---|---|
| Raw transcript, notes, voice memo, vague ask | `intake-log` |
| Business value, data advantage, costs, revenue, or negative impact unclear | `ddbm-business-model` |
| No clear why / problem / solution | `cps-framing` |
| Several actors, apps, consoles, portals, dashboards | `surface-map` |
| Terms drift or team disagrees on concepts | `principles-definitions` |
| Need entities, states, events, permissions | `domain-model` |
| Need MVP proposal, PRD, feature spec | `prd-spec` |
| Need component/dataflow/security boundary | `architecture` |
| Need AI Agent judgment/action/verification | `agent-loop` |
| Need deterministic code output across models | `code-rules` |
| Need quality metrics, golden cases, regression | `eval-design` |
| Privacy/security/compliance/high-risk action | `risk-compliance` |
| Presentation, submission, demo, delivery | `demo-handoff` |
| JB Fin:AI judging alignment | `jb-finai-adapter` |
| Existing harness needs pass/fail report | `validate-harness` |

## Output Format

```markdown
## Harness Route
- Current stage:
- User intent:
- Missing critical artifacts:
- Recommended next skill:
- First file to update:
- Why this order:
- Stop condition before implementation:
```

## Quality gates

- The route chooses one next action, not a sprawling plan.
- The route blocks implementation if there is no CPS/domain model/rules for a high-risk feature.
- The route does not invent artifact status.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:route

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
