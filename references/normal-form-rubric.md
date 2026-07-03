# Normal Form Rubric

A harness output is in normal form when different agents can produce compatible artifacts from the same input.

## Score 0 — Loose prose

- No fixed filenames.
- No schema.
- No required sections.
- Same concept appears under different names.
- No validation gate.

## Score 1 — Structured document

- Sections exist.
- Some names are stable.
- Missing traceability from problem to feature to eval.

## Score 2 — Harnessed artifact

- Fixed file path.
- Required sections.
- Definitions table.
- Traceability table.
- Acceptance criteria.
- Known risks.

## Score 3 — Executable normal form

- Schema or script validation.
- Lint/test/eval command.
- Golden cases.
- Change history.
- Handoff status.

Minimum release bar: score 2 for docs, score 3 for rules/evals before claiming repeatability.
