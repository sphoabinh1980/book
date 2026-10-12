# Kiểm tra các chương trình của Chương 2. SỐ NGUYÊN TỐ
import math

def is_prime(n):                      # Miller–Rabin tất định cho n < 3,3 · 10^24
    if n < 2: return False
    A = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in A:
        if n % p == 0: return n == p
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in A:
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True

_SV = {}
def sieve(N):                         # bảng nguyên tố 0..N (lưu lại để dùng chung)
    if N not in _SV:
        s = bytearray([1]) * (N + 1); s[0] = 0
        if N >= 1: s[1] = 0
        for i in range(2, math.isqrt(N) + 1):
            if s[i]: s[i * i::i] = bytearray(len(range(i * i, N + 1, i)))
        _SV.clear(); _SV[N] = s
    return _SV[N]

def rand_prime(r, lo, hi):
    while True:
        x = r.randint(lo, hi)
        if is_prime(x): return x

CARMI = [561, 1105, 1729, 2465, 2821, 6601, 8911, 41041, 825265, 321197185]
SPSP = [2047, 3215031751, 2152302898747, 3474749660383, 341550071728321,
        3825123056546413051]          # giả nguyên tố mạnh theo nhiều cơ sở đầu

# ---------- Bài 5. KTNT
def gen_KTNT(r):
    # số "dễ" cho bản ngây thơ: nhỏ, hoặc lớn nhưng có ước nhỏ
    def one():
        k = r.randint(0, 9)
        if k == 0: return r.randint(1, 30)
        if k == 1: return r.randint(1, 10**4)
        if k == 2: return rand_prime(r, 2, 3 * 10**6)
        if k == 3: return r.choice(CARMI[:9] + [2047])
        if k == 4: p = rand_prime(r, 2, 10**6); return p * p
        if k == 5:
            p = rand_prime(r, 2, 2 * 10**5)
            return p * rand_prime(r, p, 10**12 // p)
        if k == 6: return r.randint(1, 10**12 // 2) * 2
        if k == 7: return r.choice([999966000289, 999999999999, 10**12])
        return r.randint(1, 3 * 10**6)
    q = r.randint(1, 8)
    return f'{q}\n' + '\n'.join(str(one()) for _ in range(q)) + '\n'
def brute_KTNT(inp):
    a = list(map(int, inp.split()))[1:]
    return '\n'.join('YES' if is_prime(x) else 'NO' for x in a)

def gen_KTNT_MR(r):                   # số lớn tới 10^12, nhiều số nguyên tố
    def one():
        k = r.randint(0, 6)
        if k == 0: return rand_prime(r, 10**11, 10**12)
        if k == 1: return rand_prime(r, 1, 10**12)
        if k == 2: p = rand_prime(r, 9 * 10**5, 10**6); return p * p
        if k == 3:
            p = rand_prime(r, 5 * 10**5, 10**6)
            return p * rand_prime(r, 5 * 10**5, 10**6)
        if k == 4: return r.choice(CARMI + SPSP[:3])
        if k == 5: return r.choice([1, 2, 3, 4, 999999999989, 10**12])
        return r.randint(1, 10**12)
    q = r.randint(1, 4)
    return f'{q}\n' + '\n'.join(str(one()) for _ in range(q)) + '\n'

# ---------- Bài 6. DEMNT
def gen_DEMNT(r):
    k = r.random()
    if k < 0.05: N = 10**7
    elif k < 0.3: N = r.randint(1, 30)
    elif k < 0.8: N = r.randint(1, 3000)
    else: N = r.randint(1, 2 * 10**5)
    q = r.randint(1, 6); qs = []
    for _ in range(q):
        if N == 10**7:
            b = r.randint(10**7 - 1000, 10**7); a = r.randint(b - 1000, b)
        else:
            a = r.randint(1, N); b = r.randint(a, N)
            if r.random() < 0.15: a = 1
        qs.append(f'{a} {b}')
    return f'{q}\n' + '\n'.join(qs) + '\n'
def brute_DEMNT(inp):
    v = list(map(int, inp.split())); q = v[0]
    ab = [(v[1 + 2 * i], v[2 + 2 * i]) for i in range(q)]
    s = sieve(max(10**7, max(b for a, b in ab)))
    return '\n'.join(str(sum(s[a:b + 1])) for a, b in ab)

# ---------- Bài 7. PTTS
def gen_PTTS(r):
    def one():
        k = r.randint(0, 7)
        if k == 0: return r.randint(2, 50)
        if k == 1: return rand_prime(r, 2, 10**7)
        if k == 2: return 2 ** r.randint(1, 23)
        if k == 3: return r.choice([9699690, 10**7, 9999991, 2, 4, 8388608])
        if k == 4: p = rand_prime(r, 2, 3162); return p * p
        if k == 5: return r.randint(2, 1000)
        return r.randint(2, 10**7)
    q = r.randint(1, 8)
    return f'{q}\n' + '\n'.join(str(one()) for _ in range(q)) + '\n'
def brute_PTTS(inp):
    out = []
    for n in list(map(int, inp.split()))[1:]:
        m, parts, d = n, [], 2
        while d * d <= m:
            e = 0
            while m % d == 0: m //= d; e += 1
            if e: parts.append(f'{d}^{e}' if e > 1 else str(d))
            d += 1
        if m > 1: parts.append(str(m))
        out.append(f'{n} = ' + ' * '.join(parts))
    return '\n'.join(out)

# ---------- Bài 8. SANGDOAN
def gen_SANGDOAN(r):
    k = r.randint(0, 7)
    if k == 0: L = r.randint(1, 30); R = r.randint(L, 60)
    elif k == 1: L = r.randint(1, 10**4); R = L + r.randint(0, 300)
    elif k == 2: L = r.randint(1, 10**9); R = L + r.randint(0, 200)
    elif k == 3: R = 10**12; L = R - r.randint(0, 80)
    elif k == 4:                      # đoạn chứa p^2 với p sát √R
        p = rand_prime(r, 9 * 10**5, 10**6); L = p * p - r.randint(0, 30)
        R = p * p + r.randint(0, 30)
    elif k == 5: L = 1; R = r.randint(1, 500)
    elif k == 6: p = rand_prime(r, 10**11, 10**12); L = R = p
    else: L = r.randint(1, 10**12 - 100); R = L + r.randint(0, 60)
    return f'{L} {R}\n'
def brute_SANGDOAN(inp):
    L, R = map(int, inp.split())
    ps = [x for x in range(L, R + 1) if is_prime(x)]
    return f'{len(ps)}\n' + ' '.join(map(str, ps))

SPEC = {
    'KTNT': {'gen': gen_KTNT, 'progs': ['KTNT_ngaytho', 'KTNT_MR'],
             'brute': brute_KTNT},
    'KTNT_MR': {'gen': gen_KTNT_MR, 'progs': ['KTNT'], 'brute': brute_KTNT},
    'DEMNT': {'gen': gen_DEMNT, 'progs': ['DEMNT_ngaytho', 'DEMNT_tuyentinh'],
              'brute': brute_DEMNT},
    'PTTS': {'gen': gen_PTTS, 'progs': ['PTTS_ngaytho'], 'brute': brute_PTTS},
    'SANGDOAN': {'gen': gen_SANGDOAN, 'progs': ['SANGDOAN_ngaytho'],
                 'brute': brute_SANGDOAN},
}
