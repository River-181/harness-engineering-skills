# 06 PRD

## 1. Product Summary
JB LocalGuard OS is a financial AI Agent MVP that helps relationship managers review risky local-business customer cases through evidence-backed recommendation drafts, approval gates, and audit logs.

## 2. Users and Jobs
| User | Job |
|---|---|
| Relationship Manager | Review a flagged customer case quickly and safely |
| Compliance Reviewer | Confirm the workflow preserves policy and audit requirements |
| Competition Judge | See a working AI workflow with measurable safety controls |

## 3. Problem Statement
Risk review is slow and inconsistent when evidence, policy, and recommended actions live across separate systems. AI can help, but only if it remains reviewable and controlled.

## 4. Goals
- Reduce RM triage time in demo cases.
- Make every recommendation evidence-backed.
- Require approval before action.
- Produce audit logs and evaluation results.

## 5. Non-Goals
- Real credit decision automation.
- Customer outreach automation.
- Production banking integration in the MVP.

## 6. Success Metrics
| Metric | Target |
|---|---|
| Golden case pass rate | 3 of 3 in demo |
| Recommendations with evidence | 100 percent |
| Customer-facing actions without approval | 0 |
| Audit events per case | at least 4 |

## 7. Core Features
| Feature | Description | Acceptance Criteria |
|---|---|---|
| Case Intake | Load a synthetic flagged case | Case shows signals and owner |
| Evidence Pack | Gather and summarize case evidence | Evidence includes source and freshness |
| Recommendation Draft | Generate next-action draft | Includes rationale, confidence, and risk controls |
| Approval Gate | RM approves, rejects, or asks for evidence | No action is final before approval |
| Audit Log | Record workflow events | Log includes actor, event, timestamp |
| Eval Dashboard | Show golden case result | Displays pass/fail and reviewer notes |
