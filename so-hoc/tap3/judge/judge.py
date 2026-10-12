#!/usr/bin/env python3
"""Chấm thật mọi cách làm của Tập 3 trên bộ test theo subtask.
- Sinh test bằng tgen/chX.py (cố định hạt giống), đáp án lấy từ lời giải mẫu đã kiểm chứng ở ../tap2/sol.
- Subtask, giới hạn thời gian và bộ nhớ lấy trực tiếp từ đề bài Tập 2 (build/probs.js).
- Mỗi chương trình chạy với giới hạn thời gian của đề, ngăn xếp 8 MB, bộ nhớ theo đề.
- Một subtask được trọn điểm khi qua mọi test của nó.
Cách dùng: python3 judge.py [MÃ_BÀI ...]"""
import os, sys, json, glob, random, subprocess, resource, time, importlib
sys.set_int_max_str_digits(10**7)
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
CODE = os.path.join(ROOT, 'code'); TESTS = os.path.join(ROOT, 'tests'); BIN = os.path.join(ROOT, 'bin')
REF = os.path.join(ROOT, '..', 'tap2', 'sol')
sys.path.insert(0, os.path.join(ROOT, 'tgen'))
os.makedirs(BIN, exist_ok=True)
PROBS = json.loads(subprocess.run(['node', os.path.join(ROOT, 'build', 'probs.js')], capture_output=True, text=True, check=True).stdout)
SPEC = {}
for m in ['ch1', 'ch2', 'ch3', 'ch4', 'ch5']:
    if not os.path.exists(os.path.join(ROOT, 'tgen', m + '.py')): continue
    try: mod = importlib.import_module(m)
    except Exception as e: print('bỏ qua tgen', m, e); continue
    for code, sp in mod.SPEC.items():
        pr = PROBS[code]
        sp = dict(sp, mod=m, subtasks=pr['subtasks'], tl=pr['tl'], mem=pr['mem'])
        assert len(sp['ntests']) == len(sp['subtasks']), (code, 'số subtask không khớp đề')
        SPEC[code] = sp

def compile_(src):
    exe = os.path.join(BIN, os.path.basename(src)[:-4])
    if not os.path.exists(exe) or os.path.getmtime(exe) < os.path.getmtime(src):
        r = subprocess.run(['g++', '-O2', '-std=c++14', '-o', exe, src], capture_output=True, text=True)
        if r.returncode: print(r.stderr); raise SystemExit('lỗi biên dịch ' + src)
    return exe

def limits(mem):
    def f():
        resource.setrlimit(resource.RLIMIT_STACK, (8 << 20, 8 << 20))
        resource.setrlimit(resource.RLIMIT_AS, ((mem + 16) << 20, (mem + 16) << 20))
    return f

def run(exe, inp, tl, mem):
    t = time.time()
    try:
        r = subprocess.run([exe], stdin=open(inp), capture_output=True, timeout=tl * 1.0 + 0.05, preexec_fn=limits(mem), cwd=BIN)
    except subprocess.TimeoutExpired:
        return 'TLE', None, tl
    dt = time.time() - t
    if r.returncode != 0: return 'RTE', None, dt
    if dt > tl: return 'TLE', None, dt
    return 'OK', r.stdout.decode(), dt

def make_tests(code, sp):
    d = os.path.join(TESTS, code); os.makedirs(d, exist_ok=True)
    stamp = os.path.join(d, '.ok')
    files = []
    for s, nt in enumerate(sp['ntests'], 1):
        for i in range(1, nt + 1): files.append((s, os.path.join(d, f'st{s}_{i}.inp')))
    gsrc = os.path.join(ROOT, 'tgen', sp['mod'] + '.py')
    if os.path.exists(stamp) and os.path.getmtime(stamp) > os.path.getmtime(gsrc): return files
    ref = compile_(os.path.join(REF, code + '.cpp'))
    for s, f in files:
        i = int(f.split('_')[-1][:-4])
        r = random.Random(f'{code}-{s}-{i}')
        open(f, 'w').write(sp['gen'](s, i, r))
        st, out, _ = run(ref, f, 20, 2048)
        assert st == 'OK', (code, f, st)
        open(f[:-4] + '.ans', 'w').write(out)
    open(stamp, 'w').write('ok')
    return files

def judge(code):
    sp = SPEC[code]; files = make_tests(code, sp)
    res = {}
    for src in sorted(glob.glob(os.path.join(CODE, code + '.cpp')) + glob.glob(os.path.join(CODE, code + '_*.cpp'))):
        name = os.path.basename(src)[:-4]; exe = compile_(src)
        ok = [True] * len(sp['subtasks']); worst = [0.0] * len(sp['subtasks']); verdicts = []
        for s, f in files:
            st, out, dt = run(exe, f, sp['tl'], sp['mem'])
            worst[s - 1] = max(worst[s - 1], dt)
            if st == 'OK':
                ans = open(f[:-4] + '.ans').read()
                good = (sp['check'](open(f).read(), out, ans, s) if sp.get('stcheck') else sp['check'](open(f).read(), out, ans)) if sp.get('check') else out.split() == ans.split()
                st = 'AC' if good else 'WA'
            verdicts.append(f'{os.path.basename(f)[:-4]}:{st}')
            if st != 'AC': ok[s - 1] = False
        pts = [p if o else 0 for p, o in zip(sp['subtasks'], ok)]
        res[name] = {'points': pts, 'total': sum(pts), 'time': [round(x, 2) for x in worst], 'verdicts': verdicts}
        print(f'{name:28s} {pts} = {sum(pts):3d}   t={res[name]["time"]}')
    return res

if __name__ == '__main__':
    import fcntl
    want = sys.argv[1:] or list(SPEC)
    out = os.path.join(ROOT, 'judge', 'scores.json')
    for c in want:
        res = judge(c)
        # ghi ngay sau mỗi bài, có khóa tệp: nhiều tiến trình chấm song song không ghi đè lên nhau
        with open(out + '.lock', 'w') as lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
            allres = json.load(open(out)) if os.path.exists(out) else {}
            allres[c] = res
            tmp = out + '.tmp'; json.dump(allres, open(tmp, 'w'), ensure_ascii=False, indent=1); os.replace(tmp, out)
