# Hình Chương 3. SỐ HỌC ĐỒNG DƯ
from shlib import *
from math import gcd
import math

YEL, BLU, AMB, GRY = '#FFD966', '#BDD7EE', '#FFE7B3', '#EDEDED'
GRYE = '#9A9A9A'
SUP = str.maketrans('0123456789−()p', '⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁽⁾ᵖ')
def sup(x): return str(x).translate(SUP)

def arr(ax, p, q, color=NAVY, lw=1.6, rad=0.0, ms=12, z=2):
    ax.annotate('', xy=q, xytext=p, zorder=z, arrowprops=dict(arrowstyle='-|>', color=color, lw=lw,
                mutation_scale=ms, shrinkA=0, shrinkB=0, connectionstyle=f'arc3,rad={rad}'))

# ======================= Bài 9: LŨY THỪA NHANH
def f9_cay():
    """Cây (chuỗi) đệ quy của 3^13 mod 1000: đi xuống chia đôi số mũ, đi lên bình phương."""
    f, ax = fig(9.4, 3.3)
    bs = [13, 6, 3, 1, 0]; vals = [323, 729, 27, 3, 1]
    ops = ['729² · 3', '27²', '3² · 3', '1² · 3']
    X = [0, 2.6, 5.2, 7.8, 10.4]
    ax.text(-1.0, 1.2, 'Gọi', fontsize=11, color=NAVY, fontweight='bold', ha='right', va='center')
    ax.text(-1.0, -0.75, 'Trả về', fontsize=11, color=RED, fontweight='bold', ha='right', va='center')
    ax.text(-1.0, -1.1, '(mod 1000)', fontsize=9, color='#404040', ha='right', va='center')
    for i, (x, b, v) in enumerate(zip(X, bs, vals)):
        cellbox(ax, x, 1.2, '3' + sup(b), fc=AMB, ec=AMBER, w=1.15, h=0.62, fs=12)
        ax.text(x, 1.67, f'b = {b}', ha='center', va='bottom', fontsize=9.5, color='#404040')
        st = (YEL, RED) if i == 0 else ((GRY, GRYE) if b == 0 else (BLU, NAVY))
        cellbox(ax, x, -0.9, v, fc=st[0], ec=st[1], w=1.15, h=0.62, fs=13)
        if i < 4:
            arr(ax, (x + 0.6, 1.2), (X[i + 1] - 0.6, 1.2), color=AMBER)
            ax.text((x + X[i + 1]) / 2, 1.33, 'b lẻ' if b % 2 else 'b chẵn', ha='center', va='bottom', fontsize=8.5, color=AMBER)
            ax.text((x + X[i + 1]) / 2, 1.07, f'⌊{b}/2⌋', ha='center', va='top', fontsize=8.5, color=AMBER)
            arr(ax, (X[i + 1] - 0.6, -0.9), (x + 0.6, -0.9), color=NAVY)
            ax.text((x + X[i + 1]) / 2, -0.77, ops[i], ha='center', va='bottom', fontsize=9, color=NAVY, fontweight='bold')
        if b == 0:
            arr(ax, (x, 0.86), (x, -0.56), color=GRAY)
            ax.text(x + 0.12, 0.15, 'dừng:\n3⁰ = 1', fontsize=8.5, color='#404040', va='center', ha='left')
        else:
            ax.plot([x, x], [0.86, -0.56], color=LGRAY, lw=1, ls=(0, (3, 3)), zorder=1)
    ax.text(X[0], -1.32, '= 3¹³ mod 1000', ha='center', va='top', fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-2.3, 11.4); ax.set_ylim(-1.75, 2.05)
    save(f, 'f9_cay')

def f9_bit():
    """Các bit của số mũ 13 = 1101 (nhị phân) và các lũy thừa 3^1, 3^2, 3^4, 3^8."""
    f, ax = fig(8.4, 3.6)
    bits = [1, 1, 0, 1]                 # bit 3, 2, 1, 0
    pw = [8, 4, 2, 1]; vals = [561, 81, 9, 3]
    X = [0, 2.0, 4.0, 6.0]
    ax.text(-1.05, 1.55, 'Lũy thừa', fontsize=10.5, color=NAVY, fontweight='bold', ha='right', va='center')
    ax.text(-1.05, 1.2, '(mod 1000)', fontsize=8.5, color='#404040', ha='right', va='center')
    ax.text(-1.05, 0.0, 'Bit của 13', fontsize=10.5, color=AMBER, fontweight='bold', ha='right', va='center')
    for i, x in enumerate(X):
        on = bits[i] == 1
        cellbox(ax, x, 1.4, vals[i], fc=YEL if on else GRY, ec=RED if on else GRYE, w=1.1, h=0.62, fs=13)
        ax.text(x, 1.82, '3' + sup(pw[i]), ha='center', va='bottom', fontsize=10.5, color=NAVY, fontweight='bold')
        cellbox(ax, x, 0.0, bits[i], fc=AMB if on else 'white', ec=AMBER if on else GRYE, w=0.7, h=0.62, fs=14)
        ax.text(x, -0.42, '2' + sup(pw[i].bit_length() - 1) + f' = {pw[i]}', ha='center', va='top', fontsize=8.5, color='#404040')
        if i < 3:
            arr(ax, (X[i + 1] - 0.57, 1.4), (x + 0.57, 1.4), color=NAVY)
            ax.text((x + X[i + 1]) / 2, 1.52, 'bình\nphương', ha='center', va='bottom', fontsize=8, color=NAVY)
        ax.plot([x, x], [1.08, 0.32], color=RED if on else LGRAY, lw=1.6 if on else 1, ls='-' if on else (0, (3, 3)), zorder=1)
    ax.text(7.0, 0.0, '13 = 8 + 4 + 1', fontsize=11, color=AMBER, fontweight='bold', va='center')
    ax.text(7.0, 1.4, 'bắt đầu từ\n3¹ = 3', fontsize=9, color='#404040', va='center')
    ax.text(3.0, -1.15, '3¹³ = 3⁸ · 3⁴ · 3¹  ≡  561 · 81 · 3  ≡  323  (mod 1000)', ha='center', fontsize=11.5,
            color=RED, fontweight='bold', va='center')
    ax.set_xlim(-2.5, 9.0); ax.set_ylim(-1.5, 2.3)
    save(f, 'f9_bit')

# ======================= Bài 10: NGHỊCH ĐẢO MÔ-ĐUN
def mtable(ax, m, x0, y0, s=0.5, title=''):
    n = m - 1
    ax.text(x0 + (n + 1) * s / 2, y0 + 0.55, title, ha='center', fontsize=11, color=NAVY, fontweight='bold')
    cellbox(ax, x0 + s / 2, y0, '·', fc='#E8EEF7', ec=NAVY, w=s, h=s, fs=11, lw=1)
    for j in range(1, m):
        cellbox(ax, x0 + j * s + s / 2, y0, j, fc='#E8EEF7', ec=NAVY, w=s, h=s, fs=10.5, lw=1)
        cellbox(ax, x0 + s / 2, y0 - j * s, j, fc='#E8EEF7', ec=NAVY, w=s, h=s, fs=10.5, lw=1)
    for i in range(1, m):
        has = any(i * j % m == 1 for j in range(1, m))
        for j in range(1, m):
            v = i * j % m
            if v == 1: fc, ec = YEL, RED
            elif not has: fc, ec = GRY, GRYE
            else: fc, ec = 'white', LGRAY
            cellbox(ax, x0 + j * s + s / 2, y0 - i * s, v, fc=fc, ec=ec, w=s, h=s, fs=10.5, lw=1 if v != 1 else 1.6, bold=v == 1, z=5 if v == 1 else 3,
                    color=TXT if v == 1 else '#404040')

def f10_bangnhan():
    f, ax = fig(8.2, 3.9)
    mtable(ax, 7, 0, 0, title='Nhân theo mô-đun 7')
    mtable(ax, 6, 4.6, 0, title='Nhân theo mô-đun 6')
    ax.text(4.6 + 3.25, -1.0, 'Hàng 2, 3, 4\nkhông có số 1:\n2, 3, 4 không có\nnghịch đảo\ntheo mô-đun 6', fontsize=9.5, color=RED, va='center')
    ax.text(1.75, -3.75, 'Mỗi hàng có đúng một số 1:\nmọi b = 1..6 đều có nghịch đảo', ha='center', fontsize=9.5, color=NAVY, va='center')
    ax.set_xlim(-0.2, 9.9); ax.set_ylim(-4.25, 0.85)
    save(f, 'f10_bangnhan')

def f10_hoanvi():
    f, ax = fig(8.6, 3.0)
    p, a = 7, 3
    X = [1.3 * k for k in range(1, p)]
    ax.text(0.35, 1.2, 'k', fontsize=12, color=NAVY, fontweight='bold', ha='right', va='center', style='italic')
    ax.text(0.35, -1.2, '3k mod 7', fontsize=11, color=RED, fontweight='bold', ha='right', va='center')
    for k in range(1, p):
        cellbox(ax, X[k - 1], 1.2, k, fc=AMB, ec=AMBER, w=0.7, h=0.6)
        cellbox(ax, X[k - 1], -1.2, k, fc=BLU, ec=NAVY, w=0.7, h=0.6)
    cols = [NAVY, RED, GREEN, PURPLE, TEAL, ORANGE]
    for k in range(1, p):
        v = a * k % p
        ax.text(X[k - 1], 0.72, f'3·{k} = {a * k}', fontsize=8.5, color=cols[k - 1], ha='center', va='center', fontweight='bold')
        arr(ax, (X[k - 1], 0.55), (X[v - 1], -0.88), color=cols[k - 1], lw=1.5)
    tx = X[-1] + 0.85
    ax.text(tx, 0.75, 'Mỗi ô dưới nhận đúng\nmột mũi tên: phép\n"nhân 3" chỉ xáo trộn\ncác số 1, 2, ..., 6.', fontsize=9.5, color='#404040', va='center')
    ax.text(tx, -0.75, 'Nhân cả hàng:\n3⁶ · 6! ≡ 6!  (mod 7)\n⇒  3⁶ ≡ 1  (mod 7)', fontsize=10, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-1.7, tx + 3.3); ax.set_ylim(-1.65, 1.65)
    save(f, 'f10_hoanvi')

# ======================= Bài 11: HÀM PHI EULER
def f11_luoi():
    f, ax = fig(7.6, 5.0)
    N = 12; s = 0.42
    for n in range(1, N + 1):
        y = -n * s
        ax.text(-0.3, y, str(n), ha='right', va='center', fontsize=10, color=NAVY, fontweight='bold')
        c = 0
        for k in range(1, n + 1):
            ok = gcd(k, n) == 1; c += ok
            ax.add_patch(Rectangle(((k - 1) * s, y - s / 2), s, s, fc=BLU if ok else GRY, ec='white' if ok else '#C8C8C8', lw=1.2))
            if ok: ax.text((k - 0.5) * s, y, str(k), ha='center', va='center', fontsize=8, color=NAVY, fontweight='bold')
        ax.text(n * s + 0.18, y, f'φ = {c}', ha='left', va='center', fontsize=9.5, color=RED, fontweight='bold')
    for k in range(1, N + 1):
        ax.text((k - 0.5) * s, -0.05, str(k), ha='center', va='bottom', fontsize=9, color=AMBER, fontweight='bold')
    ax.text(N * s / 2, 0.42, 'k', ha='center', fontsize=11, color=AMBER, fontweight='bold', style='italic')
    ax.text(-0.95, -N * s / 2, 'n', ha='center', va='center', fontsize=11, color=NAVY, fontweight='bold', style='italic')
    lx = 3.0; ly = 0.55
    ax.add_patch(Rectangle((lx + 0.2, ly - 1.25), 0.3, 0.3, fc=BLU, ec='white'))
    ax.text(lx + 0.6, ly - 1.1, 'gcd(k, n) = 1', fontsize=9.5, va='center')
    ax.add_patch(Rectangle((lx + 0.2, ly - 1.75), 0.3, 0.3, fc=GRY, ec='#C8C8C8'))
    ax.text(lx + 0.6, ly - 1.6, 'gcd(k, n) > 1', fontsize=9.5, va='center')
    ax.set_xlim(-1.2, N * s + 1.3); ax.set_ylim(-N * s - 0.35, 0.7)
    save(f, 'f11_luoi')

def f11_gach():
    f, ax = fig(8.4, 3.9)
    s = 0.62
    for v in range(1, 37):
        i, j = (v - 1) // 6, (v - 1) % 6
        x, y = j * s, -i * s
        if v % 2 == 0: fc, ec, col = GRY, '#B0B0B0', '#8C8C8C'
        elif v % 3 == 0: fc, ec, col = '#F4C7D9', PINK, '#7A2A50'
        else: fc, ec, col = YEL, RED, TXT
        ax.add_patch(Rectangle((x, y - s), s, s, fc=fc, ec=ec, lw=1.2))
        ax.text(x + s / 2, y - s / 2, str(v), ha='center', va='center', fontsize=10.5, color=col, fontweight='bold')
        if v % 2 == 0: ax.plot([x + 0.08, x + s - 0.08], [y - s + 0.08, y - 0.08], color='#7F7F7F', lw=1.1)
        elif v % 3 == 0: ax.plot([x + 0.08, x + s - 0.08], [y - 0.08, y - s + 0.08], color=PINK, lw=1.1)
    tx = 6 * s + 0.5
    rows = [(GRY, '#B0B0B0', 'bội của 2: bỏ 1/2 số → còn 18'), ('#F4C7D9', PINK, 'bội của 3 (lẻ): bỏ 1/3 số còn lại → còn 12'),
            (YEL, RED, 'còn lại: nguyên tố cùng nhau với 36')]
    for t, (fc, ec, txt) in enumerate(rows):
        y = -0.45 - 0.62 * t
        ax.add_patch(Rectangle((tx, y - 0.17), 0.34, 0.34, fc=fc, ec=ec, lw=1.2))
        ax.text(tx + 0.5, y, txt, va='center', fontsize=9.5)
    ax.text(tx, -2.75, 'φ(36) = 36 · (1 − 1/2) · (1 − 1/3) = 12', fontsize=11.5, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-0.1, tx + 5.6); ax.set_ylim(-6 * s - 0.1, 0.1)
    save(f, 'f11_gach')

def f11_phanso():
    from fractions import Fraction
    f, ax = fig(8.6, 3.4)
    ds = [1, 2, 3, 4, 6, 12]
    groups = {d: [Fraction(k, 12) for k in range(1, 13) if Fraction(k, 12).denominator == d] for d in ds}
    X = [0, 1.45, 2.9, 4.35, 5.8, 7.25]
    for d, x in zip(ds, X):
        fr = groups[d]
        ax.text(x, 0.55, f'mẫu {d}', ha='center', fontsize=10, color=NAVY, fontweight='bold')
        for t, q in enumerate(fr):
            cellbox(ax, x, -0.1 - 0.62 * t, f'{q.numerator}/{q.denominator}', fc=BLU if d != 12 else YEL, ec=NAVY if d != 12 else RED,
                    w=1.05, h=0.5, fs=11)
        ax.text(x, -2.85, f'φ({d}) = {len(fr)}', ha='center', fontsize=10, color=RED, fontweight='bold')
    ax.text(3.6, -3.4, 'Tổng: 1 + 1 + 2 + 2 + 2 + 4 = 12', ha='center', fontsize=11, color=RED, fontweight='bold')
    ax.set_xlim(-0.7, 8.0); ax.set_ylim(-3.7, 0.9)
    save(f, 'f11_phanso')

# ======================= Bài 12: ĐỊNH LÍ SỐ DƯ TRUNG HOA
def crt_table(ax, m1, m2, x0, y0, s=0.62, title='', hl=None, cop=False):
    ax.text(x0 + (m2 + 1) * s / 2, y0 + 0.95, title, ha='center', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(x0 + (m2 + 2) * s / 2, y0 + 0.45, f'x mod {m2}', ha='center', fontsize=9, color=AMBER, fontweight='bold')
    ax.text(x0 - 0.12, y0 - (m1 + 1) * s / 2 - 0.05, f'x mod {m1}', ha='right', va='center', fontsize=9, color=AMBER, fontweight='bold', rotation=90)
    for j in range(m2): cellbox(ax, x0 + (j + 1.5) * s, y0, j, fc='#E8EEF7', ec=NAVY, w=s, h=s, fs=10, lw=1)
    for i in range(m1): cellbox(ax, x0 + s / 2, y0 - (i + 1) * s, i, fc='#E8EEF7', ec=NAVY, w=s, h=s, fs=10, lw=1)
    cell = {}
    for x in range(m1 * m2 // gcd(m1, m2)): cell[(x % m1, x % m2)] = x
    for i in range(m1):
        for j in range(m2):
            v = cell.get((i, j))
            if v is None: fc, ec, t = GRY, '#C8C8C8', ''
            elif v == hl: fc, ec, t = YEL, RED, v
            elif cop and (i == 0 or j == 0): fc, ec, t = GRY, '#C8C8C8', v
            else: fc, ec, t = BLU if not cop else YEL, NAVY if not cop else RED, v
            cellbox(ax, x0 + (j + 1.5) * s, y0 - (i + 1) * s, t, fc=fc, ec=ec, w=s, h=s, fs=10.5, lw=1,
                    color=TXT if not (cop and (i == 0 or j == 0)) else '#7F7F7F')

def f12_bang():
    f, ax = fig(8.6, 3.9)
    crt_table(ax, 3, 5, 0, 0, title='m₁ = 3, m₂ = 5 (nguyên tố cùng nhau)', hl=8)
    crt_table(ax, 4, 6, 5.0, 0, title='m₁ = 4, m₂ = 6 (gcd = 2)')
    ax.text(1.85, -2.95, 'Đủ 15 ô, mỗi ô đúng một số x\ntrong 0..14. Ví dụ ô (2, 3): x = 8.', ha='center', fontsize=9.5, color='#404040', va='top')
    ax.text(7.2, -2.95, 'Chỉ 12 trên 24 ô có số; ô xám (như\nx mod 4 = 1, x mod 6 = 2) vô nghiệm.', ha='center', fontsize=9.5, color='#404040', va='top')
    ax.set_xlim(-0.6, 9.5); ax.set_ylim(-3.75, 1.2)
    save(f, 'f12_bang')

def f12_nhay():
    f, ax = fig(8.8, 2.7)
    y = 0
    xs = list(range(2, 24, 3))
    numline(ax, 0, 24, y, major=5, fs=9, labels=set(xs))
    for a, b in zip(xs, xs[1:]): jump(ax, a, b, y, color=NAVY, label='+3', fs=8.5)
    for x in xs:
        ok5, ok7 = x % 5 == 3, x % 7 == 2
        good = ok5 and ok7
        ax.plot([x], [y], 'o', ms=8, mfc=YEL if good else BLU, mec=RED if good else NAVY, mew=1.6, zorder=6)
        ax.text(x, y - 1.4, f'{x % 5}', ha='center', va='center', fontsize=9.5, color=GREEN if ok5 else '#8C8C8C', fontweight='bold')
        ax.text(x, y - 2.3, f'{x % 7}', ha='center', va='center', fontsize=9.5, color=GREEN if ok7 else '#8C8C8C', fontweight='bold')
    ax.text(-1.0, y - 1.4, 'x mod 5 (cần 3)', ha='right', va='center', fontsize=9.5, color=NAVY)
    ax.text(-1.0, y - 2.3, 'x mod 7 (cần 2)', ha='right', va='center', fontsize=9.5, color=NAVY)
    ax.text(-1.0, y - 0.55, 'x', ha='right', va='center', fontsize=9.5, color=NAVY, style='italic')
    ax.add_patch(Rectangle((21.9, y - 2.65), 2.2, 2.95, fc='none', ec=RED, lw=1.4, ls=(0, (3, 2))))
    ax.text(24.4, y - 1.0, 'x = 23\nthỏa cả ba', ha='left', va='center', fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-8.6, 28.6); ax.set_ylim(-2.8, 1.25)
    save(f, 'f12_nhay')

def f12_canchi():
    f, ax = fig(8.6, 3.9)
    can = 'Giáp Ất Bính Đinh Mậu Kỷ Canh Tân Nhâm Quý'.split()
    chi = 'Tý Sửu Dần Mão Thìn Tỵ Ngọ Mùi Thân Dậu Tuất Hợi'.split()
    def wheel(cx, names, cur, title, R):
        n = len(names)
        ax.add_patch(Circle((cx, 0), R + 0.42, fc='#F3F6FA', ec=NAVY, lw=1.8))
        ax.text(cx, 0.12, title, ha='center', va='center', fontsize=12, color=NAVY, fontweight='bold')
        ax.text(cx, -0.3, f'chu kì {n}', ha='center', va='center', fontsize=9.5, color='#404040')
        for k, nm in enumerate(names):
            ang = math.pi / 2 - 2 * math.pi * k / n
            p = (cx + R * math.cos(ang), R * math.sin(ang))
            st = 'cur' if k == cur else 'done'
            node(ax, p, k, st, r=0.24, fs=9.5, lw=1.8)
            q = (cx + (R + 0.72) * math.cos(ang), (R + 0.6) * math.sin(ang))
            ax.text(q[0], q[1], nm, ha='center', va='center', fontsize=9, color=RED if k == cur else '#404040',
                    fontweight='bold' if k == cur else 'normal')
    wheel(0, can, 2, 'Can', 1.25)
    wheel(4.6, chi, 6, 'Chi', 1.38)
    tx = 7.3
    ax.text(tx, 1.0, 'Năm 2026:', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(tx, 0.45, '(2026 − 4) mod 10 = 2', fontsize=10, color='#404040')
    ax.text(tx, 0.0, '(2026 − 4) mod 12 = 6', fontsize=10, color='#404040')
    ax.text(tx, -0.55, '⇒ Bính Ngọ', fontsize=12, color=RED, fontweight='bold')
    ax.set_xlim(-2.2, 10.3); ax.set_ylim(-2.25, 2.25)
    save(f, 'f12_canchi')

def f12_phi():
    f, ax = fig(7.6, 2.9)
    crt_table(ax, 3, 5, 0, 0, title='x = 0..14 xếp theo (x mod 3, x mod 5)', cop=True)
    ax.text(4.3, -0.7, 'x nguyên tố cùng nhau với 15\n⇔ x mod 3 ≠ 0 và x mod 5 ≠ 0', fontsize=10, color=NAVY, va='center')
    ax.text(4.3, -1.75, 'Ô vàng: 2 hàng × 4 cột = 8 ô\nφ(15) = φ(3) · φ(5) = 2 · 4 = 8', fontsize=10, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-0.6, 8.6); ax.set_ylim(-2.7, 1.25)
    save(f, 'f12_phi')

f9_cay(); f9_bit()
f10_bangnhan(); f10_hoanvi()
f11_luoi(); f11_gach(); f11_phanso()
f12_bang(); f12_nhay(); f12_canchi(); f12_phi()

from flow import flow
flow('f9_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc a, b, m'), ('proc', 'r ← 1 mod m;  i ← 1'), ('loop', 'i ≤ b ?'),
                    ('proc', 'r ← r · a mod m\ni ← i + 1'), ('end', ''), ('io', 'In r'), ('term', 'Kết thúc')])
flow('f9_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc a, b, m'), ('proc', 'r ← 1 mod m;  a ← a mod m'), ('loop', 'b > 0 ?'),
                  ('dec', 'b lẻ ?', ('r ← r · a mod m', 'proc')), ('proc', 'a ← a · a mod m\nb ← ⌊b / 2⌋'), ('end', ''),
                  ('io', 'In r'), ('term', 'Kết thúc')])
flow('f10_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc Q, p'), ('loop', 'còn truy vấn\n(a, b) ?'),
                     ('proc', 'thử x = 1, 2, ..., p − 1\ntới khi b · x mod p = 1'), ('io', 'In a · x mod p'), ('end', ''),
                     ('term', 'Kết thúc')])
flow('f10_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc Q, p'), ('loop', 'còn truy vấn\n(a, b) ?'),
                   ('proc', 'x ← bᵖ⁻² mod p\n(lũy thừa nhanh)'), ('io', 'In a · x mod p'), ('end', ''),
                   ('term', 'Kết thúc')])
flow('f11_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc n'), ('proc', 'cnt ← 0;  k ← 1'), ('loop', 'k ≤ n ?'),
                     ('dec', 'gcd(k, n) = 1 ?', ('cnt ← cnt + 1', 'proc')), ('proc', 'k ← k + 1'), ('end', ''),
                     ('io', 'In cnt'), ('term', 'Kết thúc')])
flow('f11_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc n'), ('proc', 'res ← n;  p ← 2'), ('loop', 'p · p ≤ n ?'),
                   ('dec', 'p | n ?', ('chia n cho p tới hết\nres ← res − res / p', 'proc')), ('proc', 'p ← p + 1'), ('end', ''),
                   ('dec', 'n > 1 ?', ('res ← res − res / n', 'proc')), ('io', 'In res'), ('term', 'Kết thúc')])
flow('f12_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc k và các (aᵢ, mᵢ)'), ('proc', 'L ← lcm(m₁, ..., mₖ)\nx ← a₁'),
                     ('loop', 'x < L ?'), ('dec', 'x thỏa mọi\nphương trình?', ('In x, dừng', 'term')), ('proc', 'x ← x + m₁'),
                     ('end', ''), ('io', 'In −1'), ('term', 'Kết thúc')])
flow('f12_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc k'), ('proc', 'r ← 0;  M ← 1'), ('loop', 'còn phương trình\nx ≡ a (mod m)?'),
                   ('proc', 'g ← gcd(M, m)'), ('dec', 'g ∤ (a − r) ?', ('In −1, dừng', 'term')),
                   ('proc', 't ← (a − r)/g · (M/g)⁻¹\n(lấy theo mod m/g)\nr ← r + M · t\nM ← M · (m/g)'), ('end', ''),
                   ('io', 'In r'), ('term', 'Kết thúc')])
