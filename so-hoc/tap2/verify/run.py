#!/usr/bin/env python3
"""Kiểm tra lời giải mẫu bin/CODE.
  python3 verify/run.py CODE [CODE...] [-n 300]
Với mỗi bài, verify/chN.py khai báo:
  gen_CODE(rng) -> input nhỏ ngẫu nhiên
  brute_CODE(input) -> output đúng (vét cạn / tính trực tiếp bằng Python), HOẶC check_CODE(input, output) -> (ok, thông báo)
  big_CODE(rng) -> (không bắt buộc) một input cỡ tối đa; chương trình phải chạy xong trong giới hạn thời gian TL_CODE (mặc định 1 giây)
"""
import glob, importlib, os, random, subprocess, sys, time
sys.set_int_max_str_digits(10**7)
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..'); sys.path.insert(0, HERE)
M = {}
for f in sorted(glob.glob(os.path.join(HERE, 'ch*.py'))):
    try:
        mod = importlib.import_module(os.path.basename(f)[:-3])
        for k in dir(mod):
            if k.startswith('gen_'): M[k[4:]] = mod
    except Exception as e: print('bỏ qua', f, e)
args = sys.argv[1:]; N = 300
if '-n' in args: i = args.index('-n'); N = int(args[i + 1]); del args[i:i + 2]
print(subprocess.run([sys.executable, os.path.join(ROOT, 'build', 'compile.py')], capture_output=True, text=True).stdout.strip())
def run(code, inp, tl=20):
    t = time.time(); r = subprocess.run([os.path.join(ROOT, 'bin', code)], input=inp, capture_output=True, text=True, timeout=tl, cwd=HERE)
    if r.returncode: raise RuntimeError(f'{code} lỗi chạy: {r.stderr[:300]}')
    return r.stdout, time.time() - t
bad = 0
for code in args or sorted(M):
    mod = M[code]; gen = getattr(mod, 'gen_' + code); bru = getattr(mod, 'brute_' + code, None); chk = getattr(mod, 'check_' + code, None)
    rng = random.Random(2026); fail = False
    for t in range(N):
        inp = gen(rng); out, _ = run(code, inp)
        if chk: ok, msg = chk(inp, out)
        else: exp = bru(inp); ok = exp.split() == out.split(); msg = 'đúng phải là: ' + exp[:300]
        if not ok:
            bad += 1; fail = True; print('SAI', code, 'test', t, '\n--- input:\n' + inp[:1200], '\n--- output:', out[:300], '\n---', msg); break
    if fail: continue
    perf = ''
    big = getattr(mod, 'big_' + code, None)
    if big:
        tl = getattr(mod, 'TL_' + code, 1.0); worst = 0
        for k in range(getattr(mod, 'NBIG_' + code, 3)):
            inp = big(random.Random(k)); _, dt = run(code, inp, tl=60); worst = max(worst, dt)
        perf = f', test lớn nhất {worst:.2f} s / {tl} s'
        if worst > tl: bad += 1; perf += '  QUÁ THỜI GIAN'
    print('OK ', code, N, 'test' + perf)
sys.exit(1 if bad else 0)
