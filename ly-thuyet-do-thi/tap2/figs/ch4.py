from figlib import *

def xhgiaidau():
    f, ax = fig(9.2, 2.4)
    # vd1
    P = {1: (0, 1.0), 3: (1.3, 1.0), 2: (2.6, 1.0), 4: (3.9, 1.0)}
    for u, v in [(1, 3), (3, 2), (2, 4)]: edge(ax, P[u], P[v], color=NAVY, lw=2.6, directed=True)
    edge(ax, P[1], P[2], color=GRAY, lw=2, directed=True, rad=-0.45)
    for v, p in P.items(): node(ax, p, v, 'done', r=0.28, fs=13)
    caption(ax, 1.95, -0.4, 'Ví dụ 1: thứ hạng duy nhất\n1, 3, 2, 4', fs=10.5)
    Q = {1: (5.2, 1.4), 2: (6.3, 1.4), 3: (5.75, 0.4)}
    edge(ax, Q[1], Q[2], color=NAVY, lw=2.6, directed=True)
    for v, p in Q.items(): node(ax, p, v, 'done', r=0.28, fs=13)
    caption(ax, 5.75, -0.4, 'Ví dụ 2:\nchưa rõ → 0', fs=10.5)
    R_ = {1: (7.5, 1.4), 2: (8.7, 1.4), 3: (8.1, 0.4)}
    for u, v in [(1, 2), (2, 3), (3, 1)]: edge(ax, R_[u], R_[v], color=RED, lw=2.6, directed=True)
    for v, p in R_.items(): node(ax, p, v, 'ans', r=0.28, fs=13)
    caption(ax, 8.1, -0.4, 'Ví dụ 3:\nvòng tròn → −1', fs=10.5, color=RED)
    ax.set_xlim(-0.5, 9.4); ax.set_ylim(-0.85, 1.9); save(f, 'xhgiaidau')

def xaynha():
    f, ax = fig(9.0, 3.0)
    jobs = {1: (0, 3), 2: (3, 2), 3: (3, 4), 4: (5, 2), 5: (7, 1), 6: (5, 2)}
    crit = {1, 2, 3, 4, 5}
    for k, (j, (s, t)) in enumerate(sorted(jobs.items())):
        y = 2.6 - k*0.42
        ax.add_patch(FancyBboxPatch((s*0.9, y - 0.15), t*0.9, 0.3, boxstyle='round,pad=0.01,rounding_size=0.05',
                                    fc='#F8CBAD' if j in crit else '#BDD7EE', ec=RED if j in crit else NAVY, lw=1.6))
        ax.text(s*0.9 + t*0.45, y, f'việc {j}', ha='center', va='center', fontsize=9.5, fontweight='bold', color=TXT)
        if j == 6: ax.add_patch(Rectangle((7*0.9, y - 0.15), 0.9, 0.3, fc='none', ec=GRAY, lw=1.2, ls='--')); ax.text(7*0.9 + 0.45, y, 'dư 1', ha='center', va='center', fontsize=8.5, color=GRAY)
    for t in range(9):
        ax.plot([t*0.9, t*0.9], [0.15, 2.85], color='#E0E0E0', lw=0.8, zorder=0)
        ax.text(t*0.9, 0.0, str(t), ha='center', fontsize=9.5, color=GRAY)
    ax.text(3.6, -0.35, 'ngày', ha='center', fontsize=9.5, color=GRAY)
    ax.text(8.6, 2.2, 'Đỏ: việc then chốt', fontsize=10.5, color=RED, fontweight='bold')
    ax.text(8.6, 1.8, '(chậm 1 ngày là', fontsize=10, color=RED)
    ax.text(8.6, 1.45, ' dự án chậm theo)', fontsize=10, color=RED)
    ax.text(8.6, 0.9, 'Xanh: việc 6 còn', fontsize=10.5, color=NAVY, fontweight='bold')
    ax.text(8.6, 0.55, '1 ngày dự trữ', fontsize=10, color=NAVY)
    ax.set_xlim(-0.2, 11.0); ax.set_ylim(-0.5, 2.95); save(f, 'xaynha')

def demlotrinh():
    f, ax = fig(9.4, 2.7)
    P = {1: (0, 1.0), 2: (1.2, 1.9), 3: (1.2, 0.1), 4: (2.6, 1.0), 5: (3.8, 1.0)}
    cnt = {1: 1, 2: 1, 3: 2, 4: 3, 5: 5}
    for u, v in [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)]: edge(ax, P[u], P[v], color=NAVY, lw=2.4, directed=True)
    edge(ax, P[3], P[5], color=NAVY, lw=2.4, directed=True, rad=0.3)
    for v, p in P.items():
        node(ax, p, v, 'done', r=0.28, fs=13); tag(ax, (p[0] + 0.0, p[1] + (0.5 if v != 3 else -0.5)), str(cnt[v]), color=RED, fs=10)
    caption(ax, 1.9, -1.05, 'Ví dụ 1: số lộ trình\ntừ 1 tới mỗi nút (ô đỏ)', fs=10.5)
    Q = {1: (5.2, 1.0), 2: (6.4, 1.9), 3: (6.4, 0.1), 4: (7.8, 1.0)}
    edge(ax, Q[1], Q[2], color=NAVY, lw=2.4, directed=True); edge(ax, Q[1], Q[4], color=NAVY, lw=2.4, directed=True)
    edge(ax, Q[2], Q[3], color=RED, lw=2.8, directed=True, rad=0.3); edge(ax, Q[3], Q[2], color=RED, lw=2.8, directed=True, rad=0.3)
    edge(ax, Q[3], Q[4], color=NAVY, lw=2.4, directed=True)
    for v, p in Q.items(): node(ax, p, v, 'ans' if v in (2, 3) else 'done', r=0.28, fs=13)
    caption(ax, 6.5, -1.05, 'Ví dụ 3: vòng 2 ⇄ 3 nằm\ntrên đường từ 1 tới 4 → vô số', fs=10.5, color=RED)
    ax.set_xlim(-0.5, 9.0); ax.set_ylim(-1.5, 2.4); save(f, 'demlotrinh')

def huyetmach():
    f, ax = fig(8.2, 2.4)
    P = {1: (0, 1.6), 2: (0, 0.2), 3: (1.4, 0.9), 4: (3.0, 0.9), 5: (4.6, 0.9), 6: (6.2, 0.9)}
    for i, (u, v) in enumerate([(1, 2), (2, 3), (3, 1)], 1): edge(ax, P[u], P[v], color=NAVY, lw=2.4, label=i, lfs=9)
    edge(ax, P[3], P[4], color=RED, lw=3.4, label=4, lfs=10)
    edge(ax, P[4], P[5], color=NAVY, lw=2.4, rad=0.3, label=5, lfs=9); edge(ax, P[4], P[5], color=NAVY, lw=2.4, rad=-0.3, label=6, lfs=9)
    edge(ax, P[5], P[6], color=RED, lw=3.4, label=7, lfs=10)
    for v, p in P.items(): node(ax, p, v, 'done')
    ax.text(3.1, -0.35, 'Đường 4 và 7 (đỏ) là huyết mạch; hai đường song song 5, 6 thì không', ha='center', fontsize=10.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.5, 6.8); ax.set_ylim(-0.6, 2.1); save(f, 'huyetmach')

def bienap():
    f, ax = fig(8.2, 2.7)
    P = {1: (0, 1.8), 2: (0, 0.3), 3: (1.4, 1.05), 4: (3.0, 1.05), 5: (4.2, 2.0), 6: (4.2, 0.1), 7: (4.8, 1.05)}
    for u, v in [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 6), (6, 4), (4, 7)]: edge(ax, P[u], P[v], color=NAVY, lw=2.4)
    for v, p in P.items(): node(ax, p, v, 'cur' if v in (3, 4) else 'done')
    ax.text(5.6, 1.9, 'Bỏ trạm 3: còn {1, 2} và {4, 5, 6, 7}', fontsize=10.5, color=RED)
    ax.text(5.6, 1.45, '→ 2 phần', fontsize=10.5, color=RED, fontweight='bold')
    ax.text(5.6, 0.85, 'Bỏ trạm 4: còn {1, 2, 3}, {5, 6}, {7}', fontsize=10.5, color=RED)
    ax.text(5.6, 0.4, '→ 3 phần', fontsize=10.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.5, 9.6); ax.set_ylim(-0.3, 2.4); save(f, 'bienap')

def capduphong():
    f, ax = fig(9.4, 2.7)
    P = {1: (0, 1.9), 2: (0, 0.3), 3: (1.3, 1.1), 4: (2.7, 1.1), 5: (3.7, 2.0), 6: (3.9, 0.3), 7: (5.2, 0.3)}
    for u, v in [(1, 2), (2, 3), (3, 1)]: edge(ax, P[u], P[v], color=NAVY, lw=2.4)
    for u, v in [(3, 4), (4, 5), (4, 6), (6, 7)]: edge(ax, P[u], P[v], color=RED, lw=3)
    edge(ax, P[5], P[1], color=GREEN, lw=2.6, dash=True, rad=0.25); edge(ax, P[7], P[2], color=GREEN, lw=2.6, dash=True, rad=-0.45)
    for v, p in P.items(): node(ax, p, v, 'done')
    ax.text(6.0, 2.0, 'Đỏ: cáp mà đứt là mất liên lạc (cầu)', fontsize=10.5, color=RED)
    ax.text(6.0, 1.5, 'Xanh nét đứt: 2 sợi cáp dự phòng', fontsize=10.5, color=GREEN, fontweight='bold')
    ax.text(6.0, 1.0, 'Nén mỗi nhóm "vững" thành một đỉnh:', fontsize=10, color=NAVY)
    ax.text(6.0, 0.6, 'cây có 3 lá {1,2,3}, 5, 7 → ⌈3/2⌉ = 2', fontsize=10, color=NAVY)
    ax.set_xlim(-0.5, 10.4); ax.set_ylim(-1.5, 2.6); save(f, 'capduphong')

def tindon():
    f, ax = fig(8.8, 2.8)
    P = {1: (0, 2.0), 2: (1.2, 2.0), 3: (0.6, 0.9), 4: (2.4, 0.9), 5: (2.4, 2.3), 6: (3.9, 0.9), 7: (5.1, 0.9)}
    for u, v in [(1, 2), (2, 3), (3, 1)]: edge(ax, P[u], P[v], color=NAVY, lw=2.4, directed=True)
    for u, v in [(3, 4), (5, 4), (4, 6)]: edge(ax, P[u], P[v], color=GRAY, lw=2.2, directed=True)
    edge(ax, P[6], P[7], color=NAVY, lw=2.4, directed=True, rad=0.3); edge(ax, P[7], P[6], color=NAVY, lw=2.4, directed=True, rad=0.3)
    for v, p in P.items(): node(ax, p, v, 'cur' if v in (1, 5) else 'done')
    from matplotlib.patches import Ellipse
    for c, w, h in [((0.6, 1.6), 2.3, 2.0), ((4.5, 0.9), 2.0, 1.1)]:
        ax.add_patch(Ellipse(c, w, h, fc='none', ec=TEAL, lw=1.6, ls='--'))
    ax.text(5.9, 2.3, 'Thành phần nguồn (không có', fontsize=10.5, color=RED)
    ax.text(5.9, 1.95, 'cung đi vào): {1, 2, 3} và {5}', fontsize=10.5, color=RED)
    ax.text(5.9, 1.55, '→ kể cho 1 và 5 là đủ', fontsize=10.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.8, 9.0); ax.set_ylim(0.0, 2.8); save(f, 'tindon')

def khobau():
    f, ax = fig(8.4, 2.8)
    P = {1: (0, 2.0), 2: (1.3, 2.0), 3: (0.65, 0.8), 4: (2.6, 0.8), 5: (3.9, 0.8), 6: (2.8, 2.2)}
    g = {1: 5, 2: 1, 3: 3, 4: 4, 5: 2, 6: 7}
    for u, v in [(1, 2), (2, 3), (3, 1)]: edge(ax, P[u], P[v], color=RED, lw=2.8, directed=True)
    edge(ax, P[3], P[4], color=GRAY, lw=2.2, directed=True)
    edge(ax, P[4], P[5], color=GRAY, lw=2.2, directed=True, rad=0.3); edge(ax, P[5], P[4], color=GRAY, lw=2.2, directed=True, rad=0.3)
    edge(ax, P[2], P[6], color=RED, lw=2.8, directed=True)
    for v, p in P.items():
        node(ax, p, v, 'src' if v == 1 else ('cur' if v in (2, 3, 6) else 'done'))
        tag(ax, (p[0] + 0.45, p[1] + 0.42), f'{g[v]}', color=AMBER, fs=10)
    ax.text(4.8, 2.1, 'Vòng 1 → 2 → 3 → 1 nhặt hết 5 + 1 + 3 = 9,', fontsize=10.5, color=RED)
    ax.text(4.8, 1.7, 'rồi sang 6 nhặt thêm 7: tổng 16.', fontsize=10.5, color=RED, fontweight='bold')
    ax.text(4.8, 1.1, 'Sang {4, 5} chỉ được 9 + 6 = 15.', fontsize=10.5, color=NAVY)
    ax.set_xlim(-0.5, 9.4); ax.set_ylim(0.2, 2.8); save(f, 'khobau')

def tuyenchon():
    f, ax = fig(8.6, 2.6)
    labels = {1: '+1', 2: '−1', 3: '+2', 4: '−2', 5: '+3', 6: '−3'}
    P = {1: (0, 2.0), 2: (0, 0.3), 3: (2.2, 2.6), 4: (2.2, -0.3), 5: (4.4, 2.0), 6: (4.4, 0.3)}
    # yêu cầu (1 hoặc 2): −1→+2, −2→+1; (−1 hoặc 3): +1→+3, −3→−1; (−2 hoặc −3): +2→−3, +3→−2; (2 hoặc −3): −2→−3, +3→+2
    E = [(2, 3), (4, 1), (1, 5), (6, 2), (3, 6), (5, 4), (4, 6), (5, 3)]
    for u, v in E: edge(ax, P[u], P[v], color=GRAY, lw=1.8, directed=True, r=0.34, head=11)
    chosen = {2, 3, 6}
    for v, p in P.items(): node(ax, p, labels[v], 'cur' if v in chosen else 'done', r=0.34, fs=12)
    ax.text(5.3, 2.0, '"+i": nhận thí sinh i, "−i": loại i', fontsize=10.5, color=NAVY)
    ax.text(5.3, 1.55, 'Yêu cầu "x hoặc y" cho hai cung', fontsize=10.5, color=NAVY)
    ax.text(5.3, 1.15, '¬x → y và ¬y → x', fontsize=10.5, color=NAVY, fontweight='bold')
    ax.text(5.3, 0.6, 'Vàng: phương án 010', fontsize=10.5, color=AMBER, fontweight='bold')
    ax.text(5.3, 0.2, '(loại 1, nhận 2, loại 3)', fontsize=10.5, color=AMBER)
    ax.set_xlim(-0.5, 8.9); ax.set_ylim(-0.75, 3.05); save(f, 'tuyenchon')

def netve():
    f, ax = fig(9.4, 2.9)
    P = {1: (0, 1.0), 2: (1.4, 1.0), 3: (1.4, -0.4), 4: (0, -0.4), 5: (0.7, 2.0)}
    for u, v in [(1, 2), (2, 3), (3, 4), (4, 1), (1, 5), (2, 5), (1, 3), (2, 4)]: edge(ax, P[u], P[v], color=NAVY, lw=2.4, r=0.27)
    for v, p in P.items(): node(ax, p, v, 'cur' if v in (3, 4) else 'done', r=0.27, fs=12)
    caption(ax, 0.7, -1.15, 'Bộ 1: hai đỉnh lẻ\n3, 4 → YES', fs=10.5)
    Q = {1: (3.6, 0.5), 2: (3.6, 1.8), 3: (2.6, -0.4), 4: (4.6, -0.4)}
    for v in (2, 3, 4): edge(ax, Q[1], Q[v], color=NAVY, lw=2.4, r=0.27)
    for v, p in Q.items(): node(ax, p, v, 'cur', r=0.27, fs=12)
    caption(ax, 3.6, -1.15, 'Bộ 2: bốn đỉnh lẻ\n→ NO', fs=10.5, color=RED)
    R_ = {1: (6.0, 1.3), 2: (7.0, 1.3), 3: (6.5, 0.4), 4: (7.8, 1.3), 5: (8.8, 1.3), 6: (8.3, 0.4)}
    for u, v in [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]: edge(ax, R_[u], R_[v], color=NAVY, lw=2.4, r=0.27)
    for v, p in R_.items(): node(ax, p, v, 'done', r=0.27, fs=12)
    caption(ax, 7.4, -1.15, 'Bộ 3: bậc đều chẵn nhưng\nhai mảnh rời nhau → NO', fs=10.5, color=RED)
    ax.set_xlim(-0.5, 9.4); ax.set_ylim(-1.7, 2.4); save(f, 'netve')

def domino_tile(ax, x, y, a, b, w=0.9, h=0.45, hl=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.0,rounding_size=0.08', fc='#FFFDF5', ec=RED if hl else NAVY, lw=2))
    ax.plot([x + w/2, x + w/2], [y + 0.05, y + h - 0.05], color=NAVY, lw=1.4)
    import random
    pos = {0: [], 1: [(0, 0)], 2: [(-1, 1), (1, -1)], 3: [(-1, 1), (0, 0), (1, -1)], 4: [(-1, 1), (1, 1), (-1, -1), (1, -1)],
           5: [(-1, 1), (1, 1), (0, 0), (-1, -1), (1, -1)], 6: [(-1, 1), (-1, 0), (-1, -1), (1, 1), (1, 0), (1, -1)]}
    for k, val in enumerate((a, b)):
        cx = x + w/4 + k*w/2; cy = y + h/2
        for dx, dy in pos[val]: ax.add_patch(Circle((cx + dx*0.1, cy + dy*0.11), 0.035, fc=NAVY, ec='none'))
def domino():
    f, ax = fig(9.0, 2.2)
    tiles = [(1, 2, '1'), (2, 4, '2'), (3, 1, '3'), (4, 4, '4'), (3, 2, '5')]
    for k, (a, b, i) in enumerate(tiles):
        domino_tile(ax, k*1.15, 1.3, a, b); ax.text(k*1.15 + 0.45, 1.05, f'quân {i}', ha='center', fontsize=9.5, color=GRAY)
    caption(ax, 2.8, 2.0, 'Các quân domino của ví dụ 1', fs=10.5)
    row = [(2, 1, '1−'), (1, 3, '3−'), (3, 2, '5+'), (2, 4, '2+'), (4, 4, '4+')]
    for k, (a, b, t) in enumerate(row):
        domino_tile(ax, k*0.95, -0.2, a, b, hl=True); ax.text(k*0.95 + 0.45, -0.45, t, ha='center', fontsize=10, color=RED, fontweight='bold')
    caption(ax, 2.35, 0.55, 'Một cách xếp: các nửa kề nhau có cùng số chấm', fs=10.5, color=RED)
    ax.set_xlim(-0.2, 6.0); ax.set_ylim(-0.7, 2.2); save(f, 'domino')

def ketsat():
    f, ax = fig(8.8, 2.9)
    P = {'00': (0, 1.0), '01': (1.6, 2.0), '10': (1.6, 0.0), '11': (3.2, 1.0)}
    E = [('00', '00', '0'), ('00', '01', '1'), ('01', '10', '0'), ('01', '11', '1'), ('10', '00', '0'), ('10', '01', '1'), ('11', '10', '0'), ('11', '11', '1')]
    for u, v, c in E:
        if u == v:
            loop(ax, P[u], color=NAVY, r=0.36, ang=180 if u == '00' else 0, size=0.5)
            ax.text(P[u][0] + (-1.15 if u == '00' else 1.15), P[u][1], c, fontsize=11, color=RED, fontweight='bold', ha='center', va='center')
        elif (u, v) in [('01', '10'), ('10', '01')]:
            edge(ax, P[u], P[v], color=NAVY, lw=2.2, directed=True, label=c, rad=0.25, r=0.36, lcolor=RED)
        else:
            edge(ax, P[u], P[v], color=NAVY, lw=2.2, directed=True, label=c, r=0.36, lcolor=RED)
    for v, p in P.items(): node(ax, p, v, 'done', r=0.36, fs=12)
    ax.text(4.9, 2.1, 'Đỉnh: 2 chữ số cuối đã bấm (k − 1 = 2)', fontsize=10.5, color=NAVY)
    ax.text(4.9, 1.7, 'Cung: bấm thêm 1 chữ số → một mã mới', fontsize=10.5, color=NAVY)
    ax.text(4.9, 1.2, 'Mỗi cung là đúng một mã 3 chữ số;', fontsize=10.5, color=RED)
    ax.text(4.9, 0.8, 'đi qua mọi cung đúng một lần =', fontsize=10.5, color=RED)
    ax.text(4.9, 0.4, 'chu trình Euler → xâu 0001011100', fontsize=10.5, color=RED, fontweight='bold')
    ax.set_xlim(-1.4, 9.4); ax.set_ylim(-0.5, 2.5); save(f, 'ketsat')

for fn in [xhgiaidau, xaynha, demlotrinh, huyetmach, bienap, capduphong, tindon, khobau, tuyenchon, netve, domino, ketsat]: fn()
