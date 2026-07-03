#!/usr/bin/env python3
"""Scaffold Harness Engineering artifacts into a project root."""
from __future__ import annotations
import argparse
import shutil
from pathlib import Path
from datetime import date


def copy_if_missing(src: Path, dst: Path, overwrite: bool = False) -> str:
    dst.parent.mkdir(parents=True, exist_ok=True)
    existed = dst.exists()
    if existed and not overwrite:
        return 'exists'
    shutil.copyfile(src, dst)
    return 'updated' if existed else 'created'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('target', nargs='?', default='.')
    parser.add_argument('--profile', default='generic', choices=['generic', 'jb-finai', 'financial-ai', 'internal-tool'])
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()

    plugin_root = Path(__file__).resolve().parents[1]
    templates = plugin_root / 'templates'
    target = Path(args.target).resolve()
    target.mkdir(parents=True, exist_ok=True)

    results = []
    for rel in ['harness.yaml', 'project-CLAUDE.md']:
        src = templates / rel
        dst = target / ('CLAUDE.md' if rel == 'project-CLAUDE.md' else rel)
        status = copy_if_missing(src, dst, args.overwrite)
        results.append((str(dst.relative_to(target)), status))

    for sub in ['docs', 'rules', 'evals']:
        for src in (templates / sub).glob('*'):
            dst = target / sub / src.name
            status = copy_if_missing(src, dst, args.overwrite)
            results.append((str(dst.relative_to(target)), status))

    # Add lightweight profile marker
    profile_note = target / 'docs' / '00_source-log.md'
    if profile_note.exists():
        txt = profile_note.read_text(encoding='utf-8')
        marker = f"\n\n## Harness Profile\n\n- Profile: {args.profile}\n- Scaffolded: {date.today().isoformat()}\n"
        if '## Harness Profile' not in txt:
            profile_note.write_text(txt.rstrip() + marker, encoding='utf-8')

    print('# Scaffold Result')
    for rel, status in results:
        print(f'- {status}: {rel}')
    print(f'\nProfile: {args.profile}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
