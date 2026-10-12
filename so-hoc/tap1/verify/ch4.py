# Kiểm tra các chương trình của Chương 4. TỔ HỢP VÀ ĐẾM
from math import comb, gcd, isqrt
P = 10**9 + 7
def ints(s): return list(map(int, s.split()))

# ---------------- Bài 13: TOHOP
def gen_TOHOP(r):
    mx = r.choice([0, 1, 2, 5, 10, 30, 200, 2000])
    q = r.randint(1, 30)
    lines = []
    for _ in range(q):
        n = r.randint(0, mx)
        t = r.random()
        if t < 0.15: k = r.randint(n + 1, n + 5)       # k > n: đáp số 0
        elif t < 0.25: k = r.choice([0, n])            # hai đầu hàng
        else: k = r.randint(0, n)
        lines.append(f'{n} {k}')
    return f'{q}\n' + '\n'.join(lines) + '\n'
def brute_TOHOP(inp):
    v = ints(inp); q = v[0]; out = []
    for i in range(q):
        n, k = v[1 + 2 * i], v[2 + 2 * i]
        out.append(str(comb(n, k) % P if 0 <= k <= n else 0))
    return '\n'.join(out)

def gen_TOHOP_lon(r):  # n tới 10^6: chỉ so lời giải tối ưu, nhân dần và Python
    q = r.randint(1, 4); lines = []
    for _ in range(q):
        n = r.choice([10**6, r.randint(0, 10**6), r.randint(0, 3000)])
        k = r.choice([0, 1, n, n - 1, n // 2, r.randint(0, n), n + 1, r.randint(0, 50)])
        lines.append(f'{n} {max(k, 0)}')
    return f'{q}\n' + '\n'.join(lines) + '\n'

def lucas(n, k, p):
    res = 1
    while n or k:
        a, b = n % p, k % p
        if b > a: return 0
        res = res * comb(a, b) % p; n //= p; k //= p
    return res
PR = [2, 3, 5, 7, 11, 13, 97, 101, 997, 10007, 99991, 999983]
def gen_TOHOP_lucas(r):
    p = r.choice(PR)
    if r.random() < 0.5:
        n = r.randint(0, 3000); k = r.randint(0, n + 3)
    else:
        n = r.choice([r.randint(0, 10**18), 10**18, r.randint(0, 10**6)]); k = r.choice([r.randint(0, n), n, 0, n + 1, r.randint(0, 100)])
    return f'{n} {k} {p}\n'
def brute_TOHOP_lucas(inp):
    n, k, p = ints(inp)
    if k > n: return '0'
    if n <= 3000: return str(comb(n, k) % p)
    return str(lucas(n, k, p))

# ---------------- Bài 14: BUTRU
def gen_a(r, k, big):
    a = []
    for _ in range(k):
        t = r.random()
        if t < 0.05: a.append(1)
        elif t < 0.5: a.append(r.randint(2, 12))
        elif t < 0.8 or not big: a.append(r.randint(2, 1000))
        else: a.append(r.choice([r.randint(10**9, 10**18), 10**18, 10**9 + 7, 999999937]))
    return a
def gen_BUTRU(r):
    n = r.choice([1, 2, 10, 30, 100, r.randint(1, 1000), r.randint(1, 10**5), 10**6])
    k = r.choice([1, 2, 3, r.randint(1, 8), r.randint(1, 20), 20])
    a = gen_a(r, k, True)
    return f'{n} {k}\n' + ' '.join(map(str, a)) + '\n'
def brute_BUTRU(inp):  # bù trừ bằng số nguyên lớn của Python, cắt nhánh khi lcm > n
    v = ints(inp); n, k = v[0], v[1]; a = sorted(set(v[2:2 + k]))
    def go(i, l, sg):
        s = 0
        for j in range(i, len(a)):
            nl = l * a[j] // gcd(l, a[j])
            if nl > n: continue
            s += sg * (n // nl) + go(j + 1, nl, -sg)
        return s
    return str(go(0, 1, 1))
def gen_BUTRU_lon(r):  # n tới 10^18: không chạy ngây thơ
    n = r.choice([10**18, r.randint(1, 10**18), r.randint(1, 10**12), 2**62])
    k = r.choice([1, 2, 5, r.randint(1, 20), 20])
    a = gen_a(r, k, True)
    if r.random() < 0.3:  # các số nguyên tố lớn: lcm vượt xa 2^63
        a = [r.choice([10**9 + 7, 10**9 + 9, 998244353, 999999937, 2147483647]) for _ in range(k)]
    return f'{n} {k}\n' + ' '.join(map(str, a)) + '\n'

# ---------------- Bài 15: FIBO
def fib_mod(n, m):  # nhân đôi bằng số nguyên Python
    def f(n):
        if n == 0: return (0, 1)
        a, b = f(n // 2); c = a * (2 * b - a); d = a * a + b * b
        return (c % m, d % m) if n % 2 == 0 else (d % m, (c + d) % m)
    return f(n)[0] % m
def gen_FIBO(r):
    n = r.choice([0, 1, 2, 3, 10, 92, 93, 94, r.randint(0, 100), r.randint(0, 10**5), r.randint(0, 10**7)])
    m = r.choice([1, 2, 10, 1000, r.randint(1, 100), r.randint(1, 10**9), 10**9, 10**9 - 1])
    return f'{n} {m}\n'
def brute_FIBO(inp):
    n, m = ints(inp)
    a, b = 0, 1
    if n <= 2000:
        for _ in range(n): a, b = b, a + b
        return str(a % m)
    return str(fib_mod(n, m))
def gen_FIBO_lon(r):
    n = r.choice([0, 1, 2, 10**18, r.randint(0, 10**18), 2**59 - 1, r.randint(0, 1000)])
    m = r.choice([1, 2, 10**9, r.randint(1, 10**9), 999999937])
    return f'{n} {m}\n'

def gen_FIBO_tongquat(r):
    k = r.randint(1, 6)
    n = r.choice([0, 1, k - 1, k, r.randint(0, 60), r.randint(0, 10**18)])
    m = r.choice([1, 7, 10**9, r.randint(1, 10**9)])
    c = [r.randint(0, 10**9) for _ in range(k)]; f = [r.randint(0, 10**9) for _ in range(k)]
    return f'{k} {n} {m}\n' + ' '.join(map(str, c)) + '\n' + ' '.join(map(str, f)) + '\n'
def brute_FIBO_tongquat(inp):
    v = ints(inp); k, n, m = v[:3]; c = v[3:3 + k]; f = v[3 + k:3 + 2 * k]
    if n <= 200:
        f = f[:]
        while len(f) <= n: f.append(sum(c[j] * f[-1 - j] for j in range(k)))
        return str(f[n] % m)
    # lũy thừa ma trận bằng Python (số nguyên lớn, lấy dư cuối mỗi phép nhân)
    T = [[0] * k for _ in range(k)]; T[0] = c[:]
    for i in range(1, k): T[i][i - 1] = 1
    def mul(A, B): return [[sum(A[i][l] * B[l][j] for l in range(len(B))) % m for j in range(len(B[0]))] for i in range(len(A))]
    R = [[int(i == j) for j in range(k)] for i in range(k)]; e = n
    while e:
        if e & 1: R = mul(R, T)
        T = mul(T, T); e >>= 1
    v0 = [[f[k - 1 - i]] for i in range(k)]
    return str(mul(R, v0)[k - 1][0] % m)

# ---------------- Bài 16: TONGUOC
def S_brute(n):
    if n <= 10**6: return sum(n // i for i in range(1, n + 1))
    r = isqrt(n); return 2 * sum(n // i for i in range(1, r + 1)) - r * r
def gen_TONGUOC(r):
    t = r.random()
    if t < 0.3: n = r.randint(1, 200)
    elif t < 0.5: k = r.randint(1, 3000); n = r.choice([k * k, k * k - 1, k * k + 1, k * (k + 1)])
    elif t < 0.8: n = r.randint(1, 10**6)
    else: n = r.choice([1, 2, 3, 4, 10**7, r.randint(1, 10**7)])
    return f'{max(n, 1)}\n'
def brute_TONGUOC(inp): return str(S_brute(int(inp)))
def gen_TONGUOC_lon(r):
    k = r.randint(1, 10**6)
    n = r.choice([10**12, r.randint(1, 10**12), k * k, k * k - 1, k * k + k, r.randint(1, 1000)])
    return f'{max(n, 1)}\n'

SPEC = {
    'TOHOP': {'gen': gen_TOHOP, 'progs': ['TOHOP_ngaytho', 'TOHOP_nhandan'], 'brute': brute_TOHOP},
    'TOHOP_nhandan': {'gen': gen_TOHOP_lon, 'progs': ['TOHOP'], 'brute': brute_TOHOP, 'n': 40},
    'TOHOP_lucas': {'gen': gen_TOHOP_lucas, 'brute': brute_TOHOP_lucas},
    'BUTRU': {'gen': gen_BUTRU, 'progs': ['BUTRU_ngaytho', 'BUTRU_dfs'], 'brute': brute_BUTRU},
    'BUTRU_dfs': {'gen': gen_BUTRU_lon, 'progs': ['BUTRU'], 'brute': brute_BUTRU},
    'FIBO': {'gen': gen_FIBO, 'progs': ['FIBO_ngaytho', 'FIBO_nhandoi'], 'brute': brute_FIBO},
    'FIBO_nhandoi': {'gen': gen_FIBO_lon, 'progs': ['FIBO'], 'brute': brute_FIBO},
    'FIBO_tongquat': {'gen': gen_FIBO_tongquat, 'brute': brute_FIBO_tongquat},
    'TONGUOC': {'gen': gen_TONGUOC, 'progs': ['TONGUOC_ngaytho', 'TONGUOC_hyperbol'], 'brute': brute_TONGUOC},
    'TONGUOC_hyperbol': {'gen': gen_TONGUOC_lon, 'progs': ['TONGUOC'], 'brute': brute_TONGUOC},
}
