# Hình Chương 2 (Tập 2): số nguyên tố
from shlib import *

def isp(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True
def spf(n):
    d = 2
    while d * d <= n:
        if n % d == 0: return d
        d += 1
    return n
def factor(n, lim=None):
    f = []; d = 2
    while d * d <= n and (lim is None or d <= lim):
        e = 0
        while n % d == 0: n //= d; e += 1
        if e: f.append((d, e))
        d += 1
    return f, n
def grp(n):                                        # 999999999990 -> '999 999 999 990'
    return f'{n:,}'.replace(',', ' ')
SUP = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
def pe(p, e): return f'{p}' + (str(e).translate(SUP) if e > 1 else '')

Y_FC, Y_EC = '#FFD966', RED          # đáp số / đang xét
B_FC, B_EC = '#BDD7EE', NAVY         # bình thường / đã xong
O_FC, O_EC = '#FFE7B3', AMBER        # dữ liệu vào
G_FC, G_EC = '#EDEDED', '#9A9A9A'    # bị loại

# ---------------------------------------------------------------- 5.1
def ntgannhat():
    f, ax = fig(8.6, 2.9)
    n = 26; lo, hi = 20, 32; w = 0.62
    order = []; d = 0; ans = None
    while ans is None:
        for x in ([n] if d == 0 else [n - d, n + d]):
            order.append(x)
            if isp(x): ans = x; break
        d += 1
    for x in range(lo, hi + 1):
        X = (x - lo) * w
        if x == ans: fc, ec = Y_FC, Y_EC
        elif x == n: fc, ec = O_FC, O_EC
        elif isp(x): fc, ec = B_FC, B_EC
        else: fc, ec = G_FC, G_EC
        cellbox(ax, X, 0, x, fc=fc, ec=ec, w=w - 0.06, h=0.5, fs=11, color=TXT if fc != G_FC else '#707070')
        if x in order:
            k = order.index(x) + 1
            node(ax, (X, 0.62), k, 'w' if x != ans else 'cur', r=0.17, fs=9.5, lw=1.6)
    ax.text(-0.5, 0.62, 'thứ tự xét', ha='right', va='center', fontsize=10, color=NAVY, fontweight='bold')
    for dd in range(1, d):
        for s in (-1, 1):
            X = (n + s * dd - lo) * w
            ax.text(X, -0.42, f'd={dd}', ha='center', va='top', fontsize=9, color='#505050')
    ax.text((n - lo) * w, -0.42, 'n', ha='center', va='top', fontsize=10, color=AMBER, fontweight='bold', style='italic')
    other = n + (n - ans)
    ax.annotate('', xy=((ans - lo) * w, -0.95), xytext=((n - lo) * w, -0.95), arrowprops=dict(arrowstyle='<->', color=RED, lw=1.5))
    ax.annotate('', xy=((other - lo) * w, -0.95), xytext=((n - lo) * w, -0.95), arrowprops=dict(arrowstyle='<->', color=NAVY, lw=1.5))
    ax.text(((ans + n) / 2 - lo) * w, -1.08, f'{n - ans}', ha='center', va='top', fontsize=10, color=RED, fontweight='bold')
    ax.text(((other + n) / 2 - lo) * w, -1.08, f'{other - n}', ha='center', va='top', fontsize=10, color=NAVY, fontweight='bold')
    tx = (hi - lo) * w + 0.7
    ax.text(tx, 0.45, f'{ans} và {other} cách đều n = {n}', fontsize=10.5, color=TXT, va='center')
    ax.text(tx, 0.0, f'→ chọn số nhỏ hơn: {ans}', fontsize=10.5, color=RED, fontweight='bold', va='center')
    ax.text(tx, -0.45, f'(xét {n - (n - ans)} = n − d trước n + d)', fontsize=9.5, color='#505050', va='center')
    ax.set_xlim(-2.2, tx + 4.2); ax.set_ylim(-1.45, 0.95); save(f, 'ntgannhat')

# ---------------------------------------------------------------- 5.2
def goldbach():
    f, ax = fig(8.6, 2.7)
    n = 98; ps = []; p = 2
    while True:
        if isp(p):
            ps.append(p)
            if isp(n - p): break
        p += 1
    w = 1.22
    ax.text(-0.75, 0.6, 'p', ha='right', va='center', fontsize=12, color=AMBER, fontweight='bold', style='italic')
    ax.text(-0.75, -0.15, 'n − p', ha='right', va='center', fontsize=12, color=NAVY, fontweight='bold', style='italic')
    ax.text(-0.75, -0.75, 'ước', ha='right', va='center', fontsize=10, color='#505050')
    for i, p in enumerate(ps):
        X = i * w; q = n - p; ok = isp(q)
        cellbox(ax, X, 0.6, p, fc=O_FC, ec=O_EC, w=w - 0.1, h=0.5, fs=11.5)
        cellbox(ax, X, -0.15, q, fc=Y_FC if ok else G_FC, ec=Y_EC if ok else G_EC, w=w - 0.1, h=0.5, fs=11.5, color=TXT if ok else '#606060')
        if ok: ax.text(X, -0.75, 'nguyên tố', ha='center', va='center', fontsize=9, color=RED, fontweight='bold')
        else:
            d = spf(q); ax.text(X, -0.75, f'{d} · {q // d}', ha='center', va='center', fontsize=9.5, color='#505050')
    X = (len(ps) - 1) * w
    ax.text(X + 0.75, 0.22, f'{n} = {ps[-1]} + {n - ps[-1]}', fontsize=12, color=RED, fontweight='bold', va='center')
    ax.text(-0.75, 1.15, f'n = {n}', ha='right', va='center', fontsize=12, color=NAVY, fontweight='bold')
    ax.set_xlim(-2.0, X + 3.6); ax.set_ylim(-1.05, 1.4); save(f, 'goldbach')

# ---------------------------------------------------------------- 5.3
def nt64():
    f, ax = fig(9.0, 3.3)
    n = 25326001; d = n - 1; s = 0
    while d % 2 == 0: d //= 2; s += 1
    w, h = 1.55, 0.5
    heads = ['a^d', 'a^{2d}', 'a^{4d}', 'a^{8d}', 'a^{16d}']
    for j in range(s + 1):
        ax.text(j * w, 0.62, f'${heads[j]}$', ha='center', va='center', fontsize=12, color=NAVY, fontweight='bold')
    ax.text(-1.35, 0.62, 'cơ sở', ha='center', va='center', fontsize=10.5, color=NAVY, fontweight='bold')
    for i, a in enumerate([2, 3, 5, 7]):
        y = -i * 0.62
        x = pow(a, d, n); ch = [x]
        for _ in range(s): x = x * x % n; ch.append(x)
        ok = ch[0] == 1 or (n - 1) in ch[:s]
        ax.text(-1.35, y, f'a = {a}', ha='center', va='center', fontsize=11, color=TXT, fontweight='bold')
        for j, v in enumerate(ch):
            if v == n - 1: fc, ec, t = '#CDEBC5', GREEN, 'n − 1'
            elif v == 1: fc, ec, t = B_FC, B_EC, '1'
            else: fc, ec, t = (G_FC, G_EC, grp(v)) if ok else ('#F8CBAD', RED, grp(v))
            cellbox(ax, j * w, y, t, fc=fc, ec=ec, w=w - 0.1, h=h, fs=10, bold=v in (1, n - 1))
        X = s * w + 1.05
        if ok: ax.text(X, y, 'cho qua', va='center', fontsize=10.5, color=GREEN, fontweight='bold')
        else: ax.text(X, y, 'nhân chứng:\nn là hợp số', va='center', fontsize=10.5, color=RED, fontweight='bold')
    ax.text(2 * w, -3 * 0.62 - 0.62, f'n = {grp(n)} = 2251 · 11 251,   n − 1 = {grp(d)} · 2$^{s}$', ha='center', va='center', fontsize=10.5, color=TXT)
    ax.set_xlim(-2.2, s * w + 3.0); ax.set_ylim(-2.75, 0.95); save(f, 'nt64')

# ---------------------------------------------------------------- 6.1
def demnguyento():
    f, ax = fig(7.6, 2.4)
    N = 20; w = 0.56
    pr = [x for x in range(2, N + 1) if isp(x)]
    c = 0
    ax.text(-0.45, 0.55, 'x', ha='right', va='center', fontsize=11.5, color=NAVY, fontweight='bold', style='italic')
    ax.text(-0.45, 0.0, 'c[x]', ha='right', va='center', fontsize=11.5, color=NAVY, fontweight='bold')
    for x in range(1, N + 1):
        X = (x - 1) * w; c += isp(x)
        cellbox(ax, X, 0.55, x, fc=B_FC if isp(x) else G_FC, ec=B_EC if isp(x) else G_EC, w=w - 0.06, h=0.46, fs=9.5, color=TXT if isp(x) else '#707070')
        q = x == N
        cellbox(ax, X, 0.0, c, fc=Y_FC if q else 'white', ec=Y_EC if q else '#9AAFCB', w=w - 0.06, h=0.46, fs=9.5, bold=q)
    ax.text(-0.45, -0.85, 'pr[k]', ha='right', va='center', fontsize=11.5, color=NAVY, fontweight='bold')
    for k, p in enumerate(pr, 1):
        X = (k - 1) * w; q = k == 7
        cellbox(ax, X, -0.85, p, fc=Y_FC if q else B_FC, ec=Y_EC if q else B_EC, w=w - 0.06, h=0.46, fs=9.5, bold=True)
        ax.text(X, -1.15, f'{k}', ha='center', va='top', fontsize=9, color='#505050')
    ax.text(-0.45, -1.28, 'k', ha='right', va='center', fontsize=10, color='#505050', style='italic')
    tx = len(pr) * w + 0.5
    ax.text(tx, -0.62, f'"1 {N}" → c[{N}] = {len(pr)}', fontsize=11, color=RED, fontweight='bold', va='center')
    ax.text(tx, -1.08, f'"2 7" → pr[7] = {pr[6]}', fontsize=11, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-1.5, (N - 1) * w + 0.5); ax.set_ylim(-1.55, 0.9); save(f, 'demnguyento')

# ---------------------------------------------------------------- 6.2
def sinhdoi():
    f, ax = fig(7.6, 2.5)
    N = 24; w = 0.5; a, b = 6, 20
    ax.add_patch(Rectangle(((a - 1) * w - w / 2, -0.32), (b - a + 1) * w, 0.64, fc='#FFF6DB', ec=AMBER, lw=1.5, ls='--', zorder=1))
    ax.add_patch(Rectangle(((a - 1) * w - w / 2, -0.32), (b - 2 - a + 1) * w, 0.64, fc='#FFE7B3', ec='none', zorder=0.9, alpha=0.9))
    for x in range(1, N + 1):
        X = (x - 1) * w; P = isp(x)
        cellbox(ax, X, 0, x, fc=B_FC if P else G_FC, ec=B_EC if P else G_EC, w=w - 0.06, h=0.44, fs=8.5, color=TXT if P else '#707070')
    for p in range(2, N - 1):
        if isp(p) and isp(p + 2):
            inq = a <= p and p + 2 <= b
            col = RED if inq else GRAY
            ax.annotate('', xy=((p + 1) * w, 0.24), xytext=((p - 1) * w, 0.24),
                        arrowprops=dict(arrowstyle='-', color=col, lw=2.2 if inq else 1.5, connectionstyle='arc3,rad=-0.55'), zorder=4)
            ax.text(p * w, 0.78, f'({p}, {p + 2})', ha='center', va='bottom', fontsize=9, color=col, fontweight='bold' if inq else 'normal')
    ax.text(((a + b) / 2 - 1) * w, -0.55, f'truy vấn [a, b] = [{a}, {b}]', ha='center', va='top', fontsize=10.5, color=AMBER, fontweight='bold')
    ax.text(((a + b - 2) / 2 - 1) * w, -0.98, f'p chạy trong [a, b − 2] = [{a}, {b - 2}]  →  t[{b - 2}] − t[{a - 1}]', ha='center', va='top', fontsize=10.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.5, (N - 1) * w + 0.5); ax.set_ylim(-1.4, 1.2); save(f, 'sinhdoi')

# ---------------------------------------------------------------- 6.3
def bauoc():
    f, ax = fig(9.0, 3.6)
    def box(x, y, w, h, t, fc, ec, fs=10.5, bold=False):
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0.05', fc=fc, ec=ec, lw=1.6, zorder=3))
        ax.text(x, y, t, ha='center', va='center', fontsize=fs, color=TXT, fontweight='bold' if bold else 'normal', zorder=4)
    box(0, 1.5, 2.6, 0.62, 'a ≤ 10¹²', O_FC, O_EC, fs=12, bold=True)
    box(0, 0.35, 3.3, 0.95, 'chia hết cho mọi\nsố nguyên tố p ≤ 10⁴\n(đếm p có số mũ ≥ 2)', B_FC, B_EC, fs=10)
    box(0, -0.85, 2.6, 0.62, 'phần còn lại r', O_FC, O_EC, fs=11.5, bold=True)
    ax.annotate('', xy=(0, 0.85), xytext=(0, 1.18), arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=1.6))
    ax.annotate('', xy=(0, -0.53), xytext=(0, -0.15), arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=1.6))
    cases = [('r = 1', '10¹² = 2¹² · 5¹²  (đáp số 2)', '+0', G_FC, G_EC), ('r = q', '995 303 515 103 = 9973² · 10 007  (đáp số 1)', '+0', G_FC, G_EC),
             ('r = q · q′', '100 160 063 = 10 007 · 10 009  (đáp số 0)', '+0', G_FC, G_EC), ('r = q²', '998 696 708 677 = 10 007² · 9973  (đáp số 1)', '+1', Y_FC, Y_EC)]
    ys = [1.5, 0.6, -0.3, -1.2]
    for (t, ex, inc, fc, ec), y in zip(cases, ys):
        box(3.6, y, 1.6, 0.56, t, fc, ec, fs=11.5, bold=True)
        ax.annotate('', xy=(2.75, y), xytext=(1.35, -0.85), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.3, shrinkB=3))
        ax.text(4.6, y, inc, ha='left', va='center', fontsize=12, color=RED if inc == '+1' else '#606060', fontweight='bold')
        ax.text(5.3, y, ex, ha='left', va='center', fontsize=10, color=TXT)
    ax.text(4.6, 1.95, 'cộng thêm', ha='center', va='center', fontsize=9.5, color='#505050')
    ax.text(3.6, -1.9, 'q, q′ là các số nguyên tố > 10⁴; tích ba số như thế đã vượt (10⁴)³ = 10¹²', ha='left', va='center', fontsize=9.5, color='#505050', style='italic')
    ax.set_xlim(-1.8, 11.6); ax.set_ylim(-2.15, 2.15); save(f, 'bauoc')

# ---------------------------------------------------------------- 7.1
def souoc():
    f, ax = fig(7.0, 3.6)
    w, h = 1.0, 0.6
    P2 = [1, 2, 4, 8]; P3 = [1, 3, 9]
    for j, b in enumerate(P3):
        ax.text(j * w, 0.75, f'{b}', ha='center', va='center', fontsize=12, color=GREEN, fontweight='bold')
    ax.text(1 * w, 1.25, 'lũy thừa của 3', ha='center', va='center', fontsize=10.5, color=GREEN, fontweight='bold')
    ax.text(-1.25, 0.75, '×', ha='center', va='center', fontsize=12, color=NAVY)
    for i, a in enumerate(P2):
        y = -i * h * 1.12
        ax.text(-0.85, y, f'{a}', ha='center', va='center', fontsize=12, color=AMBER, fontweight='bold')
        for j, b in enumerate(P3):
            cellbox(ax, j * w, y, a * b, fc=Y_FC if a * b == 72 else B_FC, ec=Y_EC if a * b == 72 else B_EC, w=w - 0.1, h=h - 0.06, fs=12)
        ax.text(2 * w + 0.75, y, f'{a * sum(P3)}', ha='left', va='center', fontsize=11, color=NAVY)
    ax.text(-1.7, -1.7 * h * 1.12, 'lũy thừa\ncủa 2', ha='center', va='center', fontsize=10.5, color=AMBER, fontweight='bold')
    ax.text(2 * w + 0.75, 0.75, 'tổng hàng', ha='left', va='center', fontsize=10, color=NAVY)
    yb = -4 * h * 1.12 + 0.1
    ax.plot([2 * w + 0.6, 2 * w + 1.9], [yb + 0.2, yb + 0.2], color=NAVY, lw=1)
    ax.text(2 * w + 0.75, yb - 0.12, f'{sum(P2) * sum(P3)}', ha='left', va='center', fontsize=12, color=RED, fontweight='bold')
    tx = 2 * w + 2.5
    ax.text(tx, 0.2, '72 = 2³ · 3²', fontsize=12, color=TXT, fontweight='bold')
    ax.text(tx, -0.45, f'd(72) = (3 + 1)(2 + 1) = {len(P2) * len(P3)}', fontsize=11, color=TXT)
    ax.text(tx, -1.1, f'σ(72) = (1 + 2 + 4 + 8)(1 + 3 + 9)', fontsize=11, color=TXT)
    ax.text(tx + 0.55, -1.6, f'= {sum(P2)} · {sum(P3)} = {sum(P2) * sum(P3)}', fontsize=11, color=RED, fontweight='bold')
    ax.set_xlim(-2.3, tx + 4.3); ax.set_ylim(yb - 0.45, 1.5); save(f, 'souoc')

# ---------------------------------------------------------------- 7.2
def chuso0():
    f, ax = fig(8.6, 3.1)
    n = 10; w = 0.75; r = 0.13
    e2 = e3 = 0
    for x in range(1, n + 1):
        X = (x - 1) * w
        cellbox(ax, X, 0, x, fc=O_FC, ec=O_EC, w=w - 0.1, h=0.48, fs=11.5)
        a, b = 0, 0; y = x
        while y % 2 == 0: y //= 2; a += 1
        y = x
        while y % 3 == 0: y //= 3; b += 1
        e2 += a; e3 += b
        for k in range(a): ax.add_patch(Circle((X - 0.15, -0.5 - k * 0.32), r, fc='#F4B183', ec=ORANGE, lw=1.3))
        for k in range(b): ax.add_patch(Circle((X + 0.15, -0.5 - k * 0.32), r, fc=B_FC, ec=B_EC, lw=1.3))
    tx = n * w + 0.2
    ax.add_patch(Circle((tx + 0.1, 0.2), r, fc='#F4B183', ec=ORANGE, lw=1.3))
    ax.text(tx + 0.35, 0.2, f'thừa số 2: tổng {e2}', va='center', fontsize=11, color=ORANGE, fontweight='bold')
    ax.add_patch(Circle((tx + 0.1, -0.3), r, fc=B_FC, ec=B_EC, lw=1.3))
    ax.text(tx + 0.35, -0.3, f'thừa số 3: tổng {e3}', va='center', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(tx, -0.95, f'10! = 2$^{{{e2}}}$ · 3$^{{{e3}}}$ · 5² · 7', va='center', fontsize=11, color=TXT)
    ax.text(tx, -1.45, f'12 = 2² · 3:  min(⌊{e2}/2⌋, ⌊{e3}/1⌋) = {min(e2 // 2, e3)}', va='center', fontsize=11, color=RED, fontweight='bold')
    ax.set_xlim(-0.5, tx + 5.0); ax.set_ylim(-1.75, 0.4); save(f, 'chuso0')

# ---------------------------------------------------------------- 7.3
def bcnnday():
    f, ax = fig(7.6, 3.4)
    a = [4, 6, 9, 10, 4]; P = [2, 3, 5]
    E = [[0] * len(P) for _ in a]
    for i, x in enumerate(a):
        for j, p in enumerate(P):
            while x % p == 0: x //= p; E[i][j] += 1
    M = [max(E[i][j] for i in range(len(a))) for j in range(len(P))]
    C = [sum(E[i][j] == M[j] for i in range(len(a))) for j in range(len(P))]
    w, h = 1.0, 0.5
    ax.text(-1.3, 0.62, 'aᵢ', ha='center', va='center', fontsize=12, color=NAVY, fontweight='bold')
    for j, p in enumerate(P): ax.text(j * w, 0.62, f'p = {p}', ha='center', va='center', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(len(P) * w + 0.9, 0.62, 'cần thiết?', ha='center', va='center', fontsize=11, color=NAVY, fontweight='bold')
    for i, x in enumerate(a):
        y = -i * (h + 0.1)
        cellbox(ax, -1.3, y, x, fc=O_FC, ec=O_EC, w=0.8, h=h, fs=12)
        need = False
        for j in range(len(P)):
            top = E[i][j] == M[j] and M[j] > 0
            uniq = top and C[j] == 1
            need |= uniq
            fc, ec = (Y_FC, Y_EC) if uniq else ((O_FC, O_EC) if top else ('white', '#9AAFCB'))
            cellbox(ax, j * w, y, E[i][j], fc=fc, ec=ec, w=w - 0.1, h=h, fs=12, bold=top)
        ax.text(len(P) * w + 0.9, y, 'có' if need else 'không', ha='center', va='center', fontsize=11.5, color=RED if need else '#707070', fontweight='bold' if need else 'normal')
    y = -len(a) * (h + 0.1) - 0.05
    ax.plot([-1.8, len(P) * w - 0.45], [y + 0.28, y + 0.28], color=NAVY, lw=1.2)
    ax.text(-1.3, y, 'max', ha='center', va='center', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(-1.3, y - 0.45, 'số lần', ha='center', va='center', fontsize=10.5, color=NAVY, fontweight='bold')
    for j in range(len(P)):
        ax.text(j * w, y, f'{M[j]}', ha='center', va='center', fontsize=11.5, color=TXT, fontweight='bold')
        ax.text(j * w, y - 0.45, f'{C[j]}', ha='center', va='center', fontsize=11, color=TXT)
    L = 1
    for p, m in zip(P, M): L *= p ** m
    ax.text(len(P) * w + 0.9, y - 0.22, f'L = 2² · 3² · 5 = {L}', ha='left', va='center', fontsize=11.5, color=RED, fontweight='bold')
    lx = len(P) * w + 2.0
    cellbox(ax, lx, -0.2, '', fc=Y_FC, ec=Y_EC, w=0.4, h=0.32)
    ax.text(lx + 0.35, -0.2, 'max, đạt bởi\nđúng một phần tử', ha='left', va='center', fontsize=9.5, color=TXT)
    cellbox(ax, lx, -1.1, '', fc=O_FC, ec=O_EC, w=0.4, h=0.32)
    ax.text(lx + 0.35, -1.1, 'max, đạt bởi\nnhiều phần tử', ha='left', va='center', fontsize=9.5, color=TXT)
    ax.set_xlim(-1.9, lx + 2.9); ax.set_ylim(y - 0.75, 0.9); save(f, 'bcnnday')

# ---------------------------------------------------------------- 8.1
def ntdoan():
    f, ax = fig(7.0, 3.2)
    L, R = 100, 130; w = 0.36; h = 0.36
    S = int(R ** 0.5); ps = [p for p in range(2, S + 1) if isp(p)]
    for x in range(L, R + 1):
        ax.text((x - L) * w, 0.42, str(x), ha='center', va='bottom', fontsize=8.5, color=NAVY, rotation=90)
    gach = set()
    for i, p in enumerate(ps):
        y = -i * (h + 0.06)
        st = max(p * p, (L + p - 1) // p * p)
        ax.text(-0.35, y, f'p = {p}', ha='right', va='center', fontsize=9.5, color=NAVY, fontweight='bold')
        for x in range(L, R + 1):
            X = (x - L) * w
            hit = x >= st and x % p == 0
            if x == st: fc, ec = Y_FC, Y_EC
            elif hit: fc, ec = '#BFBFBF', '#8C8C8C'
            elif x in gach: fc, ec = '#F2F2F2', '#D0D0D0'
            else: fc, ec = 'white', '#D0D0D0'
            ax.add_patch(Rectangle((X - w / 2 + 0.02, y - h / 2), w - 0.04, h, fc=fc, ec=ec, lw=0.8))
            if hit and x != st: ax.plot([X - w / 2 + 0.07, X + w / 2 - 0.07], [y - h / 2 + 0.06, y + h / 2 - 0.06], color='#606060', lw=1)
        for x in range(st, R + 1, p): gach.add(x)
        ax.text((R - L) * w + 0.35, y, f'từ {st}', ha='left', va='center', fontsize=9.5, color=RED if st == p * p else '#404040', fontweight='bold' if st == p * p else 'normal')
    y = -len(ps) * (h + 0.06) - 0.12
    ax.text(-0.35, y, 'còn lại', ha='right', va='center', fontsize=10, color=RED, fontweight='bold')
    for x in range(L, R + 1):
        X = (x - L) * w; P = x not in gach
        ax.add_patch(Rectangle((X - w / 2 + 0.02, y - h / 2), w - 0.04, h, fc=B_FC if P else 'white', ec=B_EC if P else '#D0D0D0', lw=1.4 if P else 0.8))
    ax.text((R - L) * w + 0.35, y, f'{sum(1 for x in range(L, R + 1) if x not in gach)} số', ha='left', va='center', fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-1.6, (R - L) * w + 1.4); ax.set_ylim(y - 0.35, 1.3); save(f, 'ntdoan')

# ---------------------------------------------------------------- 8.2
def khoangcach():
    f, ax = fig(7.4, 2.3)
    L, R = 3, 22; w = 0.6
    ps = [x for x in range(L, R + 1) if isp(x)]
    ax.plot([-0.3, (R - L) * w + 0.3], [0, 0], color=GRAY, lw=1.5, zorder=1)
    pairs = list(zip(ps, ps[1:]))
    big = max(pairs, key=lambda t: (t[1] - t[0], -t[0])); sm = min(pairs, key=lambda t: (t[1] - t[0], t[0]))
    for x in range(L, R + 1):
        X = (x - L) * w
        if isp(x): node(ax, (X, 0), x, 'done', r=0.31, fs=9, lw=1.8)
        else:
            ax.plot([X, X], [-0.07, 0.07], color=GRAY, lw=1)
            ax.text(X, -0.2, str(x), ha='center', va='top', fontsize=9.5, color='#808080')
    for p, q in pairs:
        col = RED if (p, q) == big else (GREEN if (p, q) == sm else NAVY)
        lw = 2.4 if col != NAVY else 1.4
        ax.annotate('', xy=((q - L) * w, 0.22), xytext=((p - L) * w, 0.22),
                    arrowprops=dict(arrowstyle='-', color=col, lw=lw, connectionstyle='arc3,rad=-0.5', shrinkA=4, shrinkB=4), zorder=3)
        ax.text(((p + q) / 2 - L) * w, 0.3 + (q - p) * w * 0.25, str(q - p), ha='center', va='bottom', fontsize=10.5, color=col, fontweight='bold')
    tx = (R - L) * w + 0.6
    ax.text(tx, 0.55, f'lớn nhất: ({big[0]}, {big[1]})', fontsize=11, color=RED, fontweight='bold', va='center')
    ax.text(tx, 0.05, f'nhỏ nhất: ({sm[0]}, {sm[1]})', fontsize=11, color=GREEN, fontweight='bold', va='center')
    ax.text(tx, -0.45, 'hòa: lấy cặp bên trái', fontsize=10, color='#505050', va='center')
    ax.set_xlim(-0.5, tx + 3.6); ax.set_ylim(-0.6, 1.2); save(f, 'khoangcach')

# ---------------------------------------------------------------- 8.3
def uocdoan():
    f, ax = fig(9.4, 3.5)
    L, R = 999999999990, 999999999995; S = 10**6
    CX, CF, CR, CD = 0.0, 4.15, 7.35, 9.95
    for X, t in [(CX, 'x'), (CF, 'thừa số p ≤ √R'), (CR, 'phần còn lại'), (CD, 'd(x)')]:
        ax.text(X, 0.55, t, ha='center', va='center', fontsize=11, color=NAVY, fontweight='bold')
    ax.plot([-1.4, 11.6], [0.3, 0.3], color=NAVY, lw=1.2)
    for i, x in enumerate(range(L, R + 1)):
        y = -i * 0.5
        fs_, rem = factor(x, S)
        if 1 < rem <= S: fs_.append((rem, 1)); rem = 1      # thừa số ≤ 10^6 cũng bị sàng chia hết
        big = rem > 1
        if i % 2 == 0: ax.add_patch(Rectangle((-1.4, y - 0.25), 13.0, 0.5, fc='#F3F6FA', ec='none', zorder=0))
        ax.text(CX, y, grp(x), ha='center', va='center', fontsize=10.5, color=TXT)
        ax.text(CF, y, ' · '.join(pe(p, e) for p, e in fs_), ha='center', va='center', fontsize=10.5, color=TXT)
        cellbox(ax, CR, y, grp(rem), fc=Y_FC if big else 'white', ec=Y_EC if big else '#B0B0B0', w=1.85, h=0.4, fs=10, bold=big)
        ks = sorted((e + 1 for _, e in fs_), reverse=True); parts = []
        for k in sorted(set(ks), reverse=True):
            c = ks.count(k); parts.append(pe(k, c))
        d = 1
        for k in ks: d *= k
        if big: parts.append('2'); d *= 2
        ax.text(CD, y, ' · '.join(parts) + f' = {d}', ha='center', va='center', fontsize=10.5, color=RED if big else TXT, fontweight='bold' if big else 'normal')
    ax.set_xlim(-1.5, 11.7); ax.set_ylim(-(R - L) * 0.5 - 0.35, 0.8); save(f, 'uocdoan')

ntgannhat(); goldbach(); nt64(); demnguyento(); sinhdoi(); bauoc(); souoc(); chuso0(); bcnnday(); ntdoan(); khoangcach(); uocdoan()
