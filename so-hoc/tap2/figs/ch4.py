# Hình Chương 4 (Tập 2)
from shlib import *
import math

YEL, YEC = '#FFD966', RED          # đáp số / đang xét
BLU, BLC = '#BDD7EE', NAVY         # bình thường / đã xong
ORG, ORC = '#FFE7B3', AMBER        # dữ liệu vào
GRY, GRC = '#EDEDED', '#9A9A9A'    # bị loại

def candy(ax, x, y, fc, ec, r=0.2):
    ax.add_patch(Circle((x, y), r, fc=fc, ec=ec, lw=1.6, zorder=3))

def chiakeo():
    f, ax = fig(9.0, 3.6)
    names = ['An', 'Bình', 'Chi']
    # bước 1: phát trước mỗi bạn 1 cái
    ax.text(-0.3, 2.35, 'Bước 1: phát trước mỗi bạn t = 1 cái', fontsize=11, color=NAVY, fontweight='bold', va='center')
    for j, nm in enumerate(names):
        x = 0.4 + j * 1.5
        candy(ax, x, 1.75, ORG, ORC)
        ax.text(x, 1.3, nm, ha='center', va='center', fontsize=10, color=TXT)
    ax.text(5.0, 1.75, 'còn lại 10 − 3 · 1 = 7 cái', fontsize=10.5, color=AMBER, fontweight='bold', va='center')
    # bước 2: 7 kẹo + 2 vạch trong 9 ô
    ax.text(-0.3, 0.75, 'Bước 2: xếp 7 kẹo và 2 vạch vào 9 ô', fontsize=11, color=NAVY, fontweight='bold', va='center')
    seq = 'KK|KKKK|K'
    x0, s = 0.1, 0.78
    for i, ch in enumerate(seq):
        x = x0 + i * s
        ax.add_patch(Rectangle((x - s / 2 + 0.03, -0.38), s - 0.06, 0.66, fc='#F7F7F7', ec='#C8C8C8', lw=1, zorder=1))
        if ch == 'K': candy(ax, x, -0.05, BLU, BLC)
        else: ax.plot([x, x], [-0.32, 0.22], color=RED, lw=4, solid_capstyle='butt', zorder=3)
        ax.text(x, -0.55, str(i + 1), ha='center', va='top', fontsize=9.5, color='#707070')
    groups = [(0, 1, 'An: 2 + 1 = 3'), (3, 6, 'Bình: 4 + 1 = 5'), (8, 8, 'Chi: 1 + 1 = 2')]
    for a, b, t in groups:
        xa, xb = x0 + a * s - 0.25, x0 + b * s + 0.25
        ax.plot([xa, xa, xb, xb], [-0.95, -1.05, -1.05, -0.95], color=GREEN, lw=1.5)
        ax.text((xa + xb) / 2, -1.25, t, ha='center', va='top', fontsize=10, color=GREEN, fontweight='bold')
    tx = x0 + 9 * s + 0.4
    ax.text(tx, 0.15, 'Mỗi cách chọn 2 ô làm vạch\nứng với đúng một cách chia:', fontsize=10.5, color=TXT, va='center')
    ax.text(tx, -0.75, 'C(9, 2) = 36 cách', fontsize=12.5, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-0.4, tx + 3.6); ax.set_ylim(-1.75, 2.6); save(f, 'chiakeo')

def duongluoi():
    f, ax = fig(8.6, 3.9)
    m, n = 4, 3; bad = {(3, 2), (1, 1)}
    F = {}
    for x in range(m + 1):
        for y in range(n + 1):
            F[x, y] = 0 if (x, y) in bad else (1 if x == y == 0 else F.get((x - 1, y), 0) + F.get((x, y - 1), 0))
    s = 1.05
    for x in range(m + 1):
        ax.plot([x * s, x * s], [0, n * s], color=LGRAY, lw=1.5, zorder=0)
    for y in range(n + 1):
        ax.plot([0, m * s], [y * s, y * s], color=LGRAY, lw=1.5, zorder=0)
    path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3)]
    for p, q in zip(path, path[1:]):
        ax.plot([p[0] * s, q[0] * s], [p[1] * s, q[1] * s], color=RED, lw=3.2, zorder=1, alpha=0.75)
    for (x, y), v in F.items():
        if (x, y) in bad: st, lab = 'gray', '×'
        elif (x, y) == (m, n): st, lab = 'cur', v
        elif (x, y) == (0, 0): st, lab = 'src', v
        else: st, lab = 'done', v
        node(ax, (x * s, y * s), lab, st, r=0.3, fs=12)
    ax.text(-0.15, -0.6, 'O(0, 0)', ha='center', fontsize=9.5, color=PURPLE)
    ax.text(m * s + 0.15, n * s + 0.55, 'T(4, 3)', ha='center', fontsize=9.5, color=RED, fontweight='bold')
    ax.text(1 * s + 0.42, 1 * s - 0.42, 'B', fontsize=10.5, color='#606060', fontweight='bold')
    ax.text(3 * s + 0.42, 2 * s - 0.42, 'A', fontsize=10.5, color='#606060', fontweight='bold')
    tx = m * s + 1.3
    L = ['Không có ô cấm:  C(7, 3) = 35',
         'Qua B:  C(2, 1) · C(5, 2) = 2 · 10 = 20',
         'Qua A:  C(5, 2) · C(2, 1) = 10 · 2 = 20',
         'Qua B rồi A:  2 · C(3, 1) · 2 = 12']
    for i, t in enumerate(L):
        ax.text(tx, n * s - 0.05 - i * 0.62, t, fontsize=10.5, color=TXT, va='center')
    ax.text(tx, n * s - 0.05 - 4 * 0.62 - 0.1, '35 − 20 − 20 + 12 = 7', fontsize=12.5, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-0.75, tx + 4.6); ax.set_ylim(-0.95, n * s + 0.85); save(f, 'duongluoi')

def tohoplon():
    f, ax = fig(9.4, 3.5)
    ax.text(2.0, 2.05, 'Lucas: C(1000, 500) mod 7', ha='center', fontsize=11, color=NAVY, fontweight='bold')
    rows = [('n = 1000', [2, 6, 2, 6], ORG, ORC), ('k = 500', [1, 3, 1, 3], ORG, ORC),
            ('C(nᵢ, kᵢ)', [2, 20, 2, 20], BLU, BLC), ('mod 7', [2, 6, 2, 6], BLU, BLC)]
    for r_, (lab, vals, fc, ec) in enumerate(rows):
        y = 1.35 - r_ * 0.66
        ax.text(-0.15, y, lab, ha='right', va='center', fontsize=11, color=TXT, fontweight='bold')
        for j, v in enumerate(vals):
            cellbox(ax, 0.55 + j * 0.95, y, v, fc=fc, ec=ec, w=0.82, h=0.52, fs=11)
    for j in range(4):
        ax.text(0.55 + j * 0.95, 1.83 - 0.05, f'$7^{3 - j}$', ha='center', va='center', fontsize=10, color='#707070')
    ax.text(2.0, -1.45, '2 · 6 · 2 · 6 = 144 ≡ 4 (mod 7)', ha='center', fontsize=11.5, color=RED, fontweight='bold')
    # Trung Hoa
    bx = 6.6
    ax.text(bx + 1.6, 2.05, 'Trung Hoa: C(10, 5) mod 30', ha='center', fontsize=11, color=NAVY, fontweight='bold')
    for i, (p, r) in enumerate([(2, 0), (3, 0), (5, 2)]):
        y = 1.3 - i * 0.85
        tag(ax, (bx + 0.35, y), f'mod {p}:  {r}', color=NAVY, fs=10.5, bg=BLU)
        ax.annotate('', xy=(bx + 2.3, 0.45), xytext=(bx + 1.3, y), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.5))
    tag(ax, (bx + 3.35, 0.45), 'mod 30:  12', color=RED, fs=12, bg=YEL)
    ax.text(bx + 1.6, -1.45, 'C(10, 5) = 252 ≡ 12 (mod 30)', ha='center', fontsize=11.5, color=TXT)
    ax.plot([5.3, 5.3], [-1.6, 2.2], color=LGRAY, lw=1.2)
    ax.set_xlim(-1.6, bx + 4.3); ax.set_ylim(-1.75, 2.3); save(f, 'tohoplon')

def boiso():
    f, ax = fig(9.0, 2.6)
    s = 0.6
    for x in range(1, 31):
        i, j = (x - 1) // 15, (x - 1) % 15
        good = (x % 2 == 0 or x % 3 == 0)
        if good and x % 5: fc, ec, col = YEL, YEC, TXT
        elif good: fc, ec, col = GRY, GRC, '#8A8A8A'
        else: fc, ec, col = '#FFFFFF', '#B4C6E7', '#404040'
        cx, cy = j * s, -i * 0.72
        cellbox(ax, cx, cy, x, fc=fc, ec=ec, w=s - 0.06, h=0.6, fs=10.5, bold=good and x % 5 != 0, color=col)
        if good and x % 5 == 0:
            ax.plot([cx - 0.22, cx + 0.22], [cy - 0.22, cy + 0.22], color=RED, lw=1.6, zorder=6)
    y = -1.45
    ax.add_patch(Rectangle((0 - 0.2, y - 0.17), 0.36, 0.34, fc=YEL, ec=YEC, lw=1.4))
    ax.text(0.3, y, 'chia hết cho 2 hoặc 3, không chia hết cho 5 (16 số)', va='center', fontsize=10, color=TXT)
    ax.add_patch(Rectangle((6.0 - 0.2, y - 0.17), 0.36, 0.34, fc=GRY, ec=GRC, lw=1.4))
    ax.text(6.3, y, 'bị loại vì chia hết cho 5 (4 số)', va='center', fontsize=10, color=TXT)
    ax.text(14 * s / 2, -2.05, '⌊30/2⌋ + ⌊30/3⌋ − ⌊30/6⌋ − ⌊30/10⌋ − ⌊30/15⌋ + ⌊30/30⌋ = 15 + 10 − 5 − 3 − 2 + 1 = 16',
            ha='center', va='center', fontsize=10.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.9, 14 * s + 0.9); ax.set_ylim(-2.35, 0.45); save(f, 'boiso')

def ntcn():
    f, ax = fig(7.0, 4.0)
    s = 0.36
    for x in range(1, 101):
        i, j = (x - 1) // 10, (x - 1) % 10
        ok = math.gcd(x, 30) == 1
        cellbox(ax, j * s, -i * s, x, fc=YEL if ok else '#F4F4F4', ec=YEC if ok else '#C8C8C8', w=s - 0.03, h=s - 0.03,
                fs=9.5, bold=ok, color=TXT if ok else '#9A9A9A', lw=1.0)
    tx = 10 * s + 0.25
    rows = [('{2}', '+', '50'), ('{3}', '+', '33'), ('{5}', '+', '20'), ('{2, 3}', '−', '16'), ('{2, 5}', '−', '10'),
            ('{3, 5}', '−', '6'), ('{2, 3, 5}', '+', '3')]
    hdr = ['Tập con', 'Dấu', '⌊100 / d⌋']
    cw = [1.0, 0.55, 1.0]; rh = 0.34
    xs = [tx + sum(cw[:k]) + cw[k] / 2 for k in range(3)]
    for k in range(3): cellbox(ax, xs[k], 0.0, hdr[k], fc='#E8EEF7', ec=NAVY, w=cw[k], h=rh, fs=10)
    for r_, row in enumerate(rows):
        y = -(r_ + 1) * rh
        neg = row[1] == '−'
        for k in range(3):
            cellbox(ax, xs[k], y, row[k], fc='#FBE5EE' if neg else '#E6F2E6', ec='#C8C8C8', w=cw[k], h=rh, fs=10, bold=False, lw=1)
    y = -8 * rh - 0.2
    ax.text(tx, y, 'Có ước chung với 30:', fontsize=10.5, color=TXT, va='center')
    ax.text(tx, y - 0.32, '50 + 33 + 20 − 16 − 10 − 6 + 3 = 74', fontsize=10.5, color=TXT, va='center')
    ax.text(tx, y - 0.72, 'Đáp số: 100 − 74 = 26', fontsize=11.5, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-0.25, tx + sum(cw) + 0.1); ax.set_ylim(-9 * s - 0.25, 0.25); save(f, 'ntcn')

def tangqua():
    f, ax = fig(9.6, 3.0)
    import itertools
    perms = [p for p in itertools.permutations(range(1, 5)) if sum(p[i] == i + 1 for i in range(4)) == 1]
    s = 0.5; gw = 4 * s + 0.55
    for g in range(4):
        x0 = g * gw
        ax.text(x0 + 1.5 * s, 0.75, f'người {g + 1} may mắn', ha='center', fontsize=10.5, color=NAVY, fontweight='bold')
        for j in range(4): ax.text(x0 + j * s, 0.38, str(j + 1), ha='center', fontsize=10, color='#707070')
        grp = [p for p in perms if p[g] == g + 1]
        for r_, p in enumerate(grp):
            for j in range(4):
                fix = p[j] == j + 1
                cellbox(ax, x0 + j * s, -r_ * 0.55, p[j], fc=YEL if fix else BLU, ec=YEC if fix else BLC, w=s - 0.06, h=0.48, fs=11)
    ax.text(-0.45, 0.38, 'người', ha='right', fontsize=10, color='#707070')
    ax.text(-0.45, -0.27, 'nhận\nquà của', ha='right', va='center', fontsize=10, color='#707070')
    ax.text(1.5 * gw - 0.3, -1.35, 'C(4, 1) cách chọn người may mắn  ×  D(3) = 2 cách cho ba người còn lại  =  8',
            ha='center', fontsize=11.5, color=RED, fontweight='bold')
    ax.set_xlim(-1.6, 4 * gw - 0.2); ax.set_ylim(-1.6, 1.0); save(f, 'tangqua')

def latgach():
    f, ax = fig(9.2, 4.0)
    def tilings(n):
        if n == 0: return [[]]
        if n < 0: return []
        return [t + ['V'] for t in tilings(n - 1)] + [t + ['H'] for t in tilings(n - 2)]
    u = 0.36; y = 0
    for n in range(1, 5):
        T = tilings(n)
        ax.text(-0.35, y - u, f'n = {n}', ha='right', va='center', fontsize=10.5, color=NAVY, fontweight='bold')
        x = 0
        for t in T:
            c = 0
            for p in t:
                if p == 'V':
                    ax.add_patch(Rectangle((x + c * u, y - 2 * u), u, 2 * u, fc=BLU, ec=BLC, lw=1.4)); c += 1
                else:
                    ax.add_patch(Rectangle((x + c * u, y - u), 2 * u, u, fc=ORG, ec=ORC, lw=1.4))
                    ax.add_patch(Rectangle((x + c * u, y - 2 * u), 2 * u, u, fc=ORG, ec=ORC, lw=1.4)); c += 2
            x += n * u + 0.35
        ax.text(x + 0.15, y - u, f'{len(T)} cách', va='center', fontsize=10.5, color=RED, fontweight='bold')
        y -= 2 * u + 0.38
    ax.text(9.2, -0.3, 'Nhìn cột bên phải:', fontsize=11.5, color=TXT, va='center')
    ax.text(9.2, -0.75, '• một viên dọc → còn 2 × (n − 1)', fontsize=11, color=BLC, va='center')
    ax.text(9.2, -1.15, '• hai viên ngang → còn 2 × (n − 2)', fontsize=11, color=AMBER, va='center')
    ax.text(9.2, -1.75, 'T(n) = T(n − 1) + T(n − 2)', fontsize=11.5, color=RED, fontweight='bold', va='center')
    ax.text(9.2, -2.2, 'T(n) = F(n + 1)', fontsize=11.5, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-1.3, 13.6); ax.set_ylim(y + 0.2, 0.2); save(f, 'latgach')

def tribo():
    f, ax = fig(8.6, 3.6)
    n = 6; bad = {2, 4}
    F = [1]
    for x in range(1, n + 1): F.append(0 if x in bad else sum(F[x - d] for d in (1, 2, 3) if x - d >= 0))
    w, h = 0.95, 0.42
    for x in range(n + 1):
        st = 'gray' if x in bad else ('cur' if x == n else ('src' if x == 0 else 'done'))
        fc, ec = STY[st]
        ax.add_patch(Rectangle((x * w, 0), w, (x + 1) * h, fc=fc, ec=ec, lw=1.6, zorder=2))
        ax.text(x * w + w / 2, (x + 1) * h / 2, str(x), ha='center', va='center', fontsize=10, color='#555555', zorder=3)
        lab = 'hỏng' if x in bad else f'f = {F[x]}'
        ax.text(x * w + w / 2, (x + 1) * h + 0.2, lab, ha='center', va='bottom', fontsize=10,
                color=RED if x == n else ('#8A8A8A' if x in bad else NAVY), fontweight='bold')
    # một cách đi: 0 → 1 → 3 → 6
    pts = [0, 1, 3, 6]
    for a, b in zip(pts, pts[1:]):
        ax.annotate('', xy=(b * w + w / 2, (b + 1) * h + 0.75), xytext=(a * w + w / 2, (a + 1) * h + 0.75),
                    arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.7, connectionstyle='arc3,rad=-0.3', mutation_scale=12))
    tx = (n + 1) * w + 0.5
    ax.text(tx, 2.7, 'f[x] = f[x−1] + f[x−2] + f[x−3]', fontsize=10.5, color=TXT, va='center')
    ax.text(tx, 2.2, 'f[x] = 0 nếu bậc x hỏng', fontsize=10.5, color='#707070', va='center')
    ax.text(tx, 1.5, 'Bốn cách lên bậc 6:', fontsize=10.5, color=NAVY, fontweight='bold', va='center')
    for i, t in enumerate(['0 → 1 → 3 → 6', '0 → 3 → 6', '0 → 1 → 3 → 5 → 6', '0 → 3 → 5 → 6']):
        ax.text(tx + 0.2, 1.05 - i * 0.4, t, fontsize=10, color=GREEN if i == 0 else TXT, va='center')
    ax.set_xlim(-0.2, tx + 4.0); ax.set_ylim(-0.2, 3.95); save(f, 'tribo')

def duongk():
    f, ax = fig(9.2, 3.4)
    P = {1: (0, 1.0), 2: (1.6, 2.0), 3: (1.6, 0.0), 4: (3.1, 0.0)}
    for u, v in [(1, 2), (1, 3), (2, 3), (3, 4)]: edge(ax, P[u], P[v], color=GRAY, lw=2.2, r=0.32)
    for v, p in P.items(): node(ax, p, v, 'src' if v == 1 else ('cur' if v == 3 else 'done'), r=0.32, fs=13)
    ax.text(1.55, -0.85, 'mỗi cạnh = hai tuyến ngược chiều', ha='center', fontsize=10.5, color='#606060')
    tx = 4.3
    ax.text(tx, 2.2, 'Đường đi độ dài 3 từ 1 tới 3:', fontsize=10.5, color=NAVY, fontweight='bold', va='center')
    for i, t in enumerate(['1 → 2 → 1 → 3', '1 → 3 → 1 → 3', '1 → 3 → 2 → 3', '1 → 3 → 4 → 3']):
        ax.text(tx + 0.25, 1.7 - i * 0.42, t, fontsize=10.5, color=TXT, va='center')
    ax.text(tx, -0.2, 'A³[1][3] = 4', fontsize=12, color=RED, fontweight='bold', va='center')
    bx = 9.3
    ax.text(bx, 2.2, 'Truy vấn với K = 13 = 1101₂:', fontsize=10.5, color=NAVY, fontweight='bold', va='center')
    labs = ['eₛ', 'A¹', 'A⁴', 'A⁸']
    for i, t in enumerate(labs):
        x = bx + 0.35 + i * 1.05
        tag(ax, (x, 1.45), t, color=PURPLE if i == 0 else NAVY, fs=11, bg=STY['src'][0] if i == 0 else BLU)
        if i: ax.text(x - 0.53, 1.45, '·', ha='center', va='center', fontsize=14, color=TXT)
    ax.text(bx, 0.75, 'vectơ × ma trận: n² phép nhân', fontsize=10.5, color=TXT, va='center')
    ax.text(bx, 0.33, 'A, A², A⁴, ..., A²⁵⁹ tính sẵn', fontsize=10.5, color=TXT, va='center')
    ax.text(bx, -0.2, 'mỗi truy vấn O(n² log K)', fontsize=11, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-0.5, bx + 4.4); ax.set_ylim(-1.1, 2.55); save(f, 'duongk')

PAL = ['#BDD7EE', '#FFE7B3', '#CDEBC5', '#F4C7D9', '#B2E5E0', '#DCCCEC', '#F8CBAD', '#FFD966']
ECS = [NAVY, AMBER, GREEN, PINK, TEAL, PURPLE, RED, RED]

def blocks(n, lim=None):
    lim = lim or n; out = []; i = 1
    while i <= lim:
        q = n // i; j = min(n // q, lim); out.append((i, j, q)); i = j + 1
    return out

def tongsigma():
    f, ax = fig(7.0, 2.6)
    n = 20; w = 0.3; h = 0.075
    B = blocks(n)
    for b, (i, j, q) in enumerate(B):
        for x in range(i, j + 1):
            ax.add_patch(Rectangle(((x - 1) * w, 0), w, q * h, fc=PAL[b % 8], ec=ECS[b % 8], lw=1.2))
            ax.text((x - 0.5) * w, -0.08, str(x), ha='center', va='top', fontsize=9, color='#505050')
        ax.text(((i + j) / 2 - 0.5) * w, q * h + 0.05, str(q), ha='center', va='bottom', fontsize=10, color=ECS[b % 8], fontweight='bold')
    ax.text(n * w + 0.12, -0.16, 'i', ha='left', va='center', fontsize=10.5, color=TXT, style='italic')
    tx = 2.0
    ax.text(tx, 1.5, 'Khối [i, j] cùng thương q góp q · (i + ... + j):', fontsize=10.5, color=NAVY, fontweight='bold', va='center')
    ax.text(tx, 1.17, '20 · 1 + 10 · 2 + 6 · 3 + 5 · 4 + 4 · 5 + 3 · 6', fontsize=10.5, color=TXT, va='center')
    ax.text(tx, 0.87, '+ 2 · (7 + ... + 10) + 1 · (11 + ... + 20)', fontsize=10.5, color=TXT, va='center')
    ax.text(tx, 0.52, '= 339   (8 khối thay cho 20 số hạng)', fontsize=11, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-0.1, n * w + 0.35); ax.set_ylim(-0.4, 1.7); save(f, 'tongsigma')

def tongdu():
    f, ax = fig(9.4, 3.6)
    n, k = 20, 24; w = 0.36; h = 0.115
    B = blocks(n)
    col = {}
    for b, (i, j, q) in enumerate(B):
        for x in range(i, j + 1): col[x] = b
    for x in range(1, k + 1):
        v = n % x
        if x <= n: fc, ec = PAL[col[x] % 8], ECS[col[x] % 8]
        else: fc, ec = GRY, GRC
        if v: ax.add_patch(Rectangle(((x - 1) * w, 0), w, v * h, fc=fc, ec=ec, lw=1.2))
        else: ax.plot([(x - 1) * w + 0.04, x * w - 0.04], [0, 0], color=ec, lw=3)
        ax.text((x - 0.5) * w, v * h + 0.05, str(v), ha='center', va='bottom', fontsize=9.5, color=TXT)
        ax.text((x - 0.5) * w, -0.1, str(x), ha='center', va='top', fontsize=9, color='#505050')
    for (i, j, q), b in zip(B, range(len(B))):
        if j > i:
            ax.plot([(i - 0.5) * w, (j - 0.5) * w], [(n % i) * h + 0.42, (n % j) * h + 0.42], color=RED, lw=1.4, ls=(0, (4, 2)))
    ax.text(((11 + 20) / 2 - 0.5) * w + 0.2, 1.7, 'q = 1: giảm 1', fontsize=10.5, color=RED, ha='center')
    ax.text(((7 + 10) / 2 - 0.5) * w, 1.35, 'q = 2: giảm 2', fontsize=10.5, color=RED, ha='center')
    ax.text(((21 + 24) / 2 - 0.5) * w, 2.85, 'i > n: dư n', fontsize=10.5, color='#707070', ha='center')
    tx = k * w + 0.6
    ax.text(tx, 2.4, 'n = 20, k = 24', fontsize=11, color=NAVY, fontweight='bold', va='center')
    ax.text(tx, 1.9, 'n mod i = n − i · ⌊n / i⌋', fontsize=10.5, color=TXT, va='center')
    ax.text(tx, 1.45, 'Trong một khối, dãy số dư là', fontsize=10, color=TXT, va='center')
    ax.text(tx, 1.1, 'cấp số cộng công sai −q.', fontsize=10, color=TXT, va='center')
    ax.text(tx, 0.5, 'Tổng: 61 + 4 · 20 = 141', fontsize=11, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-0.2, tx + 3.6); ax.set_ylim(-0.45, 3.15); save(f, 'tongdu')

def haithuong():
    f, ax = fig(9.4, 3.3)
    n, m = 10, 7; L = min(n, m); s = 0.72
    Bn = blocks(n, L); Bm = blocks(m, L)
    cut = sorted({j for _, j, _ in Bn} | {j for _, j, _ in Bm})
    def bid(Bs, x): return next(b for b, (i, j, q) in enumerate(Bs) if i <= x <= j)
    rows = [('i', lambda x: x, None), ('⌊10 / i⌋', lambda x: n // x, Bn), ('⌊7 / i⌋', lambda x: m // x, Bm),
            ('10 mod i', lambda x: n % x, 'g'), ('7 mod i', lambda x: m % x, 'g'), ('tích', lambda x: (n % x) * (m % x), 'p')]
    for r_, (lab, fn, B) in enumerate(rows):
        y = -r_ * 0.5
        ax.text(-0.2, y, lab, ha='right', va='center', fontsize=10, color=TXT, fontweight='bold')
        for x in range(1, L + 1):
            if B is None: fc, ec = '#E8EEF7', NAVY
            elif B == 'g': fc, ec = '#FFFFFF', '#B4C6E7'
            elif B == 'p': fc, ec = (YEL, YEC) if fn(x) else ('#FFFFFF', '#B4C6E7')
            else: b = bid(B, x); fc, ec = PAL[b % 8], ECS[b % 8]
            cellbox(ax, (x - 0.5) * s, y, fn(x), fc=fc, ec=ec, w=s - 0.06, h=0.42, fs=10.5, bold=B != 'g')
    # các khối chung
    yb = -len(rows) * 0.5 + 0.05
    st = 1
    for k, j in enumerate(cut):
        ax.plot([(st - 1) * s + 0.06, j * s - 0.06], [yb, yb], color=RED, lw=2.4, solid_capstyle='butt')
        ax.text((st - 1 + j) * s / 2, yb - 0.12, f'[{st}, {j}]', ha='center', va='top', fontsize=10, color=RED)
        st = j + 1
    tx = L * s + 0.5
    ax.text(tx, 0.0, 'Khối chung: cả hai thương không đổi', fontsize=10.5, color=NAVY, fontweight='bold', va='center')
    ax.text(tx, -0.45, 'j = min(⌊n / ⌊n / i⌋⌋, ⌊m / ⌊m / i⌋⌋)', fontsize=10.5, color=TXT, va='center')
    ax.text(tx, -1.05, 'Trên khối [6, 7]: a = 1, b = 1', fontsize=10.5, color=TXT, va='center')
    ax.text(tx, -1.45, '(10 − i)(7 − i) = 70 − 17i + i²', fontsize=10.5, color=TXT, va='center')
    ax.text(tx, -1.85, 'cần Σ i và Σ i² trên khối', fontsize=10.5, color=TXT, va='center')
    ax.text(tx, -2.5, 'Tổng: 1 + 6 + 4 = 11', fontsize=11.5, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-1.6, tx + 4.3); ax.set_ylim(yb - 0.5, 0.35); save(f, 'haithuong')

chiakeo(); duongluoi(); tohoplon(); boiso(); ntcn(); tangqua(); latgach(); tribo(); duongk(); tongsigma(); tongdu(); haithuong()
