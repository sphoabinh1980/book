# Đối chiếu lời giải tham khảo (sol/CODE) với chương trình trâu trên test ngẫu nhiên nhỏ.
import sys, random, subprocess, importlib, os
HERE = os.path.dirname(os.path.abspath(__file__))
SOL = os.path.join(HERE, '..', 'sol')
def run(code, inp):
    r = subprocess.run([os.path.join(SOL, code)], input=inp, capture_output=True, text=True, timeout=20, cwd=HERE)
    if r.returncode != 0: raise RuntimeError('crash ' + r.stderr)
    return r.stdout
def main():
    mod, code, n = sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 300
    m = importlib.import_module(mod)
    gen = getattr(m, 'gen_' + code); rng = random.Random(12345)
    chk = getattr(m, 'check_' + code, None); bru = getattr(m, 'brute_' + code, None)
    for t in range(n):
        inp = gen(rng); out = run(code, inp)
        if chk:
            ok, msg = chk(inp, out)
        else:
            exp = bru(inp); ok = exp.split() == out.split(); msg = 'expected ' + exp[:300]
        if not ok:
            print('FAIL', code, 'test', t); print(inp[:1500]); print('got', out[:300]); print(msg); sys.exit(1)
    print('OK', code, n)
if __name__ == '__main__': main()
