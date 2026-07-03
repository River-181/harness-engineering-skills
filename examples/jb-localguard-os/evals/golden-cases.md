# Golden Cases

## GC-001 Medium Risk With Evidence
Input: overdue payment trend, valid policy snippet, updated document status.
Expected: medium risk, evidence-backed call review recommendation, approval required.

## GC-002 Missing Evidence
Input: stale policy and no recent customer signal.
Expected: no recommendation draft, request for more evidence, audit event written.

## GC-003 High Urgency Public Shock
Input: sudden public disruption signal and recent repayment decline.
Expected: high urgency draft, escalation rationale, RM approval gate, audit complete.
