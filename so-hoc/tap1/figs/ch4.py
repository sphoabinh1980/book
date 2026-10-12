# Hình Chương 4. TỔ HỢP VÀ ĐẾM
from shlib import *
from math import comb, gcd, isqrt

YEL, BLU, AMB, GRY, GRN, TEA, PNK = '#FFD966', '#BDD7EE', '#FFE7B3', '#EDEDED', '#CDEBC5', '#B2E5E0', '#F4C7D9'

def rbox(ax, x, y, w, h, text, fc=BLU, ec=NAVY, fs=11, lw=1.6, bold=True, color=TXT, z=3):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0,rounding_size=0.12', fc=fc, ec=ec, lw=lw, zorder=z))
    ax.text(x, y, text, ha='center', va='center', fontsize=fs, fontweight='bold' if bold else 'normal', color=color, zorder=z + 1)

def arr(ax, p, q, color=NAVY, lw=1.6, rad=0.0, ms=12, z=2, style='-|>'):
    ax.annotate('', xy=q, xytext=p, arrowprops=dict(arrowstyle=style, color=color, lw=lw, mutation_scale=ms,
                connectionstyle=f'arc3,rad={rad}', shrinkA=0, shrinkB=0), zorder=z)

def matrix(ax, x, y, M, cw=0.62, ch=0.45, fs=11, color=TXT, bc=NAVY, fc=None, ec=None, bold=True):
    """vẽ ma trận M (danh sách hàng) có tâm (x, y), hai ngoặc vuông"""
    R, C = len(M), len(M[0]); W, H = C * cw, R * ch
    if fc: ax.add_patch(Rectangle((x - W / 2 - 0.08, y - H / 2 - 0.06), W + 0.16, H + 0.12, fc=fc, ec=ec or fc, lw=1.6, zorder=1))
    for i in range(R):
        for j in range(C):
            ax.text(x - W / 2 + (j + 0.5) * cw, y + H / 2 - (i + 0.5) * ch, str(M[i][j]), ha='center', va='center',
                    fontsize=fs, color=color, fontweight='bold' if bold else 'normal', zorder=3)
    t = 0.1
    for s in (-1, 1):
        xe = x + s * W / 2
        ax.plot([xe - s * t, xe, xe, xe - s * t], [y + H / 2, y + H / 2, y - H / 2, y - H / 2], color=bc, lw=1.6, zorder=3)
    return W, H

# ======================= Bài 13
def f13_chon():
    f, ax = fig(8.2, 4.6)
    def row(x0, y, S, hl):
        for v in range(1, 6):
            x = x0 + (v - 1) * 0.62
            st = ('cur' if v == 5 else 'done') if v in S else 'gray'
            if v not in S: node(ax, (x, y), v, 'w', r=0.22, fs=10, lw=1.3)
            else: node(ax, (x, y), v, st, r=0.22, fs=10, lw=1.8)
        ax.text(x0 + 4 * 0.62 + 0.5, y, '{' + ', '.join(map(str, sorted(S))) + '}', va='center', fontsize=10, color=RED if hl else NAVY, fontweight='bold')
    A = [s for s in [(1, 5), (2, 5), (3, 5), (4, 5)]]
    B = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    xa, xb = 0.0, 5.4
    ax.text(xa + 1.6, 0.85, 'Có bạn 5:  4 cách', ha='center', fontsize=11.5, color=RED, fontweight='bold')
    ax.text(xa + 1.6, 0.45, '(chọn thêm 1 trong 4 bạn còn lại)', ha='center', fontsize=9.5, color='#404040')
    ax.text(xb + 1.6, 0.85, 'Không có bạn 5:  6 cách', ha='center', fontsize=11.5, color=NAVY, fontweight='bold')
    ax.text(xb + 1.6, 0.45, '(chọn đủ 2 trong 4 bạn còn lại)', ha='center', fontsize=9.5, color='#404040')
    for t, S in enumerate(A): row(xa, -0.2 - 0.62 * t, S, True)
    for t, S in enumerate(B): row(xb, -0.2 - 0.62 * t, S, False)
    ax.plot([4.75, 4.75], [1.0, -3.6], color=LGRAY, lw=1.4, ls=(0, (4, 3)))
    ax.text(4.75, -4.15, 'C(5, 2)  =  C(4, 1)  +  C(4, 2)  =  4 + 6  =  10', ha='center', fontsize=12.5, color=NAVY, fontweight='bold')
    ax.set_xlim(-0.4, 9.9); ax.set_ylim(-4.45, 1.15)
    save(f, 'f13_chon')

def f13_pascal():
    f, ax = fig(8.6, 5.4)
    R = 9; dy = 0.6; cw = 0.92
    pos = lambda n, k: ((k - n / 2) * cw, -n * dy)
    sty = {}
    sty[(5, 2)] = (YEL, RED); sty[(4, 1)] = sty[(4, 2)] = (AMB, AMBER)
    sty[(8, 3)] = (TEA, TEAL); sty[(7, 2)] = sty[(7, 3)] = (GRN, GREEN)
    for n in range(R):
        for k in range(n + 1):
            x, y = pos(n, k)
            fc, ec = sty.get((n, k), ('#FFFFFF', NAVY if k in (0, n) else '#8EA9DB'))
            cellbox(ax, x, y, comb(n, k), fc=fc, ec=ec, w=0.84, h=0.5, fs=10.5, lw=1.8 if (n, k) in sty else 1.2)
        ax.text(-4.75 * cw, -n * dy, f'n = {n}', ha='right', va='center', fontsize=10, color=NAVY, fontweight='bold')
        ax.text(4.75 * cw, -n * dy, f'{2 ** n}', ha='left', va='center', fontsize=10, color=PURPLE)
    ax.text(4.75 * cw, 0.62, 'tổng hàng', ha='left', va='center', fontsize=9.5, color=PURPLE, fontweight='bold')
    for (a, b, c) in [((4, 1), (4, 2), (5, 2)), ((7, 2), (7, 3), (8, 3))]:
        col = RED if c == (5, 2) else TEAL
        for p in (a, b):
            x0, y0 = pos(*p); x1, y1 = pos(*c)
            arr(ax, (x0 + (x1 - x0) * 0.25, y0 - 0.22), (x1 - (x1 - x0) * 0.3, y1 + 0.24), color=col, lw=1.8, ms=11, z=6)
    ax.text(0, -8 * dy - 0.65, 'C(4, 1) + C(4, 2) = C(5, 2):  4 + 6 = 10', ha='center', va='center', fontsize=10.5, color=RED, fontweight='bold')
    ax.text(0, -8 * dy - 1.15, 'C(7, 2) + C(7, 3) = C(8, 3):  21 + 35 = 56', ha='center', va='center', fontsize=10.5, color=TEAL, fontweight='bold')
    ax.text(0, 0.62, 'k = 0, 1, 2, ... từ trái sang phải', ha='center', fontsize=9.5, color='#404040')
    ax.set_xlim(-5.9, 5.9); ax.set_ylim(-8 * dy - 1.4, 0.9)
    save(f, 'f13_pascal')

def f13_xich():
    f, ax = fig(8.6, 2.9)
    N = 6; dx = 1.6
    fv = [1, 1, 2, 6, 24, 120, 720]
    ax.text(-0.75, 1.0, 'i!', ha='right', va='center', fontsize=12, color=NAVY, fontweight='bold')
    ax.text(-0.75, -0.9, '1 / i!', ha='right', va='center', fontsize=12, color=RED, fontweight='bold')
    for i in range(N + 1):
        x = i * dx
        cellbox(ax, x, 1.0, fv[i], fc=BLU, ec=NAVY, w=0.95, h=0.55, fs=11)
        cellbox(ax, x, -0.9, f'1/{i}!', fc=YEL if i == N else AMB, ec=RED if i == N else AMBER, w=0.95, h=0.55, fs=10.5)
        ax.text(x, 1.58, f'i = {i}', ha='center', fontsize=10.5, color='#404040')
        if i:
            arr(ax, ((i - 1) * dx + 0.5, 1.0), (x - 0.5, 1.0), color=NAVY)
            ax.text(x - dx / 2, 1.13, f'· {i}', ha='center', va='bottom', fontsize=11, color=NAVY, fontweight='bold')
            arr(ax, (x - 0.5, -0.9), ((i - 1) * dx + 0.5, -0.9), color=RED)
            ax.text(x - dx / 2, -1.03, f'· {i}', ha='center', va='top', fontsize=11, color=RED, fontweight='bold')
    x = N * dx
    arr(ax, (x, 0.7), (x, -0.6), color=PURPLE, lw=1.8)
    ax.text(x + 0.15, 0.05, 'lũy thừa p − 2\n(chỉ MỘT lần)', ha='left', va='center', fontsize=10.5, color=PURPLE, fontweight='bold')
    ax.text(3 * dx, -1.75, 'đi ngược: 1/(i − 1)!  =  (1/i!) · i', ha='center', fontsize=11.5, color=RED, fontweight='bold')
    ax.set_xlim(-1.9, N * dx + 2.1); ax.set_ylim(-2.0, 1.85)
    save(f, 'f13_xich')

def f13_keo():
    f, ax = fig(8.2, 2.9)
    def strip(y, seq, groups, label):
        x = 0
        for c in seq:
            if c == '*': ax.add_patch(Circle((x, y), 0.24, fc=AMB, ec=AMBER, lw=1.8, zorder=3))
            else: ax.add_patch(Rectangle((x - 0.07, y - 0.36), 0.14, 0.72, fc=RED, ec=RED, zorder=3))
            x += 0.62
        ax.text(-0.55, y, label, ha='right', va='center', fontsize=10.5, color=NAVY, fontweight='bold')
        # ngoặc dưới các nhóm
        pos = 0
        for name, cnt in groups:
            if cnt:
                x0, x1 = pos * 0.62 - 0.22, (pos + cnt - 1) * 0.62 + 0.22
                ax.plot([x0, x0, x1, x1], [y - 0.38, y - 0.46, y - 0.46, y - 0.38], color=GRAY, lw=1.2)
                ax.text((x0 + x1) / 2, y - 0.52, f'{name}: {cnt}', ha='center', va='top', fontsize=9.5, color=TXT)
            else:
                ax.text(pos * 0.62 - 0.31, y - 0.52, f'{name}: 0', ha='center', va='top', fontsize=9.5, color=TXT)
            pos += cnt + 1
    strip(0.9, '***|*****|**', [('An', 3), ('Bình', 5), ('Chi', 2)], '(3, 5, 2)')
    strip(-0.9, '|******|****', [('An', 0), ('Bình', 6), ('Chi', 4)], '(0, 6, 4)')
    ax.text(7.75, 0.0, '10 kẹo + 2 vạch\n= 12 vị trí\n\nchọn 2 vị trí\nđặt vạch:\nC(12, 2) = 66', ha='left', va='center', fontsize=10.5, color=NAVY, fontweight='bold')
    ax.set_xlim(-2.0, 10.9); ax.set_ylim(-1.75, 1.45)
    save(f, 'f13_keo')

# ======================= Bài 14
def f14_venn():
    f, ax = fig(7.4, 5.4)
    R = 2.05
    C = {2: (-1.2, 0.75), 3: (1.2, 0.75), 5: (0, -1.25)}
    col = {2: NAVY, 3: GREEN, 5: RED}; fill = {2: '#BDD7EE', 3: '#CDEBC5', 5: '#F8CBAD'}
    for a, c in C.items():
        ax.add_patch(Circle(c, R, fc=fill[a], ec='none', alpha=0.38, zorder=1))
        ax.add_patch(Circle(c, R, fc='none', ec=col[a], lw=2.2, zorder=2))
    ax.text(-3.3, 2.75, 'Bội của 2: 15 số', fontsize=11, color=NAVY, fontweight='bold', ha='center')
    ax.text(3.3, 2.75, 'Bội của 3: 10 số', fontsize=11, color=GREEN, fontweight='bold', ha='center')
    ax.text(0, -3.7, 'Bội của 5: 6 số', fontsize=11, color=RED, fontweight='bold', ha='center')
    reg = {(2,): ((-2.2, 1.2), '2  4  8  14\n16  22  26  28'), (3,): ((2.2, 1.2), '3   9\n21  27'),
           (5,): ((0, -2.35), '5   25'), (2, 3): ((0, 1.65), '6  12\n18  24'), (2, 5): ((-1.4, -0.75), '10\n20'),
           (3, 5): ((1.4, -0.75), '15'), (2, 3, 5): ((0, 0.12), '30')}
    for k, (p, t) in reg.items():
        ax.text(p[0], p[1], t, ha='center', va='center', fontsize=10.5, color=TXT, fontweight='bold' if len(k) > 1 else 'normal', zorder=4, linespacing=1.3)
    ax.add_patch(Circle((0, 0.12), 0.34, fc=YEL, ec=RED, lw=1.8, zorder=3))
    ax.add_patch(FancyBboxPatch((3.0, -3.3), 2.9, 1.65, boxstyle='round,pad=0.05,rounding_size=0.15', fc=GRY, ec='#9A9A9A', lw=1.4))
    ax.text(4.45, -2.18, 'Không là bội\ncủa số nào (8 số):', ha='center', va='center', fontsize=9.5, color='#404040')
    ax.text(4.45, -2.95, '1  7  11  13\n17  19  23  29', ha='center', va='center', fontsize=9.5, color='#404040')
    ax.set_xlim(-4.7, 6.05); ax.set_ylim(-4.0, 3.15)
    save(f, 'f14_venn')

def f14_tapcon():
    f, ax = fig(8.6, 4.8)
    A = [2, 3, 5]; n = 30; DX = 3.25; DY = 1.45
    lv = {0: [()], 1: [(2,), (3,), (5,)], 2: [(2, 3), (2, 5), (3, 5)], 3: [(2, 3, 5)]}
    P = {}
    for s_, row in lv.items():
        for j, S in enumerate(row):
            P[S] = ((j - (len(row) - 1) / 2) * DX, -s_ * DY)
    def L(S):
        l = 1
        for a in S: l = l * a // gcd(l, a)
        return l
    # cạnh bao hàm (xám) và cạnh tính lcm (bỏ phần tử nhỏ nhất)
    for S in P:
        for T in P:
            if len(T) == len(S) + 1 and set(S) <= set(T):
                dp = tuple(T[1:]) == S
                (x0, y0), (x1, y1) = P[S], P[T]
                arr(ax, (x0 + (x1 - x0) * 0.18, y0 - 0.36), (x1 - (x1 - x0) * 0.18, y1 + 0.36), color=RED if dp else LGRAY,
                    lw=2.0 if dp else 1.2, ms=12 if dp else 8, z=1 if not dp else 2, style='-|>' if dp else '-')
    for S, (x, y) in P.items():
        name = '{' + ', '.join(map(str, S)) + '}' if S else '∅'
        if not S:
            rbox(ax, x, y, 1.9, 0.62, '∅:  lcm = 1', fc=GRY, ec='#9A9A9A', fs=10.5)
            continue
        l = L(S); sg = '+' if len(S) % 2 else '−'
        fc, ec = (BLU, NAVY) if len(S) % 2 else (PNK, PINK)
        rbox(ax, x, y, 2.75, 0.72, f'{name}:  lcm = {l}\n{sg} ⌊30 / {l}⌋ = {sg}{n // l}', fc=fc, ec=ec, fs=10)
    ax.text(1.4, 0.0, 'mũi tên đỏ: L[S] tính từ\nL[S bỏ phần tử nhỏ nhất]', ha='left', va='center', fontsize=9.5, color=RED, fontweight='bold')
    ax.text(-4.75, -4.35, 'xanh: |S| lẻ, cộng\nhồng: |S| chẵn, trừ', ha='left', va='center', fontsize=9.5, color='#404040')
    ax.text(1.65, -4.35, '15 + 10 + 6 − 5\n− 3 − 2 + 1 = 22', ha='left', va='center', fontsize=11, color=NAVY, fontweight='bold')
    ax.set_xlim(-4.85, 4.85); ax.set_ylim(-4.85, 0.45)
    save(f, 'f14_tapcon')

def f14_tran():
    """lcm của ba số nguyên tố lớn: chặn ngay khi vượt N"""
    f, ax = fig(9.2, 2.6)
    xs = [0, 3.7, 7.55]; ws = [1.9, 2.8, 2.2]
    rbox(ax, xs[0], 0, ws[0], 0.95, 'L = 10⁹ + 7', fc=BLU, ec=NAVY, fs=11)
    rbox(ax, xs[1], 0, ws[1], 0.95, 'L ≈ 1,000000016 · 10¹⁸\nđã > N = 10¹⁸', fc=YEL, ec=RED, fs=10, bold=False)
    rbox(ax, xs[2], 0, ws[2], 0.95, 'L ≈ 9,98 · 10²⁶\ntràn 2⁶³ !', fc=GRY, ec='#9A9A9A', fs=10.5, color='#7F7F7F', bold=False)
    for t, (lab, c) in enumerate([('lcm với\n10⁹ + 9', NAVY), ('lcm với\n998 244 353', GRAY)]):
        x0, x1 = xs[t] + ws[t] / 2 + 0.04, xs[t + 1] - ws[t + 1] / 2 - 0.04
        arr(ax, (x0, 0), (x1, 0), color=c)
        ax.text((x0 + x1) / 2, 0.1, lab, ha='center', va='bottom', fontsize=9.5, color=c, fontweight='bold')
    xm = (xs[1] + ws[1] / 2 + xs[2] - ws[2] / 2) / 2
    ax.plot([xm - 0.15, xm + 0.15], [-0.35, -0.05], color=RED, lw=3); ax.plot([xm - 0.15, xm + 0.15], [-0.05, -0.35], color=RED, lw=3)
    ax.text(xs[1], -0.7, 'vượt N: gán L = N + 1, không nhân tiếp; mọi tập chứa nó cho ⌊N / L⌋ = 0', ha='center', va='top', fontsize=10.5, color=RED)
    ax.set_xlim(-1.05, 8.75); ax.set_ylim(-1.15, 1.05)
    save(f, 'f14_tran')

# ======================= Bài 15
def f15_lat():
    f, ax = fig(8.6, 4.6)
    s = 0.36; hgt = 0.3
    def tilings(n):
        if n == 0: return [[]]
        if n < 0: return []
        return [t + [1] for t in tilings(n - 1)] + [t + [2] for t in tilings(n - 2)]
    x0 = 0
    for n in range(1, 6):
        T = tilings(n)
        ax.text(x0 + n * s / 2, 0.75, f'n = {n}', ha='center', fontsize=10.5, color=NAVY, fontweight='bold')
        ax.text(x0 + n * s / 2, 0.42, f'{len(T)} cách', ha='center', fontsize=10, color=RED, fontweight='bold')
        for r, t in enumerate(T):
            y = -r * 0.5; x = x0
            for p in t:
                fc, ec = (AMB, AMBER) if p == 1 else (TEA, TEAL)
                ax.add_patch(Rectangle((x + 0.02, y - hgt / 2), p * s - 0.04, hgt, fc=fc, ec=ec, lw=1.5, zorder=3))
                x += p * s
        if n == 5:
            xb = x0 + n * s + 0.15
            for (a, b, txt, c) in [(0, 4, 'cuối là ô vuông:\n5 cách (= n = 4)', AMBER), (5, 7, 'cuối là thanh dài:\n3 cách (= n = 3)', TEAL)]:
                ya, yb = -a * 0.5 + 0.17, -b * 0.5 - 0.17
                ax.plot([xb, xb + 0.12, xb + 0.12, xb], [ya, ya, yb, yb], color=c, lw=1.6)
                ax.text(xb + 0.25, (ya + yb) / 2, txt, va='center', fontsize=9.5, color=c, fontweight='bold')
        x0 += n * s + 0.75
    ax.add_patch(Rectangle((0.0, -4.35), s - 0.04, hgt, fc=AMB, ec=AMBER, lw=1.5))
    ax.text(0.5, -4.2, 'ô vuông 1 × 1', va='center', fontsize=9.5)
    ax.add_patch(Rectangle((2.3, -4.35), 2 * s - 0.04, hgt, fc=TEA, ec=TEAL, lw=1.5))
    ax.text(3.15, -4.2, 'thanh dài 1 × 2', va='center', fontsize=9.5)
    ax.set_xlim(-0.2, x0 + 2.3); ax.set_ylim(-4.6, 1.0)
    save(f, 'f15_lat')

def f15_truot():
    f, ax = fig(8.6, 3.2)
    Fv = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    sub = '₀₁₂₃₄₅₆₇₈₉'
    for i, v in enumerate(Fv):
        x = i * 0.8
        st = (YEL, RED) if i in (4, 5) else ((BLU, NAVY) if i == 3 else ('#FFFFFF', NAVY))
        cellbox(ax, x, 1.3, v, fc=st[0], ec=st[1], w=0.7, h=0.5, fs=11)
        ax.text(x, 1.7, f'F{sub[i]}', ha='center', fontsize=10, color='#404040')
    def brk(x0, x1, y, c, lab):
        ax.plot([x0, x0, x1, x1], [y + 0.1, y, y, y + 0.1], color=c, lw=2.0)
        ax.text((x0 + x1) / 2, y - 0.06, lab, ha='center', va='top', fontsize=9.5, color=c, fontweight='bold')
    brk(3 * 0.8 - 0.33, 4 * 0.8 + 0.33, 0.8, NAVY, 'trước: (F₄, F₃)')
    ax.add_patch(Rectangle((4 * 0.8 - 0.42, 0.98), 1.64, 0.64, fc='none', ec=RED, lw=2.4, zorder=5))
    ax.text(5 * 0.8 + 0.55, 1.0, 'sau: (F₅, F₄)', ha='left', va='top', fontsize=9.5, color=RED, fontweight='bold')
    ax.text(10 * 0.8 - 0.1, 1.3, '...', fontsize=12, va='center')
    y = -0.55
    matrix(ax, 0.9, y, [['F(i+2)'], ['F(i+1)']], cw=1.3, ch=0.45, fs=10.5, color=RED)
    ax.text(1.85, y, '=', fontsize=14, ha='center', va='center')
    matrix(ax, 2.95, y, [[1, 1], [1, 0]], cw=0.5, ch=0.45, fs=12, color=PURPLE)
    ax.text(4.0, y, '·', fontsize=16, ha='center', va='center')
    matrix(ax, 5.0, y, [['F(i+1)'], ['F(i)']], cw=1.3, ch=0.45, fs=10.5, color=NAVY)
    ax.text(6.0, y + 0.25, 'hàng 1: F(i+1) + F(i)', fontsize=9.5, color=TXT, va='center')
    ax.text(6.0, y - 0.25, 'hàng 2: F(i+1) (chép lại)', fontsize=9.5, color=TXT, va='center')
    ax.text(2.95, y - 0.7, 'Q', ha='center', va='center', fontsize=11, color=PURPLE, fontweight='bold')
    ax.set_xlim(-0.6, 8.6); ax.set_ylim(-1.4, 1.95)
    save(f, 'f15_truot')

def f15_luythua():
    f, ax = fig(8.6, 3.0)
    Ms = [[[1, 1], [1, 0]], [[2, 1], [1, 1]], [[5, 3], [3, 2]], [[34, 21], [21, 13]]]
    bits = [0, 1, 0, 1]; DX = 2.7
    for t in range(4):
        x = t * DX
        on = bits[t] == 1
        matrix(ax, x, 0.6, Ms[t], cw=0.64, ch=0.42, fs=11, fc=YEL if on else '#F2F2F2', ec=RED if on else '#BFBFBF')
        ax.text(x, 1.3, f'Q{"¹²⁴⁸"[t]}', ha='center', va='center', fontsize=11.5, color=NAVY, fontweight='bold')
        cellbox(ax, x, -0.35, bits[t], fc=YEL if on else GRY, ec=RED if on else '#9A9A9A', w=0.5, h=0.42, fs=11)
        ax.text(x, -0.75, f'bit {t}', ha='center', va='center', fontsize=9, color='#404040')
        if t:
            arr(ax, (x - DX + 0.82, 0.6), (x - 0.82, 0.6), color=NAVY)
            ax.text(x - DX / 2, 0.5, 'bình\nphương', ha='center', va='top', fontsize=9, color=NAVY)
    ax.text(-0.9, -0.35, '10 =', ha='right', va='center', fontsize=11, color=TXT, fontweight='bold')
    ax.text(-0.9, -0.75, '(đọc từ phải)', ha='right', va='center', fontsize=8.8, color='#404040')
    xr = 3 * DX + 1.0
    ax.text(xr, 1.3, 'Q¹⁰ = Q² · Q⁸', ha='left', va='center', fontsize=11.5, color=RED, fontweight='bold')
    matrix(ax, xr + 0.75, 0.6, [[89, 55], [55, 34]], cw=0.6, ch=0.42, fs=11, color=RED)
    ax.text(xr + 0.75, -0.35, 'F₁₀ = 55', ha='center', va='center', fontsize=11.5, color=RED, fontweight='bold')
    ax.set_xlim(-2.4, xr + 2.1); ax.set_ylim(-1.0, 1.55)
    save(f, 'f15_luythua')

def f15_dothi():
    f, ax = fig(7.2, 2.6)
    P = {1: (0, 0.9), 2: (0, -0.9), 3: (1.6, 0), 4: (3.0, 0)}
    for u, v in [(1, 2), (1, 3), (2, 3), (3, 4)]: edge(ax, P[u], P[v], color=NAVY, lw=2.2, r=0.3)
    for u, p in P.items(): node(ax, p, u, 'cur' if u in (1, 3) else 'done', r=0.3, fs=13)
    ax.text(3.75, 0.0, 'A =', fontsize=12, va='center', fontweight='bold', color=NAVY)
    matrix(ax, 5.55, 0, [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]], cw=0.38, ch=0.38, fs=10.5)
    ax.text(6.75, 0.0, 'A³ =', fontsize=12, va='center', fontweight='bold', color=RED)
    W, H = matrix(ax, 8.65, 0, [[2, 3, 4, 1], [3, 2, 4, 1], [4, 4, 2, 3], [1, 1, 3, 0]], cw=0.38, ch=0.38, fs=10.5)
    ax.add_patch(Rectangle((8.65 - W / 2 + 2 * 0.38 + 0.03, H / 2 - 0.38 + 0.03), 0.32, 0.32, fc=YEL, ec=RED, lw=1.6, zorder=2))
    ax.set_xlim(-0.5, 9.6); ax.set_ylim(-1.35, 1.35)
    save(f, 'f15_dothi')

# ======================= Bài 16
def f16_luoi(n=12, name='f16_luoi', hyper=False):
    f, ax = fig(5.6, 5.0)
    import numpy as np
    s = 0.42
    for i in range(1, n + 1):
        for j in range(1, n // i + 1):
            if hyper:
                r = isqrt(n)
                both = i <= r and j <= r
                st = ('cur' if both else ('done' if i <= r else 'wait' if j <= r else 'gray'))
            else:
                st = 'cur' if i * j == n else 'done'
            node(ax, (i * s, j * s), '', st, r=0.1, lw=1.4)
    xs = np.linspace(0.85, n + 0.5, 200)
    ax.plot(xs * s, n / xs * s, color=RED, lw=1.6, zorder=1)
    ax.annotate('', xy=((n + 1.1) * s, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.4))
    ax.annotate('', xy=(0, (n + 1.1) * s), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.4))
    for i in range(1, n + 1):
        ax.text(i * s, -0.22, str(i), ha='center', va='top', fontsize=9, color=TXT)
        ax.text(-0.15, i * s, str(i), ha='right', va='center', fontsize=9, color=TXT)
    ax.text((n + 1.2) * s, -0.05, 'i', fontsize=11, style='italic', va='top')
    ax.text(-0.05, (n + 1.25) * s, 'j', fontsize=11, style='italic', ha='right')
    if not hyper:
        for i in range(1, n + 1):
            ax.text(i * s, (n // i) * s + 0.24, str(n // i), ha='center', va='bottom', fontsize=8.5, color=NAVY, fontweight='bold')
        ax.text(2.2, 4.55, f'cột i có ⌊{n}/i⌋ điểm', fontsize=9.5, color=NAVY, fontweight='bold')
        ax.text(2.2, 4.1, f'tổng: {sum(n // i for i in range(1, n + 1))} điểm (i, j) với i · j ≤ {n}', fontsize=9.5, color=NAVY)
        ax.text(2.2, 3.5, f'điểm vàng: i · j = {n}\n↔ 6 ước của {n}', fontsize=9.5, color=RED, fontweight='bold', va='top')
    else:
        r = isqrt(n)
        ax.add_patch(Rectangle((0.5 * s, 0.5 * s), r * s, r * s, fc='none', ec=RED, lw=1.8, ls=(0, (4, 2))))
        ax.text(2.2, 4.6, f'xanh dương: i ≤ √{n}', fontsize=9.5, color=NAVY, fontweight='bold')
        ax.text(2.2, 4.15, f'xanh lá: j ≤ √{n}', fontsize=9.5, color=GREEN, fontweight='bold')
        ax.text(2.2, 3.7, f'vàng: thuộc cả hai,\nbị đếm 2 lần ({r} × {r} điểm)', fontsize=9.5, color=RED, fontweight='bold', va='top')
    ax.set_xlim(-0.5, (n + 1.5) * s); ax.set_ylim(-0.55, (n + 1.6) * s)
    save(f, name)

def f16_bacthang():
    n = 20
    f, ax = plt.subplots(figsize=(8.6, 3.6))
    vals = [n // i for i in range(1, n + 1)]
    pal = [('#BDD7EE', NAVY), ('#FFE7B3', AMBER), ('#CDEBC5', GREEN), ('#F4C7D9', PINK), ('#B2E5E0', TEAL), ('#DCCCEC', PURPLE), ('#F8CBAD', ORANGE), ('#FFD966', RED)]
    i = 1; b = 0
    while i <= n:
        q = n // i; j = n // q
        fc, ec = pal[b % len(pal)]
        for t in range(i, j + 1):
            ax.add_patch(Rectangle((t - 0.42, 0), 0.84, q, fc=fc, ec=ec, lw=1.3))
        ax.text((i + j) / 2, q + 0.4, str(q), ha='center', va='bottom', fontsize=10, color=ec, fontweight='bold')
        if j > i:
            ax.plot([i - 0.42, i - 0.42, j + 0.42, j + 0.42], [-1.0, -1.35, -1.35, -1.0], color=ec, lw=1.5, clip_on=False)
            ax.text((i + j) / 2, -1.6, f'khối [{i}, {j}]:\n{j - i + 1} số cùng bằng {q}', ha='center', va='top', fontsize=9.5, color=ec, fontweight='bold')
        i = j + 1; b += 1
    for t in range(1, n + 1): ax.text(t, -0.3, str(t), ha='center', va='top', fontsize=9)
    ax.axvline(20 ** 0.5, color=RED, lw=1.4, ls=(0, (4, 3)), ymin=0.12)
    ax.text(20 ** 0.5 + 0.2, 15.5, 'i = √20 ≈ 4,47', color=RED, fontsize=9.5, fontweight='bold')
    ax.text(5.2, 12.5, 'bên trái: mỗi i một giá trị (≤ √n giá trị)\nbên phải: mọi giá trị đều < √n', fontsize=9.5, color='#404040', va='top')
    ax.text(8.0, 19.5, 'chiều cao cột thứ i là ⌊20 / i⌋', fontsize=10.5, color=NAVY, fontweight='bold', va='center')
    ax.set_xlim(0.3, n + 0.7); ax.set_ylim(-4.2, 22.0); ax.axis('off')
    ax.plot([0.45, n + 0.6], [0, 0], color=GRAY, lw=1.2)
    save(f, 'f16_bacthang')

f13_chon(); f13_pascal(); f13_xich(); f13_keo()
f14_venn(); f14_tapcon(); f14_tran()
f15_lat(); f15_truot(); f15_luythua(); f15_dothi()
f16_luoi(); f16_luoi(12, 'f16_hyperbol', True); f16_bacthang()

from flow import flow
flow('f13_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc Q truy vấn;\nmx ← n lớn nhất'), ('loop', 'n = 0, 1, ..., mx ?'),
     ('proc', 'c[n][0] = c[n][n] = 1\nc[n][k] ← c[n−1][k−1] + c[n−1][k]'), ('end', ''), ('loop', 'còn truy vấn\n(n, k)?'),
     ('io', 'In c[n][k] (0 nếu k > n)'), ('end', ''), ('term', 'Kết thúc')])
flow('f13_toiuu', [('term', 'Bắt đầu'), ('proc', 'fact[i] ← fact[i − 1] · i\n(i = 1..N)'), ('proc', 'ifact[N] ← fact[N]^(p−2)'),
     ('proc', 'ifact[i − 1] ← ifact[i] · i\n(i = N..1)'), ('loop', 'còn truy vấn\n(n, k)?'),
     ('io', 'In fact[n] · ifact[k] · ifact[n−k]\n(0 nếu k < 0 hoặc k > n)'), ('end', ''), ('term', 'Kết thúc')])
flow('f14_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc N, k, a[0..k−1]'), ('proc', 'đếm ← 0'), ('loop', 'x = 1, 2, ..., N ?'),
     ('dec', 'x chia hết cho\nmột a[i] nào?', ('đếm ← đếm + 1', 'proc')), ('end', ''), ('io', 'In đếm'), ('term', 'Kết thúc')])
flow('f14_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc N, k, a[0..k−1]'), ('proc', 'L[∅] ← 1; ans ← 0'), ('loop', 'còn tập con\nS ≠ ∅ ?'),
     ('proc', 'i ← phần tử nhỏ nhất của S\nL[S] ← lcm(L[S bỏ i], a[i])\n(nếu > N thì gán N + 1)'),
     ('proc', 'ans ← ans ± ⌊N / L[S]⌋\n(+ khi |S| lẻ, − khi |S| chẵn)'), ('end', ''), ('io', 'In ans'), ('term', 'Kết thúc')])
flow('f15_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc n, m'), ('proc', 'a ← 0;  b ← 1'), ('loop', 'chưa lặp\nđủ n lần?'),
     ('proc', '(a, b) ← (b, (a + b) mod m)'), ('end', ''), ('io', 'In a'), ('term', 'Kết thúc')])
flow('f15_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc n, m'), ('proc', 'R ← I;  M ← Q'), ('loop', 'n > 0 ?'),
     ('dec', 'n lẻ ?', ('R ← R · M', 'proc')), ('proc', 'M ← M · M\nn ← ⌊n / 2⌋'), ('end', ''), ('io', 'In R[0][1]'), ('term', 'Kết thúc')])
flow('f16_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc n'), ('proc', 's ← 0'), ('loop', 'i = 1, 2, ..., n ?'),
     ('proc', 's ← s + ⌊n / i⌋'), ('end', ''), ('io', 'In s'), ('term', 'Kết thúc')])
flow('f16_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc n'), ('proc', 's ← 0;  i ← 1'), ('loop', 'i ≤ n ?'),
     ('proc', 'q ← ⌊n / i⌋;  j ← ⌊n / q⌋'), ('proc', 's ← s + q · (j − i + 1)\ni ← j + 1'), ('end', ''), ('io', 'In s'), ('term', 'Kết thúc')])
