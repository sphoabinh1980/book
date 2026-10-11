import itertools
from collections import deque
def ints(s): return list(map(int, s.split()))
def comps(n, E):
    seen = [0]*(n+1); c = 0; sizes = []
    adj = {i: [] for i in range(1, n+1)}
    for u, v in E: adj[u].append(v); adj[v].append(u)
    for s in range(1, n+1):
        if not seen[s]:
            c += 1; seen[s] = c; st = [s]; k = 0
            while st:
                u = st.pop(); k += 1
                for v in adj[u]:
                    if not seen[v]: seen[v] = c; st.append(v)
            sizes.append(k)
    return seen, sizes

def gen_MANGBANBE(r):
    n = r.randint(1, 7); e = [(r.randint(1, n), r.randint(1, n)) for _ in range(r.randint(1, 8))]
    return f"{n} {len(e)}\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_MANGBANBE(inp):
    a = ints(inp); n, m = a[:2]; E = []; out = []
    for i in range(m):
        E.append((a[2+2*i], a[3+2*i])); _, s = comps(n, E); out.append(f"{len(s)} {max(s)}")
    return '\n'.join(out)

def gen_PHACAU(r):
    n = r.randint(1, 6); e = [(r.randint(1, n), r.randint(1, n)) for _ in range(r.randint(1, 8))]
    q = r.sample(range(1, len(e)+1), r.randint(1, len(e)))
    return f"{n} {len(e)} {len(q)}\n" + "".join(f"{u} {v}\n" for u, v in e) + ' '.join(map(str, q)) + "\n"
def brute_PHACAU(inp):
    a = ints(inp); n, m, q = a[:3]; E = [(a[3+2*i], a[4+2*i]) for i in range(m)]; K = a[3+2*m:]
    alive = [True]*m; out = []
    for k in K:
        alive[k-1] = False; _, s = comps(n, [E[i] for i in range(m) if alive[i]]); out.append(str(len(s)))
    return '\n'.join(out)

def gen_HAIPHE(r):
    n = r.randint(2, 6); e = []
    for _ in range(r.randint(1, 9)):
        a, b = r.sample(range(1, n+1), 2); e.append((a, b, r.randint(0, 1)))
    return f"{n} {len(e)}\n" + "".join(f"{a} {b} {t}\n" for a, b, t in e)
def brute_HAIPHE(inp):
    a = ints(inp); n, m = a[:2]; E = [a[2+3*i:5+3*i] for i in range(m)]
    for i in range(1, m+1):
        if not any(all(((x >> (u-1)) & 1) ^ ((x >> (v-1)) & 1) == t for u, v, t in E[:i]) for x in range(1 << n)):
            return str(i)
    return "0"

def gen_NOIMANG(r):
    n = r.randint(1, 5); k = r.randint(0, 2); m = r.randint(0, 6)
    f = [(r.randint(1, n), r.randint(1, n)) for _ in range(k)]
    e = [(r.randint(1, n), r.randint(1, n), r.randint(1, 9)) for _ in range(m)]
    return f"{n} {k} {m}\n" + "".join(f"{u} {v}\n" for u, v in f) + "".join(f"{u} {v} {c}\n" for u, v, c in e)
def brute_NOIMANG(inp):
    a = ints(inp); n, k, m = a[:3]; F = [(a[3+2*i], a[4+2*i]) for i in range(k)]
    E = [a[3+2*k+3*i:6+2*k+3*i] for i in range(m)]; best = None
    for mask in range(1 << m):
        ch = [E[i] for i in range(m) if mask >> i & 1]
        _, s = comps(n, F + [(u, v) for u, v, c in ch])
        if len(s) == 1:
            c = sum(x[2] for x in ch); best = c if best is None else min(best, c)
    return str(-1 if best is None else best)

def gen_ITDOC(r):
    n = r.randint(1, 6); e = [(r.randint(1, n), r.randint(1, n), r.randint(1, 9)) for _ in range(r.randint(0, 8))]
    e = [x for x in e if x[0] != x[1]]
    q = [(r.randint(1, n), r.randint(1, n)) for _ in range(r.randint(1, 5))]
    return f"{n} {len(e)} {len(q)}\n" + "".join(f"{u} {v} {w}\n" for u, v, w in e) + "".join(f"{u} {v}\n" for u, v in q)
def brute_ITDOC(inp):
    a = ints(inp); n, m, q = a[:3]; E = [a[3+3*i:6+3*i] for i in range(m)]; out = []
    for i in range(q):
        u, v = a[3+3*m+2*i:5+3*m+2*i]; ans = -1
        for H in range(0, 10):
            c, _ = comps(n, [(x, y) for x, y, h in E if h <= H])
            if c[u] == c[v]: ans = H; break
        out.append(str(ans))
    return '\n'.join(out)

def gen_GIENGONG(r):
    n = r.randint(1, 4); e = [(r.randint(1, n), r.randint(1, n), r.randint(1, 9)) for _ in range(r.randint(0, 4))]
    e = [x for x in e if x[0] != x[1]]
    return f"{n} {len(e)}\n" + ' '.join(str(r.randint(1, 9)) for _ in range(n)) + "\n" + "".join(f"{u} {v} {c}\n" for u, v, c in e)
def brute_GIENGONG(inp):
    a = ints(inp); n, m = a[:2]; A = a[2:2+n]; E = [a[2+n+3*i:5+n+3*i] for i in range(m)]
    best = None
    for wm in range(1, 1 << n):
        for em in range(1 << m):
            ch = [E[i] for i in range(m) if em >> i & 1]
            c, _ = comps(n, [(x, y) for x, y, _ in ch])
            if all(any(wm >> (w-1) & 1 and c[w] == c[v] for w in range(1, n+1)) for v in range(1, n+1)):
                cost = sum(A[i] for i in range(n) if wm >> i & 1) + sum(x[2] for x in ch)
                best = cost if best is None else min(best, cost)
    return str(best)

def rand_tree_par(r, n):
    perm = list(range(1, n+1)); r.shuffle(perm); par = [0]*(n+1)
    for i in range(1, n): par[perm[i]] = perm[r.randint(0, i-1)]
    return par
def gen_HOHANG(r):
    n = r.randint(1, 8); par = rand_tree_par(r, n); q = [(r.randint(1, n), r.randint(1, n)) for _ in range(r.randint(1, 6))]
    return f"{n}\n" + ' '.join(map(str, par[1:])) + f"\n{len(q)}\n" + "".join(f"{u} {v}\n" for u, v in q)
def brute_HOHANG(inp):
    a = ints(inp); n = a[0]; par = [0] + a[1:1+n]; q = a[1+n]; out = []
    def anc(v):
        L = [v]
        while par[v]: v = par[v]; L.append(v)
        return L
    for i in range(q):
        u, v = a[2+n+2*i:4+n+2*i]; A, B = anc(u), anc(v)
        l = next(x for x in A if x in B); out.append(f"{l} {abs(len(A)-len(B))}")
    return '\n'.join(out)

def gen_CAPQUANG(r):
    n = r.randint(2, 8); e = [(v, r.randint(1, v-1), r.randint(1, 20)) for v in range(2, n+1)]
    p = list(range(1, n+1)); r.shuffle(p); e = [(p[u-1], p[v-1], c) for u, v, c in e]
    q = [r.sample(range(1, n+1), 2) for _ in range(r.randint(1, 6))]
    return f"{n} {len(q)}\n" + "".join(f"{u} {v} {c}\n" for u, v, c in e) + "".join(f"{u} {v}\n" for u, v in q)
def brute_CAPQUANG(inp):
    a = ints(inp); n, q = a[:2]; E = [a[2+3*i:5+3*i] for i in range(n-1)]; out = []
    adj = {i: [] for i in range(1, n+1)}
    for u, v, c in E: adj[u].append((v, c)); adj[v].append((u, c))
    for i in range(q):
        s, t = a[2+3*(n-1)+2*i:4+3*(n-1)+2*i]
        def dfs(u, p, mn):
            if u == t: return mn
            for v, c in adj[u]:
                if v != p:
                    x = dfs(v, u, min(mn, c))
                    if x is not None: return x
        out.append(str(dfs(s, 0, 10**9)))
    return '\n'.join(out)

def gen_CAPK(r):
    n = r.randint(1, 8); par = [0, 0] + [r.randint(1, n) for _ in range(n-1)]
    # đảm bảo là cây gốc 1: sinh qua hoán vị
    perm = [1] + r.sample(range(2, n+1), n-1); par = [0]*(n+1)
    for i in range(1, n): par[perm[i]] = perm[r.randint(0, i-1)]
    q = [(r.randint(1, n), r.randint(0, n+1)) for _ in range(r.randint(1, 6))]
    return f"{n} {len(q)}\n" + ' '.join(map(str, par[2:])) + "\n" + "".join(f"{v} {k}\n" for v, k in q)
def brute_CAPK(inp):
    a = ints(inp); n, q = a[:2]; par = [0, 0] + a[2:2+n-1]; out = []
    for i in range(q):
        v, k = a[1+n+2*i:3+n+2*i]
        while k > 0 and v != 0: v = par[v]; k -= 1
        out.append(str(v if v != 0 else -1))
    return '\n'.join(out)
