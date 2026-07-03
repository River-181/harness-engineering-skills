# Import / Export Rules

## Import Groups

1. platform/runtime,
2. framework,
3. third-party,
4. internal aliases,
5. relative.

## Boundary Rules

- Do not import feature internals across feature boundaries.
- Export only public feature APIs through `index` files.
- No circular dependencies.
- No hidden side effects on import.
- Domain logic must not live in UI-only helpers.

## Completion Gate

A feature is not complete until boundary violations are resolved or explicitly waived.
