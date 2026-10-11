from common import *
from collections import Counter

# ---------------------------------------------------------------- 16.1
def g_XEPPHONG(st, i, r):
    if st == 1: n, m = r.randint(6, 10), r.randint(6, 10)
    else: n, m = 1000, 1000
    L = []
    for s in range(n):
        if st == 2 and i == 1: k = r.randint(50, 100)
        elif st == 2 and i == 3: k = 2                       # dây chuyền: s chọn được phòng s, s+1
        else: k = r.randint(1, min(3, m))
        if st == 2 and i == 3: rooms = [min(m, s % m + 2), s % m + 1]
        else: rooms = r.sample(range(1, m + 1), k)
        L.append(sorted(set(rooms)) if r.random() < 0.5 else list(dict.fromkeys(rooms)))
    return f'{n} {m}\n' + ''.join(' '.join(map(str, [len(x)] + x)) + '\n' for x in L)

# ---------------------------------------------------------------- 16.2
def g_DATDOMINO(st, i, r):
    if st == 1: R, C = [(100, 100), (99, 97), (1, 100)][i - 1]
    elif st == 2: R, C = r.randint(6, 10), r.randint(6, 10)
    else: R, C = 100, 100
    wall = 0 if st == 1 else [0.1, 0.3, 0.45][i - 1]
    g = [''.join('#' if r.random() < wall else '.' for _ in range(C)) for _ in range(R)]
    return f'{R} {C}\n' + '\n'.join(g) + '\n'

# ---------------------------------------------------------------- 16.3
def g_CAMERA(st, i, r):
    if st == 1: R, C, K = 8, 8, r.randint(10, 30)
    else: R, C, K = 1000, 1000, [100000, 3000, 100000][i - 1]
    S = set()
    while len(S) < K:
        if i == 3 and st != 1:   # ô dồn vào ít hàng / ít cột: đáp số nhỏ, nhiều cách chọn
            rr = r.randint(1, 60) if r.random() < 0.5 else r.randint(1, R)
            cc = r.randint(1, C) if rr <= 60 else r.randint(1, 60)
        else: rr, cc = r.randint(1, R), r.randint(1, C)
        S.add((rr, cc))
    S = list(S); r.shuffle(S)
    return f'{R} {C} {K}\n' + edges_txt(S)

def chk_CAMERA(inp, out, ans, st):
    o = out.split(); a = ans.split()
    if not o or o[0] != a[0]: return False
    if st == 2: return True
    t = int(o[0])
    if len(o) != 1 + 2 * t: return False
    rows, cols = set(), set()
    for k in range(t):
        kind, x = o[1 + 2 * k], o[2 + 2 * k]
        if kind == 'H': rows.add(int(x))
        elif kind == 'C': cols.add(int(x))
        else: return False
    if len(rows) + len(cols) != t: return False
    v = list(map(int, inp.split()))
    return all(v[j] in rows or v[j + 1] in cols for j in range(3, len(v), 2))

# ---------------------------------------------------------------- 17.1
def g_DUONGONG(st, i, r):
    n, m = 500, 5000
    hi = [10**9, 3, 1][i - 1]                       # trọng số nhỏ: nhiều lát cắt cùng dung lượng
    L = 10; lay = [[1]] + [[] for _ in range(L)] + [[n]]
    for v in range(2, n): lay[r.randint(1, L)].append(v)
    E = []
    while len(E) < m:
        a = r.randint(0, L); b = min(L + 1, a + r.choice([1, 1, 1, 2]))
        if r.random() < 0.15: a, b = b, a           # một ít ống đi ngược
        u, v = r.choice(lay[a]), r.choice(lay[b])
        if u != v: E.append((u, v, r.randint(1, hi)))
    return f'{n} {m}\n' + ''.join(f'{u} {v} {c}\n' for u, v, c in E)

def chk_DUONGONG(inp, out, ans, st):
    o, a = out.split(), ans.split()
    return o[:1] == a[:1] if st == 1 else o == a

# ---------------------------------------------------------------- 17.2
def g_ROINHAU(st, i, r):
    n, m = 1000, 10000
    L = [8, 30, 4][i - 1]; lay = [[1]] + [[] for _ in range(L)] + [[n]]
    for v in range(2, n): lay[r.randint(1, L)].append(v)
    E = []
    while len(E) < m:
        a = r.randint(0, L); b = min(L + 1, a + 1)
        if r.random() < 0.2: b = r.randint(1, L)          # đường "ngang" hoặc đi ngược: tạo vòng
        u, v = r.choice(lay[a]), r.choice(lay[b])
        if u == v: continue
        E.append((u, v))
        if r.random() < 0.1: E.append((u, v))             # đường song song
    x = r.randint(2, n - 1)
    E = E[:m - 6] + [(1, x)] * 3 + [(x, n)] * 3          # ba lộ trình 1 → x → n dùng ba cặp đường song song
    r.shuffle(E)
    return f'{n} {len(E)}\n' + edges_txt(E)

def chk_ROINHAU(inp, out, ans, st):
    o, a = out.split(), ans.split()
    if not o or o[0] != a[0]: return False
    if st == 1: return True
    v = list(map(int, inp.split())); n = v[0]
    avail = Counter(zip(v[2::2], v[3::2]))
    o = list(map(int, o)); k = o[0]; p = 1
    for _ in range(k):
        if p >= len(o): return False
        Lp = o[p]; path = o[p + 1:p + 1 + Lp]; p += 1 + Lp
        if len(path) != Lp or Lp < 2 or path[0] != 1 or path[-1] != n or len(set(path)) != Lp: return False
        for x, y in zip(path, path[1:]):
            if avail[(x, y)] <= 0: return False
            avail[(x, y)] -= 1
    return p == len(o)

# ---------------------------------------------------------------- 17.3
def g_TRUCNHAT(st, i, r):
    n, d = (r.randint(6, 8), r.randint(6, 8)) if st == 1 else (200, 200)
    ok = [sorted(r.sample(range(1, d + 1), r.randint(0, d if st == 1 else 60))) for _ in range(n)]
    A, B = [], [0] * (d + 1)
    for s in range(n):
        take = [j for j in ok[s] if r.random() < 0.5]
        for j in take: B[j] += 1
        A.append(min(d, len(take) + r.choice([0, 0, 1, 2])))
    if i == 2:   # không thể: đòi thêm một người cho ngày đông nhất
        j = max(range(1, d + 1), key=lambda x: B[x]); B[j] = min(n, B[j] + 1 + (st == 2) * 3)
    s = f'{n} {d}\n' + ' '.join(map(str, A)) + '\n' + ' '.join(map(str, B[1:])) + '\n'
    s += ''.join(' '.join(map(str, [len(x)] + x)) + '\n' for x in ok)
    return s

def chk_TRUCNHAT(inp, out, ans, st):
    L = out.strip('\n').split('\n')
    if ans.split()[0] == 'NO': return out.split() == ['NO']
    if not L or L[0].strip() != 'YES': return False
    v = list(map(int, inp.split())); n, d = v[0], v[1]
    A = v[2:2 + n]; B = v[2 + n:2 + n + d]; p = 2 + n + d; ok = []
    for _ in range(n): k = v[p]; ok.append(set(v[p + 1:p + 1 + k])); p += 1 + k
    L = L[1:] + [''] * (d + 1 - len(L))
    if len(L) != d: return False
    used = [0] * (n + 1)
    for j in range(1, d + 1):
        try: S = list(map(int, L[j - 1].split()))
        except ValueError: return False
        if len(S) != B[j - 1] or len(set(S)) != len(S): return False
        for x in S:
            if not (1 <= x <= n) or j not in ok[x - 1]: return False
            used[x] += 1
    return all(used[x + 1] <= A[x] for x in range(n))

def S(gen, subtasks, ntests, tl=1, mem=256, check=None):
    return {'gen': gen, 'subtasks': subtasks, 'ntests': ntests, 'tl': tl, 'mem': mem, 'check': check, 'mod': 'ch5', 'stcheck': True}
SPEC = {
    'XEPPHONG': S(g_XEPPHONG, [30, 70], [4, 3]),
    'DATDOMINO': S(g_DATDOMINO, [20, 30, 50], [3, 3, 3]),
    'CAMERA': S(g_CAMERA, [20, 30, 50], [3, 3, 3], check=chk_CAMERA),
    'DUONGONG': S(g_DUONGONG, [40, 60], [3, 3], check=chk_DUONGONG),
    'ROINHAU': S(g_ROINHAU, [40, 60], [3, 3], check=chk_ROINHAU),
    'TRUCNHAT': S(g_TRUCNHAT, [30, 70], [3, 3], check=chk_TRUCNHAT),
}
