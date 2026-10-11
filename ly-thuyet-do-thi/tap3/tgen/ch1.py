from common import *

def g_BATTAY(st, i, r):
    if st == 1:
        n = r.randint(2, 100)
        while True:
            d = [r.randint(0, 100) for _ in range(n)]
            if i % 2 == 0 and sum(d) % 2: d[0] += 1 if d[0] < 100 else -1
            if max(d) <= sum(d) - max(d): return f'{n}\n' + ' '.join(map(str, d)) + '\n'
    if st == 2:
        n = r.randint(1, 100); d = [r.randint(0, 100) for _ in range(n)]
        if i == 1: d = [r.randint(0, 3) for _ in range(n)]; d[0] = 100
        if i == 2 and n > 1: d = [100] + [r.randint(0, 2) for _ in range(n - 1)]; d[1] += (sum(d)) % 2
        if i == 4: n = 1; d = [r.choice([0, 2])]
        return f'{n}\n' + ' '.join(map(str, d)) + '\n'
    n = 100000
    d = [r.randint(0, 10**9) for _ in range(n)]
    if i in (1, 2): d[0] += sum(d) % 2              # tổng chẵn, hợp lệ, tổng ~5e13
    if i == 3: d = [r.randint(0, 10**4) for _ in range(n)]; d[5] = 10**9; d[6] += sum(d) % 2   # tổng chẵn nhưng max > phần còn lại
    if i == 4: d = [10**9] * n; d[0] -= 1             # tổng lẻ
    if i == 5: d = [r.randint(0, 10**9) for _ in range(n)]; d[0] += sum(d) % 2; d[0] = min(d[0], 10**9)
    return f'{n}\n' + ' '.join(map(str, d)) + '\n'

def g_NOITIENG(st, i, r):
    n = r.randint(500, 1000) if st == 1 else 200000
    if i == 3 and st != 1: n = 150000
    c = r.randint(1, n)
    E = set((u, c) for u in range(1, n + 1) if u != c)
    if i == 2: E.discard((r.choice([u for u in range(1, min(n, 50) + 1) if u != c]), c))   # thiếu một người theo dõi
    if i == 3: E.add((c, r.choice([u for u in range(1, 50) if u != c])))                 # người nổi tiếng theo dõi người khác
    lim = 200000 - (n // 10 if st == 3 else 0)
    while len(E) < min(lim, n - 1 + (n if st == 1 else 40000)):
        u, v = r.randint(1, n), r.randint(1, n)
        if u != v and u != c and v != c: E.add((u, v))
    E = list(E)
    if st == 3:
        dup = r.sample(E, min(len(E), 200000 - len(E)))
        if i == 4:     # một người "gần nổi tiếng": thiếu đúng 1 người theo dõi nhưng bị ghi lặp
            E = [e for e in E if e != (1 if c != 1 else 2, c)]; dup = [(3 if c != 3 else 4, c)] * 5 + dup[:1000]
        E += dup
    r.shuffle(E); E = E[:200000]
    return f'{n} {len(E)}\n' + edges_txt(E)

def g_TAMGIAC(st, i, r):
    if st == 1:
        n = 100; m = r.choice([1000, 3000, 4950]) if i < 3 else 4950
        return f'{n} {m}\n' + edges_txt(rand_simple_edges(r, n, m))
    if st == 2:
        n = 2000; m = 200000
        if i == 3:   # một đỉnh nối tất cả
            base = [(1, v) for v in range(2, n + 1)]; return f'{n} {m}\n' + edges_txt(rand_simple_edges(r, n, m, base))
        return f'{n} {m}\n' + edges_txt(rand_simple_edges(r, n, m))
    n = 100000; m = 200000
    if i == 1: return f'{n} {m}\n' + edges_txt(rand_simple_edges(r, n, m))
    if i == 2:   # khối đầy đủ 630 đỉnh
        k = 632; E = [(u, v) for u in range(1, k + 1) for v in range(u + 1, k + 1)][:m]
        return f'{n} {len(E)}\n' + edges_txt(E)
    if i == 3:   # hai đỉnh "ngôi sao" nối với gần hết, cộng cạnh ngẫu nhiên
        base = [(1, v) for v in range(3, 70001)] + [(2, v) for v in range(3, 70001)]
        return f'{n} {m}\n' + edges_txt(rand_simple_edges(r, n, m, base))
    base = [(1, v) for v in range(2, 100001)]   # một ngôi sao + 1e5 cạnh giữa lá
    return f'{n} {m}\n' + edges_txt(rand_simple_edges(r, n, m, base))

def g_CHUYENDOI(st, i, r):
    n = r.randint(1, 10) if st == 1 else 1000
    if st == 1 and i == 1: n = 1
    p = [0.5, 0.1, 0.9, 0.0][i - 1] if st == 2 else r.random()
    M = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(a + 1, n):
            if r.random() < p: M[a][b] = M[b][a] = 1
    return f'{n}\n' + ''.join(' '.join(map(str, row)) + '\n' for row in M)

def g_BANCHUNG(st, i, r):
    if st == 1:
        n = 500; m = r.choice([5000, 30000]); E = rand_simple_edges(r, n, m)
        Q = [tuple(r.sample(range(1, n + 1), 2)) for _ in range(100000)]
    elif st == 2:
        n = 100000; m = 100000; E = rand_simple_edges(r, n, m)
        deg = {}
        E2 = []
        for u, v in E:
            if deg.get(u, 0) < 300 and deg.get(v, 0) < 300: E2.append((u, v)); deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
        if i == 2:   # nhiều đỉnh bậc 300
            E2 = []; deg = {}
            for h in range(1, 300):
                for v in r.sample(range(1000, 100001), 300):
                    if deg.get(v, 0) < 300: E2.append((h, v)); deg[v] = deg.get(v, 0) + 1
            E2 = list({(min(u, v), max(u, v)) for u, v in E2})[:100000]
        E = E2; m = len(E)
        hubs = list(range(1, 300)) if i == 2 else list(range(1, n + 1))
        Q = [tuple(r.sample(hubs, 2)) for _ in range(100000)]
    else:
        n = 100000
        if i == 1:
            E = [(1, v) for v in range(3, 50002)] + [(2, v) for v in range(3, 50001)]
            Q = [(1, 2)] * 100000
        elif i == 2:
            E = [(h, v) for h in range(1, 5) for v in range(5, 25000)]
            Q = [tuple(r.sample(range(1, 5), 2)) for _ in range(100000)]
        else:
            E = rand_simple_edges(r, n, 100000); Q = [tuple(r.sample(range(1, n + 1), 2)) for _ in range(100000)]
        m = len(E)
    return f'{n} {len(E)} {len(Q)}\n' + edges_txt(E) + edges_txt(Q)

def g_BANDO(st, i, r):
    if st == 2: R = C = 100; q = 100
    else: R = C = 1000; q = 0 if st == 1 else 200000
    p = [0.5, 0.2, 0.8, 0.5, 0.3][i - 1]
    k = (i + st) % 5
    g = [''.join('.' if r.random() > p else '#' for _ in range(C)) for _ in range(R)]
    Q = [(r.randint(1, R), r.randint(1, C)) for _ in range(q)]
    return f'{R} {C} {k} {q}\n' + '\n'.join(g) + '\n' + edges_txt(Q)

def g_DEMDAO(st, i, r):
    R = C = r.randint(20, 50) if st == 1 else 1000
    if st == 2 and i == 1: g = ['#' * C] * R
    elif st == 2 and i == 2:   # đường rắn
        g = []
        for a in range(R):
            if a % 2 == 0: g.append('#' * C)
            else: g.append(('#' + '.' * (C - 1)) if a % 4 == 3 else ('.' * (C - 1) + '#'))
    else:
        p = [0.5, 0.6, 0.4, 0.55][i - 1]
        g = [''.join('#' if r.random() < p else '.' for _ in range(C)) for _ in range(R)]
    return f'{R} {C}\n' + '\n'.join(g) + '\n'

def g_CAYKHONG(st, i, r):
    tests = []; tot_n = tot_m = 0
    while True:
        n = r.choice([1, 2, 5, 50, 1000, 20000]) if i != 1 else 200000 - 1
        if tot_n + n > 200000: break
        if st == 1:
            E = rand_tree(r, n, deep=(i == 1)); extra = r.choice([0, 0, 1, 5])
            E = E + [e for e in rand_simple_edges(r, n, min(n * (n - 1) // 2, n - 1 + extra), E)[0:0]]
            E = rand_simple_edges(r, n, min(n * (n - 1) // 2, n - 1 + extra), E) if n > 1 else E
        elif st == 2:
            k = r.randint(1, max(1, n // 3)); E = rand_tree(r, n)[: max(0, n - k)]
            if n > 1: E = rand_simple_edges(r, n, min(n * (n - 1) // 2, len(E) + r.choice([0, 0, 3, n // 2])), E)
        else:
            E = rand_tree(r, n)[: max(0, n - r.randint(1, max(1, n // 2)))]
            E = E + [(u, u) for u in r.sample(range(1, n + 1), min(n, r.randint(0, 3)))] + r.sample(E, min(len(E), r.randint(0, 5)))
        if tot_m + len(E) > 200000: break
        tests.append((n, E)); tot_n += n; tot_m += len(E)
        if len(tests) >= 10000: break
    return f'{len(tests)}\n' + ''.join(f'{n} {len(E)}\n' + edges_txt(E) for n, E in tests)

def g_DUPHONG(st, i, r):
    n = [1000, 100000, 500000][st - 1]
    if i == 1: E = [(v, v + 1) for v in range(1, n)]; E = [e for k, e in enumerate(E) if k != n // 3]   # hai đường dài
    elif i == 2: E = []
    else:
        E = rand_tree(r, n)[: n - r.randint(2, max(2, n // 100))]
        E += rand_simple_edges(r, n, 10, [])
    r.shuffle(E)
    return f'{n} {len(E)}\n' + edges_txt(E)

def g_MADITUAN(st, i, r):
    if st == 1: N = r.randint(1, 8) if i != 1 else 3; Q = 100000
    elif st == 2: N = 1000; Q = 1
    else: N = 1000; Q = 100000
    sx, sy = r.randint(1, N), r.randint(1, N)
    if st == 2 and i == 1: sx = sy = 1
    T = [(r.randint(1, N), r.randint(1, N)) for _ in range(Q)]
    if st == 2 and i == 1: T = [(N, N)]
    return f'{N} {sx} {sy} {Q}\n' + edges_txt(T)

CT_SPECIAL = ["4 5\nF..#.\n.J..#\n.....\n.#.##\n", "5 6\n...#..\n.#...#\n.#.J..\n#...F.\n.....#\n", "4 6\nF.#.#.\n#J....\n..#..#\n...#..\n"]
def g_CHAYTRON(st, i, r):
    if st == 2 and i >= 4: return CT_SPECIAL[i - 4]
    if st == 3 and i == 5: return CT_SPECIAL[2]
    R = C = 100 if st == 2 else 1000
    g = [['.' if r.random() > 0.25 else '#' for _ in range(C)] for _ in range(R)]
    if i == 1:   # mê cung rắn dài
        g = [['#'] * C for _ in range(R)]
        for a in range(1, R - 1):
            if a % 2 == 1:
                for b in range(1, C - 1): g[a][b] = '.'
            else: g[a][1 if a % 4 == 0 else C - 2] = '.'
        g[R - 2][0] = '.'
    jx, jy = (1, 1) if i == 1 else (R // 2, C // 2)
    g[jx][jy] = 'J'
    if st == 2:
        fx, fy = (R // 2 + r.randint(-5, 5), C // 2 + r.randint(-5, 5)) if i != 1 else (3, 1)
        if (fx, fy) != (jx, jy): g[fx][fy] = 'F'
    if st == 3:
        for _ in range([1, 5, 50, 1000][i - 1]):
            x, y = r.randrange(R), r.randrange(C)
            if (x, y) != (jx, jy): g[x][y] = 'F'
    return f'{R} {C}\n' + '\n'.join(''.join(x) for x in g) + '\n'

def g_CHIADOI(st, i, r):
    n = [20, 100000, 5000, 100000][st - 1]
    if st == 1: n = r.randint(10, 20)
    E = []
    if st == 2:   # liên thông
        E = rand_tree(r, n)
        col = {}
        adj = {}
        for u, v in E: adj.setdefault(u, []).append(v); adj.setdefault(v, []).append(u)
        col[1] = 0; stck = [1]
        while stck:
            u = stck.pop()
            for v in adj.get(u, []):
                if v not in col: col[v] = col[u] ^ 1; stck.append(v)
        extra = 0
        while extra < 50000:
            u, v = r.randint(1, n), r.randint(1, n)
            if u != v and (col[u] != col[v] or i == 3): E.append((u, v)); extra += 1
        E = list({(min(a, b), max(a, b)) for a, b in E})
    else:
        # nhiều thành phần hai phía với kích thước hai bên khác nhau
        v = 1; m_lim = 200000
        while v <= n:
            a = r.randint(1, max(1, min(n - v + 1, r.choice([1, 2, 3, 5, 10, 100]))))
            b = r.randint(0, min(n - v + 1 - a, a * 3))
            L = list(range(v, v + a)); R_ = list(range(v + a, v + a + b)); v += a + b
            for x in R_: E.append((r.choice(L), x))
            for x in L[1:]:
                if R_: E.append((x, r.choice(R_)))
        if i == 1 and st != 1: E.append((1, 2)) if (1, 2) not in E else None
        if st in (3, 4) and i == 3:   # các ngôi sao có hiệu 3, 3, 2, 2, 2 rồi đến các đỉnh cô lập
            E = []; v = 1
            for d in (3, 3, 2, 2, 2):
                for k in range(d + 1): E.append((v, v + 1 + k))
                v += d + 2
            while v + 1 <= n: E.append((v, v + 1)); v += 2   # phần còn lại ghép thành từng cặp (hiệu 0)
        if st == 4 and i == 2: E = []          # toàn đỉnh cô lập: k = S = n
    r.shuffle(E)
    E = list(dict.fromkeys((min(a, b), max(a, b)) for a, b in E if a != b))
    return f'{n} {len(E)}\n' + edges_txt(E)

def S(gen, subtasks, ntests, tl=1, mem=256, check=None):
    return {'gen': gen, 'subtasks': subtasks, 'ntests': ntests, 'tl': tl, 'mem': mem, 'check': check, 'mod': 'ch1'}
SPEC = {
    'BATTAY': S(g_BATTAY, [30, 30, 40], [4, 4, 5]),
    'NOITIENG': S(g_NOITIENG, [30, 30, 40], [3, 3, 4]),
    'TAMGIAC': S(g_TAMGIAC, [20, 30, 50], [3, 3, 4], tl=2),
    'CHUYENDOI': S(g_CHUYENDOI, [40, 60], [4, 4]),
    'BANCHUNG': S(g_BANCHUNG, [30, 30, 40], [2, 2, 3]),
    'BANDO': S(g_BANDO, [30, 30, 40], [2, 3, 3]),
    'DEMDAO': S(g_DEMDAO, [40, 60], [3, 4]),
    'CAYKHONG': S(g_CAYKHONG, [30, 30, 40], [3, 3, 3]),
    'DUPHONG': S(g_DUPHONG, [30, 30, 40], [3, 3, 3]),
    'MADITUAN': S(g_MADITUAN, [30, 30, 40], [3, 2, 3]),
    'CHAYTRON': S(g_CHAYTRON, [30, 30, 40], [3, 6, 5]),
    'CHIADOI': S(g_CHIADOI, [20, 30, 20, 30], [3, 3, 3, 3]),
}
