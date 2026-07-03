#!/usr/bin/env python3
"""Validate Harness Engineering Skill Pack structure."""
from __future__ import annotations
import argparse, re, sys, json
from pathlib import Path

REQUIRED_SKILL_PHRASES = [
    'Use when',
    'Files to create or update',
    'Operating sequence',
    'Quality gates',
    'Stop conditions',
]

RELEASE_BLOCKED_PATTERNS = [
    'your-org',
    'harness-engineering-skillpack-v0.2',
]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('root', nargs='?', default='.')
    ap.add_argument('--strict', action='store_true')
    args = ap.parse_args()
    root = Path(args.root).resolve()
    errors, warnings = [], []
    for p in root.rglob('.DS_Store'):
        errors.append(f'forbidden macOS metadata file: {p.relative_to(root)}')

    manifest = root/'.claude-plugin/plugin.json'
    if not manifest.exists(): errors.append('missing .claude-plugin/plugin.json')
    else:
        try:
            m=json.loads(manifest.read_text())
            for k in ['name','description','version']:
                if not m.get(k): errors.append(f'manifest missing {k}')
            if 'your-org' in json.dumps(m):
                errors.append('manifest contains your-org placeholder')
        except Exception as e: errors.append(f'manifest invalid json: {e}')
    skills = sorted((root/'skills').glob('*/SKILL.md')) if (root/'skills').exists() else []
    if not skills: errors.append('no skills/*/SKILL.md files')
    for s in skills:
        txt=s.read_text(encoding='utf-8', errors='ignore')
        if not txt.startswith('---'):
            errors.append(f'{s}: missing frontmatter')
        if 'name:' not in txt or 'description:' not in txt:
            errors.append(f'{s}: missing name or description')
        for phrase in REQUIRED_SKILL_PHRASES:
            if phrase not in txt:
                warnings.append(f'{s}: missing section phrase {phrase}')
        if args.strict and '## Universal Completion Report' in txt:
            warnings.append(f'{s}: repeated completion boilerplate should move to references')
    for d in ['templates/docs','templates/rules','templates/evals','references','scripts']:
        if not (root/d).exists(): errors.append(f'missing {d}')
    if args.strict:
        scan_files = [
            p for p in root.rglob('*')
            if p.is_file()
            and '.git' not in p.parts
            and p.relative_to(root).as_posix() != 'scripts/validate_pack.py'
            and p.suffix in {'.md', '.json', '.yaml', '.yml', '.py', '.sh'}
        ]
        for p in scan_files:
            txt = p.read_text(encoding='utf-8', errors='ignore')
            for pattern in RELEASE_BLOCKED_PATTERNS:
                if pattern in txt:
                    errors.append(f'{p.relative_to(root)} contains release-blocked pattern: {pattern}')
    print('# Skill Pack Validation')
    if errors:
        print('\n## Errors'); [print(f'- FAIL: {e}') for e in errors]
    if warnings:
        print('\n## Warnings'); [print(f'- WARN: {w}') for w in warnings]
    if not errors and not warnings: print('\nPASS: package structure and skill depth look valid.')
    elif not errors: print('\nPASS with warnings.')
    else: print('\nFAIL.')
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
