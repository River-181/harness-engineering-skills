# JB LocalGuard OS Example

This is the flagship Harness Engineering example for a financial AI Agent MVP. It demonstrates the full path from messy product intent to business model, delivery artifacts, risk controls, eval gates, and handoff package.

## Artifact Tree
```text
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

## Validate
```bash
python3 ../../scripts/validate_project.py . --strict
```

The expected result is a successful Harness Validation Report with no missing required artifacts.
