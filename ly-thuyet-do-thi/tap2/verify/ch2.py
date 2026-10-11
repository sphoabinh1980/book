import itertools, heapq, math
from collections import deque
def ints(s): return list(map(int, s.split()))
INF = float('inf')

def gen_DUONGTRUONG(r):
    n = r.randint(1, 6); e = [(r.randint(1,n), r.randint(1,n), r.randint(0, 10**9 if r.random()<.2 else 9)) for _ in range(r.randint(0, 10))]
    e = [x for x in e if x[0] != x[1]]
    return f"{n} {len(e)} {r.randint(1,n)}\n" + "".join(f"{u} {v} {w}\n" for u, v, w in e)
def brute_DUONGTRUONG(inp):
    a = ints(inp); n, m, s = a[:3]; d = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(n+1): d[i][i] = 0
    for i in range(m): u, v, w = a[3+3*i:6+3*i]; d[u][v] = min(d[u][v], w)
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1): d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return ' '.join(str(d[s][v] if d[s][v] < INF else -1) for v in range(1, n+1))

def gen_NUTGIAO(r):
    n = r.randint(2, 7); e = []
    p = list(range(1, n+1)); r.shuffle(p)
    for i in range(n-1): e.append((p[i], p[i+1], r.randint(1, 3)))
    for _ in range(r.randint(0, 8)):
        u, v = r.sample(range(1, n+1), 2); e.append((u, v, r.randint(1, 3)))
    r.shuffle(e)
    return f"{n} {len(e)}\n" + "".join(f"{u} {v} {w}\n" for u, v, w in e)
def brute_NUTGIAO(inp):
    a = ints(inp); n, m = a[:2]; g = {i: [] for i in range(1, n+1)}
    for i in range(m): u, v, w = a[2+3*i:5+3*i]; g[u].append((v, w)); g[v].append((u, w))
    best = [INF]; paths = []
    def dfs(u, vis, L, path):
        if L > best[0]: return
        if u == n:
            if L < best[0]: best[0] = L; paths.clear()
            paths.append(set(path)); return
        for v, w in g[u]:
            if v not in vis: vis.add(v); path.append(v); dfs(v, vis, L+w, path); path.pop(); vis.discard(v)
    dfs(1, {1}, 0, [1])
    res = sorted(set.intersection(*paths))
    return f"{len(res)}\n" + ' '.join(map(str, res))

def dep(t, a, p, b):
    d = a if t <= a else a + (t - a + p - 1)//p*p
    return d if d <= b else None
def gen_XEBUYT(r):
    n = r.randint(2, 6); e = []
    for _ in range(r.randint(1, 10)):
        u, v = r.sample(range(1, n+1), 2); a = r.randint(0, 10); p = r.randint(1, 5); b = a + r.randint(0, 20)
        e.append((u, v, r.randint(1, 6), a, p, b))
    return f"{n} {len(e)}\n" + "".join(' '.join(map(str, x)) + "\n" for x in e)
def brute_XEBUYT(inp):
    a = ints(inp); n, m = a[:2]; E = [a[2+6*i:8+6*i] for i in range(m)]
    # mô phỏng theo từng phút: tập các bến đã có mặt
    T = 200; arrive = {}  # (time) -> set of stations reached at that time
    at = [INF]*(n+1); at[1] = 0
    events = {0: {1}}
    present = set()
    for t in range(T+1):
        present |= events.get(t, set())
        if n in present: return str(t)
        for u, v, w, aa, p, b in E:
            if u in present and t >= aa and t <= b and (t - aa) % p == 0:
                events.setdefault(t+w, set()).add(v)
    return "-1"

def gen_DOITIEN(r):
    while True:
        n = r.randint(1, 5); e = []
        for _ in range(r.randint(0, 8)):
            if n < 2: break
            u, v = r.sample(range(1, n+1), 2); e.append((u, v, r.choice([0.5, 0.8, 0.9, 1.1, 1.25, 2, 0.95, 1.05, 3, 0.3])))
        # loại bộ test có chu trình tích quá gần 1
        bad = False
        for k in range(2, n+1):
            for cyc in itertools.permutations(range(1, n+1), k):
                if cyc[0] != min(cyc): continue
                for combo in itertools.product(*[[x[2] for x in e if x[0]==cyc[i] and x[1]==cyc[(i+1)%k]] for i in range(k)]):
                    if abs(math.prod(combo) - 1) < 1e-6: bad = True
        if not bad: break
    return f"{n} {len(e)}\n" + "".join(f"{u} {v} {w}\n" for u, v, w in e)
def brute_DOITIEN(inp):
    L = inp.split(); n, m = int(L[0]), int(L[1]); E = [(int(L[2+3*i]), int(L[3+3*i]), float(L[4+3*i])) for i in range(m)]
    for k in range(2, n+1):
        for cyc in itertools.permutations(range(1, n+1), k):
            for combo in itertools.product(*[[x[2] for x in E if x[0]==cyc[i] and x[1]==cyc[(i+1)%k]] for i in range(k)]):
                if math.prod(combo) > 1 + 1e-9: return "YES"
    return "NO"

def gen_BAYRE(r):
    n = r.randint(2, 5); e = []
    for _ in range(r.randint(0, 9)):
        u, v = r.sample(range(1, n+1), 2); e.append((u, v, r.randint(1, 10)))
    return f"{n} {len(e)} {r.randint(1, n)}\n" + "".join(f"{u} {v} {w}\n" for u, v, w in e)
def brute_BAYRE(inp):
    a = ints(inp); n, m, k = a[:3]; E = [a[3+3*i:6+3*i] for i in range(m)]; best = [INF]
    def go(u, cost, steps):
        if u == n: best[0] = min(best[0], cost)
        if steps == k: return
        for x, y, c in E:
            if x == u: go(y, cost + c, steps + 1)
    go(1, 0, 0)
    return str(best[0] if best[0] < INF else -1)

def gen_LICHTHIDAU(r):
    n = r.randint(1, 4); e = []
    for _ in range(r.randint(0, 5)):
        if n < 2: break
        a, b = r.sample(range(1, n+1), 2); e.append((r.randint(1, 2), a, b, r.randint(0, 3)))
    return f"{n} {len(e)}\n" + "".join(' '.join(map(str, x)) + "\n" for x in e)
def brute_LICHTHIDAU(inp):
    a = ints(inp); n, m = a[:2]; E = [a[2+4*i:6+4*i] for i in range(m)]; Lim = 1 + 3*n
    sols = []
    for x in itertools.product(range(1, Lim+1), repeat=n):
        x = (0,) + x
        if all((x[A] >= x[B] + c) if t == 1 else (x[A] <= x[B] + c) for t, A, B, c in E): sols.append(x)
    if not sols: return "-1"
    mn = [min(s[i] for s in sols) for i in range(1, n+1)]
    assert tuple([0] + mn) in sols
    return ' '.join(map(str, mn))

def gen_THUDO(r):
    n = r.randint(1, 6); e = []
    for v in range(2, n+1): e.append((v, r.randint(1, v-1), r.randint(1, 9)))
    for _ in range(r.randint(0, 6)):
        if n < 2: break
        u, v = r.sample(range(1, n+1), 2); e.append((u, v, r.randint(1, 9)))
    r.shuffle(e)
    return f"{n} {len(e)}\n" + "".join(f"{u} {v} {w}\n" for u, v, w in e)
def brute_THUDO(inp):
    a = ints(inp); n, m = a[:2]; g = {i: [] for i in range(1, n+1)}
    for i in range(m): u, v, w = a[2+3*i:5+3*i]; g[u].append((v, w)); g[v].append((u, w))
    best = None
    for s in range(1, n+1):
        d = {s: 0}; pq = [(0, s)]
        while pq:
            du, u = heapq.heappop(pq)
            if du > d[u]: continue
            for v, w in g[u]:
                if du + w < d.get(v, INF): d[v] = du + w; heapq.heappush(pq, (d[v], v))
        tot = sum(d.values())
        if best is None or tot < best[1]: best = (s, tot)
    return f"{best[0]} {best[1]}"

def gen_XEPHANG(r):
    n = r.randint(1, 7); p = list(range(1, n+1)); r.shuffle(p); e = set()
    for _ in range(r.randint(0, 12)):
        if n < 2: break
        i, j = sorted(r.sample(range(n), 2)); e.add((p[i], p[j]))
    return f"{n} {len(e)}\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_XEPHANG(inp):
    a = ints(inp); n, m = a[:2]; E = list(zip(a[2::2], a[3::2]))
    perms = [q for q in itertools.permutations(range(1, n+1)) if all(q.index(u) < q.index(v) for u, v in E)]
    res = [v for v in range(1, n+1) if len(set(q.index(v) for q in perms)) == 1]
    return f"{len(res)}\n" + ' '.join(map(str, res))

def gen_XETAI(r):
    n = r.randint(2, 6); e = []
    for _ in range(r.randint(0, 8)):
        u, v = r.sample(range(1, n+1), 2); e.append((u, v, r.randint(1, 10)))
    q = [r.sample(range(1, n+1), 2) for _ in range(r.randint(1, 5))]
    return f"{n} {len(e)} {len(q)}\n" + "".join(f"{u} {v} {w}\n" for u, v, w in e) + "".join(f"{s} {t}\n" for s, t in q)
def brute_XETAI(inp):
    a = ints(inp); n, m, q = a[:3]; E = [a[3+3*i:6+3*i] for i in range(m)]; out = []
    for i in range(q):
        s, t = a[3+3*m+2*i:5+3*m+2*i]; best = 0
        for W in range(1, 11):
            seen = {s}; st = [s]
            while st:
                u = st.pop()
                for x, y, c in E:
                    if c >= W:
                        for p_, q_ in ((x, y), (y, x)):
                            if p_ == u and q_ not in seen: seen.add(q_); st.append(q_)
            if t in seen: best = W
        out.append(str(best))
    return '\n'.join(out)

def gen_DENGIAOTHONG(r):
    n = r.randint(1, 6); P = r.randint(1, 5); e = []
    for _ in range(r.randint(0, 8)):
        if n < 2: break
        u, v = r.sample(range(1, n+1), 2); e.append((u, v))
    s = [''.join(r.choice('01') if r.random() < .8 else '0' for _ in range(P)) for _ in range(n)]
    return f"{n} {len(e)} {P}\n" + "\n".join(s) + "\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_DENGIAOTHONG(inp):
    L = inp.split(); n, m, P = int(L[0]), int(L[1]), int(L[2]); s = [''] + L[3:3+n]
    E = [(int(L[3+n+2*i]), int(L[4+n+2*i])) for i in range(m)]
    cur = {1}
    for t in range(0, 200):
        if n in cur: return str(t)
        nxt = set(cur)
        for u in cur:
            if s[u][t % P] == '1':
                for x, y in E:
                    if x == u: nxt.add(y)
                    if y == u: nxt.add(x)
        cur = nxt
    return "-1"

def gen_PHATUONG(r):
    R, C = r.randint(1, 4), r.randint(1, 4)
    g = [[r.choice('..#') for _ in range(C)] for _ in range(R)]
    cells = [(i, j) for i in range(R) for j in range(C)]
    if len(cells) < 2: R, C = 1, 2; g = [['.', '.']]; cells = [(0,0),(0,1)]
    s, t = r.sample(cells, 2); g[s[0]][s[1]] = 'S'; g[t[0]][t[1]] = 'T'
    return f"{R} {C} {r.randint(0, 3)}\n" + "".join(''.join(row) + "\n" for row in g)
def brute_PHATUONG(inp):
    L = inp.split(); R, C, K = int(L[0]), int(L[1]), int(L[2]); g = L[3:3+R]
    walls = [(i, j) for i in range(R) for j in range(C) if g[i][j] == '#']
    S = next((i, j) for i in range(R) for j in range(C) if g[i][j] == 'S')
    best = INF
    for k in range(0, min(K, len(walls)) + 1):
        for br in itertools.combinations(walls, k):
            br = set(br); d = {S: 0}; q = deque([S])
            while q:
                x, y = q.popleft()
                for u, v in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if 0 <= u < R and 0 <= v < C and (g[u][v] != '#' or (u, v) in br) and (u, v) not in d:
                        d[(u, v)] = d[(x, y)] + 1; q.append((u, v))
            for (x, y), v in d.items():
                if g[x][y] == 'T': best = min(best, v)
    return str(best if best < INF else -1)

def gen_ROBOTXOAY(r):
    R, C = r.randint(1, 5), r.randint(1, 5)
    g = [[r.choice('...#') for _ in range(C)] for _ in range(R)]
    cells = [(i, j) for i in range(R) for j in range(C)]
    if len(cells) < 2: R, C = 1, 2; g = [['.', '.']]; cells = [(0,0),(0,1)]
    s, t = r.sample(cells, 2); g[s[0]][s[1]] = 'S'; g[t[0]][t[1]] = 'T'
    return f"{R} {C} {r.choice('NESW')}\n" + "".join(''.join(row) + "\n" for row in g)
def brute_ROBOTXOAY(inp):
    L = inp.split(); R, C, h = int(L[0]), int(L[1]), L[2]; g = L[3:3+R]
    D = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}; order = 'NESW'
    S = next((i, j) for i in range(R) for j in range(C) if g[i][j] == 'S')
    dist = {(S, h): 0}; pq = [(0, S, h)]
    while pq:
        c, (x, y), k = heapq.heappop(pq)
        if c > dist[((x, y), k)]: continue
        if g[x][y] == 'T': return str(c)
        dx, dy = D[k]; u, v = x+dx, y+dy
        nxt = []
        if 0 <= u < R and 0 <= v < C and g[u][v] != '#': nxt.append((c, (u, v), k))
        i = order.index(k)
        nxt += [(c+1, (x, y), order[(i+1) % 4]), (c+1, (x, y), order[(i+3) % 4])]
        for c2, p2, k2 in nxt:
            if c2 < dist.get((p2, k2), INF): dist[(p2, k2)] = c2; heapq.heappush(pq, (c2, p2, k2))
    return "-1"
