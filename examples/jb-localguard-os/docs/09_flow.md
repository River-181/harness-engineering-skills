# 09 Flow

## Core Demo Flow
A relationship manager opens a risky local-business case. The agent gathers synthetic signals, builds an Evidence Pack, drafts a recommended next action, runs a policy guard, waits for RM approval, writes audit events, and updates the eval dashboard.

## Flow Table
| Step | Actor | Action | System Response | Gate |
|---|---|---|---|---|
| 1 | RM | Opens flagged case | Case details and signals appear | synthetic data only |
| 2 | AI Agent | Gathers evidence | Evidence Pack created | source and freshness required |
| 3 | AI Agent | Drafts recommendation | Draft includes rationale and confidence | policy guard |
| 4 | Policy Guard | Checks constraints | Allows review or blocks draft | fail closed |
| 5 | RM | Approves, rejects, or asks for more evidence | ApprovalRecord created | human approval |
| 6 | Audit Logger | Records event | AuditEvent appended | append-only |
| 7 | Eval Runner | Scores case | Dashboard shows pass/fail | golden case rubric |

## Failure Flow
If evidence is missing or policy rules are unavailable, the draft is blocked and the RM sees a request for more evidence instead of a recommendation.
