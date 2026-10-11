import itertools
from functools import lru_cache
from collections import deque
def ints(s): return list(map(int, s.split()))

# ---------- BATTAY
def gen_BATTAY(r):
    n = r.randint(1, 5); return f"{n}\n{' '.join(str(r.randint(0,4)) for _ in range(n))}\n"
def brute_BATTAY(inp):
    a = ints(inp); n = a[0]; d = tuple(a[1:])
    @lru_cache(None)
    def ok(d):
        if sum(d) == 0: return True
        i = next(k for k in range(len(d)) if d[k] > 0)
        for j in range(len(d)):
            if j != i and d[j] > 0:
                e = list(d); e[i] -= 1; e[j] -= 1
                if ok(tuple(e)): return True
        return False
    return str(sum(d)//2) if ok(d) else "-1"

# ---------- NOITIENG
def gen_NOITIENG(r):
    n = r.randint(2, 5); e = []
    c = r.randint(1, n)
    for _ in range(r.randint(0, 14)):
        u, v = r.sample(range(1, n+1), 2)
        if r.random() < 0.5: v = c
        if u == v: continue
        if r.random() < 0.7 and u == c: continue
        e.append((u, v))
    return f"{n} {len(e)}\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_NOITIENG(inp):
    a = ints(inp); n, m = a[0], a[1]; E = set(zip(a[2::2], a[3::2]))
    for v in range(1, n+1):
        if all((u, v) in E for u in range(1, n+1) if u != v) and not any((v, u) in E for u in range(1, n+1)):
            return str(v)
    return "-1"

# ---------- TAMGIAC
def gen_TAMGIAC(r):
    n = r.randint(1, 8); p = r.random()
    e = [(u, v) for u in range(1, n+1) for v in range(u+1, n+1) if r.random() < p]
    r.shuffle(e); e = [(v, u) if r.random() < .5 else (u, v) for u, v in e]
    return f"{n} {len(e)}\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_TAMGIAC(inp):
    a = ints(inp); n = a[0]; E = set()
    for u, v in zip(a[2::2], a[3::2]): E.add((u, v)); E.add((v, u))
    return str(sum(1 for x, y, z in itertools.combinations(range(1, n+1), 3) if (x,y) in E and (y,z) in E and (x,z) in E))

# ---------- CHUYENDOI
def gen_CHUYENDOI(r):
    n = r.randint(1, 6); M = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if r.random() < .5: M[i][j] = M[j][i] = 1
    return f"{n}\n" + "".join(' '.join(map(str, row)) + "\n" for row in M)
def brute_CHUYENDOI(inp):
    a = ints(inp); n = a[0]; M = [a[1+i*n:1+(i+1)*n] for i in range(n)]
    e = [(i+1, j+1) for i in range(n) for j in range(i+1, n) if M[i][j]]
    out = [str(len(e))] + [f"{u} {v}" for u, v in e]
    for i in range(n):
        nb = [j+1 for j in range(n) if M[i][j]]; out.append(' '.join(map(str, [len(nb)] + nb)))
    return '\n'.join(out)

# ---------- BANCHUNG
def gen_BANCHUNG(r):
    n = r.randint(2, 8); e = [(u, v) for u in range(1, n+1) for v in range(u+1, n+1) if r.random() < .5]
    r.shuffle(e); q = [tuple(r.sample(range(1, n+1), 2)) for _ in range(r.randint(1, 8))]
    return f"{n} {len(e)} {len(q)}\n" + "".join(f"{u} {v}\n" for u, v in e) + "".join(f"{u} {v}\n" for u, v in q)
def brute_BANCHUNG(inp):
    a = ints(inp); n, m, q = a[:3]; g = {i: set() for i in range(1, n+1)}; p = 3
    for _ in range(m): u, v = a[p], a[p+1]; p += 2; g[u].add(v); g[v].add(u)
    out = []
    for _ in range(q): u, v = a[p], a[p+1]; p += 2; out.append(str(len(g[u] & g[v])))
    return '\n'.join(out)

# ---------- BANDO
def gen_BANDO(r):
    R, C = r.randint(1, 5), r.randint(1, 5); k = r.randint(0, 4)
    g = [''.join(r.choice('.#') for _ in range(C)) for _ in range(R)]
    q = [(r.randint(1, R), r.randint(1, C)) for _ in range(r.randint(0, 6))]
    return f"{R} {C} {k} {len(q)}\n" + "\n".join(g) + "\n" + "".join(f"{x} {y}\n" for x, y in q)
def brute_BANDO(inp):
    L = inp.split('\n'); R, C, k, q = map(int, L[0].split()); g = [list(L[1+i]) for i in range(R)]
    def cnt():
        c = 0
        for i in range(R):
            for j in range(C):
                if g[i][j] == '.' and sum(1 for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)) if 0<=x<R and 0<=y<C and g[x][y]=='.') == k: c += 1
        return c
    out = [cnt()]
    for t in range(q):
        x, y = map(int, L[1+R+t].split()); g[x-1][y-1] = '#' if g[x-1][y-1] == '.' else '.'; out.append(cnt())
    return '\n'.join(map(str, out))

# ---------- DEMDAO
def gen_DEMDAO(r):
    R, C = r.randint(1, 6), r.randint(1, 6); p = r.random()
    return f"{R} {C}\n" + "".join(''.join('#' if r.random() < p else '.' for _ in range(C)) + "\n" for _ in range(R))
def brute_DEMDAO(inp):
    L = inp.split(); R, C = int(L[0]), int(L[1]); g = L[2:2+R]
    # DSU độc lập với lời giải
    par = list(range(R*C))
    def f(x):
        while par[x] != x: x = par[x]
        return x
    for i in range(R):
        for j in range(C):
            if g[i][j] == '#':
                if i+1 < R and g[i+1][j] == '#': par[f(i*C+j)] = f((i+1)*C+j)
                if j+1 < C and g[i][j+1] == '#': par[f(i*C+j)] = f(i*C+j+1)
    from collections import Counter
    c = Counter(f(i*C+j) for i in range(R) for j in range(C) if g[i][j] == '#')
    return f"{len(c)} {max(c.values()) if c else 0}"

# ---------- CAYKHONG
def gen_CAYKHONG(r):
    T = r.randint(1, 3); s = f"{T}\n"
    for _ in range(T):
        n = r.randint(1, 4); m = r.randint(0, 4)
        e = [(r.randint(1, n), r.randint(1, n)) for _ in range(m)]
        s += f"{n} {m}\n" + "".join(f"{u} {v}\n" for u, v in e)
    return s
def brute_CAYKHONG(inp):
    a = ints(inp); T = a[0]; p = 1; out = []
    for _ in range(T):
        n, m = a[p], a[p+1]; p += 2
        E = []
        for _ in range(m): u, v = a[p], a[p+1]; p += 2; E.append((min(u,v), max(u,v)))
        def is_tree(es):
            if len(es) != n-1: return False
            par = list(range(n+1))
            def f(x):
                while par[x] != x: x = par[x]
                return x
            for u, v in es:
                if f(u) == f(v): return False
                par[f(u)] = f(v)
            return True
        start = tuple(sorted(E)); seen = {start}; dq = deque([(start, 0)])
        pairs = [(u, v) for u in range(1, n+1) for v in range(u+1, n+1)]
        while dq:
            st, d = dq.popleft()
            if is_tree(st): out.append(str(d)); break
            nxt = set(tuple(sorted(st[:i] + st[i+1:])) for i in range(len(st)))
            if len(st) < 7: nxt |= set(tuple(sorted(st + (pp,))) for pp in pairs)
            for s2 in nxt:
                if s2 not in seen: seen.add(s2); dq.append((s2, d+1))
    return '\n'.join(out)

# ---------- DUPHONG
def comps(n, E):
    par = list(range(n+1))
    def f(x):
        while par[x] != x: x = par[x]
        return x
    for u, v in E: par[f(u)] = f(v)
    return [f(v) for v in range(n+1)]
def gen_DUPHONG(r):
    n = r.randint(1, 7); e = [(r.randint(1, n), r.randint(1, n)) for _ in range(r.randint(0, 6))]
    e = [(u, v) for u, v in e if u != v]
    return f"{n} {len(e)}\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_DUPHONG(inp):
    a = ints(inp); n, m = a[0], a[1]; E = list(zip(a[2::2], a[3::2]))
    def info(E):
        c = comps(n, E); sz = [sum(1 for w in range(1, n+1) if c[w] == c[v]) for v in range(1, n+1)]
        pairs = sum(1 for u in range(1, n+1) for v in range(u+1, n+1) if c[u] == c[v]); return sz, pairs
    sz, pairs = info(E)
    best = max([pairs] + [info(E + [(u, v)])[1] for u in range(1, n+1) for v in range(u+1, n+1)])
    return ' '.join(map(str, sz)) + f"\n{pairs}\n{best}"

# ---------- MADITUAN
def gen_MADITUAN(r):
    N = r.randint(1, 7); q = [(r.randint(1, N), r.randint(1, N)) for _ in range(r.randint(1, 6))]
    return f"{N} {r.randint(1,N)} {r.randint(1,N)} {len(q)}\n" + "".join(f"{x} {y}\n" for x, y in q)
def brute_MADITUAN(inp):
    a = ints(inp); N, sx, sy, Q = a[:4]
    # lặp Bellman-Ford trên lưới thay cho BFS
    INF = 10**9; d = {(x, y): INF for x in range(1, N+1) for y in range(1, N+1)}; d[(sx, sy)] = 0
    mv = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
    ch = True
    while ch:
        ch = False
        for (x, y), v in list(d.items()):
            for dx, dy in mv:
                t = (x+dx, y+dy)
                if t in d and d[t] > v+1: d[t] = v+1; ch = True
    return '\n'.join(str(d[(a[4+2*i], a[5+2*i])] if d[(a[4+2*i], a[5+2*i])] < INF else -1) for i in range(Q))

# ---------- CHAYTRON
def gen_CHAYTRON(r):
    R, C = r.randint(1, 6), r.randint(1, 6)
    g = [[r.choice('...#F') if r.random() < .9 else '.' for _ in range(C)] for _ in range(R)]
    g[r.randrange(R)][r.randrange(C)] = 'J'
    return f"{R} {C}\n" + "".join(''.join(row) + "\n" for row in g)
def brute_CHAYTRON(inp):
    L = inp.split(); R, C = int(L[0]), int(L[1]); g = L[2:2+R]
    fire = {(i, j) for i in range(R) for j in range(C) if g[i][j] == 'F'}
    pos = {(i, j) for i in range(R) for j in range(C) if g[i][j] == 'J'}
    t = 0
    while pos and t < 100:
        for (x, y) in pos:
            if x in (0, R-1) or y in (0, C-1): return str(t+1)
        nf = set(fire)
        for (x, y) in fire:
            for u, v in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if 0 <= u < R and 0 <= v < C and g[u][v] != '#': nf.add((u, v))
        np = set()
        for (x, y) in pos:
            for u, v in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if g[u][v] != '#' and (u, v) not in nf: np.add((u, v))
        fire, pos, t = nf, np, t+1
    return "-1"

# ---------- CHIADOI
def gen_CHIADOI(r):
    n = r.randint(1, 10); e = set()
    for _ in range(r.randint(0, 9)):
        u, v = r.sample(range(1, n+1), 2) if n > 1 else (1, 1)
        if u != v: e.add((min(u,v), max(u,v)))
    return f"{n} {len(e)}\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_CHIADOI(inp):
    a = ints(inp); n, m = a[0], a[1]; E = list(zip(a[2::2], a[3::2])); best = None
    for mask in range(1 << n):
        if all(((mask >> (u-1)) & 1) != ((mask >> (v-1)) & 1) for u, v in E):
            k = bin(mask).count('1'); d = abs(n - 2*k); best = d if best is None else min(best, d)
    return str(-1 if best is None else best)
