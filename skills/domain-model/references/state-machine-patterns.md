# State Machine Patterns

## Generic case lifecycle

New → Triaged → EvidenceGathering → Judged → Drafted → PendingApproval → Approved → Executed → Monitored → Closed

Branches:

- NeedsMoreEvidence
- Rejected
- Escalated
- Failed

Every high-risk transition should write an audit event.
