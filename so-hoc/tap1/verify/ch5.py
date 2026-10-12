# Kiểm tra các chương trình của Chương 5. KĨ THUẬT SỐ HỌC TRONG LẬP TRÌNH
# Quy ước: SPEC['X'] đối chiếu lời giải tối ưu với các biến thể và brute
# trên toàn miền dữ liệu; SPEC['X_ngaytho'] (khi cách ngây thơ chỉ chạy được
# hoặc chỉ đúng trên miền nhỏ) đối chiếu ngây thơ với tối ưu trên miền đó.
import math
def ints(s): return list(map(int, s.split()))

# ---------------- Bài 17. GIAITHUA
def gen_GIAITHUA(r):
    c = r.random()
    if c < 0.15: n = r.choice([0, 1, 2, 20, 21, 22, 25, 1999, 2000])
    elif c < 0.6: n = r.randint(0, 60)
    elif c < 0.9: n = r.randint(0, 500)
    else: n = r.randint(500, 2000)
    return f'{n}\n'
def gen_GIAITHUA_small(r):        # unsigned long long chỉ đúng tới 20!
    return f'{r.choice([0, 1, 2, 19, 20, r.randint(0, 20)])}\n'
def brute_GIAITHUA(inp): return str(math.factorial(int(inp)))

def bigstr(r):
    L = r.choice([1, 1, 2, 5, 9, 10, 19, 20, 50, r.randint(1, 400)])
    if r.random() < 0.08: return '0'
    s = str(r.randint(1, 9)) + ''.join(r.choice('0123456789') for _ in range(L - 1))
    if r.random() < 0.1: s = '9' * L
    return s
def gen_CONG(r): return f'{bigstr(r)}\n{bigstr(r)}\n'
def brute_CONG(inp): a, b = ints(inp); return str(a + b)
def brute_NHAN(inp): a, b = ints(inp); return str(a * b)
def gen_CHIA(r):
    b = r.choice([1, 2, 7, 10, 999, r.randint(1, 10**9), 10**9])
    return f'{bigstr(r)}\n{b}\n'
def brute_CHIA(inp): a, b = ints(inp); return f'{a // b} {a % b}'

# ---------------- Bài 18. DEMBIT
def dembit_formula(n):            # tách bit cao nhất, viết lại bằng Python
    s = 0
    while n > 0:
        k = n.bit_length() - 1; p = 1 << k
        s += k * (p >> 1) + (n - p + 1); n -= p
    return s
def brute_DEMBIT(inp):
    n = int(inp)
    if n <= 20000: return str(sum(bin(i).count('1') for i in range(1, n + 1)))
    return str(dembit_formula(n))
def gen_DEMBIT(r):
    c = r.random()
    if c < 0.2: n = r.choice([0, 1, 2, 3, 10**18, 2**59, 2**59 - 1, 2**59 + 1, 10**18 - 1])
    elif c < 0.45: n = r.randint(0, 3000)
    elif c < 0.6: k = r.randint(1, 59); n = (1 << k) + r.choice([-1, 0, 1])
    else: n = r.randint(0, 10 ** r.randint(4, 18))
    return f'{n}\n'
def gen_DEMBIT_small(r):
    c = r.random()
    if c < 0.2: n = r.choice([0, 1, 2, 3, 7, 8, 1 << 19, (1 << 20) - 1, 10**6])
    elif c < 0.7: n = r.randint(0, 2000)
    else: n = r.randint(0, 10**6)
    return f'{n}\n'

D36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def gen_COSO(r):
    n = r.choice([0, 1, r.randint(0, 100), r.randint(0, 10**18), 10**18])
    return f'{n} {r.choice([2, 2, 3, 8, 10, 16, 36, r.randint(2, 36)])}\n'
def brute_COSO(inp):
    n, b = ints(inp); s = ''
    while True:
        s = D36[n % b] + s; n //= b
        if n == 0: return s
def gen_AM2(r):
    n = r.choice([0, 1, -1, 2, -2, r.randint(-100, 100), r.randint(-10**18, 10**18), 10**18, -10**18])
    return f'{n}\n'
def brute_AM2(inp):               # tìm theo định nghĩa rồi kiểm tra lại
    n = int(inp); s = ''
    while n != 0:
        d = n % 2; s = str(d) + s; n = (n - d) // -2
    s = s or '0'
    assert sum(int(c) * (-2) ** i for i, c in enumerate(reversed(s))) == int(inp)
    return s

# ---------------- Bài 19. DOANCHIA
def gen_DOANCHIA(r):
    c = r.random()
    n = r.choice([1, 2, 3, r.randint(1, 10), r.randint(1, 100), r.randint(1, 2000)])
    k = r.choice([1, 2, 3, r.randint(1, 10), r.randint(1, 1000), 10**6])
    B = r.choice([1, 10, 10**3, 10**9])
    if c < 0.1: a = [0] * n
    elif c < 0.2: a = [-B] * n
    elif c < 0.3: a = [r.choice([k, -k, 2 * k]) for _ in range(n)]
    else: a = [r.randint(-B, B) for _ in range(n)]
    return f'{n} {k}\n' + ' '.join(map(str, a)) + '\n'
def brute_DOANCHIA(inp):
    v = ints(inp); n, k, a = v[0], v[1], v[2:]
    if n <= 300:
        return str(sum(1 for l in range(n) for rr in range(l, n) if sum(a[l:rr + 1]) % k == 0))
    cnt = {}; s = 0; cnt[0] = 1; ans = 0
    for x in a:
        s += x; ans += cnt.get(s % k, 0); cnt[s % k] = cnt.get(s % k, 0) + 1
    return str(ans)

def gen_CHUKI(r):
    m = r.choice([1, 2, 3, r.randint(1, 50), r.randint(1, 10**4), r.randint(1, 10**6), 10**6])
    return f'{r.randint(0, m - 1)} {r.randint(0, m - 1)} {m}\n'
def brute_CHUKI(inp):
    x, c, m = ints(inp); seen = {}; i = 0
    while x not in seen:
        seen[x] = i; x = (x * x + c) % m; i += 1
    return f'{seen[x]} {i - seen[x]}'

# ---------------- Bài 20. DIEMNGUYEN
def gen_DIEMNGUYEN(r):
    M = 10**9
    c = r.random()
    x1 = r.choice([0, r.randint(-20, 20), r.randint(-M, M)])
    y1 = r.choice([0, r.randint(-20, 20), r.randint(-M, M)])
    if c < 0.1: x2, y2 = x1, y1                              # suy biến
    elif c < 0.25: x2, y2 = x1, r.randint(-M, M)             # thẳng đứng
    elif c < 0.4: x2, y2 = x1 + r.randint(-3000, 3000), y1   # nằm ngang
    else:
        d = r.choice([1, 2, 6, 12, 60, 360, r.randint(1, 3000)])
        x2 = x1 + r.choice([-1, 1]) * r.randint(0, 3000)
        y2 = y1 + r.choice([-1, 1]) * d * r.randint(0, 10**5)
        if r.random() < 0.3: y2 = r.randint(-M, M)
    x2 = max(-M, min(M, x2)); y2 = max(-M, min(M, y2))
    if r.random() < 0.5: x1, y1, x2, y2 = x2, y2, x1, y1
    return f'{x1} {y1} {x2} {y2}\n'
def brute_DIEMNGUYEN(inp):        # đếm trực tiếp bằng phân số chính xác
    x1, y1, x2, y2 = ints(inp)
    if x1 == x2: return str(abs(y2 - y1) + 1)
    lo, hi = min(x1, x2), max(x1, x2)
    return str(sum(1 for x in range(lo, hi + 1) if ((x - x1) * (y2 - y1)) % (x2 - x1) == 0))

def gen_PICK(r):                  # đa giác hình sao: sắp các đỉnh theo góc
    while True:
        R = r.choice([3, 5, 10, 30])
        n = r.randint(3, 9)
        pts = set()
        while len(pts) < n: pts.add((r.randint(-R, R), r.randint(-R, R)))
        cx = sum(p[0] for p in pts) / n + 1e-3; cy = sum(p[1] for p in pts) / n + 2e-3
        P = sorted(pts, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
        S2 = sum(P[i][0] * P[(i + 1) % n][1] - P[(i + 1) % n][0] * P[i][1] for i in range(n))
        angs = sorted(round(math.atan2(p[1] - cy, p[0] - cx), 9) for p in P)
        if S2 != 0 and len(set(angs)) == n and simple(P): break
    if r.random() < 0.5: P = P[::-1]
    sh = r.randint(-10**5, 10**5), r.randint(-10**5, 10**5)
    P = [(x + sh[0], y + sh[1]) for x, y in P]
    return f'{n}\n' + ''.join(f'{x} {y}\n' for x, y in P)
def onseg(p, a, b):
    cr = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
    return cr == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def simple(P):                    # không có hai cạnh không kề nhau cắt nhau
    n = len(P); E = [(P[i], P[(i + 1) % n]) for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if j == i + 1 or (i == 0 and j == n - 1):
                a, b = E[i]; c, d = E[j]   # cạnh kề: không được chồng lên nhau
                if cross(a, b, c) == 0 and cross(a, b, d) == 0: return False
                continue
            (a, b), (c, d) = E[i], E[j]
            d1, d2, d3, d4 = cross(c, d, a), cross(c, d, b), cross(a, b, c), cross(a, b, d)
            if ((d1 > 0) != (d2 > 0) and d1 and d2 and (d3 > 0) != (d4 > 0) and d3 and d4): return False
            if onseg(a, c, d) or onseg(b, c, d) or onseg(c, a, b) or onseg(d, a, b): return False
    return True
def brute_PICK(inp):              # đếm từng điểm nguyên trong khung bao
    v = ints(inp); n = v[0]; P = [(v[1 + 2 * i], v[2 + 2 * i]) for i in range(n)]
    xs = [p[0] for p in P]; ys = [p[1] for p in P]
    B = I = 0
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            if any(onseg((x, y), P[i], P[(i + 1) % n]) for i in range(n)): B += 1; continue
            ins = False                       # tia sang phải, quy tắc nửa mở
            for i in range(n):
                (ax, ay), (bx, by) = P[i], P[(i + 1) % n]
                if (ay > y) != (by > y) and x < ax + (y - ay) * (bx - ax) / (by - ay): ins = not ins
            I += ins
    S2 = abs(sum(P[i][0] * P[(i + 1) % n][1] - P[(i + 1) % n][0] * P[i][1] for i in range(n)))
    return f'{S2 // 2}{".5" if S2 % 2 else ""} {B} {I}'

SPEC = {
    'GIAITHUA': {'gen': gen_GIAITHUA, 'progs': ['GIAITHUA_coso10'], 'brute': brute_GIAITHUA},
    'GIAITHUA_ngaytho': {'gen': gen_GIAITHUA_small, 'progs': ['GIAITHUA', 'GIAITHUA_coso10'], 'brute': brute_GIAITHUA, 'n': 100},
    'GIAITHUA_cong': {'gen': gen_CONG, 'brute': brute_CONG},
    'GIAITHUA_nhan': {'gen': gen_CONG, 'brute': brute_NHAN},
    'GIAITHUA_chia': {'gen': gen_CHIA, 'brute': brute_CHIA},
    'DEMBIT': {'gen': gen_DEMBIT, 'progs': ['DEMBIT_dequy'], 'brute': brute_DEMBIT},
    'DEMBIT_ngaytho': {'gen': gen_DEMBIT_small, 'progs': ['DEMBIT', 'DEMBIT_dequy'], 'brute': brute_DEMBIT},
    'DEMBIT_coso': {'gen': gen_COSO, 'brute': brute_COSO},
    'DEMBIT_am2': {'gen': gen_AM2, 'brute': brute_AM2},
    'DOANCHIA': {'gen': gen_DOANCHIA, 'progs': ['DOANCHIA_ngaytho'], 'brute': brute_DOANCHIA},
    'DOANCHIA_chuki': {'gen': gen_CHUKI, 'brute': brute_CHUKI},
    'DIEMNGUYEN': {'gen': gen_DIEMNGUYEN, 'progs': ['DIEMNGUYEN_ngaytho'], 'brute': brute_DIEMNGUYEN},
    'DIEMNGUYEN_pick': {'gen': gen_PICK, 'brute': brute_PICK},
}
