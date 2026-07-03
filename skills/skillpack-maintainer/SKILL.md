---
name: skillpack-maintainer
description: Use when maintaining or releasing the Harness Engineering Skill Pack itself. Adds skills, tunes trigger descriptions, shrinks or expands playbooks, adds templates/evals, updates scripts, runs audits, and prepares release notes.
argument-hint: "[maintenance-task]"
---
# Skill Pack Maintainer

## Use when

- Editing this plugin
- Adding a new skill
- Preparing public release
- Auditing against OMC/Ponytail-level usefulness

## Do not use when

- Using the pack on an external project; use route instead

## Inputs to inspect

- Skill pack root
- Existing skills/templates/references/scripts
- User feedback

## Files to create or update

- Updated skill pack files
- README/CHANGELOG/ROADMAP updates
- Validation report

## Operating sequence

1. Classify change impact: skill/template/script/reference/example/docs.
2. Update SKILL.md with trigger, inputs, outputs, playbook, gates.
3. Move long material to references.
4. Update README skill map.
5. Add example or eval.
6. Run validate_pack.
7. Update changelog.
8. Report safety impact.

## Skill Acceptance Test

A skill is shippable only if it has:

- precise frontmatter description,
- clear trigger and non-trigger,
- input artifacts,
- output artifacts,
- ordered workflow,
- quality gate,
- stop condition,
- example invocation,
- no unnecessary tool grants.

## Optional Script

```bash
python3 scripts/validate_pack.py . --strict
```

## Quality gates

- No broad tool permission added casually.
- Examples and docs remain in sync.
- Version and changelog updated.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:skillpack-maintainer

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
