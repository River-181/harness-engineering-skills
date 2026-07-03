# 05 Domain Model

## Entities
| Entity | Description | Key Fields |
|---|---|---|
| Case | Customer risk review item | case_id, status, risk_level, owner |
| Signal | Structured or unstructured evidence | signal_id, type, source, freshness |
| EvidencePack | Curated evidence for a case | evidence_ids, summary, confidence |
| RecommendationDraft | Proposed next action | action_type, rationale, confidence |
| ApprovalRecord | Human review result | approver, decision, timestamp, reason |
| AuditEvent | Immutable workflow event | event_type, actor, payload_hash, timestamp |

## States
| Object | States |
|---|---|
| Case | new, evidence_gathered, draft_ready, approved, rejected, needs_more_evidence, closed |
| RecommendationDraft | pending_review, approved, rejected, expired |

## Events
| Event | Trigger | Result |
|---|---|---|
| case_flagged | risk signal appears | Case becomes new |
| evidence_collected | agent retrieves and summarizes signals | Case becomes evidence_gathered |
| draft_created | agent proposes action | Draft becomes pending_review |
| approval_submitted | RM approves or rejects | ApprovalRecord created |
| audit_written | any material workflow step | AuditEvent appended |

## Permissions
| Actor | Allowed Actions |
|---|---|
| AI Agent | gather evidence, draft recommendation, write proposed rationale |
| RM | approve, reject, request more evidence, close case |
| Compliance Reviewer | inspect audit trail, update policy rule set |
| Demo Viewer | view synthetic scenario and aggregate evaluation results |
