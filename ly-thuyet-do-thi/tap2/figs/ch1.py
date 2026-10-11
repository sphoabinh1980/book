from figlib import *

def battay():
    f, ax = fig(9, 3.2)
    # (a) ví dụ 1: một cách bắt tay hợp lệ
    P = {1: (0, 1.5), 2: (1.6, 2.4), 3: (1.6, 0.6), 4: (-1.5, 1.5), 5: (3.2, 1.5)}
    deg = {1: 3, 2: 2, 3: 2, 4: 1, 5: 2}
    for u, v in [(1, 2), (1, 3), (1, 4), (2, 5), (3, 5)]: edge(ax, P[u], P[v], color=NAVY, lw=3)
    for v, p in P.items():
        node(ax, p, v, 'done'); tag(ax, (p[0] + (0.55 if v != 4 else -0.55), p[1] + 0.45), f'{deg[v]}', fs=10)
    caption(ax, 0.85, -0.25, 'a) Ví dụ 1: tổng 10 → 5 cái bắt tay', fs=12)
    # (b) ví dụ 3: người 1 khai 6 lần
    Q = {1: (6.4, 1.5), 2: (8.2, 2.4), 3: (8.2, 0.6)}
    node(ax, Q[1], 1, 'ans'); node(ax, Q[2], 2, 'w'); node(ax, Q[3], 3, 'w')
    tag(ax, (6.95, 2.05), '6', color=RED, fs=10); tag(ax, (8.8, 2.85), '1', fs=10); tag(ax, (8.8, 0.15), '1', fs=10)
    edge(ax, Q[1], Q[2], color=RED, lw=3); edge(ax, Q[1], Q[3], color=RED, lw=3)
    import math
    for k, a in enumerate([135, 165, 195, 225]):
        c, s_ = math.cos(math.radians(a)), math.sin(math.radians(a))
        x, y = Q[1][0] + 1.05*c, Q[1][1] + 1.05*s_
        ax.plot([Q[1][0] + 0.36*c, x], [Q[1][1] + 0.36*s_, y], color=RED, lw=2, linestyle=(0, (3, 2)))
        ax.text(Q[1][0] + 1.3*c, Q[1][1] + 1.3*s_, '?', color=RED, fontsize=13, fontweight='bold', ha='center', va='center')
    caption(ax, 7.3, -0.25, 'b) Ví dụ 3: 6 > 1 + 1, thiếu người bắt tay', fs=12, color=RED)
    ax.set_xlim(-2.1, 9.4); ax.set_ylim(-0.55, 3.1); save(f, 'battay')

def noitieng():
    f, ax = fig(6.2, 3.2)
    P = {1: (0, 2.4), 2: (2.6, 2.4), 3: (1.3, 0.9), 4: (-1.0, 0.6)}
    edge(ax, P[1], P[3], color=RED, lw=3, directed=True)
    edge(ax, P[2], P[3], color=RED, lw=3, directed=True, rad=0.18)
    edge(ax, P[2], P[3], color=RED, lw=2, directed=True, rad=-0.18, dash=True)
    edge(ax, P[4], P[3], color=RED, lw=3, directed=True)
    edge(ax, P[1], P[2], color=GRAY, lw=2.2, directed=True)
    edge(ax, P[4], P[1], color=GRAY, lw=2.2, directed=True)
    for v, p in P.items(): node(ax, p, v, 'cur' if v == 3 else 'w')
    tag(ax, (2.35, 0.55), 'vào: 3   ra: 0', color=RED, fs=10)
    ax.text(2.85, 1.55, 'dòng "2 3" lặp lại', fontsize=10, color=GRAY, style='italic')
    ax.set_xlim(-1.5, 4.6); ax.set_ylim(0.2, 2.9); save(f, 'noitieng')

def tamgiac():
    f, ax = fig(8.6, 3.0)
    P = {1: (0, 0), 2: (1, 1.5), 3: (2, 0), 4: (3, 1.5), 5: (4, 0), 6: (5, 1.5)}
    from matplotlib.patches import Polygon
    cols = ['#FDE9D9', '#E2EFDA', '#DDEBF7', '#EDE4F5']
    for k, t in enumerate([(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]):
        ax.add_patch(Polygon([P[x] for x in t], closed=True, fc=cols[k], ec='none', zorder=0))
    for u, v in [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6)]: edge(ax, P[u], P[v], color=NAVY, lw=2.6)
    for v, p in P.items(): node(ax, p, v, 'w')
    for k, (x, y, t) in enumerate([(1, 0.5, '{1,2,3}'), (2, 1.0, '{2,3,4}'), (3, 0.5, '{3,4,5}'), (4, 1.0, '{4,5,6}')]):
        ax.text(x, y, t, ha='center', va='center', fontsize=10, color=NAVY, fontweight='bold')
    caption(ax, 2.5, -0.75, 'Ví dụ 1: 4 tam giác', fs=12)
    # ví dụ 2: chu trình 5 đỉnh
    import math
    Q = {i: (8.3 + 1.0*math.cos(math.radians(90 + 72*(i-1))), 0.75 + 1.0*math.sin(math.radians(90 + 72*(i-1)))) for i in range(1, 6)}
    for i in range(1, 6): edge(ax, Q[i], Q[i % 5 + 1], color=GRAY, lw=2.4)
    for v, p in Q.items(): node(ax, p, v, 'w', r=0.27, fs=13)
    caption(ax, 8.3, -0.75, 'Ví dụ 2: 0 tam giác', fs=12)
    ax.set_xlim(-0.5, 9.7); ax.set_ylim(-1.0, 2.1); save(f, 'tamgiac')

for fn in [battay, noitieng, tamgiac]: fn()

def chuyendoi():
    f, ax = fig(9, 3.0)
    P = {1: (0, 2.0), 2: (1.5, 2.0), 3: (0.75, 0.7), 4: (2.9, 0.7)}
    for u, v in [(1, 2), (1, 3), (2, 3), (2, 4)]: edge(ax, P[u], P[v], color=NAVY, lw=3)
    for v, p in P.items(): node(ax, p, v, 'done')
    caption(ax, 1.4, -0.2, 'Đồ thị', fs=12)
    # ma trận
    M = ["0110", "1011", "1100", "0100"]
    x0, y0, s = 4.0, 2.55, 0.5
    for i in range(4):
        ax.text(x0 - 0.25, y0 - i*s - s/2, str(i+1), ha='center', va='center', fontsize=11, color=GRAY, fontweight='bold')
        ax.text(x0 + i*s + s/2, y0 + 0.22, str(i+1), ha='center', va='center', fontsize=11, color=GRAY, fontweight='bold')
        for j in range(4):
            fc = '#BDD7EE' if M[i][j] == '1' else 'white'
            ax.add_patch(Rectangle((x0 + j*s, y0 - (i+1)*s), s, s, fc=fc, ec='#A0A0A0', lw=1))
            ax.text(x0 + j*s + s/2, y0 - i*s - s/2, M[i][j], ha='center', va='center', fontsize=12, color=TXT, fontweight='bold')
    caption(ax, x0 + 1.0, -0.2, 'Ma trận kề (dữ liệu vào)', fs=12)
    # danh sách kề
    L = ['1: 2, 3', '2: 1, 3, 4', '3: 1, 2', '4: 2']
    for i, t in enumerate(L):
        ax.text(7.0, 2.3 - i*0.5, t, fontsize=12.5, color=NAVY, fontweight='bold', va='center', family='DejaVu Sans Mono')
    caption(ax, 7.75, -0.2, 'Danh sách kề', fs=12)
    ax.annotate('', xy=(6.75, 1.3), xytext=(6.25, 1.3), arrowprops=dict(arrowstyle='-|>', color=RED, lw=2.5, mutation_scale=18))
    ax.set_xlim(-0.5, 9.2); ax.set_ylim(-0.5, 2.95); save(f, 'chuyendoi')

def banchung():
    f, ax = fig(7.6, 3.4)
    P = {1: (0, 2.2), 2: (1.6, 3.0), 3: (1.6, 1.4), 4: (1.6, -0.2), 5: (3.2, 1.4), 6: (4.8, 1.4)}
    E = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (3, 5), (4, 5), (5, 6)]
    hl = {(1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (4, 5)}
    for u, v in E: edge(ax, P[u], P[v], color=RED if (u, v) in hl else GRAY, lw=3.2 if (u, v) in hl else 2.2)
    for v, p in P.items(): node(ax, p, v, 'src' if v in (1, 5) else ('cur' if v in (2, 3, 4) else 'w'))
    ax.text(5.6, 2.6, 'Câu hỏi (1, 5):', fontsize=12, color=NAVY, fontweight='bold')
    ax.text(5.6, 2.1, 'bạn của 1: {2, 3, 4}', fontsize=11.5, color=TXT)
    ax.text(5.6, 1.65, 'bạn của 5: {2, 3, 4, 6}', fontsize=11.5, color=TXT)
    ax.text(5.6, 1.1, 'bạn chung: {2, 3, 4} → 3', fontsize=11.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.5, 9.4); ax.set_ylim(-0.6, 3.5); save(f, 'banchung')

def bando_counts(g, k):
    R, C = len(g), len(g[0]); t = {}; col = {}
    for i in range(R):
        for j in range(C):
            if g[i][j] == '.':
                c = sum(1 for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)) if 0 <= x < R and 0 <= y < C and g[x][y] == '.')
                t[(i, j)] = c
                if c == k: col[(i, j)] = '#FFD966'
    return t, col
def bando():
    f, ax = fig(9, 2.6)
    gs = [["..#.", "....", "#..#"], ["....", "....", "#..#"], ["....", ".#..", "#..#"]]
    titles = ['Ban đầu: 6 ô', 'Sau khi đào ô (1, 3): 6 ô', 'Sau khi lấp ô (2, 2): 5 ô']
    for k, g in enumerate(gs):
        t, col = bando_counts(g, 2)
        x0 = k*3.2
        grid(ax, g, x0=x0, y0=1.8, s=0.6, colors=col, texts=t, fs=12)
        caption(ax, x0 + 1.2, -0.3, titles[k], fs=11.5)
    ax.annotate('', xy=(3.05, 0.9), xytext=(2.55, 0.9), arrowprops=dict(arrowstyle='-|>', color=RED, lw=2.2, mutation_scale=15))
    ax.annotate('', xy=(6.25, 0.9), xytext=(5.75, 0.9), arrowprops=dict(arrowstyle='-|>', color=RED, lw=2.2, mutation_scale=15))
    ax.set_xlim(-0.2, 9.0); ax.set_ylim(-0.6, 1.95); save(f, 'bando')

def demdao():
    g = ["##..#.", "#...##", "..#...", ".###.#", "....##"]
    isl = {0: [(0, 0), (0, 1), (1, 0)], 1: [(0, 4), (1, 4), (1, 5)], 2: [(2, 2), (3, 1), (3, 2), (3, 3)], 3: [(3, 5), (4, 4), (4, 5)]}
    cols = ['#F8CBAD', '#C6E0B4', '#FFD966', '#BDD7EE']
    f, ax = fig(6.5, 3.2)
    colors = {}; texts = {}
    for k, cells in isl.items():
        for c in cells: colors[c] = cols[k]; texts[c] = '#'
    gg = [row.replace('#', 'L') for row in g]
    grid(ax, gg, x0=0, y0=3.0, s=0.6, colors={**{(i, j): '#DDEBF7' for i in range(5) for j in range(6)}, **colors})
    for k, cells in isl.items():
        (i, j) = cells[0]; x, y = cell_center(i, j, 0, 3.0, 0.6)
    ax.text(4.0, 2.6, 'Đảo 1: 3 ô', fontsize=11.5, color='#C55A11', fontweight='bold')
    ax.text(4.0, 2.1, 'Đảo 2: 3 ô', fontsize=11.5, color=GREEN, fontweight='bold')
    ax.text(4.0, 1.6, 'Đảo 3: 4 ô  (lớn nhất)', fontsize=11.5, color=AMBER, fontweight='bold')
    ax.text(4.0, 1.1, 'Đảo 4: 3 ô', fontsize=11.5, color=NAVY, fontweight='bold')
    ax.text(4.0, 0.45, 'Ô xanh nhạt: nước', fontsize=10.5, color=GRAY, style='italic')
    ax.set_xlim(-0.1, 7.6); ax.set_ylim(-0.1, 3.1); save(f, 'demdao')

def caykhong():
    f, ax = fig(9.4, 3.1)
    # test 1: cây
    P = {1: (0, 2), 2: (1.0, 1.2), 3: (0.3, 0.2), 4: (1.9, 0.3)}
    for u, v in [(1, 2), (2, 3), (2, 4)]: edge(ax, P[u], P[v], color=NAVY, lw=3)
    for v, p in P.items(): node(ax, p, v, 'done', r=0.28, fs=13)
    caption(ax, 0.95, -0.55, 'Bộ 1: là cây\n→ 0', fs=11)
    # test 2
    Q = {1: (3.3, 2.0), 2: (4.5, 2.0), 3: (3.9, 0.9), 4: (5.6, 1.5), 5: (6.4, 0.5)}
    edge(ax, Q[1], Q[2], color=NAVY, lw=3); edge(ax, Q[2], Q[3], color=NAVY, lw=3); edge(ax, Q[3], Q[1], color=RED, lw=3, dash=True)
    edge(ax, Q[4], Q[5], color=NAVY, lw=3); edge(ax, Q[3], Q[4], color=GREEN, lw=3, dash=True, r=0.28)
    for v, p in Q.items(): node(ax, p, v, 'done', r=0.28, fs=13)
    ax.text(3.1, 1.25, '−', color=RED, fontsize=20, fontweight='bold'); ax.text(4.95, 0.95, '+', color=GREEN, fontsize=18, fontweight='bold')
    caption(ax, 5.0, -0.55, 'Bộ 2: bỏ 1 cạnh, thêm 1 cạnh\n→ 2', fs=11)
    # test 3
    R_ = {1: (8.3, 1.5), 2: (9.7, 1.5), 3: (9.0, 0.2)}
    loop(ax, R_[1], color=RED, r=0.28, ang=135, size=0.45)
    edge(ax, R_[1], R_[2], color=NAVY, lw=3, rad=0.35, r=0.28); edge(ax, R_[1], R_[2], color=RED, lw=3, rad=-0.35, r=0.28, dash=True)
    edge(ax, R_[2], R_[3], color=GREEN, lw=3, dash=True, r=0.28)
    for v, p in R_.items(): node(ax, p, v, 'done', r=0.28, fs=13)
    caption(ax, 9.1, -0.55, 'Bộ 3: bỏ khuyên, bỏ cạnh lặp,\nthêm 1 cạnh → 3', fs=11)
    legend_line(ax, 0.0, 2.75, RED, 'cạnh bỏ đi', lw=3, dash=True, fs=10); legend_line(ax, 2.6, 2.75, GREEN, 'cạnh thêm vào', lw=3, dash=True, fs=10)
    ax.set_xlim(-0.5, 10.6); ax.set_ylim(-1.1, 3.0); save(f, 'caykhong')

def duphong():
    f, ax = fig(8, 2.6)
    P = {1: (0, 1.6), 2: (1.2, 1.6), 3: (0.6, 0.5), 4: (3.2, 1.6), 5: (4.4, 1.6), 6: (3.8, 0.5), 7: (6.2, 1.1)}
    for u, v in [(1, 2), (2, 3), (3, 1)]: edge(ax, P[u], P[v], color=NAVY, lw=3)
    for u, v in [(4, 5), (6, 4)]: edge(ax, P[u], P[v], color=TEAL, lw=3)
    edge(ax, P[2], P[4], color=RED, lw=3, dash=True)
    for v, p in P.items(): node(ax, p, v, 'done' if v <= 3 else ('teal' if v <= 6 else 'pink'))
    ax.text(2.2, 1.85, 'cáp mới', color=RED, fontsize=11, fontweight='bold', ha='center')
    caption(ax, 0.6, -0.2, '3 máy: 3 cặp', fs=11.5); caption(ax, 3.8, -0.2, '3 máy: 3 cặp', fs=11.5); caption(ax, 6.2, -0.2, '1 máy: 0 cặp', fs=11.5)
    ax.set_xlim(-0.5, 7.0); ax.set_ylim(-0.5, 2.2); save(f, 'duphong')

def madituan():
    import collections
    N = 5; d = {(1, 1): 0}; q = collections.deque([(1, 1)])
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            t = (x+dx, y+dy)
            if 1 <= t[0] <= N and 1 <= t[1] <= N and t not in d: d[t] = d[(x, y)] + 1; q.append(t)
    f, ax = fig(7.5, 3.4)
    rows = ['.....'] * 5
    colors = {(i, j): ('#EEEEEE' if (i + j) % 2 else 'white') for i in range(5) for j in range(5)}
    colors[(0, 0)] = '#DCCCEC'; colors[(4, 4)] = '#FFD966'; colors[(1, 1)] = '#FFD966'
    texts = {(i, j): d[(i+1, j+1)] for i in range(5) for j in range(5)}
    grid(ax, rows, x0=0, y0=3.2, s=0.62, colors=colors, texts=texts, fs=13)
    for j in range(5):
        ax.text(j*0.62 + 0.31, 3.42, str(j+1), ha='center', fontsize=10, color=GRAY, fontweight='bold')
        ax.text(-0.22, 3.2 - j*0.62 - 0.31, str(j+1), va='center', ha='center', fontsize=10, color=GRAY, fontweight='bold')
    path = [(1, 1), (2, 3), (3, 5), (4, 3), (5, 5)]
    pts = [cell_center(x-1, y-1, 0, 3.2, 0.62) for x, y in path]
    for a, b in zip(pts, pts[1:]):
        ax.annotate('', xy=b, xytext=a, arrowprops=dict(arrowstyle='-|>', color=RED, lw=2, mutation_scale=13, shrinkA=9, shrinkB=9))
    ax.text(3.6, 2.7, 'Số trong ô: số nước đi ít nhất', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(3.6, 2.25, 'từ ô (1, 1) tới ô đó.', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(3.6, 1.6, 'Mũi tên đỏ: một cách đi', fontsize=10.5, color=RED)
    ax.text(3.6, 1.2, '(1,1)→(2,3)→(3,5)→(4,3)→(5,5)', fontsize=10.5, color=RED)
    ax.text(3.6, 0.6, 'Ô (2, 2) cũng cần tới 4 nước!', fontsize=10.5, color=AMBER, fontweight='bold')
    ax.set_xlim(-0.45, 7.4); ax.set_ylim(0.0, 3.6); save(f, 'madituan')

def chaytron():
    g = ["###.###", "#J....#", "#.#.F.#", "#.....#", "#.#####"]
    import collections
    R, C = 5, 7; INF = 99
    fire = {(i, j): INF for i in range(R) for j in range(C)}
    q = collections.deque()
    for i in range(R):
        for j in range(C):
            if g[i][j] == 'F': fire[(i, j)] = 0; q.append((i, j))
    while q:
        x, y = q.popleft()
        for u, v in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= u < R and 0 <= v < C and g[u][v] != '#' and fire[(u, v)] == INF: fire[(u, v)] = fire[(x, y)] + 1; q.append((u, v))
    f, ax = fig(8.6, 3.0)
    texts = {}; colors = {}
    for i in range(R):
        for j in range(C):
            if g[i][j] != '#':
                texts[(i, j)] = fire[(i, j)] if fire[(i, j)] < INF else ''
                colors[(i, j)] = '#FBE2D5' if fire[(i, j)] <= 2 else 'white'
    colors[(2, 4)] = '#F4B183'; texts[(2, 4)] = 'F'; colors[(1, 1)] = '#DCCCEC'; texts[(1, 1)] = 'J'
    grid(ax, g, x0=0, y0=3.0, s=0.58, colors=colors, texts=texts, fs=12, tcolor={(i, j): RED for i in range(R) for j in range(C)})
    caption(ax, 2.03, -0.75, 'Thời điểm lửa tới từng ô', fs=11.5)
    # bên phải: đường chạy
    colors2 = {}; texts2 = {}
    path = [(1, 1), (2, 1), (3, 1), (4, 1)]
    for k, c in enumerate(path): colors2[c] = '#C6E0B4'; texts2[c] = k
    colors2[(1, 2)] = '#FFF2CC'; texts2[(1, 2)] = 1; colors2[(1, 3)] = '#F8CBAD'; texts2[(1, 3)] = '2✗'
    colors2[(2, 4)] = '#F4B183'; texts2[(2, 4)] = 'F'
    grid(ax, g, x0=4.6, y0=3.0, s=0.58, colors=colors2, texts=texts2, fs=12)
    x, y = cell_center(4, 1, 4.6, 3.0, 0.58)
    ax.annotate('', xy=(x, y - 0.75), xytext=(x, y - 0.2), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=2.5, mutation_scale=16))
    ax.text(x + 0.3, y - 0.45, 'phút 4: ra ngoài', fontsize=10.5, color=GREEN, fontweight='bold')
    caption(ax, 6.63, -0.75, 'Thời điểm An có mặt ở từng ô', fs=11.5)
    ax.set_xlim(-0.1, 8.8); ax.set_ylim(-1.0, 3.1); save(f, 'chaytron')

def chiadoi():
    f, ax = fig(8.4, 2.7)
    P = {1: (0, 1.5), 2: (1.1, 1.5), 3: (2.2, 1.5), 4: (3.3, 1.5), 5: (5.2, 1.5), 6: (4.4, 0.3), 7: (5.2, 0.3), 8: (6.0, 0.3), 9: (7.4, 1.0)}
    A = {1, 3, 5, 9}
    for u, v in [(1, 2), (2, 3), (3, 4), (5, 6), (5, 7), (5, 8)]: edge(ax, P[u], P[v], color=RED, lw=2.6, dash=True)
    for v, p in P.items(): node(ax, p, v, 'done' if v in A else 'amber', r=0.3, fs=13)
    caption(ax, 1.65, 0.6, 'hiệu 2 − 2 = 0', fs=11, color=GRAY); caption(ax, 5.2, -0.45, 'hiệu 3 − 1 = 2', fs=11, color=GRAY)
    caption(ax, 7.4, 0.3, 'hiệu 1', fs=11, color=GRAY)
    legend_node(ax, 0.0, 2.45, 'done', 'Đội A: {1, 3, 5, 9} — 4 bạn', fs=11)
    legend_node(ax, 4.2, 2.45, 'amber', 'Đội B: {2, 4, 6, 7, 8} — 5 bạn', fs=11)
    ax.set_xlim(-0.5, 8.4); ax.set_ylim(-0.75, 2.75); save(f, 'chiadoi')

for fn in [chuyendoi, banchung, bando, demdao, caykhong, duphong, madituan, chaytron, chiadoi]: fn()
