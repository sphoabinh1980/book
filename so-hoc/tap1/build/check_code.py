#!/usr/bin/env python3
"""Kiểm tra mã nguồn in trong sách: mỗi dòng không quá 76 kí tự (để không bị ngắt dòng)."""
import glob, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
bad = 0
for f in sorted(glob.glob(os.path.join(ROOT, 'code', '*.cpp'))):
    for i, ln in enumerate(open(f, encoding='utf8').read().split('\n'), 1):
        if len(ln) > 76: bad += 1; print(f'{os.path.basename(f)}:{i}: {len(ln)} kí tự')
sys.exit(1 if bad else 0)
