# Harness Engineering Plugin Development Notes

When maintaining this plugin, preserve these invariants:

1. Skills must make agent output more deterministic, not merely more verbose.
2. Main `SKILL.md` files should route and enforce; templates belong in references.
3. No skill should silently perform broad state-changing actions.
4. Every project-facing artifact must connect to `harness.yaml`.
5. Every financial or regulated workflow must include human approval, audit, and risk disclosure.
6. Validation failures must be reported honestly.
