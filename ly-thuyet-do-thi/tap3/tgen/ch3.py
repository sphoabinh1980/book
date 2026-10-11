from common import *

def wtxt(E): return ''.join(' '.join(map(str, e)) + '\n' for e in E)

def g_MANGBANBE(st, i, r):
    n = m = 1000 if st == 1 else 200000
    if i == 1:   # chuỗi xấu cho DSU gộp tùy tiện: (1,2), (1,3), (1,4), ...
        E = [(1, k) for k in range(2, n + 1)][:m]
    elif i == 2:
        E = [(k, k + 1) for k in range(1, n)][:m]
    else:
        E = [tuple(r.sample(range(1, n + 1), 2)) for _ in range(m)]
    return f'{n} {len(E)}\n' + edges_txt(E)

def g_PHACAU(st, i, r):
    n, m = (1000, 1000) if st == 1 else (200000, 200000)
    if i == 1: E = [(k, k % n + 1) for k in range(1, n + 1)][:m]     # một vòng tròn
    else: E = rand_tree(r, n)[: n - 1] + [tuple(r.sample(range(1, n + 1), 2)) for _ in range(m - (n - 1))]
    q = m if i != 3 else m // 2
    K = r.sample(range(1, len(E) + 1), q)
    return f'{n} {len(E)} {q}\n' + edges_txt(E) + ' '.join(map(str, K)) + '\n'

def g_HAIPHE(st, i, r):
    n, m = (2000, 2000) if st == 2 else (200000, 200000)
    side = [r.randint(0, 1) for _ in range(n + 1)]
    E = []
    for k in range(m):
        a, b = r.sample(range(1, n + 1), 2)
        t = side[a] ^ side[b]
        if st == 1:
            if t == 0: continue
        E.append((a, b, t))
    if st == 1:
        while len(E) < m:
            a, b = r.sample(range(1, n + 1), 2)
            if side[a] != side[b]: E.append((a, b, 1))
    # chèn một mẩu mâu thuẫn ở vị trí ngẫu nhiên (trừ test 1: không mâu thuẫn)
    if i >= 2:
        pos = r.randint(len(E) // 2, len(E) - 1) if i == 2 else r.randint(1, len(E) - 1)
        # mâu thuẫn được tạo bằng chu trình lẻ (st 1) hoặc nói ngược sự thật
        a, b = r.sample(range(1, n + 1), 2)
        if st == 1:
            # tìm c cùng phe với a để tạo cạnh "khác phe" giữa hai người cùng phe
            c = next(x for x in range(1, n + 1) if x != a and side[x] == side[a])
            E.insert(pos, (a, c, 1))
        else:
            E.insert(pos, (a, b, 1 - (side[a] ^ side[b])))
        E = E[:m]
    return f'{n} {len(E)}\n' + wtxt(E)

def g_NOIMANG(st, i, r):
    if st == 1: n, k, m = 1000, 0, 5000
    elif st == 2: n, k, m = 100000, 0, 200000
    else: n, k, m = 100000, 100000, 200000
    F = [tuple(r.sample(range(1, n + 1), 2)) for _ in range(k)]
    if st == 3 and i == 1: F = [(v, v + 1) for v in range(1, n)] + [(1, 2)]   # có sẵn gần như cả mạng
    E = [(u, v, r.randint(1, 10**9 if i != 2 else 10)) for u, v in rand_tree(r, n)] + \
        [tuple(r.sample(range(1, n + 1), 2)) + (r.randint(1, 10**9),) for _ in range(m - (n - 1))]
    if i == 3: E = E[1:]          # có thể không liên thông
    r.shuffle(E)
    return f'{n} {len(F)} {len(E)}\n' + edges_txt(F) + wtxt(E)

def g_ITDOC(st, i, r):
    if st == 1: n, m, q = 1000, 1000, 1000
    elif st == 2: n, m, q = 100000, 200000, 1000
    else: n, m, q = 100000, 200000, 100000
    E = [(u, v, r.randint(1, 10**9)) for u, v in rand_tree(r, n, deep=(i == 1))][: n - 1 - (5 if i == 2 else 0)]
    while len(E) < m:
        u, v = r.sample(range(1, n + 1), 2); E.append((u, v, r.randint(1, 10**9)))
    r.shuffle(E)
    Q = [(r.randint(1, n), r.randint(1, n)) for _ in range(q)]
    return f'{n} {len(E)} {q}\n' + wtxt(E) + edges_txt(Q)

def g_GIENGONG(st, i, r):
    n, m = [(10, 10), (1000, 5000), (100000, 200000)][st - 1]
    A = [r.randint(1, 10**9) for _ in range(n)]
    if i == 2: A = [r.randint(10**8, 10**9) for _ in range(n)]
    E = []
    while len(E) < m:
        u, v = r.sample(range(1, n + 1), 2)
        E.append((u, v, r.randint(1, 10**9 if i != 2 else 10**6)))
    if i == 3: E = E[: m // 20]   # thưa: cần nhiều giếng
    return f'{n} {len(E)}\n' + ' '.join(map(str, A)) + '\n' + wtxt(E)

def tree_par(r, n, deep=False, root=None):
    perm = list(range(1, n + 1)); r.shuffle(perm)
    if root: perm.remove(root); perm.insert(0, root)
    par = [0] * (n + 1)
    for k in range(1, n):
        par[perm[k]] = perm[k - 1] if deep else perm[r.randint(max(0, k - 30), k - 1)]
    return par

def g_HOHANG(st, i, r):
    n = q = 1000 if st == 1 else 200000
    par = tree_par(r, n, deep=(i <= 2))
    Q = [(r.randint(1, n), r.randint(1, n)) for _ in range(q)]
    return f'{n}\n' + ' '.join(map(str, par[1:])) + f'\n{q}\n' + edges_txt(Q)

def g_CAPQUANG(st, i, r):
    if st == 1: n = q = 1000
    else: n = q = 100000
    if st == 2: E = [(v, v + 1, r.randint(1, 10**9)) for v in range(1, n)]
    else:
        par = tree_par(r, n, deep=(i == 1))
        E = [(v, par[v], r.randint(1, 10**9)) for v in range(1, n + 1) if par[v]]
    r.shuffle(E)
    Q = [tuple(r.sample(range(1, n + 1), 2)) for _ in range(q)]
    return f'{n} {q}\n' + wtxt(E) + edges_txt(Q)

def g_CAPK(st, i, r):
    n = q = [1000, 200000, 1000000][st - 1]
    par = tree_par(r, n, deep=(i == 1), root=1)
    Q = [(r.randint(1, n), r.choice([r.randint(0, 50), r.randint(0, n), r.randint(0, 10**9)])) for _ in range(q)]
    return f'{n} {q}\n' + ' '.join(map(str, par[2:])) + '\n' + edges_txt(Q)

def S(gen, subtasks, ntests, tl=1, mem=256, check=None):
    return {'gen': gen, 'subtasks': subtasks, 'ntests': ntests, 'tl': tl, 'mem': mem, 'check': check, 'mod': 'ch3'}
SPEC = {
    'MANGBANBE': S(g_MANGBANBE, [40, 60], [3, 3]),
    'PHACAU': S(g_PHACAU, [30, 70], [3, 3]),
    'HAIPHE': S(g_HAIPHE, [30, 30, 40], [3, 3, 3]),
    'NOIMANG': S(g_NOIMANG, [30, 30, 40], [3, 3, 3]),
    'ITDOC': S(g_ITDOC, [30, 30, 40], [2, 2, 3]),
    'GIENGONG': S(g_GIENGONG, [20, 30, 50], [3, 3, 3]),
    'HOHANG': S(g_HOHANG, [40, 60], [3, 3]),
    'CAPQUANG': S(g_CAPQUANG, [30, 20, 50], [3, 2, 3]),
    'CAPK': S(g_CAPK, [20, 40, 40], [2, 3, 3], tl=2, mem=64),
}
