# Principle Patterns

Good principle:

> Every customer-facing action must pass an explicit approval gate.

Enforced by:

- state machine,
- UI button disabled state,
- backend route guard,
- audit event.

Reject if:

- a path sends a customer message without approval.
