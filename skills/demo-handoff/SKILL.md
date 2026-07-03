---
name: demo-handoff
description: Use before presentation, judging, client delivery, sprint closeout, or team handoff. Prepares final demo script, runbook, handoff document, known limitations, change history, maintainer notes, and submission-readiness package.
argument-hint: "[demo-or-release-context]"
---
# Demo and Handoff

## Use when

- Need presentation or live demo
- Need someone else to run the project
- Need final delivery package
- Need change history and known limitations

## Do not use when

- No product flow exists; use flow/agent-loop first

## Inputs to inspect

- PRD
- Feature spec
- Flow
- Architecture
- Eval plan
- Existing README/run commands

## Files to create or update

- `docs/09_flow.md`
- `docs/11_change-log.md`
- `docs/12_handoff.md`
- Optional `docs/demo-script.md`

## Operating sequence

1. Choose one persuasive end-to-end demo.
2. Map every demo step to a real or mock-backed behavior.
3. Separate demo shortcuts from production behavior.
4. Write minute-by-minute script.
5. Document setup/run commands and env vars.
6. Add validation status.
7. Add known limitations and next priorities.
8. Update change log.

## Demo Script Table

```markdown
| Time | Screen/Action | Narration | Evidence Shown | Risk Control Shown | Failure Backup |
```

## Fresh Maintainer Test

A maintainer who did not build the project should be able to:

1. install dependencies,
2. configure env vars,
3. run the demo,
4. identify known limitations,
5. know the next safe change.

## Quality gates

- No “ready” claim without run instructions.
- Known failures are disclosed.
- Change log is updated when scope changed.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:demo-handoff

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
