#!/usr/bin/env python3
"""Mã nguồn in trong sách (khối code trong content) và lời giải mẫu: mỗi dòng ≤ 100 kí tự với sol/, ≤ 76 với code in sách."""
import glob, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
bad = 0
for f in sorted(glob.glob(os.path.join(ROOT, 'sol', '*.cpp'))):
    for i, ln in enumerate(open(f, encoding='utf8').read().split('\n'), 1):
        if len(ln) > 100: bad += 1; print(f'{os.path.basename(f)}:{i}: {len(ln)} kí tự')
sys.exit(1 if bad else 0)
