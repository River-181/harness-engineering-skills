# Agent Rules

## Required Agent Loop

Every agent capability must declare:

1. trigger,
2. inputs,
3. context sources,
4. judgment output,
5. possible actions,
6. forbidden actions,
7. verification checks,
8. approval/escalation rule,
9. audit event,
10. feedback/eval case.

## Default Safety Posture

When uncertain, prefer asking for more evidence or escalating over executing.

## Forbidden Claims

- Do not call a chatbot flow an agent unless it has judgment, action, and verification/improvement.
- Do not claim a recommendation is evidence-based without source metadata.
- Do not allow high-risk auto-execution unless explicitly approved by project policy.
