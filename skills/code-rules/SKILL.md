---
name: code-rules
description: Use before asking coding agents to implement features, especially when outputs must converge across Claude, Codex, Gemini, or human maintainers. Creates deterministic code-generation rules for naming, imports, exports, folders, APIs, UI states, tests, lint gates, and PR gates.
argument-hint: "[stack-or-feature]"
---
# Code Harness Rules

## Use when

- Need consistent code from multiple agents
- Repo has naming/folder drift
- Implementation is about to start
- Handoff to human maintainers matters

## Do not use when

- Tiny throwaway script with no maintenance value

## Inputs to inspect

- Domain definitions
- Architecture
- Existing repo tree
- package/config files
- Team conventions

## Files to create or update

- `rules/naming-rules.md`
- `rules/import-export-rules.md`
- `rules/ui-rules.md`
- `rules/data-rules.md`
- `rules/agent-rules.md`
- Optional lint/test config suggestions

## Operating sequence

1. Inspect stack and existing conventions.
2. Extract canonical domain terms.
3. Define folder boundaries.
4. Define route/component/function/type naming.
5. Define import/export and dependency boundaries.
6. Define UI states and error states.
7. Define data/API schema rules.
8. Define required checks before completion.
9. Add compatibility mode if existing repo conflicts.

## Deterministic Code Rule Ladder

1. Reuse existing conventions if coherent.
2. If inconsistent, define canonical names from domain definitions.
3. Turn naming into examples and forbidden patterns.
4. Turn module boundaries into import rules.
5. Turn completion claims into executable checks.
6. Record tradeoffs in change log.

## Required Check Block

```markdown
## Required checks before completion
- Type check:
- Lint:
- Unit tests:
- Smoke test:
- Eval:
```

## Model Convergence Rule

If two agents could reasonably create different file names for the same feature, add a rule before implementation.

## Quality gates

- Rules are specific enough to reject code.
- Commands are not invented without inspecting repo.
- Human maintainability wins over clever generation.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:code-rules

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
