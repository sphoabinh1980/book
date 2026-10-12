# Chương 3: sinh test, vét cạn, test lớn
import math
from fractions import Fraction
def ints(s): return list(map(int, s.split()))
P7 = 10**9 + 7

def is_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
def rand_prime(r, lo, hi):
    while True:
        x = r.randint(lo, hi)
        if is_prime(x): return x

# ---------- 9.1 LUYTHUAQ
def gen_LUYTHUAQ(r):
    q = r.randint(1, 8); s = f'{q}\n'
    for _ in range(q):
        a = r.choice([0, 1, 2, P7, 2 * P7, P7 + 1, r.randint(0, 50), r.randint(0, 10**18), 10**18])
        b = r.choice([0, 1, 2, r.randint(0, 60), r.randint(0, 10**18), 10**18, P7 - 1, P7 - 2])
        s += f'{a} {b}\n'
    return s
def brute_LUYTHUAQ(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        a, b = v[1 + 2 * i], v[2 + 2 * i]
        if b <= 300: x = a ** b % P7          # tính đúng theo định nghĩa bằng số lớn
        else: x = pow(a, b, P7)
        out.append(str(x))
    return '\n'.join(out)
def big_LUYTHUAQ(r):
    q = 10**5
    return f'{q}\n' + ''.join(f'{r.randint(10**17, 10**18)} {r.randint(10**17, 10**18)}\n' for _ in range(q))

# ---------- 9.2 SOMULON
def gen_SOMULON(r):
    T = r.randint(1, 4); s = f'{T}\n'
    for _ in range(T):
        a = r.choice([0, 1, 2, 10, r.randint(0, 100), r.randint(0, 10**18)])
        b = r.choice(['0', '1', str(r.randint(0, 100)), str(r.randint(0, 10**40)), str(r.randint(1, 9)) + ''.join(r.choice('0123456789') for _ in range(r.randint(0, 300)))])
        m = r.choice([1, 2, 10, 12, 1000, P7, r.randint(1, 100), r.randint(1, 10**9), 10**9])
        s += f'{a} {b} {m}\n'
    return s
def brute_SOMULON(inp):
    L = inp.split('\n'); out = []
    for i in range(int(L[0])):
        a, b, m = map(int, L[1 + i].split())
        out.append(str(pow(a, b, m)))
    return '\n'.join(out)
def big_SOMULON(r):
    T = 10; s = f'{T}\n'
    for _ in range(T):
        b = str(r.randint(1, 9)) + ''.join(r.choice('0123456789') for _ in range(10**5 - 1))
        s += f'{r.randint(10**17, 10**18)} {b} {r.randint(10**8, 10**9)}\n'
    return s

# ---------- 9.3 TONGLT
def gen_TONGLT(r):
    T = r.randint(1, 6); s = f'{T}\n'
    for _ in range(T):
        a = r.choice([0, 1, 2, 3, 10, r.randint(0, 100), r.randint(0, 10**18)])
        n = r.choice([0, 1, 2, r.randint(0, 50), r.randint(0, 2000), r.randint(0, 10**18)])
        m = r.choice([1, 2, 7, 1000, P7, r.randint(1, 100), r.randint(1, 10**18), 10**18])
        if r.random() < 0.15: a = m + 1 if r.random() < 0.5 else m   # a ≡ 1 hoặc a ≡ 0 (mod m)
        a = min(a, 10**18)
        s += f'{a} {n} {m}\n'
    return s
def brute_TONGLT(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        a, n, m = v[1 + 3 * i: 4 + 3 * i]
        if n <= 2000: S = sum(pow(a, j) for j in range(n + 1)) % m if a < 10**4 else sum(pow(a, j, m) for j in range(n + 1)) % m
        elif a == 0: S = 1 % m
        elif a == 1: S = (n + 1) % m
        else:   # (a^(n+1) - 1) / (a - 1): tính a^(n+1) theo mô-đun m(a-1) rồi chia đúng
            M = m * (a - 1); X = (pow(a, n + 1, M) - 1) % M; S = (X // (a - 1)) % m
        out.append(str(S))
    return '\n'.join(out)
def big_TONGLT(r):
    T = 10**4
    return f'{T}\n' + ''.join(f'{r.randint(2, 10**18)} {r.randint(10**18 - 10**6, 10**18)} {r.randint(10**17, 10**18)}\n' for _ in range(T))

# ---------- 10.1 XACSUAT
def gen_XACSUAT(r):
    n = r.randint(1, 6); s = f'{n}\n'
    for _ in range(n):
        t = r.choice([1, 2, 6, r.randint(1, 20), r.randint(1, 10**9)])
        x = r.choice([0, t, r.randint(0, t)]); s += f'{x} {t - x}\n'
    return s
def brute_XACSUAT(inp):
    v = ints(inp); n = v[0]; pr = Fraction(1); pb = Fraction(1)
    for i in range(n):
        x, y = v[1 + 2 * i], v[2 + 2 * i]; pr *= Fraction(x, x + y); pb *= Fraction(y, x + y)
    f = lambda q: q.numerator * pow(q.denominator, P7 - 2, P7) % P7
    return f'{f(pr)}\n{f(1 - pb)}'
def big_XACSUAT(r):
    n = 10**5; s = f'{n}\n'
    for _ in range(n):
        t = r.randint(1, 10**9); x = r.randint(0, t); s += f'{x} {t - x}\n'
    return s

# ---------- 10.2 NGHICHDAO
def gen_NGHICHDAO(r):
    p = r.choice([2, 3, 5, 7, 11, 13, rand_prime(r, 2, 3000), rand_prime(r, 10**9, 2 * 10**9), 1999999973])
    n = min(p - 1, r.choice([1, 2, r.randint(1, 3000), 3000]))
    return f'{n} {p}\n'
def brute_NGHICHDAO(inp):
    n, p = ints(inp); inv = [pow(i, p - 2, p) for i in range(1, n + 1)]
    assert all(i * x % p == 1 for i, x in zip(range(1, n + 1), inv))
    x = 0
    for t in inv: x ^= t
    return f'{sum(inv) % p}\n{x}'
def big_NGHICHDAO(r): return f'10000000 {[1999999973, 1000000007, 10000019][r.randint(0, 2)]}\n'

# ---------- 10.3 PTDONGDU
def gen_PTDONGDU(r):
    q = r.randint(1, 6); s = f'{q}\n'
    for _ in range(q):
        m = r.choice([1, 2, 6, 10, 12, r.randint(1, 60), r.randint(1, 10**18), 10**18, 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47])
        a = r.choice([0, 1, -1, r.randint(-50, 50), r.randint(-10**18, 10**18), m, 2 * r.randint(1, 10**17)])
        a = max(-10**18, min(10**18, a))
        c = r.choice([0, r.randint(-50, 50), r.randint(-10**18, 10**18), a * r.randint(-50, 50)])
        c = max(-10**18, min(10**18, c))
        if r.random() < 0.3 and m <= 10**17 and abs(a) <= 10**16:   # bảo đảm có nghiệm và có nghiệm trong đoạn
            x = r.randint(-10**3, 10**3); c = a * x + m * r.randint(-3, 3)
        if r.random() < 0.5: L = r.randint(-300, 300)
        else: L = r.choice([-10**18, 10**18 - 400, r.randint(-10**18, 10**18 - 400)])
        R = min(10**18, L + r.randint(0, 400))
        s += f'{a} {c} {m} {L} {R}\n'
    return s
def brute_PTDONGDU(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        a, c, m, L, R = v[1 + 5 * i: 6 + 5 * i]
        sol = [x for x in range(L, R + 1) if (a * x - c) % m == 0]
        out.append(f'{len(sol)} {sol[0]}' if sol else '0')
    return '\n'.join(out)
def big_PTDONGDU(r):
    q = 10**5; s = f'{q}\n'
    for _ in range(q):
        m = r.randint(10**17, 10**18); g = r.choice([1, 2, 6, 1000, 10**6])
        m = m // g * g; a = g * r.randint(1, 10**18 // g) * r.choice([1, -1]); c = r.randint(-10**18, 10**18) // g * g
        s += f'{a} {c} {m} {-10**18} {10**18}\n'
    return s

# ---------- 11.1 PHI
def gen_PHI(r):
    q = r.randint(1, 6); s = f'{q}\n'
    for _ in range(q):
        n = r.choice([1, 2, 3, 4, 12, 36, 360, r.randint(1, 1000), 2 * 999983, 999983 ** 2, 10**12, 999999999989, 2**39, 3**25, 4 * 999983 ** 2 // 4, r.randint(1, 10**12)])
        n = min(n, 10**12); s += f'{n}\n'
    return s
def brute_PHI(inp):
    v = ints(inp); out = []
    for n in v[1:]:
        if n <= 1000: out.append(str(sum(1 for k in range(1, n + 1) if math.gcd(k, n) == 1)))
        else:   # đếm theo bù trừ trên các ước nguyên tố (phân tích bằng thử chia trực tiếp)
            ps = []; t = n; d = 2
            while d * d <= t:
                if t % d == 0:
                    ps.append(d)
                    while t % d == 0: t //= d
                d += 1
            if t > 1: ps.append(t)
            cnt = 0
            for mask in range(1 << len(ps)):
                prod = 1; bits = 0
                for j in range(len(ps)):
                    if mask >> j & 1: prod *= ps[j]; bits += 1
                cnt += (-1) ** bits * (n // prod)
            out.append(str(cnt))
    return '\n'.join(out)
def big_PHI(r):
    big_primes = [999999999989, 999999999959, 999999999961, 999999999863, 999999999877]
    return '100\n' + ''.join(f'{r.choice(big_primes + [999983 * 999979, 999979 ** 2])}\n' for _ in range(100))

# ---------- 11.2 PHANSO
def gen_PHANSO(r):
    q = r.randint(1, 6); s = f'{q}\n'
    for _ in range(q):
        R = r.choice([1, 2, 3, r.randint(1, 40), r.randint(1, 200)]); L = r.choice([1, R, r.randint(1, R)])
        s += f'{L} {R}\n'
    return s
def brute_PHANSO(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        L, R = v[1 + 2 * i], v[2 + 2 * i]
        fr = {Fraction(a, b) for b in range(L, R + 1) for a in range(1, b)}
        out.append(str(sum(1 for f in fr if L <= f.denominator <= R)))
    return '\n'.join(out)
def big_PHANSO(r):
    q = 10**5; s = f'{q}\n1 10000000\n'
    for _ in range(q - 1):
        L = r.randint(1, 10**7); R = r.randint(L, 10**7); s += f'{L} {R}\n'
    return s

# ---------- 11.3 THAPLT
def _tower_ok(a):
    """kiểm tra phần đuôi a[1:] tính được đúng bằng số lớn (số bit không quá 2·10^5)"""
    v = a[-1]
    for x in reversed(a[1:-1]):
        if x <= 1 or v == 0: v = 1 if (x == 1 or v == 0) else 0; continue
        if v * x.bit_length() > 2 * 10**5: return False
        v = x ** v
    return True
def gen_THAPLT(r):
    T = r.randint(1, 4); s = f'{T}\n'
    for _ in range(T):
        while True:
            k = r.choice([1, 2, 3, 3, 4, r.randint(1, 8)])
            pool = [0, 1, 2, 2, 3, r.randint(0, 6), r.randint(0, 30), r.randint(0, 10**9)]
            a = [r.choice(pool) for _ in range(k)]
            if _tower_ok(a): break
        m = r.choice([1, 2, 4, 12, 36, 100, 1000, 720720, 2**29, 3**18, P7, r.randint(1, 100), r.randint(1, 10**9)])
        s += f'{k} {m}\n' + ' '.join(map(str, a)) + '\n'
    return s
def brute_THAPLT(inp):
    v = ints(inp); T = v[0]; i = 1; out = []
    for _ in range(T):
        k, m = v[i], v[i + 1]; a = v[i + 2: i + 2 + k]; i += 2 + k
        E = a[-1]
        for x in reversed(a[1:-1]): E = x ** E       # giá trị đúng của phần đuôi (0^0 = 1)
        out.append(str(pow(a[0], E, m) if k > 1 else a[0] % m))
    return '\n'.join(out)
def big_THAPLT(r):
    T = 10; s = f'{T}\n'
    for t in range(T):
        k = 10**5; m = [735134400, 999999937, 2**29, 3**18, 999999000][t % 5]
        a = [r.randint(2, 10**9) for _ in range(k)]
        s += f'{k} {m}\n' + ' '.join(map(str, a)) + '\n'
    return s

# ---------- 12.1 DIEMBINH
def _coprime_mods(r, k, lim):
    ms = []
    while len(ms) < k:
        x = r.choice([1, 2, 3, 4, 5, 7, 8, 9, 11, 13, r.randint(1, 30), r.randint(1, lim)])
        if all(math.gcd(x, y) == 1 for y in ms) and math.prod(ms) * x <= lim: ms.append(x)
        elif r.random() < 0.05: ms.append(1)
    return ms
def gen_DIEMBINH(r):
    k = r.randint(1, 5); ms = _coprime_mods(r, k, r.choice([100, 10**4, 10**5]))
    L = r.choice([0, 0, r.randint(0, 50), r.randint(0, 10**5)])
    return f'{k} {L}\n' + ''.join(f'{m} {r.randint(0, m - 1)}\n' for m in ms)
def brute_DIEMBINH(inp):
    v = ints(inp); k, L = v[0], v[1]; eq = [(v[2 + 2 * i], v[3 + 2 * i]) for i in range(k)]
    x = L
    while not all(x % m == a for m, a in eq): x += 1
    return str(x)
def big_DIEMBINH(r):
    ms = [1000000000, 999999999]   # nguyên tố cùng nhau, tích gần 10^18
    return f'2 {10**18}\n' + ''.join(f'{m} {r.randint(0, m - 1)}\n' for m in ms)

# ---------- 12.2 HAIDEN
def gen_HAIDEN(r):
    q = r.randint(1, 6); s = f'{q}\n'
    for _ in range(q):
        p1 = r.choice([1, 2, 4, 6, 10, 12, r.randint(1, 60)]); p2 = r.choice([1, 3, 6, 9, 15, r.randint(1, 60), p1, 2 * p1])
        a1 = r.choice([0, r.randint(0, 100), r.randint(0, 3000)]); a2 = r.choice([0, a1, r.randint(0, 100), r.randint(0, 3000)])
        s += f'{a1} {p1} {a2} {p2}\n'
    return s
def brute_HAIDEN(inp):
    v = ints(inp); out = []
    for i in range(v[0]):
        a1, p1, a2, p2 = v[1 + 4 * i: 5 + 4 * i]
        t = a1; lim = max(a1, a2) + p1 * p2 + 1; ans = -1   # mô phỏng các lần nháy của đèn 1
        while t <= lim:
            if t >= a2 and (t - a2) % p2 == 0: ans = t; break
            t += p1
        out.append(str(ans))
    return '\n'.join(out)
def big_HAIDEN(r):
    q = 10**5; s = f'{q}\n'
    for _ in range(q):
        p1 = r.randint(10**8, 10**9); p2 = r.randint(10**8, 10**9)
        s += f'{r.randint(0, 10**18)} {p1} {r.randint(0, 10**18)} {p2}\n'
    return s

# ---------- 12.3 CANCHI
def gen_CANCHI(r):
    k = r.randint(1, 4)
    ms = [r.choice([1, 2, 3, 4, 6, 10, 12, 60, r.randint(1, 30), r.randint(1, 10**6), 999983, 720720]) for _ in range(k)]
    if r.random() < 0.3:   # bội chung nhỏ nhất vượt 10^18
        k = r.randint(4, 6); ms = [r.randint(5 * 10**5, 10**6) for _ in range(k)]
    q = r.randint(1, 5); s = f'{k} {q}\n' + ' '.join(map(str, ms)) + '\n'
    for _ in range(q):
        y = r.choice([r.randint(0, 3000), r.randint(0, 10**18)])
        if r.random() < 0.6: c = [y % m for m in ms]          # tên chắc chắn có xuất hiện (năm y)
        else: c = [r.randint(0, m - 1) for m in ms]
        L = r.choice([0, r.randint(0, 3000), r.randint(0, 10**18 - 2000), 10**18 - 2000, max(0, y - r.randint(0, 1000))])
        R = min(10**18, L + r.randint(0, 2000))
        s += ' '.join(map(str, c)) + f' {L} {R}\n'
    return s
def brute_CANCHI(inp):
    v = ints(inp); k, q = v[0], v[1]; ms = v[2: 2 + k]; i = 2 + k; out = [str(math.lcm(*ms) % P7)]
    for _ in range(q):
        c = v[i: i + k]; L, R = v[i + k], v[i + k + 1]; i += k + 2
        ys = [y for y in range(L, R + 1) if all(y % m == cc for m, cc in zip(ms, c))]
        out.append(f'{len(ys)} {ys[0]}' if ys else '0')
    return '\n'.join(out)
def big_CANCHI(r):
    k = 20; q = 10**5
    ms = [r.randint(5 * 10**5, 10**6) for _ in range(k)]
    s = f'{k} {q}\n' + ' '.join(map(str, ms)) + '\n'
    lines = []
    for _ in range(q):
        y = r.randint(0, 10**18); c = [y % m for m in ms]
        lines.append(' '.join(map(str, c)) + f' 0 {10**18}')
    return s + '\n'.join(lines) + '\n'
