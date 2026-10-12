# Chương 5: sinh test, vét cạn, test lớn
import math
from fractions import Fraction
from itertools import combinations
import numpy as _np
def ints(s): return list(map(int, s.split()))

def _bignum(r, L, lead=None):
    d = str(r.randint(1, 9) if lead is None else lead)
    return d + ''.join(str(r.randint(0, 9)) for _ in range(L - 1))

# ---------- 17.1 TONGLON
def gen_TONGLON(r):
    L1, L2 = r.randint(1, 25), r.randint(1, 25)
    a = int(_bignum(r, L1)) * r.choice([1, -1]); b = int(_bignum(r, L2)) * r.choice([1, -1])
    t = r.randint(0, 9)
    if t == 0: b = -a                                              # tổng bằng 0
    elif t == 1: a = 0
    elif t == 2: a, b = 10**L1 - 1, r.choice([1, 10**r.randint(0, 5)])   # dây chuyền nhớ
    elif t == 3: a, b = 10**L1, -r.choice([1, 10**L1 - 1, r.randint(1, 10**L1)])  # dây chuyền mượn
    elif t == 4: a = b = r.choice([a, -a, 0])                      # hai số bằng nhau
    elif t == 5: b = -(a + r.choice([1, -1]))                      # tổng ±1
    return f'{a}\n{b}\n'
def brute_TONGLON(inp):
    a, b = inp.split(); return str(int(a) + int(b))
def big_TONGLON(r):
    a = _bignum(r, 10**5); b = _bignum(r, 10**5)
    return f'{r.choice(["", "-"])}{a}\n{r.choice(["", "-"])}{b}\n'

# ---------- 17.2 LUYTHUALON
def gen_LUYTHUALON(r):
    a = r.choice([0, 1, 2, 10, r.randint(0, 30), r.randint(0, 10**9), 10**9, 10**9 - 1, 999999937])
    b = r.choice([0, 1, 2, r.randint(0, 40), r.randint(0, 400)])
    return f'{a} {b}\n'
def brute_LUYTHUALON(inp):
    a, b = ints(inp); return str(a ** b)
def big_LUYTHUALON(r):
    return f'{r.choice([10**9, 10**9 - 1, r.randint(9 * 10**8, 10**9)])} 10000\n'

# ---------- 17.3 TICHLON
def gen_TICHLON(r):
    a = int(_bignum(r, r.randint(1, 40))) * r.choice([1, -1]); b = int(_bignum(r, r.randint(1, 40))) * r.choice([1, -1])
    t = r.randint(0, 7)
    if t == 0: a = 0
    elif t == 1: b = 0
    elif t == 2: a = 10**r.randint(0, 30) * r.choice([1, -1])
    elif t == 3: a = b = -(10**r.randint(1, 30) - 1)
    elif t == 4: a, b = r.randint(-10**9, 10**9), r.randint(-10**9, 10**9)
    return f'{a}\n{b}\n'
def brute_TICHLON(inp):
    a, b = inp.split(); return str(int(a) * int(b))
def big_TICHLON(r):
    return f'{r.choice(["", "-"])}{_bignum(r, 5 * 10**4)}\n{r.choice(["", "-"])}{_bignum(r, 5 * 10**4)}\n'

# ---------- 18.1 DOICOSO
_DIG = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def _enc(v, b):
    s = ''
    while True:
        s = _DIG[v % b] + s; v //= b
        if v == 0: return s
def _doicoso_line(r, small):
    a, b = r.randint(2, 36), r.randint(2, 36)
    if r.random() < 0.2: a = b = r.randint(2, 36)
    v = r.choice([0, 1, r.randint(0, 100), r.randint(0, 10**18), 10**18, r.randint(0, 2**r.randint(1, 59))]) if small else r.randint(0, 10**18)
    s = _enc(v, a)
    if r.random() < 0.25: s = '0' * r.randint(1, 100 - len(s)) + s     # chữ số 0 thừa ở đầu
    return f'{a} {b} {s}\n'
def gen_DOICOSO(r):
    q = r.randint(1, 6); return f'{q}\n' + ''.join(_doicoso_line(r, True) for _ in range(q))
def brute_DOICOSO(inp):
    t = inp.split(); q = int(t[0]); out = []
    for i in range(q):
        a, b, s = int(t[1 + 3 * i]), int(t[2 + 3 * i]), t[3 + 3 * i]
        out.append(_np.base_repr(int(s, a), b))
    return '\n'.join(out)
def big_DOICOSO(r):
    q = 10**5; s = f'{q}\n'
    for _ in range(q):
        a, b = r.choice([2, 3, r.randint(2, 36)]), r.choice([2, r.randint(2, 36)])
        x = _enc(r.randint(10**17, 10**18), a); s += f'{a} {b} {"0" * (100 - len(x)) + x}\n'
    return s

# ---------- 18.2 BITDOAN
def gen_BITDOAN(r):
    q = r.randint(1, 5); s = f'{q}\n'
    for _ in range(q):
        L = r.choice([1, r.randint(1, 50), r.randint(1, 10**6), r.randint(1, 10**18 - 3000), 2**r.randint(1, 59) - r.randint(0, 1500) + 1,
                      10**18 - r.randint(0, 2000)])
        L = max(L, 1); R = min(10**18, L + r.choice([0, r.randint(0, 20), r.randint(0, 2500)]))
        s += f'{L} {R}\n'
    return s
def brute_BITDOAN(inp):
    v = ints(inp); return '\n'.join(str(sum(bin(x).count('1') for x in range(v[1 + 2 * i], v[2 + 2 * i] + 1))) for i in range(v[0]))
def big_BITDOAN(r):
    q = 10**5; s = f'{q}\n'
    for _ in range(q):
        L, R = sorted((r.randint(1, 10**18), r.randint(1, 10**18))); s += f'{L} {R}\n'
    return s

# ---------- 18.3 KBIT
def _kth_brute(k, m):
    B = k
    while math.comb(B, k) < m: B += 1
    return sorted(sum(1 << p for p in c) for c in combinations(range(B), k))[m - 1]
def gen_KBIT(r):
    q = r.randint(1, 6); s = f'{q}\n'
    for _ in range(q):
        if r.random() < 0.55:
            L = r.choice([0, 0, 1, r.randint(0, 100), r.randint(0, 10**18 - 3000), 2**r.randint(1, 59) - r.randint(0, 1000)])
            L = max(L, 0); R = min(10**18, L + r.choice([0, r.randint(0, 30), r.randint(0, 2000)]))
            k = r.choice([0, 1, r.randint(0, 6), r.randint(0, 60), bin(R).count('1')])
            s += f'1 {L} {R} {k}\n'
        else:
            while True:
                k = r.choice([1, 2, r.randint(1, 5), r.randint(1, 59), r.randint(50, 59)]); m = r.choice([1, 2, r.randint(1, 300)])
                if _kth_brute(k, m) <= 10**18: break
            s += f'2 {k} {m}\n'
    return s
def brute_KBIT(inp):
    t = inp.split('\n'); q = int(t[0]); out = []
    for i in range(1, q + 1):
        v = ints(t[i])
        if v[0] == 1: out.append(str(sum(1 for x in range(v[1], v[2] + 1) if bin(x).count('1') == v[3])))
        else: out.append(str(_kth_brute(v[1], v[2])))
    return '\n'.join(out)
def big_KBIT(r):
    q = 10**5; s = f'{q}\n'
    for _ in range(q):
        if r.random() < 0.5:
            L, R = sorted((r.randint(0, 10**18), r.randint(0, 10**18))); s += f'1 {L} {R} {r.randint(0, 60)}\n'
        else:
            k = r.randint(1, 59); s += f'2 {k} {r.randint(1, math.comb(59, k))}\n'
    return s

# ---------- 19.1 TONG0
def gen_TONG0(r):
    n = r.randint(1, 30); t = r.randint(0, 3)
    if t == 0: a = [r.randint(-3, 3) for _ in range(n)]
    elif t == 1: a = [0] * n
    elif t == 2: a = [r.choice([10**9, -10**9]) for _ in range(n)]
    else: a = [r.randint(-10**9, 10**9) for _ in range(n)]
    return f'{n}\n{" ".join(map(str, a))}\n'
def brute_TONG0(inp):
    v = ints(inp); n, a = v[0], v[1:]
    return str(sum(1 for l in range(n) for r in range(l, n) if sum(a[l:r + 1]) == 0))
def big_TONG0(r):
    n = 10**6
    if r.random() < 0.5: a = [r.randint(-2, 2) for _ in range(n)]
    else: a = [r.choice([10**9, -10**9]) for _ in range(n)]
    return f'{n}\n{" ".join(map(str, a))}\n'

# ---------- 19.2 DOANDAI
def gen_DOANDAI(r):
    n = r.randint(1, 25); k = r.choice([1, 2, 3, r.randint(1, 12), r.randint(1, 10**6)])
    a = [r.choice([r.randint(-9, 9), r.randint(-10**9, 10**9), 0]) for _ in range(n)]
    if r.random() < 0.2: a = [r.choice([1, 2, 4, 5]) for _ in range(n)]
    return f'{n} {k}\n{" ".join(map(str, a))}\n'
def brute_DOANDAI(inp):
    v = ints(inp); n, k, a = v[0], v[1], v[2:]
    best, bl = 0, 0
    for l in range(n):
        for rr in range(l, n):
            if sum(a[l:rr + 1]) % k == 0 and (rr - l + 1 > best or (rr - l + 1 == best and l + 1 < bl)):
                best, bl = rr - l + 1, l + 1
    return '0' if best == 0 else f'{best} {bl}'
def big_DOANDAI(r):
    n = 10**6; k = r.choice([10**6, 999983])
    return f'{n} {k}\n{" ".join(str(r.randint(-10**9, 10**9)) for _ in range(n))}\n'

# ---------- 19.3 HCNCHIAHET
def gen_HCNCHIAHET(r):
    m, n = r.randint(1, 7), r.randint(1, 7); k = r.choice([1, 2, 3, r.randint(1, 10), r.randint(1, 10**6)])
    lo = r.choice([0, -9, -10**9]); hi = r.choice([9, 10**9])
    return f'{m} {n} {k}\n' + ''.join(' '.join(str(r.randint(lo, hi)) for _ in range(n)) + '\n' for _ in range(m))
def brute_HCNCHIAHET(inp):
    v = ints(inp); m, n, k = v[:3]; a = [v[3 + i * n: 3 + (i + 1) * n] for i in range(m)]
    c = 0
    for i1 in range(m):
        for i2 in range(i1, m):
            for j1 in range(n):
                for j2 in range(j1, n):
                    if sum(a[i][j] for i in range(i1, i2 + 1) for j in range(j1, j2 + 1)) % k == 0: c += 1
    return str(c)
def big_HCNCHIAHET(r):
    m = n = 400; k = r.choice([10**6, 999983, 1])
    return f'{m} {n} {k}\n' + ''.join(' '.join(str(r.randint(-10**9, 10**9)) for _ in range(n)) + '\n' for _ in range(m))

# ---------- hình học: tiện ích
def _cr(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def _onseg(p, a, b):
    return _cr(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
def _inter(a, b, c, d):          # hai đoạn [a, b], [c, d] có điểm chung?
    d1, d2, d3, d4 = _cr(c, d, a), _cr(c, d, b), _cr(a, b, c), _cr(a, b, d)
    if ((d1 > 0) != (d2 > 0)) and d1 and d2 and ((d3 > 0) != (d4 > 0)) and d3 and d4: return True
    return _onseg(a, c, d) or _onseg(b, c, d) or _onseg(c, a, b) or _onseg(d, a, b)

# ---------- 20.1 TRONGCAY
def _polyline(r, n, W):
    P = [(r.randint(-W, W), r.randint(-W, W))]
    tries = 0
    while len(P) < n and tries < 2000:
        tries += 1
        if r.random() < 0.3:      # đoạn đứng / ngang / đi thẳng tiếp
            q = r.choice([(P[-1][0], r.randint(-W, W)), (r.randint(-W, W), P[-1][1])])
        else: q = (r.randint(-W, W), r.randint(-W, W))
        a = P[-1]
        if q == a: continue
        if len(P) >= 2:
            d1 = (a[0] - P[-2][0], a[1] - P[-2][1]); d2 = (q[0] - a[0], q[1] - a[1])
            if d1[0] * d2[1] - d1[1] * d2[0] == 0 and d1[0] * d2[0] + d1[1] * d2[1] < 0: continue   # quay ngược
        if any(_inter(P[i], P[i + 1], a, q) for i in range(len(P) - 2)): continue
        P.append(q)
    return P
def gen_TRONGCAY(r):
    W = r.choice([3, 6, 10]); P = _polyline(r, r.randint(2, 7), W)
    if len(P) < 2: P.append((P[0][0] + 1, P[0][1]))
    return f'{len(P)}\n' + ''.join(f'{x} {y}\n' for x, y in P)
def brute_TRONGCAY(inp):
    v = ints(inp); n = v[0]; P = [(v[1 + 2 * i], v[2 + 2 * i]) for i in range(n)]
    S = set()
    for i in range(n - 1):
        a, b = P[i], P[i + 1]
        for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                if _cr(a, b, (x, y)) == 0: S.add((x, y))
    return str(len(S))
def big_TRONGCAY(r):
    n = 10**5; xs = sorted(r.sample(range(-10**9, 10**9 + 1), n))
    return f'{n}\n' + ''.join(f'{x} {r.choice([r.randint(-10**9, 10**9), 0, 10**9])}\n' for x in xs)

# ---------- 20.2 DAGIAC
def _star(r, pts, c):
    """Sắp các điểm theo góc quanh c (c không là điểm nguyên, đã nhân 21); bỏ điểm trùng hướng."""
    def key(p):
        return math.atan2(21 * p[1] - c[1], 21 * p[0] - c[0])
    pts = sorted(set(pts), key=key); out = []
    for p in pts:
        if out:
            u = (21 * out[-1][0] - c[0], 21 * out[-1][1] - c[1]); w = (21 * p[0] - c[0], 21 * p[1] - c[1])
            if u[0] * w[1] - u[1] * w[0] == 0 and u[0] * w[0] + u[1] * w[1] > 0: continue
        out.append(p)
    if len(out) >= 2:
        u = (21 * out[-1][0] - c[0], 21 * out[-1][1] - c[1]); w = (21 * out[0][0] - c[0], 21 * out[0][1] - c[1])
        if u[0] * w[1] - u[1] * w[0] == 0 and u[0] * w[0] + u[1] * w[1] > 0: out.pop()
    return out
def _area2(P): return abs(sum(P[i][0] * P[(i + 1) % len(P)][1] - P[(i + 1) % len(P)][0] * P[i][1] for i in range(len(P))))
def _simple(P):
    n = len(P)
    for i in range(n):
        for j in range(i + 1, n):
            a, b, c, d = P[i], P[(i + 1) % n], P[j], P[(j + 1) % n]
            if j == i + 1 or (i == 0 and j == n - 1):
                sh = b if j == i + 1 else a; o1 = a if j == i + 1 else b; o2 = d if j == i + 1 else c
                if _cr(sh, o1, o2) == 0 and (o1[0] - sh[0]) * (o2[0] - sh[0]) + (o1[1] - sh[1]) * (o2[1] - sh[1]) > 0: return False
            elif _inter(a, b, c, d): return False
    return True
def gen_DAGIAC(r):
    while True:
        W = r.choice([3, 5, 8]); t = r.randint(0, 4)
        if t == 0:
            x1, x2 = sorted(r.sample(range(-W, W + 1), 2)); y1, y2 = sorted(r.sample(range(-W, W + 1), 2))
            P = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        elif t == 1: P = [(r.randint(-W, W), r.randint(-W, W)) for _ in range(3)]
        else:
            c = (21 * r.randint(-W, W - 1) + r.choice([5, 7, 10]), 21 * r.randint(-W, W - 1) + r.choice([3, 8, 11]))
            P = _star(r, [(r.randint(-W, W), r.randint(-W, W)) for _ in range(r.randint(3, 9))], c)
        if r.random() < 0.3 and len(P) >= 3:   # thêm điểm thẳng hàng giữa một cạnh
            i = r.randrange(len(P)); a, b = P[i], P[(i + 1) % len(P)]; g = math.gcd(b[0] - a[0], b[1] - a[1])
            if g >= 2:
                t2 = r.randint(1, g - 1); P.insert(i + 1, (a[0] + (b[0] - a[0]) // g * t2, a[1] + (b[1] - a[1]) // g * t2))
        if len(P) >= 3 and _area2(P) > 0 and _simple(P): break
    if r.random() < 0.5: P = P[::-1]
    k = r.randrange(len(P)); P = P[k:] + P[:k]
    return f'{len(P)}\n' + ''.join(f'{x} {y}\n' for x, y in P)
def _classify(p, P):
    n = len(P)
    for i in range(n):
        if _onseg(p, P[i], P[(i + 1) % n]): return 'B'
    inside = False
    for i in range(n):
        a, b = P[i], P[(i + 1) % n]
        if (a[1] > p[1]) != (b[1] > p[1]):
            xi = a[0] + Fraction((p[1] - a[1]) * (b[0] - a[0]), b[1] - a[1])
            if p[0] < xi: inside = not inside
    return 'I' if inside else 'O'
def brute_DAGIAC(inp):
    v = ints(inp); n = v[0]; P = [(v[1 + 2 * i], v[2 + 2 * i]) for i in range(n)]
    I = B = 0
    for x in range(min(p[0] for p in P), max(p[0] for p in P) + 1):
        for y in range(min(p[1] for p in P), max(p[1] for p in P) + 1):
            c = _classify((x, y), P); I += c == 'I'; B += c == 'B'
    return f'{I} {B}'
def big_DAGIAC(r):
    n = 10**5; D = {}
    while len(D) < n:
        t = r.random() * 2 * math.pi; R = r.uniform(5 * 10**5, 10**6)
        p = (round(R * math.cos(t)), round(R * math.sin(t))); g = math.gcd(*p)
        D.setdefault((p[0] // g, p[1] // g), p)          # mỗi hướng một điểm
    P = sorted(D.values(), key=lambda p: math.atan2(p[1], p[0]))
    return f'{n}\n' + ''.join(f'{x} {y}\n' for x, y in P)

# ---------- 20.3 TAMGIAC
def gen_TAMGIAC(r):
    q = r.randint(1, 4); s = f'{q}\n'
    for _ in range(q):
        while True:
            W = r.choice([2, 5, 9, 10**18]) if r.random() < 0.85 else 10**18
            if W == 10**18 and r.random() < 0.5:
                P = [(r.choice([-W, W, 0, r.randint(-W, W)]), r.choice([-W, W, 0, r.randint(-W, W)])) for _ in range(3)]
            else: P = [(r.randint(-W, W), r.randint(-W, W)) for _ in range(3)]
            if _cr(*P) != 0: break
        s += ''.join(f'{x} {y}\n' for x, y in P)
    return s
def brute_TAMGIAC(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        P = [(v[1 + 6 * i + 2 * j], v[2 + 6 * i + 2 * j]) for j in range(3)]
        xs = [p[0] for p in P]; ys = [p[1] for p in P]
        if max(xs) - min(xs) <= 40 and max(ys) - min(ys) <= 40:     # đếm trực tiếp
            c = 0
            for x in range(min(xs), max(xs) + 1):
                for y in range(min(ys), max(ys) + 1):
                    d = [_cr(P[j], P[(j + 1) % 3], (x, y)) for j in range(3)]
                    if all(t > 0 for t in d) or all(t < 0 for t in d): c += 1
        else:                                                          # tọa độ lớn: Pick bằng số nguyên lớn của Python
            S2 = abs(_cr(*P)); B = sum(math.gcd(P[(j + 1) % 3][0] - P[j][0], P[(j + 1) % 3][1] - P[j][1]) for j in range(3))
            c = (S2 - B + 2) // 2
        out.append(str(c))
    return '\n'.join(out)
def big_TAMGIAC(r):
    q = 10**5; s = f'{q}\n'; W = 10**18
    for _ in range(q):
        P = [(r.randint(-W, W), r.randint(-W, W)) for _ in range(3)]
        s += ''.join(f'{x} {y}\n' for x, y in P)
    return s
