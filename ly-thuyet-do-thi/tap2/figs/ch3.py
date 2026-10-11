from figlib import *

def mangbanbe():
    f, ax = fig(9.6, 2.4)
    P = {1: (0, 1.0), 2: (0.7, 1.0), 3: (0, 0.0), 4: (0.7, 0.0), 5: (1.4, 0.5)}
    steps = [([(1, 2)], '1 2', '4 nhóm\nlớn nhất 2'), ([(1, 2), (3, 4)], '3 4', '3 nhóm\nlớn nhất 2'), ([(1, 2), (3, 4)], '2 1', '3 nhóm\nlớn nhất 2'),
             ([(1, 2), (3, 4), (2, 3)], '2 3', '2 nhóm\nlớn nhất 4'), ([(1, 2), (3, 4), (2, 3), (4, 5)], '4 5', '1 nhóm\nlớn nhất 5')]
    for k, (E, ev, txt) in enumerate(steps):
        x0 = k*2.0
        from collections import defaultdict
        par = {v: v for v in P}
        def F(x):
            while par[x] != x: x = par[x]
            return x
        for u, v in E: par[F(u)] = F(v)
        cols = {}; pal = ['done', 'teal', 'amber', 'pink', 'wait']; roots = []
        for v in P:
            r = F(v)
            if r not in roots: roots.append(r)
            cols[v] = pal[roots.index(r)]
        new = {(1, 2), (3, 4), (2, 3), (4, 5)}
        for u, v in E: edge(ax, (x0+P[u][0], P[u][1]), (x0+P[v][0], P[v][1]), color=NAVY, lw=2.4, r=0.22)
        for v, p in P.items(): node(ax, (x0+p[0], p[1]), v, cols[v], r=0.22, fs=11, lw=2)
        caption(ax, x0+0.7, 1.65, f'Sau "{ev}"', fs=10.5, color=RED)
        caption(ax, x0+0.7, -0.75, txt, fs=10)
    ax.set_xlim(-0.4, 9.7); ax.set_ylim(-1.2, 1.85); save(f, 'mangbanbe')

def phacau():
    f, ax = fig(9.8, 2.9)
    P = {1: (0, 1.2), 2: (1.0, 1.2), 3: (0.5, 0.2), 4: (1.5, -0.5), 5: (1.9, 0.5)}
    E = {1: (1, 2), 2: (2, 3), 3: (3, 1), 4: (3, 4), 5: (4, 5), 6: (5, 3)}
    order = [4, 1, 6, 2]
    alive_sets = [set(E), set(E) - {4}, set(E) - {4, 1}, set(E) - {4, 1, 6}, set(E) - {4, 1, 6, 2}]
    titles = ['Ban đầu', 'Phá cầu 4\n1 nhóm', 'Phá cầu 1\n1 nhóm', 'Phá cầu 6\n2 nhóm', 'Phá cầu 2\n3 nhóm']
    for k, al in enumerate(alive_sets):
        x0 = k*2.7
        for i, (u, v) in E.items():
            a = (x0+P[u][0], P[u][1]); b = (x0+P[v][0], P[v][1])
            if i in al: edge(ax, a, b, color=NAVY, lw=2.4, r=0.2, label=i, lfs=8)
            else: edge(ax, a, b, color=RED, lw=1.6, dash=True, r=0.2, label=i, lfs=8)
        for v, p in P.items(): node(ax, (x0+p[0], p[1]), v, 'done', r=0.2, fs=10, lw=1.8)
        caption(ax, x0+0.95, -1.25, titles[k], fs=10.5, color=NAVY if k == 0 else RED)
    ax.annotate('', xy=(0.4, 1.95), xytext=(12.4, 1.95), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=2, mutation_scale=15))
    ax.text(6.4, 2.2, 'Đi ngược thời gian: mỗi bước là XÂY lại một cây cầu (DSU làm được)', ha='center', fontsize=10, color=GREEN, fontweight='bold')
    ax.set_xlim(-0.4, 13.2); ax.set_ylim(-1.7, 2.5); save(f, 'phacau')

def haiphe():
    f, ax = fig(7.6, 2.8)
    P = {1: (0, 2.0), 2: (2.0, 2.0), 3: (2.0, 0.2), 4: (0, 0.2)}
    E = [(1, 2, 'khác', 1), (2, 3, 'khác', 2), (1, 3, 'cùng', 3), (3, 4, 'khác', 4), (4, 1, 'cùng', 5)]
    for u, v, t, i in E:
        col = RED if i == 5 else (NAVY if t == 'khác' else TEAL)
        edge(ax, P[u], P[v], color=col, lw=2.8, dash=(t == 'cùng'), label=f'({i}) {t}', lfs=10, lpos=0.62 if i == 3 else 0.5)
    for v, p in P.items(): node(ax, p, v, 'done' if v in (1, 3) else 'amber')
    ax.text(3.0, 1.9, 'Phe A (xanh): 1, 3', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(3.0, 1.45, 'Phe B (cam): 2, 4', fontsize=11, color=AMBER, fontweight='bold')
    ax.text(3.0, 0.8, 'Thông tin (5) nói 4 và 1 cùng phe:', fontsize=10.5, color=RED)
    ax.text(3.0, 0.4, 'mâu thuẫn với (3) và (4)!', fontsize=10.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.5, 7.2); ax.set_ylim(-0.3, 2.5); save(f, 'haiphe')

def noimang():
    f, ax = fig(7.2, 2.9)
    P = {1: (0, 2.0), 2: (0, 0.2), 3: (2.0, 2.0), 4: (2.0, 0.2), 5: (4.0, 1.1)}
    chosen = {(2, 3), (2, 4), (4, 5)}
    for u, v, c in [(1, 3, 4), (2, 3, 2), (3, 4, 5), (2, 4, 3), (4, 5, 1), (3, 5, 6)]:
        edge(ax, P[u], P[v], color=RED if (u, v) in chosen else GRAY, lw=3.2 if (u, v) in chosen else 2, label=c)
    edge(ax, P[1], P[2], color=GREEN, lw=4, label='0')
    for v, p in P.items(): node(ax, p, v, 'done')
    legend_line(ax, 4.9, 2.0, GREEN, 'cáp có sẵn (miễn phí)', lw=4, fs=10)
    legend_line(ax, 4.9, 1.5, RED, 'cáp lắp thêm', lw=3.2, fs=10)
    ax.text(4.9, 0.8, 'Chi phí: 2 + 3 + 1 = 6', fontsize=11.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.5, 8.4); ax.set_ylim(-0.3, 2.5); save(f, 'noimang')

def itdoc():
    f, ax = fig(7.6, 2.9)
    P = {1: (0, 2.0), 2: (1.8, 2.0), 3: (0.9, 0.3), 4: (2.9, 0.3), 5: (3.9, 1.6), 6: (5.4, 1.6)}
    mst = {(1, 2), (2, 3), (3, 4), (4, 5)}
    for u, v, h in [(1, 2, 5), (2, 3, 3), (1, 3, 7), (3, 4, 4), (4, 5, 6), (2, 5, 8)]:
        edge(ax, P[u], P[v], color=NAVY if (u, v) in mst else GRAY, lw=3.2 if (u, v) in mst else 2, label=h, dash=(u, v) not in mst)
    for v, p in P.items(): node(ax, p, v, 'gray' if v == 6 else 'done')
    ax.text(4.6, 0.75, 'Cạnh đậm: cây khung nhỏ nhất', fontsize=10.5, color=NAVY, fontweight='bold')
    ax.text(4.6, 0.35, 'Hỏi (1, 4): đi 1-2-3-4, dốc nhất 5', fontsize=10.5, color=RED)
    ax.text(4.6, -0.05, 'Hỏi (6, 1): không có đường → −1', fontsize=10.5, color=GRAY)
    ax.set_xlim(-0.5, 8.0); ax.set_ylim(-0.35, 2.4); save(f, 'itdoc')

def giengong():
    f, ax = fig(8.6, 3.0)
    P = {1: (0, 0.3), 2: (1.8, 0.3), 3: (3.6, 0.3), 4: (5.4, 0.3)}
    W = (2.7, 2.4)
    for i, a in zip(range(1, 5), [5, 4, 4, 3]):
        edge(ax, W, P[i], color=RED if i == 4 else GRAY, lw=3 if i == 4 else 1.8, label=a, dash=(i != 4), lpos=0.55)
    for u, v, c in [(1, 2, 2), (2, 3, 2), (3, 4, 3)]: edge(ax, P[u], P[v], color=RED, lw=3, label=c)
    edge(ax, P[1], P[4], color=GRAY, lw=1.8, label=7, rad=0.35, dash=True)
    for v, p in P.items(): node(ax, p, v, 'done')
    node(ax, W, '0', 'teal', r=0.36)
    ax.text(3.2, 2.75, 'đỉnh ảo "nguồn nước"', fontsize=10.5, color=TEAL, fontweight='bold')
    ax.text(6.2, 1.6, 'Cạnh 0 – i: đào giếng ở nhà i', fontsize=10.5, color=TXT)
    ax.text(6.2, 1.15, 'Cạnh đỏ: cây khung nhỏ nhất', fontsize=10.5, color=RED, fontweight='bold')
    ax.text(6.2, 0.7, '3 + 2 + 2 + 3 = 10', fontsize=11, color=RED, fontweight='bold')
    ax.set_xlim(-0.5, 9.4); ax.set_ylim(-1.0, 3.0); save(f, 'giengong')

TREE7 = {1: (2.0, 3.0), 2: (1.0, 2.0), 3: (3.0, 2.0), 4: (0.4, 1.0), 5: (1.6, 1.0), 6: (3.0, 1.0), 7: (1.6, 0.0)}
def hohang():
    f, ax = fig(7.6, 3.2)
    P = TREE7; par = {2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 5}
    path = {(7, 5), (5, 2), (4, 2)}
    for v, p in par.items(): edge(ax, P[v], P[p], color=RED if (v, p) in path else NAVY, lw=3.2 if (v, p) in path else 2.4)
    for v, p in P.items(): node(ax, p, v, 'cur' if v == 2 else ('src' if v in (7, 4) else 'done'))
    for d in range(4): ax.text(-0.6, 3.0 - d, f'đời {d}', fontsize=10, color=GRAY, va='center', ha='center', style='italic')
    ax.text(4.2, 2.6, 'Hỏi (7, 4):', fontsize=11.5, color=NAVY, fontweight='bold')
    ax.text(4.2, 2.15, 'ông tổ chung gần nhất là 2,', fontsize=11, color=RED)
    ax.text(4.2, 1.7, '7 ở đời 3, 4 ở đời 2: chênh 1 đời.', fontsize=11, color=TXT)
    ax.set_xlim(-1.0, 8.2); ax.set_ylim(-0.4, 3.4); save(f, 'hohang')

def capquang():
    f, ax = fig(7.4, 3.0)
    P = {1: (2.0, 2.4), 2: (1.0, 1.2), 3: (3.0, 1.2), 4: (0.3, 0.0), 5: (1.7, 0.0), 6: (3.7, 0.0)}
    path = {(1, 2), (2, 4), (1, 3), (3, 6)}
    for u, v, c in [(1, 2, 10), (1, 3, 4), (2, 4, 7), (2, 5, 3), (3, 6, 9)]:
        edge(ax, P[u], P[v], color=RED if (u, v) in path else NAVY, lw=3.2 if (u, v) in path else 2.4, label=c)
    for v, p in P.items(): node(ax, p, v, 'src' if v in (4, 6) else 'done')
    ax.text(4.6, 1.9, 'Hỏi (4, 6):', fontsize=11.5, color=NAVY, fontweight='bold')
    ax.text(4.6, 1.45, 'đường 4 – 2 – 1 – 3 – 6', fontsize=11, color=RED)
    ax.text(4.6, 1.0, 'yếu nhất: min(7, 10, 4, 9) = 4', fontsize=11, color=RED, fontweight='bold')
    ax.set_xlim(-0.3, 8.4); ax.set_ylim(-0.45, 2.8); save(f, 'capquang')

def capk():
    f, ax = fig(7.6, 3.4)
    P = {1: (2.0, 3.0), 2: (1.0, 2.0), 3: (3.2, 2.0), 4: (0.3, 1.0), 5: (1.7, 1.0), 6: (3.2, 1.0), 7: (1.2, 0.0), 8: (2.2, 0.0)}
    par = {2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 5, 8: 5}
    for v, p in par.items(): edge(ax, P[v], P[p], color=RED if v in (7, 5) else NAVY, lw=3.2 if v in (7, 5) else 2.4)
    for v, p in P.items(): node(ax, p, v, 'src' if v == 7 else ('cur' if v == 2 else 'done'))
    ax.text(4.3, 2.7, '(7, 2): cấp trên trực tiếp của 7 là 5,', fontsize=10.5, color=RED)
    ax.text(4.3, 2.3, '         của 5 là 2 → in 2', fontsize=10.5, color=RED)
    ax.text(4.3, 1.75, '(8, 0): chính là 8', fontsize=10.5, color=TXT)
    ax.text(4.3, 1.3, '(6, 3): 6 → 3 → 1 → ? → in −1', fontsize=10.5, color=TXT)
    ax.text(4.3, 0.85, '(4, 1): in 2', fontsize=10.5, color=TXT)
    ax.set_xlim(-0.2, 8.6); ax.set_ylim(-0.4, 3.4); save(f, 'capk')

for fn in [mangbanbe, phacau, haiphe, noimang, itdoc, giengong, hohang, capquang, capk]: fn()
