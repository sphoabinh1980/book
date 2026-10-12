# Hình Chương 2. SỐ NGUYÊN TỐ
from shlib import *
import math

# màu ô theo quy ước của sách
C_CUR = ('#FFD966', RED)      # đang xét / kết quả
C_DONE = ('#BDD7EE', NAVY)    # đã xong (số nguyên tố đã chắc chắn)
C_IN = ('#FFE7B3', AMBER)     # dữ liệu vào
C_GRAY = ('#EDEDED', '#9A9A9A')
C_NEW = ('#F8CBAD', RED)      # vừa bị gạch ở lượt này
C_GREEN = ('#CDEBC5', GREEN)


def primes_upto(n):
    s = [True] * (n + 1); s[0] = False
    if n >= 1: s[1] = False
    for i in range(2, math.isqrt(n) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i): s[j] = False
    return s


def spf(x):
    d = 2
    while x % d: d += 1
    return d


def slash(ax, x, y, w, h, color=RED, lw=1.4, z=6):
    ax.plot([x - w / 2 + 0.08, x + w / 2 - 0.08], [y - h / 2 + 0.08, y + h / 2 - 0.08], color=color, lw=lw, zorder=z)


# ================= Bài 5
def f5_capuoc():
    f, ax = fig(7.2, 3.4)
    n = 36; y = 1.6; sx = 0.42
    X = lambda v: v * sx
    ax.plot([X(0.4), X(37)], [y, y], color=GRAY, lw=1.6, zorder=1)
    for v in range(1, 37):
        ax.plot([X(v), X(v)], [y - 0.07, y + 0.07], color=GRAY, lw=1, zorder=1)
    divs = [d for d in range(1, 37) if n % d == 0]
    cols = [NAVY, TEAL, PURPLE, GREEN]
    hs = [1.55, 1.15, 0.8, 0.48]
    for k, d in enumerate([1, 2, 3, 4]):
        e = n // d; c = cols[k]; h = hs[k]
        mid = (X(d) + X(e)) / 2; w = X(e) - X(d)
        ax.add_patch(Arc((mid, y), w, 2 * h, theta1=0, theta2=180, color=c, lw=1.8, zorder=2))
        if k == 0: ax.text(mid, y + h + 0.05, f'{d} · {e}', ha='center', va='bottom', fontsize=10, color=c, fontweight='bold', zorder=5)
        else: ax.text(X(e) + 0.1, y + 0.3, f'{d} · {e}', ha='left', va='center', fontsize=10, color=c, fontweight='bold', zorder=5,
                      bbox=dict(boxstyle='round,pad=0.05', fc='white', ec='none'))
    for d in divs:
        st = C_CUR if d == 6 else (C_DONE if d < 6 else C_IN)
        ax.add_patch(Circle((X(d), y), 0.2, fc=st[0], ec=st[1], lw=1.6, zorder=4))
        ax.text(X(d), y - 0.33, str(d), ha='center', va='top', fontsize=10, color=TXT, fontweight='bold')
    ax.plot([X(6), X(6)], [y - 0.75, y + 1.75], color=RED, lw=1.5, ls=(0, (4, 3)), zorder=3)
    ax.text(X(6) - 0.12, y + 1.62, '√36 = 6', fontsize=10.5, color=RED, fontweight='bold', ha='right', va='center',
            bbox=dict(boxstyle='round,pad=0.1', fc='white', ec='none'), zorder=6)
    ax.text(X(3.5), y - 0.78, 'ước nhỏ: d ≤ 6', fontsize=9.5, color=NAVY, ha='center', va='top')
    ax.text(X(22), y - 0.78, 'ước lớn: 36 / d ≥ 6  (cặp đôi của một ước nhỏ)', fontsize=9.5, color=AMBER, ha='center', va='top')
    ax.text(X(0.3), y + 2.3, 'n = 36: các ước đi thành cặp (d, 36 / d), "soi gương" qua √36', fontsize=11, color=NAVY, fontweight='bold', ha='left')
    y2 = -0.9
    ax.text(X(0.3), y2 + 0.62, 'n = 97: chỉ cần thử d = 2, 3, ..., 9  (vì 10 · 10 > 97)', fontsize=11, color=NAVY, fontweight='bold', ha='left')
    for i, d in enumerate(range(2, 10)):
        x = X(1.5) + i * 1.0
        cellbox(ax, x, y2, d, fc=C_IN[0], ec=C_IN[1], w=0.8, h=0.5, fs=11)
        ax.text(x, y2 - 0.4, f'dư {97 % d}', ha='center', va='top', fontsize=9.5, color='#404040')
    ax.text(X(1.5) + 8 * 1.0 - 0.2, y2, '⇒  không có ước nào ≤ 9,\n     nên 97 là số nguyên tố', fontsize=10.5, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-0.1, X(37.5)); ax.set_ylim(y2 - 0.85, y + 2.6)
    save(f, 'f5_capuoc')


def f5_6k():
    f, ax = fig(5.6, 4.3)
    P = primes_upto(60); s = 0.62; hs = 0.5; dx = 1.0
    heads = ['6k + 1', '6k + 2', '6k + 3', '6k + 4', '6k + 5', '6k + 6']
    why = ['', 'bội\ncủa 2', 'bội\ncủa 3', 'bội\ncủa 2', '', 'bội\ncủa 6']
    for j in range(6):
        x = j * dx
        good = j in (0, 4)
        ax.text(x, 0.48, heads[j], ha='center', va='center', fontsize=9, fontweight='bold', color=RED if good else '#606060')
        if not good:
            ax.text(x, -8 * hs - 0.12, why[j], ha='center', va='top', fontsize=8.8, color='#606060')
        else:
            ax.add_patch(FancyBboxPatch((x - 0.44, -8 * hs - 0.1), 0.88, 8 * hs + 0.36, boxstyle='round,pad=0,rounding_size=0.1', fc='none', ec=RED, lw=1.8, zorder=5))
        for i in range(8):
            v = 6 * i + j + 1; y = -i * hs - 0.05
            if P[v]: fc, ec = C_CUR
            elif good: fc, ec = '#FFFFFF', NAVY
            else: fc, ec = C_GRAY
            cellbox(ax, x, y, v, fc=fc, ec=ec, w=s, h=hs * 0.86, fs=10.5, color=TXT if (good or P[v]) else '#8A8A8A')
    ax.text(6 * dx - 0.3, -1.2, 'Số nguyên tố\n(ô vàng) lớn hơn 3\nchỉ nằm ở hai cột\n6k + 1 và 6k + 5\n(tức 6k − 1).', fontsize=9.5, color=NAVY, va='top')
    ax.set_xlim(-0.5, 6 * dx + 1.9); ax.set_ylim(-8 * hs - 0.75, 0.75)
    save(f, 'f5_6k')


def f5_mr():
    f, ax = fig(7.4, 2.3)
    st = 1.7
    def row(y, title, vals, labs, flag):
        ax.text(-0.3, y + 0.55, title, fontsize=10.5, color=NAVY, fontweight='bold', ha='left')
        for i, (v, lb) in enumerate(zip(vals, labs)):
            x = 0.6 + i * st
            fc, ec = flag(i, v)
            cellbox(ax, x, y, v, fc=fc, ec=ec, w=0.95, h=0.5, fs=11)
            ax.text(x, y - 0.33, lb, ha='center', va='top', fontsize=9, color='#404040')
            if i:
                ax.annotate('', xy=(x - 0.52, y), xytext=(x - st + 0.52, y), arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=1.4))
                ax.text(x - st / 2, y + 0.05, '( )²', ha='center', va='bottom', fontsize=8.5, color=NAVY)
    row(0, 'n = 561 = 3 · 11 · 17, a = 2, 560 = 35 · 2⁴  (mũi tên: bình phương rồi lấy dư cho n)', [263, 166, 67, 1, 1], ['2³⁵', '2⁷⁰', '2¹⁴⁰', '2²⁸⁰', '2⁵⁶⁰'],
        lambda i, v: C_NEW if i == 2 else (C_GRAY if v == 1 else ('#FFFFFF', NAVY)))
    ax.text(0.6 + 5 * st - 0.6, 0, '67² ≡ 1 mà 67 ≢ ±1:\n561 là hợp số', fontsize=10, color=RED, fontweight='bold', va='center')
    row(-1.75, 'n = 97, a = 2, 96 = 3 · 2⁵', [8, 64, 22, 96, 1, 1], ['2³', '2⁶', '2¹²', '2²⁴', '2⁴⁸', '2⁹⁶'],
        lambda i, v: C_CUR if i == 3 else (C_GRAY if v == 1 else ('#FFFFFF', NAVY)))
    ax.text(0.6 + 6 * st - 0.6, -1.75, '96 ≡ −1:\nqua kiểm tra', fontsize=10, color=GREEN, fontweight='bold', va='center')
    ax.set_xlim(-0.4, 0.6 + 6 * st + 1.6); ax.set_ylim(-2.4, 0.85)
    save(f, 'f5_mr')


def sieve_panel(ax, x0, y0, upto_p, title, final=False, s=1.0):
    """Lưới 1..100 sau khi đã xử lí xong các số nguyên tố ≤ upto_p."""
    plist = [p for p in (2, 3, 5, 7) if p <= upto_p]
    crossed_by = {}
    for p in plist:
        for j in range(p * p, 101, p):
            crossed_by.setdefault(j, p)
    for v in range(1, 101):
        i, j = (v - 1) // 10, (v - 1) % 10
        x, y = x0 + j * s + s / 2, y0 - i * s - s / 2
        cb = crossed_by.get(v)
        tcol = TXT
        if v == 1: fc, ec = C_GRAY; tcol = '#8A8A8A'
        elif cb is not None and cb == upto_p and not final: fc, ec = C_NEW
        elif cb is not None: fc, ec = C_GRAY; tcol = '#8A8A8A'
        elif v == upto_p and not final: fc, ec = C_CUR
        elif v in plist or final: fc, ec = C_DONE
        else: fc, ec = '#FFFFFF', '#A0A0A0'
        ax.add_patch(Rectangle((x - s / 2, y - s / 2), s, s, fc=fc, ec='#A0A0A0', lw=0.8, zorder=2))
        if fc == C_CUR[0]:
            ax.add_patch(Rectangle((x - s / 2 + 0.04, y - s / 2 + 0.04), s - 0.08, s - 0.08, fc='none', ec=RED, lw=1.8, zorder=3))
        ax.text(x, y, str(v), ha='center', va='center', fontsize=9 if v == 100 else 9.5, color=tcol,
                fontweight='bold' if (fc in (C_DONE[0], C_CUR[0])) else 'normal', zorder=4)
        if cb is not None and cb == upto_p and not final:
            slash(ax, x, y, s, s, color=RED, lw=1.1, z=5)
    ax.add_patch(Rectangle((x0, y0 - 10 * s), 10 * s, 10 * s, fc='none', ec=NAVY, lw=1.8, zorder=6))
    ax.text(x0 + 5 * s, y0 + 0.75, title, ha='center', va='center', fontsize=10, color=NAVY, fontweight='bold', linespacing=1.2)


def legend_cells(ax, pos, items, fs=9.5):
    for ((fc, ec), text, sl), (x, y) in zip(items, pos):
        ax.add_patch(Rectangle((x, y - 0.3), 0.6, 0.6, fc=fc, ec=ec, lw=1.4))
        if sl: slash(ax, x + 0.3, y, 0.6, 0.6, color=RED, lw=1.1)
        ax.text(x + 0.8, y, text, va='center', fontsize=fs, color=TXT)


def f6_luoi1():
    f, ax = fig(6.6, 3.9)
    sieve_panel(ax, 0, 0, 2, 'Lượt p = 2\ngạch 4, 6, 8, ..., 100')
    sieve_panel(ax, 11.2, 0, 3, 'Lượt p = 3\ngạch 9, 12, 15, ..., 99')
    legend_cells(ax, [(0.2, -10.8), (11.4, -10.8), (0.2, -11.7), (11.4, -11.7)],
                 [(C_CUR, 'số nguyên tố p đang xét', False), (C_NEW, 'vừa bị gạch ở lượt này', True),
                  (C_GRAY, 'đã bị gạch từ lượt trước', False), (C_DONE, 'số nguyên tố đã chắc chắn', False)], fs=9.5)
    ax.set_xlim(-0.2, 21.4); ax.set_ylim(-12.2, 1.6)
    save(f, 'f6_luoi1')


def f6_luoi2():
    f, ax = fig(6.6, 3.9)
    sieve_panel(ax, 0, 0, 5, 'Lượt p = 5\ngạch 25, 30, 35, ..., 100')
    sieve_panel(ax, 11.2, 0, 7, 'Lượt p = 7\ngạch 49, 56, 63, ..., 98')
    ax.set_xlim(-0.2, 21.4); ax.set_ylim(-10.3, 1.6)
    save(f, 'f6_luoi2')


def f6_ketqua():
    f, ax = fig(3.4, 3.7)
    sieve_panel(ax, 0, 0, 7, '11 · 11 > 100: dừng\ncòn lại 25 số nguyên tố', final=True)
    ax.set_xlim(-0.2, 10.2); ax.set_ylim(-10.2, 1.6)
    save(f, 'f6_ketqua')


def f6_p2():
    f, ax = fig(7.0, 2.1)
    vals = [(k, 7 * k) for k in range(2, 10)]
    for i, (k, v) in enumerate(vals):
        x = i * 1.25
        if k < 7:
            q = spf(k)
            cellbox(ax, x, 0, v, fc=C_GRAY[0], ec=C_GRAY[1], w=1.0, h=0.62, fs=12, color='#7A7A7A')
            slash(ax, x, 0, 1.0, 0.62, color='#7A7A7A', lw=1.2)
            ax.text(x, -0.42, f'7 · {k}', ha='center', va='top', fontsize=10, color='#404040')
            ax.text(x, -0.78, f'đã gạch ở\nlượt {q}', ha='center', va='top', fontsize=9, color=GRAY)
        else:
            fc, ec = C_CUR if k == 7 else C_NEW
            cellbox(ax, x, 0, v, fc=fc, ec=ec, w=1.0, h=0.62, fs=12)
            ax.text(x, -0.42, f'7 · {k}', ha='center', va='top', fontsize=10, color='#404040')
    x7 = 5 * 1.25
    ax.annotate('bắt đầu gạch từ 7² = 49', xy=(x7, 0.38), xytext=(x7 + 1.0, 1.1), fontsize=10.5, color=RED, fontweight='bold', ha='center',
                arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.5))
    ax.text(1.25 * 2, 1.1, 'k < 7: k có ước nguyên tố nhỏ hơn 7', fontsize=10, color='#404040', ha='center')
    ax.set_xlim(-0.7, 7 * 1.25 + 0.7); ax.set_ylim(-1.55, 1.45)
    save(f, 'f6_p2')


def f6_tiento():
    f, ax = fig(7.0, 2.7)
    P = primes_upto(30); s = 0.62; c = 0
    for band in range(2):
        y0 = -band * 1.55
        ax.text(-0.45, y0, 'x', ha='right', va='center', fontsize=10.5, color=NAVY, fontweight='bold', style='italic')
        ax.text(-0.45, y0 - 0.5, 'c[x]', ha='right', va='center', fontsize=10.5, color=RED, fontweight='bold')
        for k in range(15):
            x = band * 15 + k + 1
            c += P[x]
            cx = k * s
            fc, ec = C_DONE if P[x] else ('#FFFFFF', '#A0A0A0')
            cellbox(ax, cx, y0, x, fc=fc, ec=ec, w=s, h=0.46, fs=10, lw=1.0, bold=bool(P[x]))
            hl = x in (9, 30)
            cellbox(ax, cx, y0 - 0.5, c, fc='#FFD966' if hl else '#FFFFFF', ec=RED if hl else '#A0A0A0', w=s, h=0.46, fs=10, lw=1.6 if hl else 1.0, bold=hl)
            if 10 <= x <= 30:
                ax.plot([cx - s / 2 + 0.03, cx + s / 2 - 0.03], [y0 + 0.31, y0 + 0.31], color=GREEN, lw=2.2)
    ax.text(15 * s + 0.2, 0.05, 'vạch xanh lá: truy vấn [10, 30]\ncó 6 số nguyên tố\n(11, 13, 17, 19, 23, 29)', fontsize=9.5, color=GREEN, fontweight='bold', va='center')
    ax.text(15 * s + 0.2, -1.8, 'đáp số = c[30] − c[9]\n          = 10 − 4 = 6', fontsize=10.5, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-1.5, 15 * s + 4.0); ax.set_ylim(-2.35, 0.55)
    save(f, 'f6_tiento')


def tree(ax, root, x0, y0, kids_of, sp=0.82, dy=0.95, r=0.36):
    """Vẽ cây phân tích; kids_of[key] = ((a, ka), (b, kb)) nếu tách thành a · b. Lá xếp cách đều."""
    pos = {}; cnt = [0]
    def place(key, depth):
        ch = kids_of.get(key)
        if ch is None:
            pos[key] = (x0 + cnt[0] * sp, y0 - depth * dy); cnt[0] += 1
        else:
            place(ch[0][1], depth + 1); place(ch[1][1], depth + 1)
            pos[key] = ((pos[ch[0][1]][0] + pos[ch[1][1]][0]) / 2, y0 - depth * dy)
    place('r', 0)
    def draw(v, key):
        ch = kids_of.get(key)
        node(ax, pos[key], v, 'cur' if ch is None else 'done', r=r, fs=11 if v < 100 else 9.5)
        if ch:
            for u, ku in ch:
                edge(ax, pos[key], pos[ku], r=r, lw=1.6)
                draw(u, ku)
    draw(root, 'r')


def f7_cay():
    f, ax = fig(6.8, 3.4)
    A = {'r': ((6, 'a'), (60, 'b')), 'a': ((2, 'a1'), (3, 'a2')), 'b': ((6, 'b1'), (10, 'b2')),
         'b1': ((2, 'x'), (3, 'y')), 'b2': ((2, 'z'), (5, 't'))}
    tree(ax, 360, 0.3, 0, A)
    B = {'r': ((8, 'a'), (45, 'b')), 'a': ((2, 'a1'), (4, 'a2')), 'a2': ((2, 'x'), (2, 'y')),
         'b': ((9, 'b1'), (5, 'b2')), 'b1': ((3, 'z'), (3, 't'))}
    tree(ax, 360, 6.6, 0, B)
    ax.text(2.35, 0.6, '360 = 6 · 60', ha='center', fontsize=10.5, color=NAVY, fontweight='bold')
    ax.text(8.65, 0.6, '360 = 8 · 45', ha='center', fontsize=10.5, color=NAVY, fontweight='bold')
    ax.text(5.5, -3.55, 'Hai cách tách khác nhau, cùng một bộ lá:  360 = 2³ · 3² · 5', ha='center', fontsize=11, color=RED, fontweight='bold')
    ax.set_xlim(-0.3, 11.2); ax.set_ylim(-3.9, 0.95)
    save(f, 'f7_cay')


def f7_spf():
    f, ax = fig(6.6, 2.5)
    st = {2: C_DONE, 3: C_GREEN, 5: C_IN}
    s = 0.62
    for v in range(2, 32):
        i, j = (v - 2) // 10, (v - 2) % 10
        x, y = j * s * 1.05, -i * 0.56
        p = spf(v)
        fc, ec = C_CUR if p == v else st.get(p, C_GRAY)
        cellbox(ax, x, y, v, fc=fc, ec=ec, w=s, h=0.46, fs=11)
    lx = 10 * s * 1.05 + 0.1
    items = [(C_CUR, 'số nguyên tố\n(spf là chính nó)'), (C_DONE, 'spf = 2'), (C_GREEN, 'spf = 3'), (C_IN, 'spf = 5')]
    for k, ((fc, ec), t) in enumerate(items):
        yy = 0.12 - k * 0.48 - (0.1 if k else 0)
        ax.add_patch(Rectangle((lx, yy - 0.15), 0.4, 0.3, fc=fc, ec=ec, lw=1.4))
        ax.text(lx + 0.55, yy, t, va='center', fontsize=9.5)
    ax.set_xlim(-0.4, lx + 2.4); ax.set_ylim(-1.75, 0.5)
    save(f, 'f7_spf')


def f7_nhay():
    f, ax = fig(7.2, 1.75)
    chain = [(360, 2), (180, 2), (90, 2), (45, 3), (15, 3), (5, 5), (1, None)]
    for i, (v, p) in enumerate(chain):
        x = i * 1.85
        fc, ec = C_IN if i == 0 else (C_GRAY if v == 1 else ('#FFFFFF', NAVY))
        cellbox(ax, x, 0, v, fc=fc, ec=ec, w=0.95, h=0.55, fs=12)
        if p:
            ax.annotate('', xy=(x + 1.85 - 0.5, 0), xytext=(x + 0.5, 0), arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=1.5))
            ax.text(x + 0.925, 0.1, f'÷ {p}', ha='center', va='bottom', fontsize=10, color=NAVY, fontweight='bold')
            node(ax, (x + 0.925, -0.6), p, 'cur', r=0.24, fs=10.5)
    ax.text(3 * 1.85, -1.25, 'các thừa số lần lượt rơi ra: 2, 2, 2, 3, 3, 5   ⇒   360 = 2³ · 3² · 5', ha='center', va='top', fontsize=10.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.6, 6 * 1.85 + 0.6); ax.set_ylim(-1.65, 0.6)
    save(f, 'f7_nhay')


# ================= Bài 8
def f8_cuaso():
    f, ax = fig(7.2, 1.9)
    y = 0
    ax.plot([0, 3.2], [y, y], color=GRAY, lw=1.8)
    ax.plot([3.6, 7.6], [y, y], color=GRAY, lw=1.8, ls=(0, (3, 3)))
    ax.plot([8.0, 11.6], [y, y], color=GRAY, lw=1.8)
    ax.annotate('', xy=(12.0, y), xytext=(11.5, y), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.8))
    for xx in (3.4, 7.8):
        ax.plot([xx - 0.12, xx + 0.08], [y - 0.18, y + 0.18], color=GRAY, lw=1.5)
    ax.add_patch(Rectangle((0.1, y - 0.22), 2.6, 0.44, fc=C_DONE[0], ec=NAVY, lw=1.6, zorder=3))
    ax.text(1.4, y, '2 .. √R', ha='center', va='center', fontsize=10.5, fontweight='bold', zorder=4)
    ax.text(1.4, y - 0.38, 'sàng thường\n(≤ 10⁶ số)', ha='center', va='top', fontsize=9.5, color=NAVY)
    ax.add_patch(Rectangle((8.6, y - 0.22), 2.4, 0.44, fc=C_CUR[0], ec=RED, lw=1.8, zorder=3))
    ax.text(9.8, y, '[L, R]', ha='center', va='center', fontsize=10.5, fontweight='bold', zorder=4)
    ax.text(9.8, y - 0.38, 'cửa sổ: R − L ≤ 10⁶\n(R tới 10¹²)', ha='center', va='top', fontsize=9.5, color=RED)
    ax.annotate('', xy=(9.0, y + 0.3), xytext=(1.6, y + 0.3), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.6, connectionstyle='arc3,rad=-0.1'))
    ax.text(5.3, y + 0.92, 'mỗi số nguyên tố p ≤ √R gạch các bội của nó nằm trong cửa sổ', ha='center', va='bottom', fontsize=10, color=GREEN, fontweight='bold')
    ax.text(5.6, y - 0.38, 'phần ở giữa: không lưu, không xét', ha='center', va='top', fontsize=9.5, color=GRAY)
    ax.set_xlim(-0.1, 12.2); ax.set_ylim(-1.15, 1.35)
    save(f, 'f8_cuaso')


def f8_doan():
    L, R = 100, 130
    f, ax = fig(7.4, 2.9)
    s = 0.36; h = 0.34; x0 = 1.9
    ps = [2, 3, 5, 7, 11]
    gone = set()
    for k in range(R - L + 1):
        ax.text(x0 + k * s, 0.05, str(L + k), rotation=90, ha='center', va='bottom', fontsize=8.6, color=TXT)
    for r, p in enumerate(ps):
        y = -0.3 - r * (h + 0.06)
        st = max(p * p, (L + p - 1) // p * p)
        ax.text(x0 - 0.35, y, f'p = {p}', ha='right', va='center', fontsize=9.5, color=NAVY, fontweight='bold')
        ax.text(x0 + (R - L) * s + 0.35, y, f'từ {st}', ha='left', va='center', fontsize=9, color=RED)
        for k in range(R - L + 1):
            v = L + k; x = x0 + k * s
            hit = v >= st and (v - st) % p == 0
            if hit:
                fc, ec = (C_CUR if v == st else C_NEW)
            elif v in gone: fc, ec = C_GRAY
            else: fc, ec = ('#FFFFFF', '#B0B0B0')
            ax.add_patch(Rectangle((x - s / 2, y - h / 2), s, h, fc=fc, ec='#A0A0A0', lw=0.6, zorder=2))
            if hit: slash(ax, x, y, s, h, color=RED, lw=1.0)
        for v in range(st, R + 1, p): gone.add(v)
    y = -0.3 - len(ps) * (h + 0.06) - 0.08
    ax.text(x0 - 0.35, y, 'còn lại', ha='right', va='center', fontsize=9.5, color=RED, fontweight='bold')
    for k in range(R - L + 1):
        v = L + k; x = x0 + k * s
        fc, ec = (C_GRAY if v in gone else C_DONE)
        ax.add_patch(Rectangle((x - s / 2, y - h / 2), s, h, fc=fc, ec='#A0A0A0', lw=0.6, zorder=2))
        if v not in gone:
            ax.add_patch(Rectangle((x - s / 2, y - h / 2), s, h, fc='none', ec=NAVY, lw=1.6, zorder=3))
    ax.text(x0 + (R - L) * s + 0.35, y, '6 số', ha='left', va='center', fontsize=9.5, color=NAVY, fontweight='bold')
    ax.set_xlim(0.6, x0 + (R - L) * s + 1.3); ax.set_ylim(y - 0.3, 1.3)
    save(f, 'f8_doan')


f5_capuoc(); f5_6k(); f5_mr()
f6_luoi1(); f6_luoi2(); f6_ketqua(); f6_p2(); f6_tiento()
f7_cay(); f7_spf(); f7_nhay()
f8_cuaso(); f8_doan()

from flow import flow
flow('f5_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc n'), ('dec', 'n < 2 ?', ('In NO, dừng', 'term')), ('proc', 'd ← 2'),
                    ('loop', 'd ≤ n − 1 ?'), ('dec', 'd | n ?', ('In NO, dừng', 'term')), ('proc', 'd ← d + 1'), ('end', ''),
                    ('io', 'In YES'), ('term', 'Kết thúc')])
flow('f5_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc n'), ('dec', 'n ≤ 3 hoặc\n2 | n hoặc 3 | n ?', ('trả lời ngay:\nYES khi n = 2, 3', 'term')),
                  ('proc', 'i ← 5'), ('loop', 'i · i ≤ n ?'), ('dec', 'i | n hoặc\n(i + 2) | n ?', ('In NO, dừng', 'term')),
                  ('proc', 'i ← i + 6'), ('end', ''), ('io', 'In YES'), ('term', 'Kết thúc')])
flow('f6_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc Q'), ('loop', 'còn truy vấn\n(a, b) ?'), ('proc', 'đếm ← 0'),
                    ('loop', 'còn x trong\n[a, b] ?'), ('proc', 'nếu laNT(x) (Bài 5)\nthì đếm ← đếm + 1'), ('end', ''),
                    ('io', 'In đếm'), ('end', ''), ('term', 'Kết thúc')])
flow('f6_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc mọi truy vấn,\nN ← max b'), ('proc', 'gạch[0] = gạch[1] = 1\np ← 2'),
                  ('loop', 'p · p ≤ N ?'), ('proc', 'nếu p chưa bị gạch:\ngạch p², p² + p, ... ≤ N'), ('proc', 'p ← p + 1'), ('end', ''),
                  ('proc', 'c[x] ← c[x − 1] + (x chưa gạch)'), ('io', 'Mỗi truy vấn:\nin c[b] − c[a − 1]'), ('term', 'Kết thúc')])
flow('f7_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc n'), ('proc', 'd ← 2'), ('loop', 'd · d ≤ n ?'),
                    ('proc', 'e ← 0; trong khi d | n:\nn ← n / d, e ← e + 1'), ('proc', 'nếu e > 0: in d^e'), ('proc', 'd ← d + 1'), ('end', ''),
                    ('dec', 'n > 1 ?', ('in n (là SNT)', 'io')), ('term', 'Kết thúc')])
flow('f7_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc mọi n, N ← max n'), ('proc', 'sàng spf[2..N]'), ('loop', 'còn số n ?'),
                  ('loop', 'n > 1 ?'), ('proc', 'p ← spf[n]; chia n cho p\ntới hết, đếm số mũ e'), ('io', 'in p^e'), ('end', ''),
                  ('end', ''), ('term', 'Kết thúc')])
flow('f8_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc L, R'), ('proc', 'x ← L'), ('loop', 'x ≤ R ?'),
                    ('proc', 'nếu laNT(x) (thử tới √x)\nthì ghi nhận x'), ('proc', 'x ← x + 1'), ('end', ''),
                    ('io', 'In số lượng và danh sách'), ('term', 'Kết thúc')])
flow('f8_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc L, R'), ('proc', 'sàng thường: mọi SNT p ≤ √R'), ('proc', 'gạch[0..R − L] ← 0'),
                  ('loop', 'còn SNT\np ≤ √R ?'), ('proc', 'j ← max(p², ⌈L / p⌉ · p)\ngạch j, j + p, ... ≤ R'), ('end', ''),
                  ('dec', 'L = 1 ?', ('gạch ô của số 1', 'proc')), ('io', 'In các x chưa bị gạch'), ('term', 'Kết thúc')])
