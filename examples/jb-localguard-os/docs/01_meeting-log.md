# 01 Meeting Log

## Artifact Metadata
- Owner: River
- Last updated: 2026-07-03
- Meeting type: synthesis
- Confidence: medium

## Summary
The team selected a narrow demo: relationship managers review a flagged local-business customer case. The AI Agent gathers evidence, grades urgency, drafts a recommended next action, and stops for human approval.

## Decisions
| ID | Decision | Rationale | Owner |
|---|---|---|---|
| DEC-001 | Human approval is mandatory | Prevents autonomous customer-facing action | Product owner |
| DEC-002 | Synthetic data only | Keeps public demo safe | Engineering |
| DEC-003 | Evidence must be shown with recommendation | Improves trust and judge evaluation | AI lead |

## Action Items
| ID | Action | Owner | Due |
|---|---|---|---|
| ACT-001 | Prepare demo cases | Product | before demo |
| ACT-002 | Validate golden cases | QA | before submission |
| ACT-003 | Rehearse three-minute flow | Presenter | before judging |

## Open Questions
| ID | Question | Default Assumption | Owner |
|---|---|---|---|
| Q-001 | Which risk categories should ship first? | overdue payment, news shock, missing document | Product |
