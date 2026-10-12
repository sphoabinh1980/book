# Chương 4: sinh test, vét cạn, test lớn
import math, itertools
def ints(s): return list(map(int, s.split()))
MOD = 10**9 + 7

# ---------- 13.1 CHIAKEO
def gen_CHIAKEO(r):
    q = r.randint(1, 6); s = f'{q}\n'
    for _ in range(q):
        c = r.random()
        if c < 0.6: n, k, t = r.randint(0, 12), r.randint(1, 6), r.choice([0, 0, 1, 1, 2, 3])
        elif c < 0.8: n, k, t = r.randint(0, 10**6), r.randint(1, 10**6), r.choice([0, 1, r.randint(0, 10**6)])
        else: n, k, t = r.randint(0, 10**6), r.choice([1, 10**6, r.randint(1, 10**6)]), r.choice([0, 1, 10**6])
        s += f'{n} {k} {t}\n'
    return s
def brute_CHIAKEO(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        n, k, t = v[1 + 3 * i: 4 + 3 * i]
        if n <= 12 and k <= 6:
            # đếm trực tiếp: thêm từng bạn, ways[s] = số cách phát tổng s kẹo cho các bạn đã xét
            ways = [1] + [0] * n
            for _ in range(k):
                ways = [sum(ways[s - x] for x in range(t, s + 1)) for s in range(n + 1)]
            out.append(ways[n] % MOD)
        else:
            out.append(math.comb(n - k * t + k - 1, k - 1) % MOD if k * t <= n else 0)
    return '\n'.join(map(str, out))
def big_CHIAKEO(r):
    q = 10**5
    return f'{q}\n' + ''.join(f'{r.randint(0, 10**6)} {r.randint(1, 10**6)} {r.choice([0, 0, 1, r.randint(0, 3)])}\n' for _ in range(q))

# ---------- 13.2 DUONGLUOI
def gen_DUONGLUOI(r):
    if r.random() < 0.85: m, n = r.randint(0, 12), r.randint(0, 12)
    else: m, n = r.randint(0, 60), r.randint(0, 60)
    K = r.choice([0, 1, 2, 2, 2])
    cells = [(x, y) for x in range(m + 1) for y in range(n + 1)]
    K = min(K, len(cells)); pts = r.sample(cells, K)
    if K and r.random() < 0.1: pts[0] = r.choice([(0, 0), (m, n)])
    if K == 2 and pts[0] == pts[1]: pts = pts[:1]
    return f'{m} {n} {len(pts)}\n' + ''.join(f'{x} {y}\n' for x, y in pts)
def brute_DUONGLUOI(inp):
    v = ints(inp); m, n, K = v[:3]; bad = {(v[3 + 2 * i], v[4 + 2 * i]) for i in range(K)}
    f = [[0] * (n + 1) for _ in range(m + 1)]
    for x in range(m + 1):
        for y in range(n + 1):
            if (x, y) in bad: continue
            f[x][y] = 1 if x == y == 0 else (f[x - 1][y] if x else 0) + (f[x][y - 1] if y else 0)
    return str(f[m][n] % MOD)
def big_DUONGLUOI(r):
    return f'1000000 1000000 2\n{r.randint(0, 10**6)} {r.randint(0, 10**6)}\n{r.randint(0, 10**6)} {r.randint(0, 10**6)}\n'

# ---------- 13.3 TOHOPLON
_SMALLP = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 97, 101, 997, 1009, 10007, 99991]
def gen_TOHOPLON(r):
    c = r.random()
    if c < 0.3: m = r.choice(_SMALLP)
    elif c < 0.9:
        while True:
            ps = r.sample(_SMALLP, r.randint(1, 4)); m = math.prod(ps)
            if m <= 10**9: break
    else: m = r.choice([1, 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23, 99991 * 99989, 30])
    q = r.randint(1, 6); s = f'{q} {m}\n'
    for _ in range(q):
        n = r.choice([r.randint(0, 30), r.randint(0, 2000), r.randint(0, 2000)])
        k = r.choice([r.randint(0, n), r.randint(0, n), n, 0, n + r.randint(1, 5)])
        s += f'{n} {k}\n'
    return s
def brute_TOHOPLON(inp):
    v = ints(inp); q, m = v[:2]
    return '\n'.join(str(math.comb(v[2 + 2 * i], v[3 + 2 * i]) % m) for i in range(q))
def big_TOHOPLON(r):
    q = 10**5; m = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23
    s = f'{q} {m}\n'
    for _ in range(q):
        n = r.randint(10**17, 10**18); s += f'{n} {r.randint(0, n)}\n'
    return s
TL_TOHOPLON = 1.0

# ---------- 14.1 BOISO
def gen_BOISO(r):
    q = r.randint(1, 5); s = f'{q}\n'
    for _ in range(q):
        if r.random() < 0.6:
            L = r.randint(1, 300); R = r.randint(L, 600)
            a, b, c = (r.randint(1, 30) for _ in range(3))
        else:
            L = r.choice([1, r.randint(1, 10**18 - 3000)]); R = min(10**18, L + r.randint(0, 3000))
            pick = lambda: r.choice([r.randint(1, 50), r.randint(10**9, 10**9 + 100), r.randint(1, 10**18), 10**18, 999999999989])
            a, b, c = pick(), pick(), pick()
        s += f'{L} {R} {a} {b} {c}\n'
    return s
def brute_BOISO(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        L, R, a, b, c = v[1 + 5 * i: 6 + 5 * i]
        out.append(sum(1 for x in range(L, R + 1) if (x % a == 0 or x % b == 0) and x % c))
    return '\n'.join(map(str, out))
def big_BOISO(r):
    q = 10**5; s = f'{q}\n'
    for _ in range(q):
        L = r.randint(1, 10**18); R = r.randint(L, 10**18)
        s += f'{L} {R} {r.randint(1, 10**18)} {r.randint(1, 10**6)} {r.randint(10**9, 10**18)}\n'
    return s

# ---------- 14.2 NTCN
def gen_NTCN(r):
    q = r.randint(1, 5); s = f'{q}\n'
    for _ in range(q):
        n = r.choice([1, r.randint(1, 100), r.randint(1, 10**12), 999999999989, 999983 * 1000003, 200560490130,
                      2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31, 2**39, 30])
        N = r.choice([1, r.randint(1, 3000), r.randint(1, 3000)])
        s += f'{n} {N}\n'
    return s
def brute_NTCN(inp):
    v = ints(inp)
    return '\n'.join(str(sum(1 for x in range(1, v[2 + 2 * i] + 1) if math.gcd(x, v[1 + 2 * i]) == 1)) for i in range(v[0]))
def big_NTCN(r):
    q = 1000; s = f'{q}\n'
    big = [999999999989, 999999999959, 999983 * 1000003, 999979 * 999983]
    return s + ''.join(f'{r.choice(big)} {r.randint(10**11, 10**12)}\n' for _ in range(q))

# ---------- 14.3 TANGQUA
def _der(k): return sum((-1)**j * math.comb(k, j) * math.factorial(k - j) for j in range(k + 1))
def gen_TANGQUA(r):
    c = r.random()
    if c < 0.5: n = r.randint(1, 8); m = r.randint(0, n)
    elif c < 0.8: n = r.choice([r.randint(1, 10**18), MOD + r.randint(0, 10), 2 * MOD + r.randint(0, 5), 10**18]); m = n - r.randint(0, min(n, 12))
    else: n = r.randint(1, 300); m = r.randint(0, n)
    return f'{n} {m}\n'
def brute_TANGQUA(inp):
    n, m = ints(inp)
    if n <= 8:   # liệt kê mọi cách rút quà
        return str(sum(1 for p in itertools.permutations(range(n)) if sum(p[i] == i for i in range(n)) == m) % MOD)
    return str(math.comb(n, m) * _der(n - m) % MOD)
def big_TANGQUA(r): n = 10**18 - r.randint(0, 100); return f'{n} {n - 10**7}\n'

# ---------- 15.1 LATGACH
def _tilings(n):
    # đếm trực tiếp: lát lần lượt ô trống đầu tiên (theo cột) của bảng 2 x n
    full = [[False] * n for _ in range(2)]
    def go():
        for c in range(n):
            for rr in range(2):
                if not full[rr][c]:
                    cnt = 0
                    if rr == 0 and not full[1][c]:          # viên dọc
                        full[0][c] = full[1][c] = True; cnt += go(); full[0][c] = full[1][c] = False
                    if c + 1 < n and not full[rr][c + 1]:   # viên ngang
                        full[rr][c] = full[rr][c + 1] = True; cnt += go(); full[rr][c] = full[rr][c + 1] = False
                    return cnt
        return 1
    return go()
def gen_LATGACH(r):
    T = r.randint(1, 5); return f'{T}\n' + ''.join(f'{r.randint(1, 16)}\n' for _ in range(T))
def brute_LATGACH(inp):
    v = ints(inp); return '\n'.join(str(_tilings(n) % MOD) for n in v[1:1 + v[0]])
def big_LATGACH(r):
    T = 1000; return f'{T}\n' + ''.join(f'{r.randint(10**17, 10**18)}\n' for _ in range(T))

# ---------- 15.2 TRIBO
def gen_TRIBO(r):
    n = r.choice([r.randint(1, 15), r.randint(1, 60), r.randint(1, 2000)])
    K = r.choice([0, r.randint(0, min(n, 5)), r.randint(0, min(n, 30))])
    b = r.sample(range(1, n + 1), K)
    if K and r.random() < 0.15: b[0] = n
    if K >= 3 and r.random() < 0.15: x = r.randint(1, max(1, n - 2)); b = list({*b, x, x + 1, x + 2} & set(range(1, n + 1)))
    return f'{n} {len(b)}\n' + ' '.join(map(str, b)) + '\n'
def brute_TRIBO(inp):
    v = ints(inp); n, K = v[:2]; bad = set(v[2:2 + K])
    f = [0] * (n + 1); f[0] = 1
    for x in range(1, n + 1):
        f[x] = 0 if x in bad else sum(f[x - d] for d in (1, 2, 3) if x - d >= 0)
    return str(f[n] % MOD)
def big_TRIBO(r):
    n = 10**18; K = 10**4
    return f'{n} {K}\n' + ' '.join(map(str, r.sample(range(1, n), K))) + '\n'

# ---------- 15.3 DUONGK
def _matmul(A, B):
    n = len(A); return [[sum(A[i][l] * B[l][j] for l in range(n)) % MOD for j in range(n)] for i in range(n)]
def gen_DUONGK(r):
    n = r.randint(1, 6)
    arcs = [(u, v) for u in range(1, n + 1) for v in range(1, n + 1) if r.random() < r.choice([0.2, 0.4, 0.7])]
    q = r.randint(1, 5); s = f'{n} {len(arcs)} {q}\n' + ''.join(f'{u} {v}\n' for u, v in arcs)
    for _ in range(q):
        K = r.choice([0, 1, r.randint(0, 40), r.randint(0, 10**18)])
        s += f'{r.randint(1, n)} {r.randint(1, n)} {K}\n'
    return s
def brute_DUONGK(inp):
    v = ints(inp); n, m, q = v[:3]; arcs = [(v[3 + 2 * i], v[4 + 2 * i]) for i in range(m)]; p = 3 + 2 * m; out = []
    for i in range(q):
        s, t, K = v[p + 3 * i: p + 3 * i + 3]
        if K <= 40:   # quy hoạch động theo số bước: cnt[u] = số đường đi từ s tới u
            cnt = [0] * (n + 1); cnt[s] = 1
            for _ in range(K):
                nc = [0] * (n + 1)
                for a, b in arcs: nc[b] += cnt[a]
                cnt = nc
            out.append(cnt[t] % MOD)
        else:         # lũy thừa cả ma trận bằng số nguyên lớn của Python
            A = [[0] * n for _ in range(n)]
            for a, b in arcs: A[a - 1][b - 1] = 1
            R = [[int(i == j) for j in range(n)] for i in range(n)]
            while K:
                if K & 1: R = _matmul(R, A)
                A = _matmul(A, A); K >>= 1
            out.append(R[s - 1][t - 1])
    return '\n'.join(map(str, out))
def big_DUONGK(r):
    n = 50; q = 1000
    arcs = [(u, v) for u in range(1, n + 1) for v in range(1, n + 1)]
    return f'{n} {len(arcs)} {q}\n' + ''.join(f'{u} {v}\n' for u, v in arcs) + \
        ''.join(f'{r.randint(1, n)} {r.randint(1, n)} {r.choice([10**18, 2**59 - 1, r.randint(1, 10**18)])}\n' for _ in range(q))

# ---------- 16.1 TONGSIGMA
def gen_TONGSIGMA(r): return f'{r.choice([1, 2, r.randint(1, 50), r.randint(1, 1500)])}\n'
def brute_TONGSIGMA(inp):
    n = int(inp); return str(sum(d for x in range(1, n + 1) for d in range(1, x + 1) if x % d == 0) % MOD)
def big_TONGSIGMA(r): return f'{10**12 - r.randint(0, 1000)}\n'

# ---------- 16.2 TONGDU
def gen_TONGDU(r):
    n = r.choice([0, 1, r.randint(0, 100), r.randint(0, 3000), r.randint(0, 10**12)])
    k = r.choice([1, r.randint(1, 100), r.randint(1, 3000), n if 1 <= n <= 3000 else 1])
    return f'{n} {k}\n'
def brute_TONGDU(inp):
    n, k = ints(inp); return str(sum(n % i for i in range(1, k + 1)) % MOD)
def big_TONGDU(r): return f'{10**12 - r.randint(0, 10)} {r.choice([10**12, r.randint(10**11, 10**12)])}\n'

# ---------- 16.3 HAITHUONG
def gen_HAITHUONG(r):
    n = r.choice([1, r.randint(1, 100), r.randint(1, 3000)]); m = r.choice([n, r.randint(1, 100), r.randint(1, 3000)])
    return f'{n} {m}\n'
def brute_HAITHUONG(inp):
    n, m = ints(inp); return str(sum((n % i) * (m % i) for i in range(1, min(n, m) + 1)) % MOD)
def big_HAITHUONG(r): return f'{10**12} {10**12 - r.randint(1, 10**6)}\n'
