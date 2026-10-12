# Chương 1: sinh test, vét cạn, test lớn
import random as _r
def ints(s): return list(map(int, s.split()))

# ---------- 1.1 NGAYTHU
def gen_NGAYTHU(r):
    q = r.randint(1, 8); s = f'{q}\n'
    for _ in range(q):
        k = r.choice([r.randint(-30, 30), r.randint(-10**18, 10**18), 0, 7 * r.randint(-10**17, 10**17)])
        s += f'{r.randint(2, 8)} {k}\n'
    return s
def brute_NGAYTHU(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        t, k = v[1 + 2 * i], v[2 + 2 * i]
        out.append(str((t - 2 + k) % 7 + 2))       # Python: % luôn không âm
    return '\n'.join(out)
def big_NGAYTHU(r):
    q = 10**5
    return f'{q}\n' + ''.join(f'{r.randint(2, 8)} {r.randint(-10**18, 10**18)}\n' for _ in range(q))

# ---------- 1.2 CHUSOCUOI
def gen_CHUSOCUOI(r):
    T = r.randint(1, 5); s = f'{T}\n'
    for _ in range(T):
        a = r.choice([r.randint(0, 20), r.randint(0, 10**30)]); b = r.choice([0, 1, r.randint(0, 50), r.randint(0, 10**30)])
        s += f'{a} {b}\n'
    return s
def brute_CHUSOCUOI(inp):
    v = ints(inp); return '\n'.join(str(pow(v[1 + 2 * i], v[2 + 2 * i], 10)) for i in range(v[0]))
def big_CHUSOCUOI(r):
    T = 10
    return f'{T}\n' + ''.join(str(r.randint(1, 9)) + ''.join(str(r.randint(0, 9)) for _ in range(10**5 - 1)) + ' ' + str(r.randint(1, 9)) + ''.join(str(r.randint(0, 9)) for _ in range(10**5 - 1)) + '\n' for _ in range(T))

# ---------- 1.3 VIETLIEN
def gen_VIETLIEN(r):
    return f'{r.choice([r.randint(1, 12), r.randint(1, 3000)])} {r.choice([1, 2, 7, 10, 1000, r.randint(1, 10**9)])}\n'
def brute_VIETLIEN(inp):
    n, m = ints(inp); return str(int(''.join(map(str, range(1, n + 1)))) % m)
def big_VIETLIEN(r): return f'10000000 {r.randint(10**8, 10**9)}\n'

# ---------- 2.1 XEPHANG
def gen_XEPHANG(r):
    T = r.randint(1, 6); s = f'{T}\n'
    for _ in range(T):
        n = r.choice([r.randint(1, 12), r.randint(1, 3000), r.randint(2, 60) ** 2, r.choice([1, 2, 3, 4, 6, 9, 97, 101, 1024, 4096]),
                      r.randint(1, 10**5)])
        s += f'{n}\n'
    return s
def brute_XEPHANG(inp):
    v = ints(inp); out = []
    for n in v[1:1 + v[0]]:
        ways = [(rr, n // rr) for rr in range(1, n + 1) if n % rr == 0 and rr >= 2 and n // rr >= 2]
        if not ways: out.append('0'); continue
        rr, c = min((w for w in ways if w[0] <= w[1]), key=lambda w: w[1] - w[0])
        out.append(f'{len(ways)} {rr} {c}')
    return '\n'.join(out)
def big_XEPHANG(r):
    ns = [10**12, 999999999989, 999966000289, 963761198400] + [r.randint(9 * 10**11, 10**12) for _ in range(6)]
    return '10\n' + ''.join(f'{n}\n' for n in ns)

# ---------- 2.2 UOCTANG
def gen_UOCTANG(r):
    n = r.choice([1, r.randint(1, 50), r.randint(1, 10**4), r.choice([36, 60, 97, 360, 5040, 65536, 720720]), r.randint(2, 300) ** 2])
    q = r.randint(1, 8)
    xs = [r.choice([1, n, n + 1, r.randint(1, n + 3), r.randint(1, 10**12), max(1, n - r.randint(0, 3))]) for _ in range(q)]
    return f'{n} {q}\n' + ' '.join(map(str, xs)) + '\n'
def brute_UOCTANG(inp):
    v = ints(inp); n, q = v[0], v[1]
    dv = [d for d in range(1, n + 1) if n % d == 0]
    out = [str(len(dv)), ' '.join(map(str, dv))]
    for x in v[2:2 + q]: out.append(str(next((d for d in dv if d >= x), -1)))
    return '\n'.join(out)
def big_UOCTANG(r):
    n = [963761198400, 999999999989, 10**12][r.randint(0, 2)]; q = 10**5
    return f'{n} {q}\n' + ' '.join(str(r.randint(1, 10**12)) for _ in range(q)) + '\n'

# ---------- 2.3 BANBE
TL_BANBE = 2.0
def gen_BANBE(r):
    N = r.choice([r.randint(1, 30), r.randint(1, 3000), r.randint(200, 3000)])
    k = r.choice([0, 0, 1, 2, r.randint(0, 20), r.randint(0, N), r.randint(0, 10**7)])
    return f'{N} {k}\n'
def brute_BANBE(inp):
    N, k = ints(inp)
    def sp(x):                                     # tổng ước thực sự, thử ước tới √x
        t, d = 0, 1
        while d * d <= x:
            if x % d == 0: t += d + (x // d if d * d != x else 0)
            d += 1
        return t - x
    s = [0] + [sp(x) for x in range(1, N + 1)]
    P = [(a, b) for a in range(1, N + 1) for b in [s[a] - k] if a < b <= N and s[b] - k == a]
    return '\n'.join([str(len(P))] + [f'{a} {b}' for a, b in P])
def big_BANBE(r): return f'10000000 {r.choice([0, 1, r.randint(0, 1000)])}\n'

# ---------- 3.1 CATGACH
def gen_CATGACH(r):
    T = r.randint(1, 6); s = f'{T}\n'
    for _ in range(T):
        g = r.choice([1, r.randint(1, 20), r.randint(1, 10**9)])
        a = g * r.randint(1, 10**18 // g); b = g * r.randint(1, 10**18 // g)
        a, b = r.choice([(a, b), (r.randint(1, 30), r.randint(1, 30)), (a, a), (1, b), (10**18, 10**18 - 1), (10**18, 10**18)])
        s += f'{a} {b}\n'
    return s
def brute_CATGACH(inp):
    import math
    v = ints(inp); out = []
    for i in range(v[0]):
        a, b = v[1 + 2 * i], v[2 + 2 * i]
        g = max(d for d in range(1, min(a, b) + 1) if a % d == 0 and b % d == 0) if min(a, b) <= 1000 else math.gcd(a, b)
        out.append(f'{g} {(a * b) // (g * g)}')
    return '\n'.join(out)
def big_CATGACH(r):
    T = 10**5
    return f'{T}\n' + ''.join(f'{r.randint(1, 10**18)} {r.randint(1, 10**18)}\n' for _ in range(T))

# ---------- 3.2 BOMOTSO
def gen_BOMOTSO(r):
    n = r.randint(2, 8); g = r.choice([1, 2, 6, r.randint(1, 10**6), r.randint(1, 10**17)])
    a = [g * r.choice([1, 2, 3, 5, r.randint(1, 30), r.randint(1, 10**18 // g)]) for _ in range(n)]
    if r.random() < 0.3: a[r.randrange(n)] = r.randint(1, 10**18)
    if r.random() < 0.2: a = [a[0]] * n
    return f'{n}\n' + ' '.join(map(str, a)) + '\n'
def brute_BOMOTSO(inp):
    from math import gcd
    from functools import reduce
    v = ints(inp); n, a = v[0], v[1:]
    best = max(range(n), key=lambda i: (reduce(gcd, a[:i] + a[i + 1:]), -i))
    return f'{reduce(gcd, a[:best] + a[best + 1:])} {best + 1}'
def big_BOMOTSO(r):
    n = 5 * 10**5; g = r.randint(1, 10**6)
    a = [g * r.randint(1, 10**18 // g) for _ in range(n)]; a[r.randrange(n)] = r.randint(1, 10**18)
    return f'{n}\n' + ' '.join(map(str, a)) + '\n'

# ---------- 3.3 DENNHAY
def gen_DENNHAY(r):
    n = r.randint(1, 8)
    mode = r.randint(0, 3)
    if mode == 0: t = [r.randint(1, 12) for _ in range(n)]
    elif mode == 1: t = [r.choice([10**9, 10**18, 999999999989, 2, 5, 10**6, r.randint(1, 10**18)]) for _ in range(n)]
    elif mode == 2: t = [r.choice([2, 3, 5, 7, 11, 13, 4, 9]) ** r.randint(1, 18) for _ in range(n)]
    else: t = [2 ** r.randint(0, 60) for _ in range(n)]
    t = [min(x, 10**18) for x in t]
    q = r.randint(1, 8); qs = []
    for _ in range(q):
        l = r.randint(1, n); qs.append((l, r.randint(l, n)))
    return f'{n} {q}\n' + ' '.join(map(str, t)) + '\n' + ''.join(f'{l} {rr}\n' for l, rr in qs)
def brute_DENNHAY(inp):
    from math import lcm
    v = ints(inp); n, q = v[0], v[1]; t = v[2:2 + n]; out = []
    for i in range(q):
        l, rr = v[2 + n + 2 * i], v[3 + n + 2 * i]
        x = lcm(*t[l - 1:rr]); out.append(str(x if x <= 10**18 else -1))
    return '\n'.join(out)
def big_DENNHAY(r):
    n = q = 2 * 10**5; P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    t = [r.choice(P) ** r.randint(1, 3) if r.random() < 0.9 else r.randint(1, 10**18) for _ in range(n)]
    qs = []
    for _ in range(q):
        l = r.randint(1, n); qs.append(f'{l} {min(n, l + r.randint(0, 200))}\n' if r.random() < 0.7 else f'{l} {r.randint(l, n)}\n')
    return f'{n} {q}\n' + ' '.join(map(str, t)) + '\n' + ''.join(qs)

# ---------- 4.1 DONGNUOC
def gen_DONGNUOC(r):
    n = r.randint(1, 3); g = r.choice([1, 1, 2, 3, 6])
    a = [g * r.randint(1, 20 // g + 1) for _ in range(n)]
    q = r.randint(1, 6); cs = [r.choice([0, r.randint(0, 60), a[0], g, g + 1]) for _ in range(q)]
    return f'{n} {q}\n' + ' '.join(map(str, a)) + '\n' + ' '.join(map(str, cs)) + '\n'
def brute_DONGNUOC(inp):
    v = ints(inp); n, q = v[0], v[1]; a = v[2:2 + n]; cs = v[2 + n:2 + n + q]
    S = sum(a) * 3; lo, hi = -S, max(cs) + S         # BFS: đổ vào (+a) hoặc múc ra (−a)
    seen = {0}; st = [0]
    while st:
        x = st.pop()
        for d in a:
            for y in (x + d, x - d):
                if lo <= y <= hi and y not in seen: seen.add(y); st.append(y)
    return '\n'.join([str(min(x for x in seen if x > 0))] + ['CO' if c in seen else 'KHONG' for c in cs])
def big_DONGNUOC(r):
    n = q = 10**5; g = r.randint(1, 10**6)
    a = [g * r.randint(1, 10**18 // g) for _ in range(n)]
    return f'{n} {q}\n' + ' '.join(map(str, a)) + '\n' + ' '.join(str(r.randint(0, 10**18)) for _ in range(q)) + '\n'

# ---------- 4.2 MUAHANG
def gen_MUAHANG(r):
    Q = r.randint(1, 6); s = f'{Q}\n'
    for _ in range(Q):
        m = r.randint(0, 4)
        if m == 0: a, b, c = r.randint(1, 20), r.randint(1, 20), r.randint(0, 300)
        elif m == 1: g = r.randint(1, 50); a, b = g * r.randint(1, 30), g * r.randint(1, 30); c = r.choice([g * r.randint(0, 3000), r.randint(0, 10**5)])
        elif m == 2: a, b = r.randint(10**8, 10**9), r.randint(10**8, 10**9); c = r.randint(0, 10**13)
        elif m == 3: a, b = r.randint(1, 10**5), r.randint(1, 10**9); c = r.choice([r.randint(0, 10**18), 10**18])
        else: a, b, c = r.choice([(1, 1, 10**18), (10**9, 10**9, 10**18), (999999937, 99991, 10**18), (2, 4, 10**18 - 1)])
        if r.random() < 0.5: a, b = b, a
        s += f'{a} {b} {c}\n'
    return s
def brute_MUAHANG(inp):
    from math import gcd
    v = ints(inp); out = []
    for i in range(v[0]):
        a, b, c = v[1 + 3 * i:4 + 3 * i]
        if a < b: a, b = b, a                       # a là giá lớn hơn: x chạy tới c // a
        if c // a <= 10**5: out.append(str(sum(1 for x in range(c // a + 1) if (c - a * x) % b == 0))); continue
        P = b // gcd(a, b)                          # (c − a·x) mod b tuần hoàn theo x với chu kì P
        x0 = next((x for x in range(P) if (c - a * x) % b == 0), None)
        out.append(str(0 if x0 is None or x0 > c // a else (c // a - x0) // P + 1))
    return '\n'.join(out)
def big_MUAHANG(r):
    Q = 10**5
    return f'{Q}\n' + ''.join(f'{r.randint(1, 10**9)} {r.randint(1, 10**9)} {r.randint(0, 10**18)}\n' for _ in range(Q))

# ---------- 4.3 DONGHO
def gen_DONGHO(r):
    Q = r.randint(1, 6); s = f'{Q}\n'
    for _ in range(Q):
        m = r.choice([1, 2, 12, 60, r.randint(1, 40), r.randint(1, 2000)])
        p, q = r.randrange(m), r.randrange(m); a, b = r.randrange(m), r.randrange(m)
        if r.random() < 0.15: b = a
        if r.random() < 0.15: q = p
        T = r.choice([0, r.randint(0, 100), r.randint(0, 10**18), 10**18])
        s += f'{m} {p} {a} {q} {b} {T}\n'
    return s
def brute_DONGHO(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        m, p, a, q, b, T = v[1 + 6 * i:7 + 6 * i]
        S = [t for t in range(m) if (p + a * t) % m == (q + b * t) % m]   # vị trí lặp lại sau m giây
        out.append(f'{S[0]} {sum((T - t) // m + 1 for t in S if t <= T)}' if S else '-1 0')
    return '\n'.join(out)
def big_DONGHO(r):
    Q = 10**5; s = f'{Q}\n'
    for _ in range(Q):
        m = r.randint(1, 10**18)
        s += f'{m} {r.randrange(m)} {r.randrange(m)} {r.randrange(m)} {r.randrange(m)} {r.randint(0, 10**18)}\n'
    return s
