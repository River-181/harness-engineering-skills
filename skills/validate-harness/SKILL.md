---
name: validate-harness
description: Use before implementation, submission, demo, handoff, or public release. Validates the current project harness for required files, sections, placeholders, traceability, gates, risk disclosures, and readiness.
argument-hint: "[project-root]"
---
# Validate Harness

## Use when

- Before coding begins
- Before final submission/demo
- After major changes
- When user asks “is this ready?”

## Do not use when

- User asks for new artifact creation and no validation needed

## Inputs to inspect

- Project root
- harness.yaml
- docs/rules/evals
- Repo config files

## Files to create or update

- Validation report
- Optional updates to quality gates if user permits

## Operating sequence

1. Check required files.
2. Check headings and placeholders.
3. Check traceability problem→feature→flow→eval.
4. Check high-risk approval/audit/fail-closed coverage.
5. Check change log if feature scope changed.
6. Check handoff and run commands.
7. Return PASS/WARN/FAIL with fixes.

## Optional Script

Ask before running:

```bash
python3 ${CLAUDE_SKILL_DIR}/../../scripts/validate_project.py . --strict
```

## Report Shape

```markdown
| Area | Status | Evidence | Fix |
```

Status labels: PASS, WARN, FAIL.

## Quality gates

- A file existing is not enough; content shape matters.
- Failed tests or missing evals are not hidden.
- Production-ready and demo-ready are separate statuses.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:validate-harness

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
