# Kiểm tra các chương trình của Chương 1
def ints(s): return list(map(int, s.split()))

def gen_SODU(r):
    L = r.choice([1, 2, 5, 18, 19, 25, 300, 5000])
    s = str(r.randint(1, 9)) + ''.join(str(r.randint(0, 9)) for _ in range(L - 1)) if r.random() < 0.95 else '0'
    m = r.choice([1, 2, 7, 10, r.randint(1, 1000), r.randint(1, 10**9), 10**9])
    return f'{s}\n{m}\n'
def brute_SODU(inp):
    s, m = inp.split(); return str(int(s) % int(m))

import math
def gen_DEMUOC(r):
    t = r.random()
    if t < 0.2: n = r.choice([1, 2, 3, 4, 36, 49, 64, 720720, 999983, 10**6])
    elif t < 0.4: n = r.randint(1, 100) ** 2
    else: n = r.randint(1, 10**6)
    return f'{n}\n'
def brute_DEMUOC(inp):
    n = int(inp); ds = [d for d in range(1, n + 1) if n % d == 0]
    return f'{len(ds)} {sum(ds)}'

def gen_UCLN(r):
    t = r.random()
    if t < 0.3: a, b = r.randint(1, 10**5), r.randint(1, 10**5)
    elif t < 0.6: g = r.randint(1, 1000); a, b = g * r.randint(1, 1000), g * r.randint(1, 1000)
    else: a, b = r.randint(1, 10**6), r.randint(1, 10**18)
    if r.random() < 0.5: a, b = b, a
    return f'{a} {b}\n'
def brute_UCLN(inp):
    a, b = map(int, inp.split()); g = math.gcd(a, b); l = a // g * b
    return f'{g} {l if l <= 10**18 else -1}'

def gen_PTNGUYEN(r):
    q = 20; s = f'{q}\n'
    for _ in range(q):
        a, b = r.randint(1, 3000), r.randint(1, 3000)
        if r.random() < 0.3: g = r.randint(2, 50); a, b = a * g, b * g
        c = r.choice([r.randint(-10**6, 10**6), r.randint(-10**18, 10**18), 0, math.gcd(a, b) * r.randint(-10**9, 10**9)])
        s += f'{a} {b} {c}\n'
    return s
def brute_PTNGUYEN(inp):
    v = list(map(int, inp.split())); out = []
    for i in range(v[0]):
        a, b, c = v[1 + 3 * i: 4 + 3 * i]; g = math.gcd(a, b)
        if c % g: out.append('-1'); continue
        bg = b // g; x = (c // g) * pow(a // g, -1, bg) % bg if bg > 1 else 0
        out.append(f'{x} {(c - a * x) // b}')
    return ' '.join(out)

SPEC = {
    'SODU': {'gen': gen_SODU, 'brute': brute_SODU},
    'DEMUOC': {'gen': gen_DEMUOC, 'progs': ['DEMUOC_ngaytho'], 'brute': brute_DEMUOC, 'n': 200},
    'UCLN': {'gen': gen_UCLN, 'progs': ['UCLN_ngaytho'], 'brute': brute_UCLN},
    'PTNGUYEN': {'gen': gen_PTNGUYEN, 'progs': ['PTNGUYEN_ngaytho'], 'brute': brute_PTNGUYEN},
}
