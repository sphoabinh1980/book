#!/usr/bin/env python3
"""Đối chiếu các chương trình của cùng một bài trên test ngẫu nhiên nhỏ.
Cách dùng: python3 verify/run.py [CODE ...] [-n 300]
Mỗi bài khai báo trong verify/chN.py: SPEC[CODE] = {'gen': hàm(rng) -> input, 'progs': [tên chương trình], 'brute': hàm(input) -> output (tùy chọn)}"""
import glob, importlib, os, random, subprocess, sys
sys.set_int_max_str_digits(10**7)
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..'); sys.path.insert(0, HERE)
SPEC = {}
for f in sorted(glob.glob(os.path.join(HERE, 'ch*.py'))):
    try: SPEC.update(importlib.import_module(os.path.basename(f)[:-3]).SPEC)
    except Exception as e: print('bỏ qua', f, e)
args = sys.argv[1:]; N = 300
if '-n' in args: i = args.index('-n'); N = int(args[i + 1]); del args[i:i + 2]
print(subprocess.run([sys.executable, os.path.join(ROOT, 'build', 'run_examples.py')], capture_output=True, text=True).stdout.strip())
bad = 0
for code in args or sorted(SPEC):
    sp = SPEC[code]; progs = [code] + [p for p in sp.get('progs', []) if p != code]
    r = random.Random(12345)
    for t in range(sp.get('n', N)):
        inp = sp['gen'](r)
        outs = {}
        for p in progs:
            res = subprocess.run([os.path.join(ROOT, 'bin', p)], input=inp, capture_output=True, text=True, timeout=20)
            outs[p] = res.stdout.split()
        if 'brute' in sp: outs['brute'] = sp['brute'](inp).split()
        ref = outs[code]
        diff = [p for p, o in outs.items() if o != ref]
        if diff:
            bad += 1; print('SAI', code, diff, '\n--- input:\n' + inp[:500], '\n--- out:', {p: ' '.join(o)[:200] for p, o in outs.items()}); break
    else: print('OK ', code, len(progs), 'chương trình', sp.get('n', N), 'test')
sys.exit(1 if bad else 0)
