#!/usr/bin/env python3
"""Compare multiple harness output directories for normal-form convergence."""
from __future__ import annotations
import sys
from pathlib import Path

CHECK_FILES = [
    'docs/02_cps.md', 'docs/03_principles.md', 'docs/04_definitions.md',
    'docs/05_domain-model.md', 'docs/06_prd.md', 'docs/08_feature-spec.md',
    'docs/09_flow.md', 'docs/10_eval-plan.md'
]


def headings(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {line.strip() for line in path.read_text(encoding='utf-8', errors='ignore').splitlines() if line.startswith('#')}


def main() -> int:
    roots = [Path(arg).resolve() for arg in sys.argv[1:]]
    if len(roots) < 2:
        print('Usage: compare_normal_form.py <run-a> <run-b> [run-c...]')
        return 2
    print('# Normal Form Comparison')
    all_ok = True
    for rel in CHECK_FILES:
        sets = [headings(root / rel) for root in roots]
        union = set().union(*sets)
        inter = set.intersection(*sets) if sets else set()
        score = len(inter) / len(union) if union else 1.0
        status = 'PASS' if score >= 0.8 else 'WARN' if score >= 0.5 else 'FAIL'
        if status == 'FAIL':
            all_ok = False
        print(f'- {status}: {rel} heading overlap {score:.0%}')
    return 0 if all_ok else 1

if __name__ == '__main__':
    raise SystemExit(main())
