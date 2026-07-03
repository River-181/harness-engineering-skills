# Failure Modes

| Failure Mode | Example | Detection | Mitigation | Owner | Eval Case |
|---|---|---|---|---|---|
| Hallucinated evidence | Agent invents source | Evidence check | Require source metadata | Product/AI | |
| Automation bias | Human rubber-stamps output | Approval analytics | Reviewer rubric | Ops | |
| Missing change log | Feature changed but not recorded | Harness validation | Release gate | PM | |
| Scope creep | MVP includes non-demoable future feature | PRD review | Non-goals and scope gate | PM | |
| Unsafe auto-action | Customer action executes without approval | Flow/risk audit | Approval gate | Engineering | |
