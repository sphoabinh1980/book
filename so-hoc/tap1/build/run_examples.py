#!/usr/bin/env python3
"""Biên dịch mọi chương trình trong code/ (vào bin/) và sinh output cho examples/CODE/k.inp bằng lời giải mẫu bin/CODE."""
import glob, os, subprocess, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
os.makedirs(os.path.join(ROOT, 'bin'), exist_ok=True)
def compile_(src):
    exe = os.path.join(ROOT, 'bin', os.path.basename(src)[:-4])
    if not os.path.exists(exe) or os.path.getmtime(exe) < os.path.getmtime(src):
        r = subprocess.run(['g++', '-O2', '-std=c++14', '-o', exe, src], capture_output=True, text=True)
        if r.returncode: print('LỖI BIÊN DỊCH', src, '\n', r.stderr[:2000]); return None
    return exe
for src in sorted(glob.glob(os.path.join(ROOT, 'code', '*.cpp'))): compile_(src)
for d in sorted(glob.glob(os.path.join(ROOT, 'examples', '*'))):
    code = os.path.basename(d); exe = os.path.join(ROOT, 'bin', code)
    if not os.path.exists(exe): print('THIẾU chương trình', code); continue
    for f in sorted(glob.glob(os.path.join(d, '*.inp'))):
        r = subprocess.run([exe], stdin=open(f), capture_output=True, text=True, timeout=10)
        if r.returncode: print('LỖI CHẠY', f, r.stderr[:500]); continue
        open(f[:-4] + '.out', 'w').write(r.stdout)
print('ok')
