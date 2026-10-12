#!/usr/bin/env python3
"""Biên dịch mọi lời giải mẫu sol/*.cpp (C++14) vào bin/. Lỗi biên dịch được báo nhưng không dừng các tệp khác."""
import glob, os, subprocess, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
os.makedirs(os.path.join(ROOT, 'bin'), exist_ok=True)
bad = 0
for src in sorted(glob.glob(os.path.join(ROOT, 'sol', '*.cpp'))):
    exe = os.path.join(ROOT, 'bin', os.path.basename(src)[:-4])
    if os.path.exists(exe) and os.path.getmtime(exe) >= os.path.getmtime(src): continue
    r = subprocess.run(['g++', '-O2', '-std=c++14', '-o', exe, src], capture_output=True, text=True)
    if r.returncode: bad += 1; print('LỖI BIÊN DỊCH', src, '\n', r.stderr[:2000])
print('ok' if not bad else f'{bad} tệp lỗi')
