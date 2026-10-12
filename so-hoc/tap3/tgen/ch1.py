# Bộ sinh test Chương 1 — gen(subtask, i, rng) trả về nội dung tệp vào
from common import *

def g_NGAYTHU(st, i, r):
    q = 100 if st == 1 else 10**5
    if st == 1: K = lambda: r.randint(0, 10**6)
    elif st == 2: K = lambda: r.choice([r.randint(0, 10**18), 10**18, r.randint(0, 100)])
    else: K = lambda: r.choice([r.randint(-10**18, 10**18), -10**18, r.randint(-100, 0), -7 * r.randint(1, 10**17)])
    rows = [(r.randint(2, 8), K()) for _ in range(q)]
    return f'{q}\n' + lines(*rows)

def big_digits(r, L):
    return str(r.randint(1, 9)) + ''.join(r.choice('0123456789') for _ in range(L - 1))
def g_CHUSOCUOI(st, i, r):
    T = 10; rows = []
    for k in range(T):
        if st == 1: a, b = r.randint(0, 10**6), r.choice([r.randint(0, 10**6), 4 * r.randint(1, 250000), 0])
        elif st == 2: a, b = r.randint(0, 10**18), r.choice([r.randint(0, 10**18), 4 * r.randint(1, 10**17), 0])
        else:
            a = big_digits(r, r.choice([10**5, r.randint(1, 10**5)])); b = big_digits(r, 10**5)
            if k % 3 == 0: b = b[:-2] + r.choice(['00', '04', '12', '96'])   # b chia hết cho 4
            if k == 1: a = '0'
            rows.append((a, b)); continue
        if k == 0: a = 0
        rows.append((a, b))
    return f'{T}\n' + lines(*rows)

def g_VIETLIEN(st, i, r):
    n = [r.randint(1, 9), r.randint(100, 1000), 10**7 - r.randint(0, 3)][st - 1]
    m = [r.randint(10**8, 10**9), 10**9, r.randint(1, 1000)][i % 3]
    return f'{n} {m}\n'

SPEC = {
    'NGAYTHU': S(g_NGAYTHU, [3, 3, 4]),
    'CHUSOCUOI': S(g_CHUSOCUOI, [3, 3, 4]),
    'VIETLIEN': S(g_VIETLIEN, [3, 3, 3]),
}
