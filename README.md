# Harness Engineering Skills

Vague enterprise conversations -> deterministic artifacts, business-model checks, executable rules, eval gates, risk controls, and handoff packages.

This is a Claude Code plugin for teams using AI agents to move from messy product intent to reviewable delivery artifacts. It is not an autonomous deployment system. It creates the normal form that makes implementation, evaluation, demo, and handoff safer.

See [End-to-End Delivery Workflow](WORKFLOW.md) for the combined DDBM -> Harness Engineering -> SDD -> Evidence -> Demo/Pitch lifecycle, including feedback and revision loops.

## What You Get

```text
messy input
  -> source log
  -> meeting log
  -> DDBM business model
  -> CPS
  -> principles and definitions
  -> domain model
  -> PRD / feature spec
  -> architecture / agent loop
  -> deterministic code rules
  -> evals
  -> risk controls
  -> demo and handoff
```

## Install With Claude Code

From the repository root:

```bash
claude --plugin-dir .
```

Or install into your local Claude skills directory:

```bash
./scripts/install.sh
```

Then use:

```text
/harness-engineering:route
```

## Core Commands

| Command | Use it for |
|---|---|
| `/harness-engineering:route` | Decide the next skill and artifact order. |
| `/harness-engineering:init-project` | Scaffold harness files. |
| `/harness-engineering:intake-log` | Normalize raw notes/transcripts. |
| `/harness-engineering:ddbm-business-model` | Build the 11-block data-driven business model. |
| `/harness-engineering:cps-framing` | Context -> Problem -> Solution. |
| `/harness-engineering:domain-model` | Entities, states, events, permissions. |
| `/harness-engineering:prd-spec` | PRD and feature specs. |
| `/harness-engineering:architecture` | Components, dataflow, boundaries. |
| `/harness-engineering:agent-loop` | Judgment -> action -> verification loops. |
| `/harness-engineering:code-rules` | Deterministic code-generation rules. |
| `/harness-engineering:eval-design` | Golden cases, rubrics, regression. |
| `/harness-engineering:risk-compliance` | Privacy/security/approval/audit controls. |
| `/harness-engineering:demo-handoff` | Demo script, runbook, handoff. |
| `/harness-engineering:validate-harness` | Readiness validation. |
| `/harness-engineering:jb-finai-adapter` | JB Fin:AI scorecard alignment. |

## Flagship Example

The first complete example is a financial AI Agent MVP:

```text
examples/jb-localguard-os/
  harness.yaml
  CLAUDE.md
  docs/00_source-log.md
  docs/01_meeting-log.md
  docs/01_business-model.md
  docs/02_cps.md
  docs/03_principles.md
  docs/04_definitions.md
  docs/05_domain-model.md
  docs/06_prd.md
  docs/07_architecture.md
  docs/08_feature-spec.md
  docs/09_flow.md
  docs/10_eval-plan.md
  docs/11_change-log.md
  docs/12_handoff.md
  rules/*.md
  evals/*.md
  validation-report.md
```

Validate it:

```bash
python3 scripts/validate_project.py examples/jb-localguard-os --strict
```

Current result:

```text
# Harness Validation Report

PASS: project harness shape looks complete.
```

## DDBM Layer

The `ddbm-business-model` skill adds 11 business blocks before the PRD:

```text
Mission, Key Partners, Key Activities, Key Data, Key Enablers,
Key Barriers, Value Proposition, Benefits, Negative Impacts,
Costs, Revenues
```

For high-risk products, `Negative Impacts` should map to stable `Risk-ID` rows so business risk, compliance risk, evals, and demo controls stay traceable.

## Validate The Pack

```bash
python3 scripts/validate_pack.py --strict
python3 scripts/validate_project.py examples/jb-localguard-os --strict
```

## Security Model

- No hooks, MCP servers, background agents, or external network calls by default.
- No customer-facing action should execute without explicit user request and approval.
- Financial and regulated workflows must include evidence, approval, audit logging, and fail-closed behavior.
- Public examples use synthetic data only.

## Roadmap

v0.1 focuses on Claude Code plugin readiness, DDBM minimum integration, and one complete flagship example.

Next releases can add SSD implementation workflow, Codex manifest, GitHub Actions CI, deeper benchmarks, and more examples.
