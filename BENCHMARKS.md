# Benchmarks

This pack is evaluated as an agent delivery tool: artifact shape first, then cross-agent normal form, safety regression, and handoff quality.

## Current Measured Result

```bash
python3 scripts/validate_project.py examples/jb-localguard-os --strict
```

```text
# Harness Validation Report

PASS: project harness shape looks complete.
```

## Benchmark 1 - Artifact Shape

Input: messy financial AI Agent product concept.

Expected:

- `harness.yaml`
- `CLAUDE.md`
- `docs/00` through `docs/12`
- `docs/01_business-model.md`
- `rules/*.md`
- `evals/*.md`

Current flagship example: PASS.

## Benchmark 2 - Normal Form Across Agents

Run the same input through multiple agents with this pack and compare:

- file paths
- section headings
- domain terms
- feature names
- state names
- eval cases
- risk gate coverage

Use:

```bash
python3 scripts/compare_normal_form.py run_a run_b run_c
```

Current status: protocol exists; multi-agent score not yet published.

## Benchmark 3 - Safety Regression

High-risk customer action input should produce escalation/approval, not autonomous execution.

Current flagship example includes:

- human approval gate
- audit log
- fail-closed policy guard
- synthetic data boundary

## Benchmark 4 - Handoff Test

A new maintainer should be able to validate the example using only `docs/12_handoff.md`.

Current status: command is present and validator passes.
