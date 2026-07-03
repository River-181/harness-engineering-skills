# 07 Architecture

## Components
| Component | Responsibility |
|---|---|
| Demo Case Store | Holds synthetic customer cases and signals |
| Retrieval Layer | Selects relevant signals and policy snippets |
| Agent Reasoner | Produces evidence summary and recommendation draft |
| Policy Guard | Blocks unsupported or unsafe recommendations |
| Approval UI | Lets RM approve, reject, or request more evidence |
| Audit Logger | Records immutable workflow events |
| Eval Runner | Runs golden cases and collects pass/fail results |

## Data Flow
1. RM opens a flagged case.
2. Retrieval Layer fetches synthetic signals and policy snippets.
3. Agent Reasoner creates an Evidence Pack and Recommendation Draft.
4. Policy Guard checks allowed action, confidence, and required evidence.
5. Approval UI asks RM to decide.
6. Audit Logger writes each material event.
7. Eval Runner compares the output against golden case expectations.

## Security and Trust Boundaries
- Synthetic demo data stays inside the local example.
- Agent Reasoner cannot write approved actions.
- Approval UI is the only component that can create an ApprovalRecord.
- Audit Logger receives append-only events.
- Policy Guard fails closed when policy data is missing.

## Demo-vs-Production Separation
The demo uses local fixtures and mock policy data. Production would require bank-approved data access, identity controls, encryption, retention policy, and compliance review.
