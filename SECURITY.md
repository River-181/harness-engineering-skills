# Security Policy

This plugin is intentionally conservative.

## Default posture

- No hooks are shipped.
- No background monitors are shipped.
- No MCP servers are shipped.
- No automatic network calls are shipped.
- No skill grants broad `allowed-tools` permissions.
- Scripts are deterministic helpers and should be run only after user approval.

## Treat skills as executable influence

A `SKILL.md` file changes agent behavior. Review any third-party modification like you would review executable code.

## For enterprise or financial work

- Do not paste production PII, account data, credit data, secrets, private keys, or regulated customer data into agent sessions.
- Use mock, redacted, synthetic, or tokenized data for demos and evals.
- Keep all customer-facing actions behind an explicit human approval gate.
- Disclose known limitations and failed gates in `docs/12_handoff.md`.

## Reporting issues

Open a private issue or contact the repository owner if you find:

- hidden tool escalation,
- prompt injection vulnerability,
- unsafe script behavior,
- misleading security claims,
- accidental inclusion of private client content.
