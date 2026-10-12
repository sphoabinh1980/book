# Kiểm tra các chương trình của Chương 3. SỐ HỌC ĐỒNG DƯ
from math import gcd

def is_prime(n):
    if n < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0: return n == p
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True
def rand_prime(r, lo, hi):
    while True:
        p = r.randint(lo, hi)
        if is_prime(p): return p
BIG = 10**18

# ---------------- Bài 9: LUYTHUA
def pick_m(r):
    return r.choice([1, 1, 2, 7, 1000, 10**9 + 7, r.randint(1, 100), r.randint(1, 10**9),
                     r.randint(1, BIG), r.randint(BIG - 1000, BIG), BIG, 999999999999999989])
def pick_a(r):
    return r.choice([0, 1, 2, r.randint(0, 100), r.randint(0, BIG), BIG, BIG - 1])
def gen_LUYTHUA(r):      # b nhỏ để chương trình ngây thơ chạy kịp
    b = r.choice([0, 1, 2, 3, r.randint(0, 64), r.randint(0, 5000), r.randint(0, 200000)])
    return f'{pick_a(r)} {b} {pick_m(r)}\n'
def gen_LUYTHUA_lon(r):  # b tới 10^18: chỉ các cách nhanh và Python
    b = r.choice([0, 1, r.randint(0, BIG), BIG, 2**59 - 1, 2**59, r.randint(0, 10**9)])
    return f'{pick_a(r)} {b} {pick_m(r)}\n'
def brute_LUYTHUA(inp):
    a, b, m = map(int, inp.split()); return str(pow(a, b, m))

# ---------------- Bài 10: CHIAMOD
def gen_chiamod(r, p):
    q = r.randint(1, 8); rows = []
    for _ in range(q):
        a = r.choice([0, 1, p - 1, p, r.randint(0, 1000), r.randint(0, BIG), BIG])
        while True:
            b = r.choice([1, p - 1, p + 1, r.randint(1, 1000), r.randint(1, BIG), BIG])
            if b % p: break
        rows.append(f'{a} {b}')
    return f'{q} {p}\n' + '\n'.join(rows) + '\n'
def gen_CHIAMOD(r):      # p nhỏ để cách thử x chạy kịp
    return gen_chiamod(r, r.choice([2, 3, 5, 7, 11, 13, rand_prime(r, 2, 1000), rand_prime(r, 2, 200000)]))
def gen_CHIAMOD_lon(r):
    return gen_chiamod(r, r.choice([2, 10**9 + 7, 10**9 + 9, 998244353, 2147483647, 1999999973,
                                    rand_prime(r, 2, 2 * 10**9)]))
def brute_CHIAMOD(inp):
    t = inp.split(); q, p = int(t[0]), int(t[1]); out = []
    for i in range(q):
        a, b = int(t[2 + 2 * i]), int(t[3 + 2 * i]); out.append(str(a * pow(b, p - 2, p) % p))
    return '\n'.join(out)
def gen_NGHICHDAO(r):
    n = r.choice([1, 2, r.randint(1, 50), r.randint(1, 2000)])
    p = r.choice([rand_prime(r, n + 1, 3 * n + 10), 10**9 + 7, 998244353, rand_prime(r, n + 1, 2 * 10**9)])
    return f'{n} {p}\n'
def brute_NGHICHDAO(inp):
    n, p = map(int, inp.split()); return ' '.join(str(pow(i, p - 2, p)) for i in range(1, n + 1))

# ---------------- Bài 11: PHIEULER
def phi_py(n):
    res, p = n, 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0: n //= p
            res -= res // p
        p += 1
    if n > 1: res -= res // n
    return res
def gen_PHIEULER(r):     # n vừa phải để chương trình ngây thơ chạy kịp
    c = r.randint(0, 7)
    if c == 0: n = r.choice([1, 2, 3, 4, 6, 12, 360, 1024, 2310, 30030, 510510, 999983])
    elif c == 1: n = rand_prime(r, 2, 2 * 10**6)
    elif c == 2: p = rand_prime(r, 2, 1400); n = p * p
    elif c == 3: n = 2 * rand_prime(r, 2, 10**6)
    elif c == 4: n = 2**r.randint(0, 21)
    else: n = r.randint(1, r.choice([100, 10**4, 2 * 10**6]))
    return f'{n}\n'
def brute_PHIEULER(inp): return str(phi_py(int(inp)))
def gen_SANGPHI(r): return f'{r.choice([1, 2, 12, r.randint(1, 100), r.randint(1, 3000)])}\n'
def brute_SANGPHI(inp): return ' '.join(str(phi_py(i)) for i in range(1, int(inp) + 1))
def gen_THAPLT(r):
    p = r.choice([2, 3, 5, 7, 13, 1000000007, rand_prime(r, 2, 100), rand_prime(r, 2, 2 * 10**9)])
    a = r.choice([0, 1, p, 2 * p, p - 1, r.randint(0, 100), r.randint(0, BIG)])
    b = r.choice([1, 2, p - 1, p, r.randint(1, 60)]) if p < 100 else r.choice([1, 2, r.randint(1, 60)])
    c = r.randint(1, 6) if b > 1 else r.randint(1, BIG)
    return f'{a} {b} {c} {p}\n'
def brute_THAPLT(inp):
    a, b, c, p = map(int, inp.split()); return str(pow(a, b**c, p))

# ---------------- Bài 12: CRT
def crt_py(eq):
    r, M = 0, 1
    for a, m in eq:
        g = gcd(M, m)
        if (a - r) % g: return -1
        m2 = m // g
        t = (a - r) // g * pow(M // g, -1, m2) % m2 if m2 > 1 else 0
        r, M = r + M * t, M * m2
    return r
def lcm_all(ms):
    L = 1
    for m in ms: L = L // gcd(L, m) * m
    return L
def fmt_crt(eq): return f'{len(eq)}\n' + '\n'.join(f'{a} {m}' for a, m in eq) + '\n'
def gen_CRT(r):          # bội chung nhỏ (hoặc m1 lớn) để cách ngây thơ chạy kịp
    while True:
        k = r.randint(1, r.choice([2, 3, 5, 10]))
        c = r.randint(0, 4)
        if c == 0: ms = [r.randint(1, 12) for _ in range(k)]
        elif c == 1: ms = [r.choice([1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 30, 36, 60]) for _ in range(k)]
        elif c == 2:
            base = r.randint(1, 10**9 // 60); ms = [base * r.choice([1, 2, 3, 4, 5, 6, 10, 12, 60])]
            ms += [ms[0] // r.choice([1, 2, 3]) if ms[0] % 6 == 0 else r.randint(1, 30) for _ in range(k - 1)]
        elif c == 3: ms = [r.randint(1, 1000) for _ in range(min(k, 3))]
        else: ms = [r.randint(1, 10**9)] + [r.randint(1, 50) for _ in range(k - 1)]
        if lcm_all(ms) // ms[0] <= 3 * 10**5: break
    x = r.randint(0, lcm_all(ms) - 1)
    eq = [(x % m, m) for m in ms]
    if r.random() < 0.45:  # làm hỏng một phương trình: thường thành vô nghiệm
        i = r.randrange(len(ms)); eq[i] = (r.randint(0, ms[i] - 1), ms[i])
    return fmt_crt(eq)
def gen_CRT_tontu(r):    # đôi một nguyên tố cùng nhau, tích ≤ 10^18
    while True:
        k = r.randint(1, 10); lim = r.choice([10, 1000, 10**9])
        ms = []
        for _ in range(k):
            m = r.randint(1, lim)
            if all(gcd(m, q) == 1 for q in ms): ms.append(m)
        if r.random() < 0.3: ms = [10**9, 999999999][:k] if k <= 2 else ms
        L = 1
        for m in ms: L *= m
        if L <= BIG: break
    return fmt_crt([(r.randint(0, m - 1), m) for m in ms])
def brute_CRT(inp):
    t = list(map(int, inp.split())); k = t[0]
    return str(crt_py([(t[1 + 2 * i], t[2 + 2 * i]) for i in range(k)]))

SPEC = {
    'LUYTHUA': {'gen': gen_LUYTHUA, 'progs': ['LUYTHUA_ngaytho', 'LUYTHUA_dequy', 'LUYTHUA_ando'], 'brute': brute_LUYTHUA},
    'LUYTHUA_dequy': {'gen': gen_LUYTHUA_lon, 'progs': ['LUYTHUA', 'LUYTHUA_ando'], 'brute': brute_LUYTHUA},
    'CHIAMOD': {'gen': gen_CHIAMOD, 'progs': ['CHIAMOD_ngaytho', 'CHIAMOD_euclid'], 'brute': brute_CHIAMOD},
    'CHIAMOD_euclid': {'gen': gen_CHIAMOD_lon, 'progs': ['CHIAMOD'], 'brute': brute_CHIAMOD},
    'CHIAMOD_1n': {'gen': gen_NGHICHDAO, 'brute': brute_NGHICHDAO},
    'PHIEULER': {'gen': gen_PHIEULER, 'progs': ['PHIEULER_ngaytho'], 'brute': brute_PHIEULER},
    'PHIEULER_sang': {'gen': gen_SANGPHI, 'brute': brute_SANGPHI},
    'PHIEULER_mu': {'gen': gen_THAPLT, 'brute': brute_THAPLT},
    'CRT': {'gen': gen_CRT, 'progs': ['CRT_ngaytho'], 'brute': brute_CRT},
    'CRT_tontu': {'gen': gen_CRT_tontu, 'progs': ['CRT'], 'brute': brute_CRT},
}
