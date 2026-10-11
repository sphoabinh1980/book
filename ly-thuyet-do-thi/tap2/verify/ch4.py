import itertools
from collections import Counter
def ints(s): return list(map(int, s.split()))
def ncomp(n, E, nodes=None):
    par = list(range(n+1))
    def f(x):
        while par[x] != x: x = par[x]
        return x
    for u, v in E: par[f(u)] = f(v)
    nodes = range(1, n+1) if nodes is None else nodes
    return len(set(f(v) for v in nodes))

def gen_XHGIAIDAU(r):
    n = r.randint(1, 6); e = set()
    for _ in range(r.randint(0, 10)):
        if n < 2: break
        a, b = r.sample(range(1, n+1), 2); e.add((a, b))
    return f"{n} {len(e)}\n" + "".join(f"{a} {b}\n" for a, b in e)
def brute_XHGIAIDAU(inp):
    a = ints(inp); n, m = a[:2]; E = list(zip(a[2::2], a[3::2]))
    P = [q for q in itertools.permutations(range(1, n+1)) if all(q.index(x) < q.index(y) for x, y in E)]
    if not P: return "-1"
    if len(P) > 1: return "0"
    return ' '.join(map(str, P[0]))

def gen_XAYNHA(r):
    n = r.randint(1, 7); s = f"{n}\n"
    for i in range(1, n+1):
        pre = r.sample(range(1, i), r.randint(0, min(3, i-1))) if i > 1 else []
        s += ' '.join(map(str, [r.randint(1, 5), len(pre)] + pre)) + "\n"
    # hoán vị nhãn để không phải luôn là thứ tự tô pô
    return s
def brute_XAYNHA(inp):
    a = ints(inp); n = a[0]; p = 1; t = [0]*(n+1); pre = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        t[i] = a[p]; k = a[p+1]; pre[i] = a[p+2:p+2+k]; p += 2+k
    def total(t):
        fin = {}
        def F(i):
            if i not in fin: fin[i] = max([F(j) for j in pre[i]] + [0]) + t[i]
            return fin[i]
        return max(F(i) for i in range(1, n+1))
    T = total(t); crit = []
    for i in range(1, n+1):
        t2 = t[:]; t2[i] += 1
        if total(t2) > T: crit.append(i)
    return f"{T}\n{len(crit)}\n" + ' '.join(map(str, crit))

def gen_DEMLOTRINH(r):
    n = r.randint(2, 5); e = [(r.randint(1, n), r.randint(1, n)) for _ in range(r.randint(0, 8))]
    if r.random() < .6: e = [(u, v) for u, v in e if u < v]
    return f"{n} {len(e)}\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_DEMLOTRINH(inp):
    a = ints(inp); n, m = a[:2]; E = list(zip(a[2::2], a[3::2]))
    cur = Counter({1: 1}); total = 0
    for L in range(0, 2*n+2):
        if L >= n and cur.get(n, 0) > 0: return "-1"
        if L < n: total += cur.get(n, 0)
        nxt = Counter()
        for u, c in cur.items():
            for x, y in E:
                if x == u: nxt[y] += c
        cur = nxt
    return str(total % (10**9+7))

def bridges_brute(n, E):
    base = ncomp(n, E); return [i+1 for i in range(len(E)) if ncomp(n, E[:i]+E[i+1:]) > base]
def gen_HUYETMACH(r):
    n = r.randint(1, 6); e = [(r.randint(1, n), r.randint(1, n)) for _ in range(r.randint(0, 8))]
    e = [(u, v) for u, v in e if u != v]
    return f"{n} {len(e)}\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_HUYETMACH(inp):
    a = ints(inp); n, m = a[:2]; E = list(zip(a[2::2], a[3::2])); b = bridges_brute(n, E)
    return f"{len(b)}\n" + ' '.join(map(str, b))

def gen_conn(r, nmax, extra):
    n = r.randint(1, nmax); e = [(v, r.randint(1, v-1)) for v in range(2, n+1)]
    for _ in range(r.randint(0, extra)):
        if n < 2: break
        u, v = r.sample(range(1, n+1), 2); e.append((u, v))
    p = list(range(1, n+1)); r.shuffle(p); e = [(p[u-1], p[v-1]) for u, v in e]; r.shuffle(e)
    return n, e
def gen_BIENAP(r):
    n, e = gen_conn(r, 7, 4); return f"{n} {len(e)}\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_BIENAP(inp):
    a = ints(inp); n, m = a[:2]; E = list(zip(a[2::2], a[3::2])); res = []
    for v in range(1, n+1):
        nodes = [x for x in range(1, n+1) if x != v]
        c = ncomp(n, [(x, y) for x, y in E if x != v and y != v], nodes) if nodes else 0
        if c >= 2: res.append(f"{v} {c}")
    return f"{len(res)}\n" + '\n'.join(res)

def gen_CAPDUPHONG(r):
    n, e = gen_conn(r, 6, 2); return f"{n} {len(e)}\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_CAPDUPHONG(inp):
    a = ints(inp); n, m = a[:2]; E = list(zip(a[2::2], a[3::2]))
    pairs = [(u, v) for u in range(1, n+1) for v in range(u+1, n+1)]
    for k in range(0, 5):
        for add in itertools.combinations_with_replacement(pairs, k):
            if not bridges_brute(n, E + list(add)): return str(k)
    return "?"

def reach(n, E, s):
    seen = {s}; st = [s]
    while st:
        u = st.pop()
        for x, y in E:
            if x == u and y not in seen: seen.add(y); st.append(y)
    return seen
def gen_TINDON(r):
    n = r.randint(1, 7); e = [(r.randint(1, n), r.randint(1, n)) for _ in range(r.randint(0, 10))]
    e = [(u, v) for u, v in e if u != v]
    return f"{n} {len(e)}\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_TINDON(inp):
    a = ints(inp); n, m = a[:2]; E = list(zip(a[2::2], a[3::2])); R = {v: reach(n, E, v) for v in range(1, n+1)}
    for k in range(1, n+1):
        for S in itertools.combinations(range(1, n+1), k):
            if set().union(*[R[v] for v in S]) == set(range(1, n+1)): return str(k)

def gen_KHOBAU(r):
    n = r.randint(1, 6); e = [(r.randint(1, n), r.randint(1, n)) for _ in range(r.randint(0, 9))]
    e = [(u, v) for u, v in e if u != v]
    return f"{n} {len(e)}\n" + ' '.join(str(r.randint(0, 9)) for _ in range(n)) + "\n" + "".join(f"{u} {v}\n" for u, v in e)
def brute_KHOBAU(inp):
    a = ints(inp); n, m = a[:2]; g = [0] + a[2:2+n]; E = list(zip(a[2+n::2], a[3+n::2]))
    start = (1, frozenset([1])); seen = {start}; st = [start]; best = 0
    while st:
        u, S = st.pop(); best = max(best, sum(g[x] for x in S))
        for x, y in E:
            if x == u:
                s2 = (y, S | {y})
                if s2 not in seen: seen.add(s2); st.append(s2)
    return str(best)

def gen_TUYENCHON(r):
    n = r.randint(1, 5); m = r.randint(1, 8)
    w = [(r.choice([-1, 1])*r.randint(1, n), r.choice([-1, 1])*r.randint(1, n)) for _ in range(m)]
    return f"{n} {m}\n" + "".join(f"{x} {y}\n" for x, y in w)
def check_TUYENCHON(inp, out):
    a = ints(inp); n, m = a[:2]; W = list(zip(a[2::2], a[3::2]))
    sat = lambda s, x: (s[abs(x)-1] == '1') == (x > 0)
    exists = any(all(sat(s, x) or sat(s, y) for x, y in W) for s in (''.join(t) for t in itertools.product('01', repeat=n)))
    o = out.split()
    if not exists: return (o == ['NO'], 'expected NO')
    if len(o) != 2 or o[0] != 'YES' or len(o[1]) != n or set(o[1]) - set('01'): return (False, 'bad format')
    return (all(sat(o[1], x) or sat(o[1], y) for x, y in W), 'assignment fails')

def gen_NETVE(r):
    T = r.randint(1, 3); s = f"{T}\n"
    for _ in range(T):
        n = r.randint(1, 5); m = r.randint(1, 6); e = [(r.randint(1, n), r.randint(1, n)) for _ in range(m)]
        s += f"{n} {m}\n" + "".join(f"{u} {v}\n" for u, v in e)
    return s
def brute_NETVE(inp):
    a = ints(inp); T = a[0]; p = 1; out = []
    for _ in range(T):
        n, m = a[p], a[p+1]; p += 2; E = []
        for _ in range(m): E.append((a[p], a[p+1])); p += 2
        ok = False
        def dfs(u, used, cnt):
            if cnt == m: return True
            for i, (x, y) in enumerate(E):
                if not used[i] and u in (x, y):
                    used[i] = True
                    if dfs(y if u == x else x, used, cnt+1): return True
                    used[i] = False
            return False
        for s in range(1, n+1):
            if dfs(s, [False]*m, 0): ok = True; break
        out.append("YES" if ok else "NO")
    return '\n'.join(out)

def gen_DOMINO(r):
    n = r.randint(1, 7); hi = r.choice([2, 3, 6])
    return f"{n}\n" + "".join(f"{r.randint(0, hi)} {r.randint(0, hi)}\n" for _ in range(n))
def check_DOMINO(inp, out):
    a = ints(inp); n = a[0]; D = [None] + [(a[1+2*i], a[2+2*i]) for i in range(n)]
    def possible():
        def dfs(last, used):
            if all(used[1:]): return True
            for i in range(1, n+1):
                if not used[i]:
                    for x, y in (D[i], D[i][::-1]):
                        if last is None or x == last:
                            used[i] = True
                            if dfs(y, used): used[i] = False; return True
                            used[i] = False
            return False
        return dfs(None, [False]*(n+1))
    o = out.split(); ex = possible()
    if o == ['NO']: return (not ex, 'should be possible')
    if not ex: return (False, 'should be NO')
    if len(o) != 2*n: return (False, 'bad length')
    ids = [int(o[2*i]) for i in range(n)]; sg = [o[2*i+1] for i in range(n)]
    if sorted(ids) != list(range(1, n+1)): return (False, 'not permutation')
    seq = [D[i] if s == '+' else D[i][::-1] for i, s in zip(ids, sg)]
    return (all(seq[i][1] == seq[i+1][0] for i in range(n-1)), 'mismatch')

def gen_KETSAT(r):
    while True:
        b, k = r.randint(1, 10), r.randint(1, 6)
        if b**k <= 20000: return f"{b} {k}\n"
def check_KETSAT(inp, out):
    b, k = ints(inp); o = out.split(); L = int(o[0]); s = o[1]
    if L != len(s) or L != b**k + k - 1: return (False, 'length')
    if set(s) - set(str(d) for d in range(b)): return (False, 'digit')
    return (len(set(s[i:i+k] for i in range(L-k+1))) == b**k, 'missing code')
