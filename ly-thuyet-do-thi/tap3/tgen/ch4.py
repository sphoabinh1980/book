from common import *

def perm1n(r, n):
    """hoán vị nhãn: vị trí 0 là đỉnh 1, vị trí cuối là đỉnh n."""
    p = list(range(2, n)); r.shuffle(p); return [1] + p + [n] if n >= 2 else [1]

# ---------------------------------------------------------------- 12.1
def g_XHGIAIDAU(st, i, r):
    n = r.randint(5, 8) if st == 1 else 100000
    m = (min(r.randint(n, 2 * n), n * (n - 1) // 2 - 2) if st == 1 else 200000)
    p = list(range(1, n + 1)); r.shuffle(p)
    gap = {1: -1, 2: r.randint(0, n - 2), 3: 0, 4: -1}[i]       # khe hở trong chuỗi: gây nhiều đáp án
    E = set((p[k], p[k + 1]) for k in range(n - 1) if k != gap)
    while len(E) < m - (1 if i in (3, 4) else 0):
        a, b = sorted(r.sample(range(n), 2))
        if b - a > (3 if st == 2 else n) and r.random() < 0.7: continue
        if (a, b) == (gap, gap + 1): continue
        E.add((p[a], p[b]))
    if i in (3, 4):   # một vòng mâu thuẫn ở cuối bảng
        a = r.randint(n // 2, n - 2); E.add((p[n - 1], p[a]))
    E = list(E); r.shuffle(E)
    return f'{n} {len(E)}\n' + edges_txt(E)

# ---------------------------------------------------------------- 12.2
def g_XAYNHA(st, i, r):
    n = 1000 if st == 1 else 100000
    p = list(range(1, n + 1)); r.shuffle(p)       # p[k]: công việc ở vị trí k của một thứ tự tô pô
    pre = {}
    for k in range(n):
        c = r.randint(0, min(k, 3)) if k else 0
        pre[p[k]] = [p[x] for x in set(r.randint(max(0, k - 5), k - 1) for _ in range(c))] if c else []
    hi = [10**9, 2, 3][i - 1]
    s = f'{n}\n'
    for v in range(1, n + 1):
        s += ' '.join(map(str, [r.randint(1, hi), len(pre[v])] + pre[v])) + '\n'
    return s

# ---------------------------------------------------------------- 12.3
def g_DEMLOTRINH(st, i, r):
    n, m = (1000, 1000) if st == 2 else (100000, 200000)
    if st == 1:
        E = [(k, k + 1) for k in range(1, n)] if i == 1 else []
        while len(E) < m:
            a = r.randint(1, n - 1); b = min(n, a + r.randint(1, 4)); E.append((a, b))
        r.shuffle(E); return f'{n} {len(E)}\n' + edges_txt(E)
    core = n - 10 if i != 1 or st == 2 else n
    lab = list(range(2, n)); r.shuffle(lab)
    p = [1] + lab[: core - 2] + [n]; others = lab[core - 2:]
    E = [(p[k], p[k + 1]) for k in range(core - 1)]
    while len(E) < m - 12:
        a = r.randint(0, core - 2); b = min(core - 1, a + r.randint(1, 4)); E.append((p[a], p[b]))
    if others:   # các nút "chết": có vòng nhưng không tới được n, và vòng không tới được từ 1
        d = others
        E += [(p[r.randint(0, core - 2)], d[0]), (d[0], d[1]), (d[1], d[0]), (d[2], d[2]),
              (d[1], d[2]), (d[3], d[4]), (d[4], d[3]), (d[4], n)]
    if i == 3:   # một vòng nằm trên lộ trình 1 → n: vô số
        a = r.randint(core // 3, core - 3); E.append((p[a + 2], p[a]))
    r.shuffle(E)
    return f'{n} {len(E)}\n' + edges_txt(E)

# ---------------------------------------------------------------- 13.x
def blocks_graph(r, n, m, multi, conn, deep, bsz=6):
    """đồ thị gồm các 'khối' (vòng + dây cung) nối với nhau bằng cầu."""
    p = list(range(1, n + 1)); r.shuffle(p)
    B = []; k = 0
    while k < n:
        s = r.randint(1, bsz); B.append(p[k:k + s]); k += s
    E = []
    for b in B:
        if len(b) >= 3: E += [(b[j], b[(j + 1) % len(b)]) for j in range(len(b))]
        elif len(b) == 2: E.append((b[0], b[1])); E += [(b[0], b[1])] if multi and r.random() < 0.5 else []
    for j in range(1, len(B)):
        if not conn and r.random() < 0.02: continue
        o = j - 1 if deep and r.random() < 0.9 else r.randint(0, j - 1)
        e = (r.choice(B[j]), r.choice(B[o])); E.append(e)
        if multi and r.random() < 0.1: E.append(e[::-1])          # cạnh song song: không còn là cầu
    big = [b for b in B if len(b) >= 4]
    while len(E) < m and big:
        b = r.choice(big); u, v = r.sample(b, 2)
        if multi or abs(b.index(u) - b.index(v)) not in (1, len(b) - 1): E.append((u, v))
    if not multi:
        S = set(); F = []
        for u, v in E:
            k = (min(u, v), max(u, v))
            if k not in S: S.add(k); F.append((u, v))
        E = F
    r.shuffle(E)
    return E

def g_HUYETMACH(st, i, r):
    n, m = (1000, 1000) if st == 1 else (100000, 200000)
    if i == 3 and st == 3:
        E = rand_tree(r, n, deep=True); E.append(E[0]); r.shuffle(E)
    else:
        E = blocks_graph(r, n, m if i != 1 else int(1.2 * n), multi=(st != 2), conn=(i != 2), deep=(i == 1), bsz=[6, 6, 10][i - 1])
    return f'{n} {len(E)}\n' + edges_txt(E)

def g_BIENAP(st, i, r):
    n, m = (1000, 1000) if st == 1 else (100000, 200000)
    if i == 1: E = rand_tree(r, n, deep=(st == 2))
    elif i == 2: E = blocks_graph(r, n, m, multi=False, conn=True, deep=True, bsz=4)
    else:
        E = rand_tree(r, n) + [tuple(r.sample(range(1, n + 1), 2)) for _ in range(m - n + 1)]
    return f'{n} {len(E)}\n' + edges_txt(E)

def g_CAPDUPHONG(st, i, r):
    n, m = [(100000, 99999), (1000, 1000), (100000, 200000)][st - 1]
    if st == 1:
        E = rand_tree(r, n, deep=(i == 1)) if i != 3 else [(1, v) for v in range(2, n + 1)]
        return f'{n} {len(E)}\n' + edges_txt(E)
    E = blocks_graph(r, n, m, multi=True, conn=True, deep=(i == 1), bsz=[5, 8, 3][i - 1])
    return f'{n} {len(E)}\n' + edges_txt(E)

# ---------------------------------------------------------------- 14.x
def scc_graph(r, n, m, dag, deep_cycle=False, gsz=5):
    p = list(range(1, n + 1)); r.shuffle(p)
    if deep_cycle:
        E = [(p[k], p[(k + 1) % n]) for k in range(n)]
        h = p[: n // 2]
        while len(E) < m: E.append(tuple(r.sample(h, 2)))
        r.shuffle(E); return E
    G = []; k = 0
    while k < n:
        s = 1 if dag else r.choice([1, 1, 2, 3, gsz]); G.append(p[k:k + s]); k += s
    E = []
    for g in G:
        if len(g) >= 2: E += [(g[j], g[(j + 1) % len(g)]) for j in range(len(g))]
    while len(E) < m:
        a, b = sorted(r.sample(range(len(G)), 2))
        if r.random() < 0.3: continue
        E.append((r.choice(G[a]), r.choice(G[b])))
    r.shuffle(E); return E

def g_TINDON(st, i, r):
    n, m = (1000, 1000) if st == 2 else (100000, 200000)
    if st == 1: E = scc_graph(r, n, [m, n // 2, m][i - 1], dag=True)
    else: E = scc_graph(r, n, [m, n // 2, m, m][i - 1], dag=False, deep_cycle=(st == 3 and i == 3))
    if st == 3 and i == 4: E = [(k, k + 1) for k in range(1, n)][::-1]   # chuỗi dài: 1 người
    return f'{n} {len(E)}\n' + edges_txt(E)

def g_KHOBAU(st, i, r):
    n, m = 100000, 200000
    if st == 1:
        p = list(range(1, n + 1)); r.shuffle(p); p.remove(1); p = [1] + p
        E = [(p[k], p[k + 1]) for k in range(n - 1)] if i == 1 else []
        while len(E) < m:
            a = r.randint(0, n - 2); b = min(n - 1, a + r.randint(1, [3, 50, 3][i - 1])); E.append((p[a], p[b]))
    else:
        E = scc_graph(r, n, m, dag=False, deep_cycle=(i == 3), gsz=[5, 50, 5][i - 1])
    g = [r.randint(0, 10**9) for _ in range(n)]
    return f'{n} {len(E)}\n' + ' '.join(map(str, g)) + '\n' + edges_txt(E)

def g_TUYENCHON(st, i, r):
    n, m = (r.randint(15, 20), 60) if st == 1 else (100000, 100000)
    hid = [None] + [r.randint(0, 1) for _ in range(n)]
    lit = lambda v, val: v if val else -v
    W = []
    while len(W) < m:
        a, b = r.randint(1, n), r.randint(1, n)
        x, y = lit(a, r.randint(0, 1)), lit(b, r.randint(0, 1))
        if (x > 0) != hid[a] and (y > 0) != hid[b]: continue      # cả hai đều sai theo phương án ẩn
        W.append((x, y))
    if i == 2:   # mâu thuẫn: dây chuyền x → ... → ¬x và ¬x → ... → x
        L = r.sample(range(1, n + 1), min(n, 8)); x = L[0]
        for k in range(len(L) - 1): W.append((-L[k], L[k + 1]))     # L[k] → L[k+1]
        W.append((-L[-1], -x))                                    # L[-1] → ¬x
        W.append((x, x))                                          # ¬x → x
        r.shuffle(W)
    return f'{n} {len(W)}\n' + edges_txt(W)

def chk_TUYENCHON(inp, out, ans):
    o = out.split()
    if ans.split()[0] == 'NO': return o == ['NO']
    a = list(map(int, inp.split())); n = a[0]
    if len(o) != 2 or o[0] != 'YES' or len(o[1]) != n: return False
    s = o[1]
    ok = lambda x: (s[abs(x) - 1] == '1') == (x > 0)
    return all(ok(a[k]) or ok(a[k + 1]) for k in range(2, len(a), 2))

# ---------------------------------------------------------------- 15.x
def euler_fig(r, n, m, kind, loops):
    """kind: 0 = chu trình Euler, 1 = đường Euler, 2 = bốn đỉnh bậc lẻ, 3 = hai mảnh rời."""
    vs = r.sample(range(1, n + 1), max(2, n // 2) if kind != 3 else n)
    if kind == 3:
        A, B = vs[: len(vs) // 2], vs[len(vs) // 2:]
        return walk(r, A, m // 2, True, loops) + walk(r, B, m - m // 2, True, loops)
    E = walk(r, vs, m - (kind == 2), kind == 0, loops)
    if kind == 2:
        u, v = r.sample(vs, 2)
        E.append((u, v))
    return E
def walk(r, vs, m, closed, loops):
    cur = start = vs[0]; E = []
    for k in range(m - (1 if closed else 0)):
        nx = cur if loops and r.random() < 0.05 else r.choice(vs)
        if nx == cur and not loops: nx = vs[(vs.index(cur) + 1) % len(vs)]
        E.append((cur, nx)); cur = nx
    if closed:
        if cur == start and not loops: E.append((cur, vs[1])); E.append((vs[1], start))
        else: E.append((cur, start))
    return E

def g_NETVE(st, i, r):
    T = 5; s = f'{T}\n'
    for t in range(T):
        n, m = (100000, 200000) if t < 2 else (r.randint(5, 2000), r.randint(5, 4000))
        if st == 1: kind = r.choice([0, 1, 2])
        else: kind = r.choice([0, 1, 2, 3])
        E = euler_fig(r, n if st == 2 else n, m, kind, loops=(st == 2))
        if st == 1:   # mọi điểm đều có đoạn nối, liên thông: đánh lại nhãn các điểm đã dùng
            used = sorted(set(x for e in E for x in e)); mp = {v: k + 1 for k, v in enumerate(used)}
            E = [(mp[u], mp[v]) for u, v in E]; n = len(used)
        r.shuffle(E)
        s += f'{n} {len(E)}\n' + edges_txt(E)
    return s

def g_DOMINO(st, i, r):
    n = r.randint(5, 8) if st == 1 else 100000
    hi = r.choice([3, 6])
    if i == 3:   # hai nhóm số chấm rời nhau
        D = walk(r, list(range(0, 3)), n // 2, True, True) + walk(r, list(range(3, 7)), n - n // 2, True, True)
    else:
        D = walk(r, list(range(0, hi + 1)), n, i == 1, True)
        if i == 4:
            D[-1] = (D[-1][0], (D[-1][1] + 1) % (hi + 1))    # thường làm hỏng: bốn số lẻ
    r.shuffle(D)
    D = [(a, b) if r.random() < 0.5 else (b, a) for a, b in D]
    return f'{len(D)}\n' + edges_txt(D)

def chk_DOMINO(inp, out, ans):
    o = out.split()
    if ans.split()[0] == 'NO': return o == ['NO']
    a = list(map(int, inp.split())); n = a[0]; D = [None] + [(a[1 + 2 * k], a[2 + 2 * k]) for k in range(n)]
    if len(o) != 2 * n: return False
    try: ids = [int(o[2 * k]) for k in range(n)]
    except ValueError: return False
    if sorted(ids) != list(range(1, n + 1)): return False
    seq = []
    for k in range(n):
        if o[2 * k + 1] not in '+-': return False
        seq.append(D[ids[k]] if o[2 * k + 1] == '+' else D[ids[k]][::-1])
    return all(seq[k][1] == seq[k + 1][0] for k in range(n - 1))

KS = {1: [(10, 2), (1, 1), (7, 1)], 2: [(2, 10), (3, 6), (10, 3), (1, 5)], 3: [(10, 6), (2, 19), (3, 12), (5, 8)]}
def g_KETSAT(st, i, r):
    b, k = KS[st][i - 1]; return f'{b} {k}\n'

def chk_KETSAT(inp, out, ans):
    b, k = map(int, inp.split()); o = out.split()
    if len(o) != 2 or not o[0].isdigit(): return False
    L, s = int(o[0]), o[1]
    if L != len(s) or L != b ** k + k - 1: return False
    if set(s) - set(str(d) for d in range(b)): return False
    return len(set(s[j:j + k] for j in range(L - k + 1))) == b ** k

def S(gen, subtasks, ntests, tl=1, mem=256, check=None):
    return {'gen': gen, 'subtasks': subtasks, 'ntests': ntests, 'tl': tl, 'mem': mem, 'check': check, 'mod': 'ch4'}
SPEC = {
    'XHGIAIDAU': S(g_XHGIAIDAU, [30, 70], [4, 4]),
    'XAYNHA': S(g_XAYNHA, [40, 60], [3, 3]),
    'DEMLOTRINH': S(g_DEMLOTRINH, [30, 30, 40], [2, 3, 3]),
    'HUYETMACH': S(g_HUYETMACH, [30, 30, 40], [3, 3, 3]),
    'BIENAP': S(g_BIENAP, [30, 70], [3, 3]),
    'CAPDUPHONG': S(g_CAPDUPHONG, [20, 30, 50], [3, 3, 3]),
    'TINDON': S(g_TINDON, [30, 30, 40], [3, 3, 4]),
    'KHOBAU': S(g_KHOBAU, [30, 70], [3, 3]),
    'TUYENCHON': S(g_TUYENCHON, [20, 80], [3, 3], check=chk_TUYENCHON),
    'NETVE': S(g_NETVE, [30, 70], [3, 3]),
    'DOMINO': S(g_DOMINO, [30, 70], [4, 4], check=chk_DOMINO),
    'KETSAT': S(g_KETSAT, [20, 30, 50], [3, 4, 4], check=chk_KETSAT),
}
