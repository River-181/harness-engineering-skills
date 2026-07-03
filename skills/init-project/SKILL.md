---
name: init-project
description: Use at the start of a product, AI Agent, MVP, or enterprise delivery repo, or when a repo lacks harness.yaml, docs, rules, evals, and CLAUDE.md project memory. Creates a complete local harness scaffold.
argument-hint: "[target-path] [--profile generic|jb-finai|financial-ai|internal-tool]"
---
# Initialize Harness Project

## Use when

- New project needs a repeatable agent operating system
- Existing repo has code but no harness artifacts
- Team wants Claude/Codex/Gemini to converge on the same structure

## Do not use when

- Repo already has a mature harness and user asked only for validation

## Inputs to inspect

- Project root
- Existing README/package files
- User-stated domain and stage

## Files to create or update

- `harness.yaml`
- `CLAUDE.md`
- `docs/00_source-log.md` through `docs/12_handoff.md`
- `rules/*.md`
- `evals/*.md`

## Operating sequence

1. Inspect root before writing.
2. Detect profile: generic, jb-finai, financial-ai, internal-tool.
3. Copy missing templates only; do not overwrite unless user requested.
4. Fill obvious project metadata in `harness.yaml`.
5. Add a source log entry recording scaffold date and profile.
6. Run or offer `scripts/validate_project.py`.
7. Report created/existing files.

## Practical Init Modes

### Safe init
Create only missing files. Use this by default.

### Adoption init
If a repo already has docs, create `docs/harness-migration-map.md` mapping old docs to harness artifacts instead of replacing them.

### Competition init
For hackathon/competition projects, prioritize `02_cps`, `08_feature-spec`, `09_flow`, `10_eval-plan`, and `11_change-log`.

## Optional Script
Ask before running:

```bash
python3 ${CLAUDE_SKILL_DIR}/../../scripts/scaffold_project.py . --profile generic
python3 ${CLAUDE_SKILL_DIR}/../../scripts/validate_project.py .
```

## Quality gates

- No user file is overwritten silently.
- The scaffold passes structure validation.
- The generated CLAUDE.md tells future agents how to use the harness.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:init-project

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
