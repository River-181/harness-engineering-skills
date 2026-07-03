# 00 Source Log

## Artifact Metadata
- Owner: River
- Last updated: 2026-07-03
- Source status: synthetic
- Confidence: medium

## Source
- Type: competition product concept
- Date: 2026-07-03
- Provided by: River
- Scope: financial AI Agent MVP for judging and demo
- Link or location: local example

## Raw Intent
Build a financial AI Agent that helps a relationship manager detect risky local-business customer cases, gather evidence, draft a safe next action, and prove that approval, audit, and evaluation controls exist.

## Explicit Requirements
| ID | Requirement | Source Phrase | Priority | Confidence |
|---|---|---|---|---|
| REQ-001 | Assist RM review of risky cases | financial AI Agent MVP | High | Medium |
| REQ-002 | Require human approval before action | approval gate | High | High |
| REQ-003 | Preserve audit trail | audit log defined | High | High |

## Implied Requirements
| ID | Requirement | Why Implied | Risk if Wrong | Confidence |
|---|---|---|---|---|
| IMP-001 | Use synthetic demo data | Public competition demos should not expose customer data | Privacy breach | High |
| IMP-002 | Explain evidence for each recommendation | Financial decisions need reviewable basis | Low trust | High |

## Unknowns / Ambiguities
| ID | Question | Why It Matters | Default Assumption | Owner |
|---|---|---|---|---|
| Q-001 | Which internal banking signals are available? | Changes model accuracy and compliance | Use synthetic mock signals | Product owner |

## Assumptions Made
| ID | Assumption | Reason | Reversal Cost |
|---|---|---|---|
| ASM-001 | MVP is advisory, not autonomous | Reduces legal and operational risk | Low |

## Source-to-Artifact Trace
| Source Signal | Interpreted As | Artifact Impact | Confidence |
|---|---|---|---|
| high-prize financial competition | judge-facing proof matters | eval and handoff are first-class | High |
| approval gate | human-in-loop required | flow and compliance rules include approval | High |

## Definition of Done
- [x] Raw source identity preserved.
- [x] Explicit and implied requirements separated.
- [x] Assumptions are labeled.
- [x] Open questions are actionable.
