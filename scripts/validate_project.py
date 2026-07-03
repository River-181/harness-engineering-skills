#!/usr/bin/env python3
"""Validate a project-level Harness Engineering scaffold."""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

REQUIRED = [
    'harness.yaml', 'CLAUDE.md',
    'docs/00_source-log.md', 'docs/01_meeting-log.md', 'docs/02_cps.md',
    'docs/03_principles.md', 'docs/04_definitions.md', 'docs/05_domain-model.md',
    'docs/06_prd.md', 'docs/07_architecture.md', 'docs/08_feature-spec.md',
    'docs/09_flow.md', 'docs/10_eval-plan.md', 'docs/11_change-log.md', 'docs/12_handoff.md',
    'rules/naming-rules.md', 'rules/import-export-rules.md', 'rules/ui-rules.md',
    'rules/data-rules.md', 'rules/agent-rules.md', 'rules/compliance-rules.md',
    'evals/golden-cases.md', 'evals/rubric.md', 'evals/failure-modes.md',
]
REQUIRED_HEADINGS = {
    'docs/02_cps.md': ['## Context','## Problem','## Solution','## Non-Solutions','## Success Evidence'],
    'docs/05_domain-model.md': ['## Entities','## States','## Events','## Permissions'],
    'docs/06_prd.md': ['## 1. Product Summary','## 2. Users and Jobs','## 7. Core Features'],
    'docs/07_architecture.md': ['## Components','## Data Flow','## Security and Trust Boundaries'],
    'docs/08_feature-spec.md': ['## Feature Index','## Feature Template'],
    'docs/09_flow.md': ['## Core Demo Flow','## Flow Table'],
    'docs/10_eval-plan.md': ['## Golden Cases','## Metrics','## Human Review Rubric'],
    'docs/12_handoff.md': ['## What Was Built','## How to Run','## Known Limitations'],
}
PLACEHOLDERS = ['TODO', '<Name>', '<user>', '<capability>', '<outcome>', 'fill with actual commands']

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('root', nargs='?', default='.')
    ap.add_argument('--strict', action='store_true')
    args = ap.parse_args()
    root = Path(args.root).resolve()
    missing, warnings, fails = [], [], []
    for rel in REQUIRED:
        p = root / rel
        if not p.exists():
            missing.append(rel); continue
        txt = p.read_text(encoding='utf-8', errors='ignore')
        if len(txt.strip()) < 80:
            warnings.append(f'{rel}: very short')
        ph = sum(txt.count(x) for x in PLACEHOLDERS)
        if ph > (3 if args.strict else 10):
            warnings.append(f'{rel}: placeholder count {ph}')
    for rel, heads in REQUIRED_HEADINGS.items():
        p = root / rel
        if p.exists():
            txt = p.read_text(encoding='utf-8', errors='ignore')
            for h in heads:
                if h not in txt:
                    fails.append(f'{rel}: missing heading {h}')
    print('# Harness Validation Report')
    if missing:
        print('\n## Missing')
        for x in missing: print(f'- FAIL: {x}')
    if fails:
        print('\n## Shape Failures')
        for x in fails: print(f'- FAIL: {x}')
    if warnings:
        print('\n## Warnings')
        for x in warnings: print(f'- WARN: {x}')
    if not missing and not fails and not warnings:
        print('\nPASS: project harness shape looks complete.')
    elif not missing and not fails:
        print('\nPASS with warnings: artifacts exist but need completion.')
    else:
        print('\nFAIL: missing or malformed required artifacts.')
    return 1 if missing or fails else 0
if __name__ == '__main__':
    raise SystemExit(main())
