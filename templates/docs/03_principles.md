# 03 Principles

## Artifact Metadata
- Owner:
- Last updated:

## Non-Negotiable Principles

| ID | Principle | Meaning | Enforced By | Reject If |
|---|---|---|---|---|
| P1 | Evidence before action | Recommendations show source/evidence/uncertainty | Feature spec, UI rules, evals | Output contains action without evidence |
| P2 | Approval for high-risk actions | Customer-facing or regulated actions require reviewer gate | Agent rules, compliance rules, flow | High-risk action can auto-execute |
| P3 | Fail closed on uncertainty | Missing evidence/permission/policy blocks or escalates | Risk rules, evals | Agent speculates and acts |
| P4 | Normal form over prompt hope | Schemas, rules, tests, evals constrain output | Templates, scripts, lint | “Prompt says so” is the only control |

## Tradeoffs

| Tradeoff | Preferred Direction | Reason | Exception |
|---|---|---|---|

## Principle-to-Artifact Map

| Principle | Docs | Rules | Evals | Code/UX Implication |
|---|---|---|---|---|
