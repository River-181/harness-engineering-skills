# Failure Modes

| ID | Failure Mode | Detection | Mitigation |
|---|---|---|---|
| FM-001 | Recommendation without evidence | Rubric grounding check | Block draft |
| FM-002 | Approval gate bypass | Flow test | Fail closed and write audit event |
| FM-003 | Stale policy rule | Data freshness check | Request compliance review |
| FM-004 | Overconfident risk label | Confidence review | Lower confidence and ask for RM review |
