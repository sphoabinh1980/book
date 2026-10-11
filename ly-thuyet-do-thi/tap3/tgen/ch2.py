from common import *
import math

def wedges(r, n, m, wmin, wmax, directed=False, conn=False, simple=False):
    E = []
    if conn:
        p = list(range(1, n + 1)); r.shuffle(p)
        for i in range(1, n): E.append((p[r.randint(max(0, i - 3), i - 1)], p[i]))
    while len(E) < m:
        u, v = r.randint(1, n), r.randint(1, n)
        if u != v: E.append((u, v))
    r.shuffle(E)
    return [(u, v, r.randint(wmin, wmax)) for u, v in E]
def wtxt(E): return ''.join(' '.join(map(str, e)) + '\n' for e in E)

def g_DUONGTRUONG(st, i, r):
    n, m = (1000, 5000) if st == 1 else (100000, 200000)
    W = [10**9, 9, 10**9, 1000][i - 1] if i <= 4 else 10**9
    if i == 2:   # đường dài trọng số lớn: khoảng cách tới ~1e14 (st2) / 1e12 (st1)
        p = list(range(1, n + 1)); r.shuffle(p)
        E = [(p[k], p[k + 1], r.randint(9 * 10**8, 10**9)) for k in range(n - 1)] + wedges(r, n, m - (n - 1), 10**9 - 10, 10**9, True)
        r.shuffle(E); return f'{n} {len(E)} {p[0]}\n' + wtxt(E)
    E = wedges(r, n, m, 0, W, True, conn=(i != 3))
    return f'{n} {len(E)} {r.randint(1, n)}\n' + wtxt(E)

def g_NUTGIAO(st, i, r):
    n, m = (1000, 2000) if st == 1 else (100000, 200000)
    if i == 1:   # chuỗi "kim cương": nhiều đường ngắn nhất, các nút nối giữa là quan trọng
        E = []; v = 1; k = (n - 1) // 3
        for _ in range(k):
            a, b, c = v, v + 1, v + 2; d = v + 3
            E += [(a, b, 2), (a, c, 2), (b, d, 2), (c, d, 2)]; v = d
        nn = v
        while len(E) < m:
            x, y = r.randint(1, nn), r.randint(1, nn)
            if abs(x - y) > 3: E.append((x, y, 10**6))
        r.shuffle(E); return f'{nn} {len(E)}\n' + wtxt(E)
    if i == 2:   # trọng số nhỏ: rất nhiều đường ngắn nhất
        E = wedges(r, n, m, 1, 2, conn=True)
    else:
        E = wedges(r, n, m, 1, [10**9, 5][i % 2], conn=True)
    # đảm bảo có đường 1 -> n: thêm đường nối thẳng một dãy
    return f'{n} {len(E)}\n' + wtxt(E)

def g_XEBUYT(st, i, r):
    n, m = (100000, 200000) if st != 2 else (1000, 1000)
    p = list(range(2, n)); r.shuffle(p); p = [1] + p + [n]
    base = [(p[k], p[k + 1]) for k in range(n - 1)]
    extra = []
    while len(extra) < m - len(base):
        u, v = r.randint(1, n), r.randint(1, n)
        if u != v: extra.append((u, v))
    E = []
    for idx, (u, v) in enumerate(base + extra):
        chain = idx < len(base)
        w = r.randint(1, 1000) if chain else (r.randint(1, 10**6) if i != 1 else 10**9)
        if st == 1: a, pp = 0, 1
        else: a, pp = r.randint(0, 10**6), r.randint(1, [10**3, 1, 10**5][i % 3])
        b = 10**9 if r.random() < 0.97 else r.randint(a, 10**9)
        E.append((u, v, w, a, pp, b))
    if i == 1:   # các tuyến trên đường chính được liệt kê ngược chiều: Bellman-Ford phải chạy rất nhiều lượt
        E = E[:len(base)][::-1] + E[len(base):]
    else:
        r.shuffle(E)
    return f'{n} {len(E)}\n' + wtxt(E)

def g_DOITIEN(st, i, r):
    # tỉ giá chọn từ các giá trị "tròn" và kiểm tra không có vòng nào có tích quá gần 1 (chỉ với vòng ngắn)
    if st == 1:
        n = 3; m = r.randint(3, 8)
        while True:
            E = [tuple(r.sample(range(1, 4), 2)) + (r.choice([0.5, 0.8, 0.9, 1.1, 1.25, 2.0, 0.95, 1.05]),) for _ in range(m)]
            ok = True; prods = []
            for a in E:
                for b in E:
                    if a[1] == b[0] and b[1] == a[0]: prods.append(a[2] * b[2])
                    for c in E:
                        if a[1] == b[0] and b[1] == c[0] and c[1] == a[0]: prods.append(a[2] * b[2] * c[2])
            if all(abs(x - 1) > 1e-4 for x in prods): break
        return f'{n} {len(E)}\n' + ''.join(f'{u} {v} {x}\n' for u, v, x in E)
    n = 100; m = 10000
    # gán "giá trị" mỗi loại tiền; tỉ giá u->v = val[v]/val[u] * (1 - phí)  => mọi vòng lỗ, trừ khi cài cố ý một vòng lãi
    val = [0] + [math.exp(r.uniform(-3, 3)) for _ in range(n)]
    E = []
    for _ in range(m):
        u, v = r.sample(range(1, n + 1), 2)
        rate = val[v] / val[u] * (1 - r.uniform(0.001, 0.05))
        if 0.0001 <= rate <= 100: E.append((u, v, round(rate * 0.999, 4)))
    if i == 3:   # loại tiền 1 không đổi được sang loại nào, vòng lãi nằm ở phần còn lại
        E = [e for e in E if e[0] != 1]
    if i in (2, 3, 4):   # cài một vòng lãi dài, không đi qua loại tiền 1
        cyc = r.sample(range(2, n + 1), 20 if i == 2 else 60)
        for k in range(len(cyc)):
            u, v = cyc[k], cyc[(k + 1) % len(cyc)]
            rate = val[v] / val[u] * (1.0006)
            if not (0.0001 <= rate <= 100): rate = min(100, max(0.0001, rate))
            E.append((u, v, round(rate, 4) + 0.0001))
    E = [e for e in E if 0.0001 <= e[2] <= 100]
    return f'{n} {len(E)}\n' + ''.join(f'{u} {v} {x:.4f}\n' for u, v, x in E)

def g_BAYRE(st, i, r):
    if st == 1: n, m = 1000, 10000; k = r.randint(n - 1, 1000)
    elif st == 2: n, m = 100, 1000; k = r.randint(1, 10)
    else: n, m = 1000, 10000; k = [1, 3, 10, 500][i - 1]
    E = wedges(r, n, m, 1, 10**6, True, conn=True)
    if i == 2:   # đường nhiều chặng rất rẻ, đường ít chặng đắt
        E += [(1 + j, 2 + j, 1) for j in range(min(n - 1, 50))] + [(1, n, 10**6)]
    return f'{n} {len(E)} {k}\n' + wtxt(E)

def g_LICHTHIDAU(st, i, r):
    n, m = 1000, 5000
    perm = list(range(1, n + 1)); r.shuffle(perm); pos = {v: k for k, v in enumerate(perm)}
    E = []
    while len(E) < m:
        a, b = r.sample(range(1, n + 1), 2)
        if st == 1:
            if pos[a] < pos[b]: a, b = b, a           # A sau B theo một thứ tự ngầm: không có chu trình dương
            E.append((1, a, b, r.randint(0, 10**6 if i != 2 else 10)))
        else:
            if r.random() < 0.5:
                if pos[a] < pos[b]: a, b = b, a
                E.append((1, a, b, r.randint(0, 1000)))
            else:
                E.append((2, a, b, r.randint(0, 10**6) if i != 3 else r.randint(0, 50)))
    return f'{n} {len(E)}\n' + wtxt(E)

def g_THUDO(st, i, r):
    n = r.randint(30, 50) if st == 1 else 400
    m = [n * (n - 1) // 2, 3 * n, 10 * n][i - 1] if st == 1 else [79800, 3000, 20000][i - 1]
    if st == 2 and i >= 2:   # xương sống là một đường dài n đỉnh, cạnh nhẹ; cạnh phụ rất nặng
        p = list(range(1, n + 1)); r.shuffle(p)
        E = [(p[k], p[k + 1], r.randint(1, 10)) for k in range(n - 1)]
        while len(E) < m:
            u, v = r.sample(range(1, n + 1), 2); E.append((u, v, r.randint(10**5, 10**6)))
        E.sort(key=lambda e: -min(p.index(e[0]), p.index(e[1])) if e[2] <= 10 else r.random())
        return f'{n} {len(E)}\n' + wtxt(E)
    E = wedges(r, n, m, 1, 10**6, conn=True)
    return f'{n} {len(E)}\n' + wtxt(E)

def g_XEPHANG(st, i, r):
    n = [100, 500, 2000][st - 1]; m = [3 * n, 20 * n, 100000][st - 1] if i != 1 else n - 1
    perm = list(range(1, n + 1)); r.shuffle(perm); pos = {v: k for k, v in enumerate(perm)}
    if i == 2: m = min(m, 3 * n - 10)
    E = set()
    if i == 1:
        for k in range(n - 1): E.add((perm[k], perm[k + 1]))   # chuỗi đầy đủ: mọi người xác định
    while len(E) < m:
        a, b = r.sample(range(1, n + 1), 2)
        if pos[a] > pos[b]: a, b = b, a
        if i == 2 and pos[b] - pos[a] > 3: continue        # chỉ biết kết quả giữa người gần nhau
        E.add((a, b))
    E = list(E); r.shuffle(E)
    return f'{n} {len(E)}\n' + edges_txt(E)

def g_XETAI(st, i, r):
    if st == 1: n, m, q = 50, 500, 50
    else: n, m, q = 500, 100000, 100000
    E = wedges(r, n, m, 1, 10**9 if i != 2 else 20)
    Q = [tuple(r.sample(range(1, n + 1), 2)) for _ in range(q)]
    return f'{n} {len(E)} {q}\n' + wtxt(E) + edges_txt(Q)

def g_DENGIAOTHONG(st, i, r):
    n, m, P = [(10000, 20000, 1), (100, 200, 60), (10000, 20000, 60)][st - 1]
    if st == 2: P = r.randint(2, 60)
    dens = [0.5, 0.15, 0.05, 0.3][i - 1]
    S = [''.join('1' if r.random() < dens else '0' for _ in range(P)) for _ in range(n)]
    if st == 1: S = ['1' if r.random() < 0.8 else '0' for _ in range(n)]
    if st == 3 and i == 3:   # một con đường rất dài, mỗi nút chỉ xanh đúng một phút: đáp số cỡ n*P/2
        m = n - 1
        S = [''.join('1' if k == x else '0' for k in range(P)) for x in (r.randrange(P) for _ in range(n))]
    p = list(range(2, n)); r.shuffle(p); chain = [1] + p + [n]
    E = [(chain[k], chain[k + 1]) for k in range(n - 1)] if i != 4 else []
    while len(E) < m:
        u, v = r.randint(1, n), r.randint(1, n)
        if u != v: E.append((u, v))
    return f'{n} {len(E)} {P}\n' + '\n'.join(S) + '\n' + edges_txt(E)

def maze(r, R, C, wall):
    g = [['#' if r.random() < wall else '.' for _ in range(C)] for _ in range(R)]
    return g
def g_PHATUONG(st, i, r):
    R = C = 100; k = [0, 1, r.randint(2, 10)][st - 1]
    if i == 1:   # các bức tường ngang có khe ở hai đầu: đi vòng rất xa hoặc phá tường đi thẳng
        g = [['.'] * C for _ in range(R)]
        for a in range(2, R - 1, 3):
            for b in range(C): g[a][b] = '#'
            g[a][0 if (a // 3) % 2 else C - 1] = '.'
    else:
        g = maze(r, R, C, [0, 0.3, 0.45, 0.6][i - 1])
    g[0][C // 2] = 'S'; g[R - 1][C // 2] = 'T'
    return f'{R} {C} {k}\n' + '\n'.join(''.join(x) for x in g) + '\n'

def g_ROBOTXOAY(st, i, r):
    R = C = 50 if st == 1 else 1000
    if i == 1:
        g = [['.'] * C for _ in range(R)]
        for a in range(1, R - 1, 2):
            for b in range(C): g[a][b] = '#'
            g[a][0 if a % 4 == 1 else C - 1] = '.'
    else:
        g = maze(r, R, C, [0, 0.2, 0.35, 0.1][i - 1])
    g[0][0] = 'S'; g[R - 1][C - 1] = 'T'
    return f'{R} {C} {r.choice("NESW")}\n' + '\n'.join(''.join(x) for x in g) + '\n'

def S(gen, subtasks, ntests, tl=1, mem=256, check=None):
    return {'gen': gen, 'subtasks': subtasks, 'ntests': ntests, 'tl': tl, 'mem': mem, 'check': check, 'mod': 'ch2'}
def chk_doitien(inp, out, ans): return out.split() == ans.split()
SPEC = {
    'DUONGTRUONG': S(g_DUONGTRUONG, [40, 60], [4, 4]),
    'NUTGIAO': S(g_NUTGIAO, [30, 70], [4, 4]),
    'XEBUYT': S(g_XEBUYT, [30, 30, 40], [3, 3, 3]),
    'DOITIEN': S(g_DOITIEN, [30, 70], [5, 4]),
    'BAYRE': S(g_BAYRE, [30, 30, 40], [3, 3, 4]),
    'LICHTHIDAU': S(g_LICHTHIDAU, [40, 60], [3, 3]),
    'THUDO': S(g_THUDO, [30, 70], [3, 3]),
    'XEPHANG': S(g_XEPHANG, [40, 40, 20], [3, 3, 3]),
    'XETAI': S(g_XETAI, [30, 70], [3, 3]),
    'DENGIAOTHONG': S(g_DENGIAOTHONG, [30, 30, 40], [3, 3, 4]),
    'PHATUONG': S(g_PHATUONG, [30, 30, 40], [4, 4, 4]),
    'ROBOTXOAY': S(g_ROBOTXOAY, [30, 70], [3, 4], tl=2),
}
