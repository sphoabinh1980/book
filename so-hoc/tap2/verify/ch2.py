# Chương 2: sinh test, vét cạn, test lớn
import math
from functools import lru_cache
def ints(s): return list(map(int, s.split()))

# ---------- công cụ dùng chung cho các hàm vét cạn (viết độc lập với lời giải C++)
def isp_td(n):                                     # thử chia trực tiếp theo định nghĩa
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True
_MR = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
def isprime(n):                                    # thử chia khi n nhỏ, Miller-Rabin 16 cơ sở khi n lớn
    if n < 10**7: return isp_td(n)
    for p in _MR:
        if n % p == 0: return False
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in _MR:
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True
@lru_cache(None)
def plist(m):                                      # danh sách số nguyên tố ≤ m (sàng đơn giản)
    s = bytearray([1]) * (m + 1); s[0] = s[1] = 0
    for i in range(2, int(m ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(range(i * i, m + 1, i)))
    return [i for i in range(m + 1) if s[i]]
def nextprime(n):
    while not isprime(n): n += 1
    return n
def bigprimes(r, lo, hi, k):                       # k số nguyên tố ngẫu nhiên trong [lo, hi]
    return [nextprime(r.randint(lo, hi)) for _ in range(k)]

# ================= Bài 5
# ---------- 5.1 NTGANNHAT
def gen_NTGANNHAT(r):
    q = r.randint(1, 6); s = f'{q}\n'
    for _ in range(q):
        n = r.choice([r.randint(1, 30), r.randint(1, 10**4), r.randint(1, 10**12), 10**12 - r.randint(0, 100),
                      r.choice([1, 2, 3, 4, 9, 10**12, 999999999989])])
        s += f'{n}\n'
    return s
def brute_NTGANNHAT(inp):
    v = ints(inp); out = []
    for n in v[1:v[0] + 1]:
        d = 0                                      # xét lần lượt các khoảng cách d = 0, 1, 2, ...
        while not isprime(n - d) and not isprime(n + d): d += 1
        out.append(str(n - d if isprime(n - d) else n + d))
    return '\n'.join(out)
def big_NTGANNHAT(r):
    # n nằm giữa 5 khoảng trống dài nhất trong [10^12 − 10^7, 10^12] (dài 306, 264, 252, 252, 252; tìm trước bằng máy)
    mids = [999999549106, 999999061309, 999998268635, 999998180135, 999995586325]
    q = 100; s = f'{q}\n'
    for i in range(q):
        s += f'{r.choice(mids) + r.randint(-20, 20) if i % 2 else 10**12 - r.randint(0, 10**6)}\n'
    return s

# ---------- 5.2 GOLDBACH
def gen_GOLDBACH(r):
    q = r.randint(1, 6); s = f'{q}\n'
    for _ in range(q):
        n = r.choice([r.randint(2, 40), r.randint(2, 10**5), 2 * r.randint(1, 5 * 10**5), r.randint(10**11, 10**12),
                      2 * r.randint(5 * 10**10, 5 * 10**11), 2 + r.choice(bigprimes(r, 10**9, 10**12, 1))])
        s += f'{n}\n'
    return s
def brute_GOLDBACH(inp):
    v = ints(inp); out = []
    for n in v[1:v[0] + 1]:
        ans = '-1'
        # n lẻ thì p, q khác tính chẵn lẻ nên p = 2 (với n lớn chỉ thử p = 2 để vét cạn chạy kịp)
        for p in (range(2, n // 2 + 1) if n % 2 == 0 or n < 10**6 else [2]):
            if isprime(p) and isprime(n - p): ans = f'{p} {n - p}'; break
        out.append(ans)
    return '\n'.join(out)
def big_GOLDBACH(r):
    # trong [10^12 − 2·10^6, 10^12], các số chẵn có p nhỏ nhất lớn nhất (p = 1669, 1523, 1433, 1427, 1381; tìm trước bằng máy)
    hard = [999999634148, 999998033872, 999998684926, 999999699004, 999999777998]
    q = 100; s = f'{q}\n'
    for i in range(q):
        if i % 4 == 3: n = 2 + nextprime(10**12 - r.randint(10, 10**6))
        elif i % 4 == 2: n = 2 * r.randint(4 * 10**11, 5 * 10**11)
        else: n = r.choice(hard)
        s += f'{n}\n'
    return s

# ---------- 5.3 NT64
SPSP = [2047, 1373653, 25326001, 3215031751, 2152302898747, 3474749660383, 341550071728321, 3825123056546413051,
        561, 1105, 1729, 2465, 2821, 6601, 8911, 41041, 825265, 321197185]
def gen_NT64(r):
    q = r.randint(1, 8); s = f'{q}\n'
    for _ in range(q):
        k = r.randint(0, 6)
        if k == 0: n = r.randint(1, 100)
        elif k == 1: n = r.choice(SPSP)
        elif k == 2: a, b = bigprimes(r, 2, 2**32 - 1, 2); n = a * b
        elif k == 3: n = r.choice(bigprimes(r, 2**63, 2**64 - 60, 1) + [2**64 - 59, 2**64 - 1, 2**63 - 25, 2**61 - 1])
        elif k == 4: p = nextprime(r.randint(2, 4 * 10**9)); n = p * p if p * p < 2**64 else p
        elif k == 5: n = r.randint(1, 2**64 - 1)
        else: n = r.randint(1, 10**6)
        s += f'{n}\n'
    return s
def brute_NT64(inp):
    v = ints(inp); return '\n'.join('YES' if isprime(n) else 'NO' for n in v[1:v[0] + 1])
def big_NT64(r):
    ps = bigprimes(r, 2**64 - 10**15, 2**64 - 1, 300) + bigprimes(r, 9 * 10**17, 10**18, 300)
    q = 10**5
    return f'{q}\n' + ''.join(f'{r.choice(ps)}\n' for _ in range(q))
TL_NT64 = 2.0

# ================= Bài 6
# ---------- 6.1 DEMNGUYENTO
def gen_DEMNGUYENTO(r):
    q = r.randint(1, 10); s = f'{q}\n'
    m = r.choice([30, 1000, 10**5])
    for _ in range(q):
        if r.random() < 0.5: s += f'1 {r.choice([1, 2, 3, m, r.randint(1, m)])}\n'
        else: s += f'2 {r.choice([1, 2, r.randint(1, 100), r.randint(1, 9592)])}\n'
    return s
def brute_DEMNGUYENTO(inp):
    v = ints(inp); ps = plist(110000); out = []
    for i in range(v[0]):
        t, x = v[1 + 2 * i], v[2 + 2 * i]
        out.append(str(sum(1 for p in ps if p <= x)) if t == 1 else str(ps[x - 1]))
    return '\n'.join(out)
def big_DEMNGUYENTO(r):
    q = 10**6
    return f'{q}\n' + ''.join(f'1 {r.randint(1, 10**7)}\n' if r.random() < 0.5 else f'2 {r.randint(1, 664579)}\n' for _ in range(q))

# ---------- 6.2 SINHDOI
def gen_SINHDOI(r):
    q = r.randint(1, 10); s = f'{q}\n'
    m = r.choice([12, 100, 3000])
    for _ in range(q):
        a = r.randint(1, m); b = r.randint(a, m)
        if r.random() < 0.3: a, b = r.choice([(1, 1), (1, 5), (3, 5), (3, 4), (4, 7), (5, 7), (1, 2), (11, 13), (12, 13)])
        s += f'{a} {b}\n'
    return s
def brute_SINHDOI(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        a, b = v[1 + 2 * i], v[2 + 2 * i]
        out.append(str(sum(1 for p in range(a, b - 1) if isp_td(p) and isp_td(p + 2))))
    return '\n'.join(out)
def big_SINHDOI(r):
    q = 10**6; s = [f'{q}\n']
    for _ in range(q):
        a = r.randint(1, 10**7); b = r.randint(a, 10**7); s.append(f'{a} {b}\n')
    return ''.join(s)

# ---------- 6.3 BAUOC
def gen_BAUOC(r):
    n = r.randint(1, 6); s = f'{n}\n'
    for _ in range(n):
        k = r.randint(0, 5)
        if k == 0: a = r.randint(1, 200)
        elif k == 1: a = r.randint(1, 10**12)
        elif k == 2:                               # bình phương một số nguyên tố lớn nhân thêm vài thừa số nhỏ
            p = nextprime(r.randint(10**4, 10**6)); a = p * p
            while a * 2 <= 10**12 and r.random() < 0.6: a *= r.choice([2, 3, 4, 9, 7, 25])
        elif k == 3:                               # tích hai số nguyên tố > 10^4 (không phải bình phương)
            p = nextprime(r.randint(10**4, 10**6)); q = nextprime(r.randint(10**4, 10**12 // p)) if 10**12 // p > 10**4 else 1; a = p * q
        elif k == 4: a = r.choice([1, 4, 10**12, 999966000289, 2**39, 720720, 9699690 ** 1, 10007 ** 2, 9973 ** 2 * 10007, 997 ** 2 * 1009 ** 2 * 7])
        else:
            a = 1
            for p in r.sample([2, 3, 5, 7, 11, 13, 9973, 10007], r.randint(1, 4)):
                e = r.randint(1, 3)
                if a * p ** e <= 10**12: a *= p ** e
        s += f'{a}\n'
    return s
def brute_BAUOC(inp):
    v = ints(inp); ps = plist(10**6); out = []
    for a in v[1:v[0] + 1]:                        # x có đúng 3 ước <=> x = p^2: đếm p với p^2 | a
        out.append(str(sum(1 for p in ps if p * p <= a and a % (p * p) == 0)))
    return '\n'.join(out)
def big_BAUOC(r):
    n = 10**5; ps = bigprimes(r, 10**4, 10**6, 50); s = [f'{n}\n']
    for i in range(n):
        if i % 3 == 0: p = r.choice(ps); a = p * p * r.randint(1, 10**12 // (p * p))
        else: a = r.randint(10**12 - 10**9, 10**12)
        s.append(f'{a}\n')
    return ''.join(s)

# ================= Bài 7
# ---------- 7.1 SOUOC
def gen_SOUOC(r):
    q = r.randint(1, 8); s = f'{q}\n'
    for _ in range(q):
        s += f'{r.choice([1, 2, r.randint(1, 100), r.randint(1, 10**5), r.randint(1, 10**7), 10**7, 9699690, 8648640, 8388608, 9999991])}\n'
    return s
def brute_SOUOC(inp):
    v = ints(inp); out = []
    for n in v[1:v[0] + 1]:
        ds = set()
        d = 1
        while d * d <= n:
            if n % d == 0: ds.add(d); ds.add(n // d)
            d += 1
        out.append(f'{len(ds)} {sum(ds)}')
    return '\n'.join(out)
def big_SOUOC(r):
    q = 10**6
    return f'{q}\n' + ''.join(f'{r.randint(1, 10**7)}\n' for _ in range(q))

# ---------- 7.2 CHUSO0
def gen_CHUSO0(r):
    t = r.randint(1, 5); s = f'{t}\n'
    for _ in range(t):
        n = r.choice([0, 1, r.randint(0, 30), r.randint(0, 300)])
        b = r.choice([2, 10, 16, 12, r.randint(2, 50), r.randint(2, 10**6), nextprime(r.randint(2, 400)), 2 ** r.randint(1, 20), 360, 997 ** 2])
        s += f'{n} {b}\n'
    return s
def brute_CHUSO0(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        n, b = v[1 + 2 * i], v[2 + 2 * i]
        f = math.factorial(n); z = 0
        while f % b == 0: f //= b; z += 1           # đếm trực tiếp số chữ số 0 tận cùng trong cơ số b
        out.append(str(z))
    return '\n'.join(out)
def big_CHUSO0(r):
    t = 100; ps = bigprimes(r, 10**12 - 10**6, 10**12, 5)
    return f'{t}\n' + ''.join(f'{r.randint(10**17, 10**18)} {r.choice(ps + [999966000289, 999999999989])}\n' for _ in range(t))

# ---------- 7.3 BCNNDAY
def gen_BCNNDAY(r):
    n = r.randint(1, 12); m = r.choice([10, 50, 1000, 10**7])
    a = [r.randint(1, m) for _ in range(n)]
    if r.random() < 0.3: a = [r.choice([1, 2, 4, 6, 12, 9, 8, 3]) for _ in range(n)]
    return f'{n}\n' + ' '.join(map(str, a)) + '\n'
def brute_BCNNDAY(inp):
    v = ints(inp); n = v[0]; a = v[1:n + 1]
    L = math.lcm(*a)
    can = sum(1 for i in range(n) if math.lcm(*(a[:i] + a[i + 1:]), 1) != L)   # BCNN của dãy rỗng = 1
    return f'{L % (10**9 + 7)}\n{can}'
def big_BCNNDAY(r):
    n = 10**5
    return f'{n}\n' + ' '.join(str(r.choice([r.randint(1, 10**7), nextprime(r.randint(9 * 10**6, 10**7 - 200))]) if i < 1000 else r.randint(1, 10**7)) for i in range(n)) + '\n'

# ================= Bài 8
# ---------- 8.1 NTDOAN
def gen_NTDOAN(r):
    t = r.randint(1, 4); s = f'{t}\n'
    for _ in range(t):
        k = r.randint(0, 3)
        if k == 0: L = r.randint(1, 50); R = r.randint(L, 120)
        elif k == 1: L = r.randint(1, 10**12 - 200); R = L + r.randint(0, 150)
        elif k == 2: R = 10**12; L = R - r.randint(0, 150)
        else: L, R = r.choice([(1, 1), (1, 2), (2, 2), (4, 4), (24, 28), (999966000289, 999966000289), (999999999989, 10**12)])
        s += f'{L} {R}\n'
    return s
def brute_NTDOAN(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        L, R = v[1 + 2 * i], v[2 + 2 * i]
        ps = [x for x in range(L, R + 1) if isprime(x)]
        out.append(f'{len(ps)} {sum(ps)}')
    return '\n'.join(out)
def big_NTDOAN(r):
    t = 10; s = f'{t}\n'
    for i in range(t):
        R = 10**12 - r.randint(0, 10**6) if i else 10**12; s += f'{R - 10**6} {R}\n'
    return s

# ---------- 8.2 KHOANGCACH
def gen_KHOANGCACH(r):
    k = r.randint(0, 3)
    if k == 0: L = r.randint(1, 60); R = r.randint(L, 150)
    elif k == 1: L = r.randint(1, 10**12 - 300); R = L + r.randint(0, 300)
    elif k == 2: R = 10**12; L = R - r.randint(0, 300)
    else: L, R = r.choice([(1, 1), (1, 2), (1, 3), (2, 3), (3, 5), (24, 28), (23, 29), (114, 126), (113, 127), (999999999989, 10**12)])
    return f'{L} {R}\n'
def brute_KHOANGCACH(inp):
    L, R = ints(inp); ps = [x for x in range(L, R + 1) if isprime(x)]
    if len(ps) < 2: return '-1'
    pairs = list(zip(ps, ps[1:]))
    big = max(pairs, key=lambda t: (t[1] - t[0], -t[0])); sm = min(pairs, key=lambda t: (t[1] - t[0], t[0]))
    return f'{big[0]} {big[1]}\n{sm[0]} {sm[1]}'
def big_KHOANGCACH(r):
    R = 10**12 - r.randint(0, 10**6); return f'{R - 10**7} {R}\n'

# ---------- 8.3 UOCDOAN
def gen_UOCDOAN(r):
    k = r.randint(0, 3)
    if k == 0: L = r.randint(1, 100); R = r.randint(L, 300)
    elif k == 1: L = r.randint(1, 10**12 - 10); R = L + r.randint(0, 6)
    elif k == 2: R = 10**12; L = R - r.randint(0, 6)
    else: L, R = r.choice([(1, 1), (1, 2), (720719, 720721), (999966000287, 999966000291), (963761198400, 963761198400), (735134400, 735134405)])
    return f'{L} {R}\n'
def ndiv(x):
    res = 1
    for p in plist(10**6):
        if p * p > x: break
        e = 0
        while x % p == 0: x //= p; e += 1
        res *= e + 1
    return res * (2 if x > 1 else 1)
def brute_UOCDOAN(inp):
    L, R = ints(inp); d = [(ndiv(x), x) for x in range(L, R + 1)]
    best = max(d, key=lambda t: (t[0], -t[1]))
    return f'{sum(t[0] for t in d)}\n{best[1]} {best[0]}'
def big_UOCDOAN(r):
    R = 10**12 - r.randint(0, 10**5); return f'{R - 10**6} {R}\n'
TL_SOUOC = 2.0
TL_SINHDOI = 2.0
