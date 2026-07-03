# JB LocalGuard OS Example

Use this folder as a complete Harness Engineering example for a financial AI Agent MVP. The agent assists a relationship manager by gathering evidence, judging customer risk, drafting a recommended next action, and requiring human approval before any customer-facing step.

Rules for this example:

- Treat all customer records as synthetic demo data.
- Do not present recommendations as automated financial advice.
- Preserve the approval gate and audit log in every flow.
- Validate the harness with `python3 ../../scripts/validate_project.py . --strict` from this directory.
