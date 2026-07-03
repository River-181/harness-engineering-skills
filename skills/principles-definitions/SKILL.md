---
name: principles-definitions
description: Use when terms drift, the team needs non-negotiables, or downstream docs/code need consistent names. Defines enforceable project principles, canonical vocabulary, anti-synonyms, and concept hierarchy.
argument-hint: "[domain-or-project]"
---
# Principles and Definitions

## Use when

- Same concept appears under multiple names
- Team needs rules that reject bad outputs
- Domain terms must be shared across UI/API/docs/evals

## Do not use when

- Only a cosmetic wording pass is requested

## Inputs to inspect

- CPS
- Meeting log
- Existing domain language
- Regulatory or organizational constraints

## Files to create or update

- `docs/03_principles.md`
- `docs/04_definitions.md`
- Updates to `rules/naming-rules.md`

## Operating sequence

1. Extract candidate principles from source and risks.
2. Rewrite each principle as an enforceable rule.
3. Add “Reject If” test for every principle.
4. Create definitions table with examples and non-examples.
5. Create anti-synonyms for banned duplicate terms.
6. Propagate canonical terms to naming rules.

## Principle Test

A principle is valid only if it can say “no.”

Bad: “We value trust.”
Good: “Every AI judgment must show evidence, uncertainty, and reviewer action; reject outputs without evidence.”

## Definition Test

Every canonical term must have:

- definition,
- examples,
- non-examples,
- owner,
- downstream usage: UI label, API name, database object, eval case.

## Quality gates

- No principle is merely aspirational.
- No key concept remains with multiple competing names.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:principles-definitions

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
