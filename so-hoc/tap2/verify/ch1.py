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
