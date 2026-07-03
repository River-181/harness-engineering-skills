# 01 Business Model

## Artifact Metadata
- Owner: River
- Last updated: 2026-07-03
- Business stage: MVP
- Confidence: medium

## Judge-Facing Thesis
JB LocalGuard OS gives relationship managers a safer and faster way to review local-business customer risk by combining banking signals, public context, policy constraints, and human approval into one auditable recommendation flow. The defensibility comes from trusted financial workflow integration, risk controls, and local-business data interpretation rather than a generic chatbot.

## DDBM 11 Blocks
| Block | Product-Specific Answer | Evidence | Confidence |
|---|---|---|---|
| Mission | Help financial institutions protect customers and local merchants through early risk detection and responsible intervention. | Competition brief and financial AI use case | Medium |
| Key Partners | Bank RM teams, compliance reviewers, data governance, local business support partners. | Operating model | Medium |
| Key Activities | Gather signals, classify risk, generate evidence-backed action draft, get approval, log outcome. | Demo flow | High |
| Key Data | Synthetic account status, repayment trend, document status, public news snippets, policy rules. | Example data design | Medium |
| Key Enablers | LLM reasoning, retrieval, rules engine, audit log, approval UI, eval dashboard. | Architecture | High |
| Key Barriers | Data permission, compliance review, workflow adoption, trust in recommendations. | Risk register | High |
| Value Proposition | RM reviews risky cases faster with clearer evidence and lower operational risk. | PRD | High |
| Benefits | Faster triage, better consistency, auditable decisions, safer customer contact. | Eval plan | High |
| Negative Impacts | Privacy exposure, biased prioritization, over-trust in AI, incorrect urgency. | Risk linkage | High |
| Costs | LLM/API cost per case, data integration, compliance review, RM training, monitoring. | Cost model | Medium |
| Revenues | Enterprise SaaS license, per-seat RM add-on, implementation service, risk workflow module. | Commercial model | Medium |

## Key Data Inventory
| Data-ID | Data Asset | Source | Permission / Consent Basis | Freshness | Quality Risk | Fallback |
|---|---|---|---|---|---|---|
| DATA-001 | Repayment trend | Core banking mock | Contractual banking operation | Daily | Missing transactions | Mark unavailable and lower confidence |
| DATA-002 | Document status | CRM mock | Operational workflow | Real-time | Stale status | Ask RM to confirm |
| DATA-003 | Policy rules | Internal policy mock | Internal approved policy | Release-based | Outdated rule | Block recommendation until reviewed |
| DATA-004 | Public context snippet | Curated public source mock | Public information | Daily | Irrelevant article | Require citation and reviewer check |

## Barrier and Risk Linkage
| Risk-ID | DDBM Source Block | Risk / Negative Impact | Mitigation | Owner | Review Gate |
|---|---|---|---|---|---|
| RISK-PRIVACY-001 | Negative Impacts | Sensitive customer context exposure | Redaction and synthetic demo data | Compliance | pre-demo |
| RISK-BIAS-001 | Negative Impacts | Risk score may prioritize vulnerable merchants unfairly | Human review and explainability rubric | AI lead | eval review |
| RISK-ACTION-001 | Key Activities | Draft could be treated as automatic action | Approval gate and fail-closed workflow | Product | release gate |

## Cost and Revenue Units
| Unit | Assumption | Value | Evidence | Sensitivity |
|---|---|---|---|---|
| API/data cost per active case | One retrieval and one reasoning pass | 100-500 KRW equivalent | MVP estimate | Medium |
| Monthly operating cost | Small pilot for RM team | under 1M KRW equivalent | MVP estimate | Medium |
| Revenue per branch/team | SaaS module subscription | pilot-priced enterprise package | Market assumption | High |
| Gross margin driver | Reusable workflow and low marginal inference cost | improves with case volume | SaaS logic | Medium |

## Open Questions
| ID | Question | Why It Matters | Default Assumption | Owner |
|---|---|---|---|---|
| Q-BM-001 | Which buyer owns budget: risk, branch operations, or digital innovation? | Changes pitch and pricing | Digital innovation sponsor | Founder |

## Definition of Done
- [x] All 11 DDBM blocks are filled.
- [x] `Key Data` includes permission, freshness, and fallback.
- [x] Negative impacts map to `Risk-ID` rows.
- [x] Costs and revenues use measurable units.
- [x] Judge-facing thesis is specific and evidence-backed.
