from figlib import *
import math

def duongtruong():
    f, ax = fig(7.6, 3.3)
    P = {1: (0, 1.5), 2: (2.2, 2.7), 3: (2.2, 0.3), 4: (4.6, 1.5), 5: (6.6, 1.5), 6: (-1.6, 3.0)}
    d = {1: 0, 2: 3, 3: 1, 4: 8, 5: 11, 6: '−1'}
    tree = {(1, 3), (3, 2), (2, 4), (4, 5)}
    E = [(1, 2, 4), (1, 3, 1), (3, 2, 2), (2, 4, 5), (3, 4, 8), (4, 5, 3), (5, 1, 2), (6, 1, 7)]
    for u, v, w in E:
        rad = 0.32 if (u, v) == (5, 1) else 0.0
        if (u, v) == (5, 1):
            edge(ax, P[u], P[v], color=GRAY, lw=2, directed=True, label=w, rad=-0.62)
        else:
            edge(ax, P[u], P[v], color=RED if (u, v) in tree else GRAY, lw=3.2 if (u, v) in tree else 2, directed=True, label=w)
    for v, p in P.items():
        node(ax, p, v, 'src' if v == 1 else ('gray' if v == 6 else 'done'))
        tag(ax, (p[0] + (0.05 if v != 3 else 0.95), p[1] + (0.55 if v != 3 else -0.05)), f'd = {d[v]}', color=RED if v != 6 else GRAY, fs=10)
    ax.set_xlim(-2.1, 7.2); ax.set_ylim(-1.4, 3.75); save(f, 'duongtruong')

def nutgiao():
    f, ax = fig(8, 3.0)
    P = {1: (0, 1.2), 2: (1.6, 2.2), 3: (1.6, 0.2), 4: (3.2, 1.2), 5: (4.8, 2.2), 6: (4.8, 0.2), 7: (6.4, 1.2)}
    E = [(1, 2, 2), (1, 3, 2), (2, 4, 3), (3, 4, 3), (4, 5, 1), (5, 7, 4), (4, 6, 2), (6, 7, 3), (5, 6, 5)]
    for u, v, w in E:
        sp = (u, v) != (5, 6)
        edge(ax, P[u], P[v], color=RED if sp else GRAY, lw=3.2 if sp else 2, label=w)
    for v, p in P.items(): node(ax, p, v, 'cur' if v in (1, 4, 7) else 'done')
    ax.text(3.2, -0.55, 'Bốn đường đi ngắn nhất, cùng độ dài 10, đều qua 1, 4, 7', ha='center', fontsize=11, color=NAVY, fontweight='bold')
    ax.set_xlim(-0.5, 6.9); ax.set_ylim(-0.8, 2.6); save(f, 'nutgiao')

def xebuyt():
    f, ax = fig(9, 3.6)
    P = {1: (0, 1.5), 2: (3.6, 2.9), 3: (3.6, 0.1), 4: (7.2, 1.5)}
    E = [(1, 2, 'đi 10 phút\nxuất bến 0, 15, …, 60'), (1, 3, 'đi 5 phút\nxuất bến 10, 30, 50'), (2, 4, 'đi 12 phút\nxuất bến 20, 30, 40'),
         (3, 4, 'đi 3 phút\nxuất bến 0, 30'), (3, 2, 'đi 2 phút\nxuất bến 5, 10, …')]
    best = {(1, 2), (2, 4)}
    for u, v, t in E:
        edge(ax, P[u], P[v], color=RED if (u, v) in best else GRAY, lw=3.2 if (u, v) in best else 2, directed=True)
        mx, my = (P[u][0]+P[v][0])/2, (P[u][1]+P[v][1])/2
        off = {(1, 2): (-0.9, 0.35), (1, 3): (-0.9, -0.35), (2, 4): (0.9, 0.35), (3, 4): (0.9, -0.35), (3, 2): (0.85, 0)}[(u, v)]
        ax.text(mx+off[0], my+off[1], t, ha='center', va='center', fontsize=9.5, color=RED if (u, v) in best else '#404040',
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none'))
    arr = {1: '0', 2: '10', 3: '15', 4: '32'}
    for v, p in P.items():
        node(ax, p, v, 'src' if v == 1 else ('cur' if v == 4 else 'done'))
        tag(ax, (p[0], p[1] - 0.6 if v != 2 else p[1] + 0.6), f'tới lúc {arr[v]}', color=RED, fs=10)
    ax.set_xlim(-1.3, 8.4); ax.set_ylim(-0.75, 3.75); save(f, 'xebuyt')

def doitien():
    f, ax = fig(8.6, 2.7)
    def tri(cx, rates, title, col):
        P = {1: (cx, 2.0), 2: (cx + 1.6, 0.2), 3: (cx - 1.6, 0.2)}
        for (u, v, r, rad) in rates:
            edge(ax, P[u], P[v], color=col, lw=2.6, directed=True, label=r, rad=rad)
        for v, p in P.items(): node(ax, p, v, 'done')
        caption(ax, cx, -0.6, title, fs=11.5, color=col)
    tri(0, [(1, 2, '0.9', 0), (2, 3, '1.2', 0), (3, 1, '0.95', 0)], 'Ví dụ 1: 0,9 · 1,2 · 0,95 = 1,026 > 1', RED)
    tri(5.4, [(1, 2, '2', 0.25), (2, 1, '0.45', 0.25), (2, 3, '0.8', 0), (3, 1, '0.6', 0)], 'Ví dụ 2: mọi vòng đổi đều lỗ', NAVY)
    ax.set_xlim(-2.2, 7.6); ax.set_ylim(-0.9, 2.55); save(f, 'doitien')

def bayre():
    f, ax = fig(8.6, 2.6)
    for k, (cx, kk, best, title) in enumerate([(0, 2, [(1, 2), (2, 4)], 'k = 2: 1 → 2 → 4, giá 200'), (5.0, 3, [(1, 3), (3, 2), (2, 4)], 'k = 3: 1 → 3 → 2 → 4, giá 170')]):
        P = {1: (cx, 1.0), 2: (cx + 1.7, 2.0), 3: (cx + 1.7, 0.0), 4: (cx + 3.4, 1.0)}
        for u, v, w in [(1, 2, 100), (2, 4, 100), (1, 3, 50), (3, 2, 20), (3, 4, 300)]:
            on = (u, v) in best
            edge(ax, P[u], P[v], color=RED if on else GRAY, lw=3.2 if on else 2, directed=True, label=w)
        for v, p in P.items(): node(ax, p, v, 'src' if v == 1 else ('cur' if v == 4 else 'done'))
        caption(ax, cx + 1.7, -0.75, title, fs=11.5, color=RED)
    ax.set_xlim(-0.5, 8.9); ax.set_ylim(-1.05, 2.45); save(f, 'bayre')

def lichthidau():
    f, ax = fig(8.6, 2.7)
    P = {1: (0, 1.0), 2: (2.4, 2.0), 3: (4.8, 1.0), 4: (2.4, -0.7)}
    edge(ax, P[1], P[2], color=NAVY, lw=2.8, directed=True, label='+3')
    edge(ax, P[2], P[3], color=NAVY, lw=2.8, directed=True, label='+2')
    edge(ax, P[3], P[1], color=PURPLE, lw=2.4, directed=True, label='−6', dash=True, rad=-0.25)
    edge(ax, P[1], P[4], color=NAVY, lw=2.8, directed=True, label='+1')
    x = {1: 1, 2: 4, 3: 6, 4: 2}
    for v, p in P.items():
        node(ax, p, v, 'done'); tag(ax, (p[0] + 0.0, p[1] + 0.6 if v != 4 else p[1] - 0.6), f'ngày {x[v]}', color=RED, fs=10)
    ax.text(6.0, 1.9, 'Cung u → v nhãn c:', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(6.0, 1.45, 'ngày[v] ≥ ngày[u] + c', fontsize=11, color=NAVY)
    ax.text(6.0, 0.8, '"Trận 3 không muộn hơn', fontsize=10.5, color=PURPLE)
    ax.text(6.0, 0.4, ' trận 1 quá 6 ngày" thành', fontsize=10.5, color=PURPLE)
    ax.text(6.0, 0.0, ' ngày[1] ≥ ngày[3] − 6', fontsize=10.5, color=PURPLE)
    ax.set_xlim(-0.5, 9.0); ax.set_ylim(-1.65, 2.75); save(f, 'lichthidau')

def thudo():
    f, ax = fig(8.4, 2.7)
    P = {1: (0, 2.0), 2: (2.0, 2.0), 3: (2.0, 0.0), 4: (0, 0.0)}
    for u, v, w in [(1, 2, 3), (2, 3, 4), (3, 4, 2), (1, 4, 7), (2, 4, 1)]: edge(ax, P[u], P[v], color=NAVY if (u, v) != (1, 4) else GRAY, lw=2.6, label=w)
    for v, p in P.items(): node(ax, p, v, 'cur' if v == 2 else 'done')
    rows = [['', '1', '2', '3', '4', 'Tổng'], ['1', '0', '3', '6', '4', '13'], ['2', '3', '0', '3', '1', '7'], ['3', '6', '3', '0', '2', '11'], ['4', '4', '1', '2', '0', '7']]
    x0, y0, cw, ch = 3.4, 2.5, 0.72, 0.5
    for i, r in enumerate(rows):
        for j, t in enumerate(r):
            fc = '#E8EEF7' if i == 0 or j == 0 else ('#FFD966' if i == 2 else ('#FFF2CC' if i == 4 and j == 5 else 'white'))
            ax.add_patch(Rectangle((x0 + j*cw, y0 - (i+1)*ch), cw, ch, fc=fc, ec='#A0A0A0', lw=1))
            ax.text(x0 + j*cw + cw/2, y0 - i*ch - ch/2, t, ha='center', va='center', fontsize=11, fontweight='bold', color=NAVY if i == 0 or j == 0 else TXT)
    ax.set_xlim(-0.5, 7.8); ax.set_ylim(-0.4, 2.6); save(f, 'thudo')

def xephang():
    f, ax = fig(7.6, 2.6)
    P = {4: (0, 1.8), 1: (0, 0.2), 3: (1.8, 1.8), 2: (3.6, 1.0), 5: (5.4, 1.0)}
    for u, v in [(4, 3), (4, 2), (3, 2), (1, 2), (2, 5)]: edge(ax, P[u], P[v], color=NAVY, lw=2.6, directed=True)
    for v, p in P.items(): node(ax, p, v, 'cur' if v in (2, 5) else 'done')
    tag(ax, (3.6, 1.65), 'hạng 4', color=RED, fs=10); tag(ax, (5.4, 1.65), 'hạng 5', color=RED, fs=10)
    ax.text(6.0, 1.3, 'Cung a → b:', fontsize=10.5, color=NAVY, fontweight='bold'); ax.text(6.0, 0.9, 'a thắng b', fontsize=10.5, color=NAVY)
    ax.set_xlim(-0.5, 7.4); ax.set_ylim(-0.3, 2.3); save(f, 'xephang')

def xetai():
    f, ax = fig(7.4, 2.8)
    P = {1: (0, 2.0), 2: (2.0, 2.0), 3: (1.0, 0.3), 4: (3.6, 0.9), 5: (5.4, 0.9)}
    best = {(1, 2), (2, 3), (3, 4)}
    for u, v, c in [(1, 2, 10), (2, 3, 5), (1, 3, 3), (3, 4, 8), (4, 5, 2), (2, 4, 4)]:
        edge(ax, P[u], P[v], color=RED if (u, v) in best else GRAY, lw=3.2 if (u, v) in best else 2, label=c)
    for v, p in P.items(): node(ax, p, v, 'src' if v == 1 else ('cur' if v == 4 else 'done'))
    ax.text(2.8, -0.45, 'Từ 1 tới 4: đường 1 → 2 → 3 → 4 có cạnh yếu nhất 5', ha='center', fontsize=10.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.5, 5.9); ax.set_ylim(-0.75, 2.5); save(f, 'xetai')

def dengiaothong():
    f, ax = fig(8.8, 3.0)
    P = {1: (0, 1.2), 2: (2.2, 2.3), 3: (2.2, 0.1), 4: (4.4, 1.2)}
    for u, v in [(1, 2), (2, 4), (1, 3), (3, 4)]: edge(ax, P[u], P[v], color=RED if (u, v) in [(1, 3), (3, 4)] else GRAY, lw=3 if (u, v) in [(1, 3), (3, 4)] else 2.2)
    S = {1: '101', 2: '100', 3: '001', 4: '000'}
    for v, p in P.items():
        node(ax, p, v, 'src' if v == 1 else ('cur' if v == 4 else 'done'))
        for k, ch in enumerate(S[v]):
            x = p[0] - 0.45 + k*0.3; y = p[1] - 0.62 if v != 2 else p[1] + 0.55
            ax.add_patch(Circle((x + 0.15, y), 0.11, fc='#3FA34D' if ch == '1' else '#D9534F', ec='#404040', lw=1))
    # bảng thời gian
    rows = [('t = 0', 'ở 1, đèn 1 xanh → đi sang 3'), ('t = 1', 'tới 3, đèn 3 đỏ → đứng chờ'), ('t = 2', 'đèn 3 xanh → đi sang 4'), ('t = 3', 'tới 4: đích!')]
    for i, (a, b) in enumerate(rows):
        ax.text(5.4, 2.3 - i*0.55, a, fontsize=11, color=RED, fontweight='bold'); ax.text(6.2, 2.3 - i*0.55, b, fontsize=11, color=TXT)
    ax.text(5.4, -0.2, 'Chấm xanh/đỏ: màu đèn ở các phút 0, 1, 2 (lặp lại)', fontsize=9.5, color=GRAY, style='italic')
    ax.set_xlim(-0.6, 10.4); ax.set_ylim(-0.95, 3.0); save(f, 'dengiaothong')

def phatuong():
    g = ["S.#..", ".##.#", ".#..T", "...##"]
    f, ax = fig(8.4, 2.8)
    # k = 1: S(0,0)->(0,1)->(0,2)#->(0,3)->(1,3)->(2,3)->(2,4)
    p1 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 4)]
    p0 = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4)]
    for k, (path, x0, title) in enumerate([(p1, 0, 'k = 1: phá ô (1, 3), đi 6 bước'), (p0, 4.3, 'k = 0: đi vòng, 8 bước')]):
        colors = {c: '#C6E0B4' for c in path}; texts = {c: i for i, c in enumerate(path)}
        if k == 0: colors[(0, 2)] = '#F8CBAD'
        texts[(0, 0)] = 'S'; texts[path[-1]] = 'T'
        gg = [row.replace('S', '.').replace('T', '.') for row in g]
        if k == 0: gg[0] = 'S..' .replace('S', '.') + '..'
        grid(ax, g, x0=x0, y0=2.6, s=0.6, colors=colors, texts=texts, fs=12)
        caption(ax, x0 + 1.5, -0.2, title, fs=11.5, color=RED if k == 0 else NAVY)
    ax.set_xlim(-0.2, 7.5); ax.set_ylim(-0.5, 2.7); save(f, 'phatuong')

def robotxoay():
    g = ["S....", ".###.", ".#T..", "....."]
    f, ax = fig(7.6, 2.8)
    path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 3), (2, 2)]
    colors = {c: '#DDEBF7' for c in path}; colors[(0, 4)] = '#FFD966'; colors[(2, 4)] = '#FFD966'
    grid(ax, g, x0=0, y0=2.6, s=0.62, colors=colors, texts={(0, 0): 'S', (2, 2): 'T'}, fs=12)
    pts = [cell_center(i, j, 0, 2.6, 0.62) for i, j in path]
    for a, b in zip(pts, pts[1:]):
        ax.annotate('', xy=b, xytext=a, arrowprops=dict(arrowstyle='-|>', color=RED, lw=2, mutation_scale=12, shrinkA=6, shrinkB=6))
    ax.text(3.5, 2.2, 'Ô vàng: robot quay 90°', fontsize=11, color=AMBER, fontweight='bold')
    ax.text(3.5, 1.75, 'Xuất phát hướng Đông (E)', fontsize=11, color=NAVY)
    ax.text(3.5, 1.3, 'quay sang Nam ở ô (1, 5),', fontsize=11, color=NAVY)
    ax.text(3.5, 0.85, 'quay sang Tây ở ô (3, 5).', fontsize=11, color=NAVY)
    ax.text(3.5, 0.3, 'Tổng cộng: 2 lần quay', fontsize=11.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.1, 6.6); ax.set_ylim(-0.0, 2.7); save(f, 'robotxoay')

for fn in [duongtruong, nutgiao, xebuyt, doitien, bayre, lichthidau, thudo, xephang, xetai, dengiaothong, phatuong, robotxoay]: fn()
