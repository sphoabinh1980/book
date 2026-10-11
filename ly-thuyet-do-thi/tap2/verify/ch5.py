import itertools
def ints(s): return list(map(int, s.split()))

def maxmatch_brute(L, adj):
    best = [0]
    def go(i, used, c):
        if c + (L - i) <= best[0]: return
        if i == L: best[0] = max(best[0], c); return
        go(i+1, used, c)
        for v in adj[i]:
            if v not in used: used.add(v); go(i+1, used, c+1); used.discard(v)
    go(0, set(), 0); return best[0]

def gen_XEPPHONG(r):
    n, m = r.randint(1, 6), r.randint(1, 6); s = f"{n} {m}\n"
    for _ in range(n):
        k = r.randint(0, m); s += ' '.join(map(str, [k] + r.sample(range(1, m+1), k))) + "\n"
    return s
def brute_XEPPHONG(inp):
    a = ints(inp); n, m = a[:2]; p = 2; adj = []
    for _ in range(n): k = a[p]; adj.append(a[p+1:p+1+k]); p += 1+k
    return str(maxmatch_brute(n, adj))

def gen_DATDOMINO(r):
    R, C = r.randint(1, 4), r.randint(1, 4)
    return f"{R} {C}\n" + "".join(''.join(r.choice('..#') for _ in range(C)) + "\n" for _ in range(R))
def brute_DATDOMINO(inp):
    L = inp.split(); R, C = int(L[0]), int(L[1]); g = L[2:2+R]
    from functools import lru_cache
    cells = [(i, j) for i in range(R) for j in range(C) if g[i][j] == '.']
    @lru_cache(None)
    def f(mask):
        # mask: các ô đã xử lí; lấy ô đầu tiên chưa xử lí
        for idx, (i, j) in enumerate(cells):
            if not mask >> idx & 1: break
        else: return 0
        best = f(mask | 1 << idx)
        for u, v in ((i+1, j), (i, j+1)):
            if (u, v) in cells:
                k = cells.index((u, v))
                if not mask >> k & 1: best = max(best, 1 + f(mask | 1 << idx | 1 << k))
        return best
    return str(f(0))

def gen_CAMERA(r):
    R, C = r.randint(1, 5), r.randint(1, 5); cells = [(i, j) for i in range(1, R+1) for j in range(1, C+1)]
    K = r.randint(1, len(cells)); ch = r.sample(cells, K)
    return f"{R} {C} {K}\n" + "".join(f"{a} {b}\n" for a, b in ch)
def check_CAMERA(inp, out):
    a = ints(inp); R, C, K = a[:3]; cells = list(zip(a[3::2], a[4::2]))
    adj = [[c for (rr, c) in cells if rr == r] for r in range(1, R+1)]
    best = maxmatch_brute(R, adj)
    o = out.split(); t = int(o[0])
    if t != best: return (False, f'min should be {best}')
    items = [(o[1+2*i], int(o[2+2*i])) for i in range(t)]
    if len(o) != 1 + 2*t or len(set(items)) != t: return (False, 'format')
    rows = {x for k, x in items if k == 'H'}; cols = {x for k, x in items if k == 'C'}
    return (all(r in rows or c in cols for r, c in cells), 'not covering')

def maxflow_py(n, E, s, t):
    cap = {}
    adj = {i: set() for i in range(1, n+1)}
    for u, v, c in E: cap[(u, v)] = cap.get((u, v), 0) + c; cap.setdefault((v, u), 0); adj[u].add(v); adj[v].add(u)
    F = 0
    while True:
        par = {s: None}; st = [s]
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in par and cap[(u, v)] > 0: par[v] = u; st.append(v)
        if t not in par: return F
        f = float('inf'); v = t
        while par[v] is not None: f = min(f, cap[(par[v], v)]); v = par[v]
        v = t
        while par[v] is not None: cap[(par[v], v)] -= f; cap[(v, par[v])] += f; v = par[v]
        F += f

def gen_DUONGONG(r):
    n = r.randint(2, 5); e = []
    for _ in range(r.randint(1, 9)):
        u, v = r.sample(range(1, n+1), 2); e.append((u, v, r.randint(1, 9)))
    return f"{n} {len(e)}\n" + "".join(f"{u} {v} {c}\n" for u, v, c in e)
def brute_DUONGONG(inp):
    a = ints(inp); n, m = a[:2]; E = [a[2+3*i:5+3*i] for i in range(m)]
    others = list(range(2, n)); best = None
    for k in range(len(others)+1):
        for sub in itertools.combinations(others, k):
            S = {1, *sub}; c = sum(e[2] for e in E if e[0] in S and e[1] not in S)
            if best is None or c < best[0] or (c == best[0] and len(S) < len(best[1])): best = (c, S)
    c, S = best
    cut = [i+1 for i, e in enumerate(E) if e[0] in S and e[1] not in S]
    return f"{c}\n{len(cut)}\n" + ' '.join(map(str, cut))

def gen_ROINHAU(r):
    n = r.randint(2, 5); e = []
    for _ in range(r.randint(0, 10)):
        u, v = r.sample(range(1, n+1), 2); e.append((u, v))
    return f"{n} {len(e)}\n" + "".join(f"{u} {v}\n" for u, v in e)
def check_ROINHAU(inp, out):
    from collections import Counter
    a = ints(inp); n, m = a[:2]; E = list(zip(a[2::2], a[3::2]))
    best = maxflow_py(n, [(u, v, 1) for u, v in E], 1, n)
    o = ints(out); k = o[0]; p = 1
    if k != best: return (False, f'k should be {best}')
    avail = Counter(E)
    for _ in range(k):
        L = o[p]; path = o[p+1:p+1+L]; p += 1+L
        if path[0] != 1 or path[-1] != n or len(set(path)) != L: return (False, 'path endpoints/simple')
        for x, y in zip(path, path[1:]):
            if avail[(x, y)] <= 0: return (False, 'edge reuse')
            avail[(x, y)] -= 1
    return (p == len(o), 'trailing')

def gen_TRUCNHAT(r):
    n, d = r.randint(1, 4), r.randint(1, 4)
    A = [r.randint(0, 3) for _ in range(n)]; B = [r.randint(0, 3) for _ in range(d)]
    s = f"{n} {d}\n" + ' '.join(map(str, A)) + "\n" + ' '.join(map(str, B)) + "\n"
    for _ in range(n):
        k = r.randint(0, d); s += ' '.join(map(str, [k] + r.sample(range(1, d+1), k))) + "\n"
    return s
def check_TRUCNHAT(inp, out):
    a = ints(inp); n, d = a[:2]; A = a[2:2+n]; B = a[2+n:2+n+d]; p = 2+n+d; ok = []
    for i in range(n): k = a[p]; ok.append(set(a[p+1:p+1+k])); p += 1+k
    E = [(0+0, i+1, A[i]) for i in range(n)]
    S, T = n+d+1, n+d+2
    E = [(S, i+1, A[i]) for i in range(n)] + [(n+j, T, B[j-1]) for j in range(1, d+1)] + [(i+1, n+j, 1) for i in range(n) for j in ok[i]]
    feas = maxflow_py(n+d+2, E, S, T) == sum(B)
    L = out.split('\n')
    if L[0].strip() == 'NO': return (not feas, 'should be YES')
    if not feas or L[0].strip() != 'YES': return (False, 'should be NO')
    used = [0]*(n+1)
    for j in range(1, d+1):
        st = list(map(int, L[j].split()))
        if len(st) != B[j-1] or len(set(st)) != len(st): return (False, 'day count')
        for i in st:
            if j not in ok[i-1]: return (False, 'not allowed')
            used[i] += 1
    return (all(used[i+1] <= A[i] for i in range(n)), 'over limit')
