#!/usr/bin/env python3
"""Check call-music string coverage without building Android resources."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

RES = Path(__file__).resolve().parents[1] / 'base/app/src/main/res'
KEYS = {'music_during_calls_title', 'music_during_calls_detail'}
LOCALE_DIR = re.compile(r'values-(?:[a-z]{2,3}(?:-r[A-Z]{2})?|b\+[A-Za-z0-9+]+)')


def main():
    folders = sorted(p for p in RES.iterdir() if p.is_dir() and (
        p.name == 'values' or LOCALE_DIR.fullmatch(p.name)))
    errors = []
    for folder in folders:
        counts = dict.fromkeys(KEYS, 0)
        for path in folder.glob('*.xml'):
            for node in ET.parse(path).getroot().findall('string'):
                key = node.get('name')
                if key in KEYS:
                    counts[key] += 1
                    if not ''.join(node.itertext()).strip():
                        errors.append(f'{path}: blank {key}')
        for key, count in sorted(counts.items()):
            if count != 1:
                errors.append(f'{folder.name}: expected one {key}, found {count}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Both call-music strings present in {len(folders)} resource sets (including default)')


if __name__ == '__main__':
    main()
