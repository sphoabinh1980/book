from figlib import *

def bip(ax, L, R, E, M, lx=0, rx=3.0, top=2.4, gapy=0.75, lst='done', rst='teal', lab=('', '')):
    PL = {u: (lx, top - i*gapy) for i, u in enumerate(L)}; PR = {v: (rx, top - i*gapy) for i, v in enumerate(R)}
    for u, v in E: edge(ax, PL[u], PR[v], color=RED if (u, v) in M else GRAY, lw=3.2 if (u, v) in M else 1.8, r=0.3)
    for u, p in PL.items(): node(ax, p, u[1:] if isinstance(u, str) else u, lst, r=0.3, fs=12)
    for v, p in PR.items(): node(ax, p, v[1:] if isinstance(v, str) else v, rst, r=0.3, fs=12)
    caption(ax, lx, top + 0.6, lab[0], fs=10.5); caption(ax, rx, top + 0.6, lab[1], fs=10.5)
    return PL, PR

def xepphong():
    f, ax = fig(7.0, 3.3)
    E = [('c1', 'r1'), ('c1', 'r2'), ('c2', 'r1'), ('c3', 'r2'), ('c3', 'r3'), ('c4', 'r2')]
    M = {('c1', 'r2'), ('c2', 'r1'), ('c3', 'r3')}
    bip(ax, ['c1', 'c2', 'c3', 'c4'], ['r1', 'r2', 'r3', 'r4'], E, M, lab=('Thí sinh', 'Phòng'))
    ax.text(4.0, 2.2, 'Cạnh đỏ: một cách xếp 3 thí sinh', fontsize=10.5, color=RED, fontweight='bold')
    ax.text(4.0, 1.75, 'Thí sinh 1, 2, 4 chỉ thi được ở', fontsize=10.5, color=NAVY)
    ax.text(4.0, 1.35, 'phòng 1 hoặc phòng 2:', fontsize=10.5, color=NAVY)
    ax.text(4.0, 0.95, 'ba người mà chỉ có hai phòng.', fontsize=10.5, color=NAVY)
    ax.text(4.0, 0.4, 'Không thể xếp đủ 4 người.', fontsize=10.5, color=RED)
    ax.set_xlim(-0.5, 8.4); ax.set_ylim(-0.5, 3.2); save(f, 'xepphong')

def datdomino():
    g = ["..#.", "....", ".#.."]
    f, ax = fig(7.4, 2.4)
    colors = {(i, j): ('#FFFFFF' if (i + j) % 2 == 0 else '#E7E6E6') for i in range(3) for j in range(4) if g[i][j] == '.'}
    grid(ax, g, x0=0, y0=2.0, s=0.62, colors=colors)
    caption(ax, 1.24, -0.2, 'Bảng ban đầu (tô màu bàn cờ)', fs=10.5)
    grid(ax, g, x0=3.6, y0=2.0, s=0.62, colors=colors)
    doms = [((0, 0), (0, 1)), ((0, 3), (1, 3)), ((1, 0), (2, 0)), ((1, 1), (1, 2)), ((2, 2), (2, 3))]
    cols = ['#F8CBAD', '#BDD7EE', '#C6E0B4', '#FFD966', '#D9C8EC']
    for k, (a, b) in enumerate(doms):
        (i1, j1), (i2, j2) = a, b
        x = 3.6 + min(j1, j2)*0.62 + 0.06; y = 2.0 - (max(i1, i2) + 1)*0.62 + 0.06
        w = (abs(j1 - j2) + 1)*0.62 - 0.12; h = (abs(i1 - i2) + 1)*0.62 - 0.12
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=0.08', fc=cols[k], ec=NAVY, lw=1.8, zorder=5))
    caption(ax, 4.84, -0.2, '5 quân domino', fs=10.5, color=RED)
    ax.set_xlim(-0.2, 6.3); ax.set_ylim(-0.45, 2.1); save(f, 'datdomino')

def camera():
    f, ax = fig(8.0, 2.9)
    cells = [(1, 1), (1, 2), (1, 4), (2, 3), (3, 3), (4, 3)]
    g = ['....'] * 4
    colors = {}
    for j in range(4): colors[(0, j)] = '#FFF2CC'
    for i in range(4): colors[(i, 2)] = '#DDEBF7'
    colors[(0, 2)] = '#E2EFDA'
    texts = {(r - 1, c - 1): '★' for r, c in cells}
    grid(ax, g, x0=0.4, y0=2.6, s=0.6, colors=colors, texts=texts, fs=13, tcolor=RED)
    for j in range(4): ax.text(0.4 + j*0.6 + 0.3, 2.78, str(j+1), ha='center', fontsize=10, color=GRAY, fontweight='bold')
    for i in range(4): ax.text(0.2, 2.6 - i*0.6 - 0.3, str(i+1), ha='center', va='center', fontsize=10, color=GRAY, fontweight='bold')
    ax.annotate('H 1', xy=(0.05, 2.3), xytext=(-0.75, 2.3), fontsize=10.5, color=AMBER, fontweight='bold', va='center', arrowprops=dict(arrowstyle='-|>', color=AMBER, lw=1.8))
    ax.annotate('C 3', xy=(1.9, 0.2), xytext=(1.9, -0.45), fontsize=10.5, color=NAVY, fontweight='bold', ha='center', arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=1.8))
    # đồ thị hai phía hàng - cột
    PL = {r: (4.4, 2.5 - (r-1)*0.62) for r in range(1, 5)}; PR = {c: (6.4, 2.5 - (c-1)*0.62) for c in range(1, 5)}
    M = {(1, 1), (2, 3)}
    for r, c in cells: edge(ax, PL[r], PR[c], color=RED if (r, c) in M else GRAY, lw=3 if (r, c) in M else 1.6, r=0.26)
    for r, p in PL.items(): node(ax, p, f'H{r}', 'amber' if r == 1 else 'done', r=0.26, fs=10)
    for c, p in PR.items(): node(ax, p, f'C{c}', 'teal' if c == 3 else 'done', r=0.26, fs=10)
    ax.text(5.4, -0.35, 'Ghép cặp tối đa = 2\n= phủ đỉnh nhỏ nhất {H1, C3}', ha='center', va='center', fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-1.0, 7.2); ax.set_ylim(-0.8, 3.0); save(f, 'camera')

def duongong():
    f, ax = fig(8.4, 3.1)
    P = {1: (0, 1.2), 2: (2.0, 2.4), 3: (2.0, 0.0), 4: (4.2, 2.4), 5: (6.2, 1.2)}
    E = [(1, 2, 10, 1), (1, 3, 8, 2), (2, 3, 2, 3), (2, 4, 5, 4), (3, 4, 4, 5), (3, 5, 7, 6), (4, 5, 9, 7)]
    cut = {2, 3, 4}
    for u, v, c, i in E:
        edge(ax, P[u], P[v], color=RED if i in cut else NAVY, lw=3.2 if i in cut else 2.2, directed=True, label=f'[{i}] {c}', lfs=10)
    for v, p in P.items(): node(ax, p, v, 'src' if v in (1, 2) else 'done')
    from matplotlib.patches import Ellipse
    ax.add_patch(Ellipse((1.0, 1.85), 3.0, 2.0, angle=30, fc='#F1ECF8', ec=PURPLE, lw=1.5, ls='--', zorder=0))
    ax.text(-0.3, 2.6, 'S = {1, 2}', fontsize=11, color=PURPLE, fontweight='bold')
    ax.text(3.4, -0.55, 'Lát cắt nhỏ nhất: ống [2] + [3] + [4] = 8 + 2 + 5 = 15', ha='center', fontsize=10.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.7, 6.8); ax.set_ylim(-0.85, 3.0); save(f, 'duongong')

def roinhau():
    f, ax = fig(7.6, 2.8)
    P = {1: (0, 1.1), 2: (1.6, 2.2), 3: (1.6, 0.0), 4: (3.4, 2.2), 5: (3.4, 0.0), 6: (5.0, 1.1)}
    A = {(1, 2), (2, 4), (4, 6)}; B = {(1, 3), (3, 5), (5, 6)}
    for u, v in [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 3), (4, 6), (5, 6), (5, 4)]:
        c = RED if (u, v) in A else (TEAL if (u, v) in B else GRAY)
        edge(ax, P[u], P[v], color=c, lw=3.2 if c != GRAY else 1.8, directed=True)
    for v, p in P.items(): node(ax, p, v, 'src' if v == 1 else ('cur' if v == 6 else 'done'))
    ax.text(5.7, 1.7, 'Lộ trình 1: 1 → 2 → 4 → 6', fontsize=10.5, color=RED, fontweight='bold')
    ax.text(5.7, 1.25, 'Lộ trình 2: 1 → 3 → 5 → 6', fontsize=10.5, color=TEAL, fontweight='bold')
    ax.text(5.7, 0.6, 'Từ 1 chỉ có 2 con đường đi ra,', fontsize=10, color=NAVY)
    ax.text(5.7, 0.25, 'nên không thể có 3 lộ trình.', fontsize=10, color=NAVY)
    ax.set_xlim(-0.5, 9.6); ax.set_ylim(-0.4, 2.6); save(f, 'roinhau')

def trucnhat():
    f, ax = fig(8.2, 3.0)
    s = (0, 1.2); t = (6.6, 1.2)
    S = {1: (2.0, 2.4), 2: (2.0, 1.2), 3: (2.0, 0.0)}; Dd = {1: (4.6, 2.4), 2: (4.6, 1.2), 3: (4.6, 0.0)}
    a = {1: 2, 2: 1, 3: 2}; b = {1: 2, 2: 1, 3: 2}
    for i, p in S.items(): edge(ax, s, p, color=NAVY, lw=2.2, directed=True, label=a[i], r=0.3, lpos=0.55)
    for j, p in Dd.items(): edge(ax, p, t, color=NAVY, lw=2.2, directed=True, label=b[j], r=0.3, lpos=0.45)
    allowed = [(1, 1), (1, 2), (2, 3), (3, 1), (3, 3)]
    used = {(1, 1), (1, 2), (2, 3), (3, 1), (3, 3)}
    for i, j in allowed: edge(ax, S[i], Dd[j], color=RED if (i, j) in used else GRAY, lw=2.6, directed=True, label='1', r=0.3, lfs=9)
    node(ax, s, 's', 'src', r=0.3, fs=12); node(ax, t, 't', 'cur', r=0.3, fs=12)
    for i, p in S.items(): node(ax, p, f'HS{i}', 'done', r=0.34, fs=10)
    for j, p in Dd.items(): node(ax, p, f'N{j}', 'teal', r=0.34, fs=10)
    ax.text(3.3, -0.65, 's → HS: số ngày tối đa a; HS → N: được trực; N → t: số người cần b', ha='center', fontsize=9.5, color=NAVY)
    ax.set_xlim(-0.5, 7.1); ax.set_ylim(-0.95, 2.85); save(f, 'trucnhat')

for fn in [xepphong, datdomino, camera, duongong, roinhau, trucnhat]: fn()
