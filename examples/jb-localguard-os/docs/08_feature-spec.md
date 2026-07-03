# 08 Feature Spec

## Feature Index
| ID | Feature | Status | Trace |
|---|---|---|---|
| F-001 | Case Intake | MVP | REQ-001 |
| F-002 | Evidence Pack | MVP | REQ-001 |
| F-003 | Recommendation Draft | MVP | REQ-001, REQ-002 |
| F-004 | Approval Gate | MVP | REQ-002 |
| F-005 | Audit Log | MVP | REQ-003 |
| F-006 | Eval Dashboard | MVP | Success Evidence |

## Feature Template
### F-004 Approval Gate
- User: Relationship Manager
- Trigger: Recommendation Draft is ready
- Input: draft, evidence, confidence, policy guard result
- Output: approval, rejection, or request for more evidence
- Acceptance criteria: customer-facing next action remains blocked until approval exists
- Risks: over-trust in AI, missing evidence, policy mismatch
- Eval case: GC-002 approval required

### F-005 Audit Log
- User: Compliance Reviewer
- Trigger: material workflow step occurs
- Input: actor, event, payload hash, timestamp
- Output: append-only audit event
- Acceptance criteria: case open, evidence generation, draft creation, and approval all create events
- Risks: incomplete audit trail
- Eval case: GC-003 audit completeness
