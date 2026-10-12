# Hình Chương 1 (Tập 2)
from shlib import *
import math

def ngaythu():
    f, ax = fig(8.0, 3.7)
    names = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ nhật']
    R = 1.55
    P = []
    for k in range(7):
        a = math.pi / 2 - 2 * math.pi * k / 7; P.append((R * math.cos(a), R * math.sin(a)))
    ax.add_patch(Circle((0, 0), R, fc='#F3F6FA', ec='#B4C6E7', lw=1.5))
    for k in range(7):
        st = 'src' if k == 0 else ('ans' if k in (5, 6) else 'done')
        node(ax, P[k], k + 2 if k < 6 else 'CN', st, r=0.33, fs=12)
        a = math.pi / 2 - 2 * math.pi * k / 7
        ax.text((R + 1.05) * math.cos(a), (R + 0.72) * math.sin(a), names[k], ha='center', va='center', fontsize=9.5, color=TXT)
    ax.text(0, 0.18, 'thứ = (d + k) mod 7', ha='center', fontsize=10.5, color=NAVY, fontweight='bold')
    ax.text(0, -0.3, '(thứ Hai: d = 0)', ha='center', fontsize=9, color='#404040')
    tx = 3.4
    ax.text(tx, 1.3, 'Hôm nay: thứ Hai (d = 0)', fontsize=11, color=PURPLE, fontweight='bold')
    ax.text(tx, 0.65, 'k = 1000:  1000 mod 7 = 6  →  Chủ nhật', fontsize=11, color=RED)
    ax.text(tx, 0.05, 'k = −100:  (−100) mod 7 = 5  →  thứ Bảy', fontsize=11, color=RED)
    ax.text(tx, -0.6, 'Trong C++: −100 % 7 = −2 (âm!)\nphải cộng thêm 7 rồi lấy dư lần nữa', fontsize=10, color='#404040', va='top')
    ax.set_xlim(-3.0, 9.6); ax.set_ylim(-2.5, 2.5); save(f, 'ngaythu')

def chusocuoi():
    f, ax = fig(8.2, 4.4)
    B = 8
    ax.text(-0.9, 0.42, 'a mod 10', ha='center', fontsize=10, color=NAVY, fontweight='bold')
    ax.text(B / 2 * 0.72 + 0.1, 0.95, 'chữ số tận cùng của a$^{b}$, với b = 1, 2, ..., 8', ha='center', fontsize=10.5, color=NAVY, fontweight='bold')
    for b in range(1, B + 1):
        ax.text(b * 0.72, 0.42, str(b), ha='center', fontsize=10, color=RED if b % 4 == 0 else NAVY, fontweight='bold')
    for a in range(10):
        y = -a * 0.48
        ax.text(-0.9, y, str(a), ha='center', va='center', fontsize=11, color=NAVY, fontweight='bold')
        seq = [pow(a, b, 10) for b in range(1, B + 1)]
        per = next(p for p in (1, 2, 4) if all(seq[i] == seq[i + p] for i in range(B - p)))
        for b in range(1, B + 1):
            first = b <= per
            cellbox(ax, b * 0.72, y, seq[b - 1], fc='#FFD966' if first else '#EEF3FA', ec=RED if first else '#B4C6E7', w=0.62, h=0.42, fs=10, bold=first)
        ax.text(B * 0.72 + 0.65, y, f'chu kì {per}', va='center', fontsize=9, color=GREEN if per < 4 else AMBER)
    ax.text(B * 0.72 + 2.5, -1.8, 'Mọi chu kì đều là\nước của 4:\nchỉ cần biết\nb mod 4', fontsize=10.5, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-1.5, B * 0.72 + 4.2); ax.set_ylim(-4.7, 1.25); save(f, 'chusocuoi')

def vietlien():
    f, ax = fig(9.6, 2.7)
    n, m = 12, 1000; r = 0; x = 0
    ax.text(-0.5, 0.95, 'viết thêm', ha='right', va='center', fontsize=9.5, color=AMBER, fontweight='bold')
    ax.text(-0.5, -0.15, 'r', ha='right', va='center', fontsize=12, color=RED, fontweight='bold', style='italic')
    for i in range(1, n + 1):
        w = 0.78 if i < 10 else 0.95
        p = 10 if i < 10 else 100
        r = (r * p + i) % m
        cellbox(ax, x + w / 2, 0.95, i, fc='#FFE7B3', ec=AMBER, w=w - 0.06, h=0.5, fs=11)
        cellbox(ax, x + w / 2, -0.15, r, fc='#FFD966' if i == n else '#BDD7EE', ec=RED if i == n else NAVY, w=w - 0.06, h=0.5, fs=9.5 if r >= 100 else 10.5)
        ax.text(x + w / 2, -0.62, f'·{p}', ha='center', va='top', fontsize=8, color=GREEN if p == 100 else '#606060', fontweight='bold' if p == 100 else 'normal')
        x += w
    ax.text(x + 0.25, -0.15, '= 123456789101112 mod 1000', va='center', fontsize=10.5, color=RED, fontweight='bold')
    ax.text(x - 1.45, 1.4, 'từ 10 trở đi: nhân 100', va='center', ha='center', fontsize=9, color=GREEN, fontweight='bold')
    ax.set_xlim(-1.6, x + 4.7); ax.set_ylim(-1.0, 1.65); save(f, 'vietlien')


# ---------- Bài 2
def dots(ax, x0, y0, rows, cols, s=0.3, st='done', r=0.1):
    for i in range(rows):
        for j in range(cols):
            fc, ec = STY[st]
            ax.add_patch(Circle((x0 + j * s, y0 - i * s), r, fc=fc, ec=ec, lw=1.3, zorder=4))

def xephang():
    f, ax = fig(8.6, 3.6)
    s = 0.3; x = 0
    for (rr, c) in [(2, 6), (3, 4), (4, 3), (6, 2)]:
        w = (c - 1) * s; best = (rr, c) == (3, 4)
        if best:
            ax.add_patch(FancyBboxPatch((x - 0.22, -(rr - 1) * s - 0.22), w + 0.44, (rr - 1) * s + 0.44, boxstyle='round,pad=0.04',
                                        fc='#FFF2CC', ec=RED, lw=1.8, zorder=2))
        dots(ax, x, 0, rr, c, s, 'cur' if best else 'done')
        ax.text(x + w / 2, -1.95, f'{rr} hàng × {c}', ha='center', fontsize=10, color=RED if best else NAVY, fontweight='bold')
        if best: ax.text(x + w / 2, 0.55, 'cân đối nhất', ha='center', fontsize=9.5, color=RED, fontweight='bold')
        x += max(w, 1.0) + 1.0
    # các cách bị loại
    y = -2.75
    dots(ax, 0, y, 1, 12, s, 'gray')
    ax.text(12 * s + 0.1, y, '1 hàng × 12 (và 12 hàng × 1): không được tính', va='center', fontsize=10, color='#707070')
    tx = x + 0.2
    ax.text(tx, 0.25, 'n = 12', fontsize=12, color=NAVY, fontweight='bold')
    ax.text(tx, -0.35, 'ước: 1, 2, 3, 4, 6, 12', fontsize=10.5, color=TXT)
    ax.text(tx, -0.95, 'd(12) − 2 = 4 cách', fontsize=10.5, color=RED, fontweight='bold')
    ax.text(tx, -1.55, 'cân đối nhất: 3 × 4\n(3 = ước lớn nhất ≤ √12)', fontsize=10, color=TXT, va='top')
    ax.set_xlim(-0.4, tx + 3.4); ax.set_ylim(-3.1, 0.95); save(f, 'xephang')

def uoctang():
    f, ax = fig(8.6, 3.4)
    n = 36; lo = [d for d in range(1, 7) if n % d == 0]; hi = [n // d for d in lo if d * d != n]
    w = 0.78
    ax.text(-0.6, 1.9, 'd ≤ √36: d', ha='right', va='center', fontsize=10, color=NAVY, fontweight='bold')
    ax.text(-0.6, 1.1, 'n / d', ha='right', va='center', fontsize=10, color=AMBER, fontweight='bold')
    for i, d in enumerate(lo):
        cellbox(ax, i * w, 1.9, d, fc='#BDD7EE', ec=NAVY, w=w - 0.08, h=0.55, fs=11)
    for i, d in enumerate(hi):
        cellbox(ax, i * w, 1.1, d, fc='#FFE7B3', ec=AMBER, w=w - 0.08, h=0.55, fs=11)
    cellbox(ax, 4 * w, 1.1, '', fc='#F4F4F4', ec='#C0C0C0', w=w - 0.08, h=0.55, fs=11, lw=1.0)
    ax.text(5.2 * w, 1.9, 'tăng dần →', va='center', fontsize=9.5, color=NAVY)
    ax.text(5.2 * w, 1.1, '← giảm dần  (36 / 6 = 6 trùng với d: bỏ)', va='center', fontsize=9.5, color=AMBER)
    dv = lo + hi[::-1]
    ax.text(-0.6, -0.2, 'dãy ước', ha='right', va='center', fontsize=10, color=TXT, fontweight='bold')
    for i, d in enumerate(dv):
        hl = d == 12
        cellbox(ax, i * w, -0.2, d, fc='#FFD966' if hl else ('#BDD7EE' if i < len(lo) else '#FFE7B3'), ec=RED if hl else (NAVY if i < len(lo) else AMBER),
                w=w - 0.08, h=0.55, fs=11)
    ax.annotate('', xy=(6 * w, 0.15), xytext=(3 * w, 0.78), arrowprops=dict(arrowstyle='-|>', color=AMBER, lw=1.5, connectionstyle='arc3,rad=0.25'))
    ax.text(6.0 * w + 0.15, 0.55, 'đảo ngược rồi nối vào sau', fontsize=9, color=AMBER)
    ax.annotate('', xy=(6 * w, -0.52), xytext=(6 * w, -1.15), arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.6))
    ax.text(6 * w, -1.38, 'x = 10: ước nhỏ nhất ≥ 10 là 12 (tìm kiếm nhị phân)', ha='center', fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-2.0, 9 * w + 1.6); ax.set_ylim(-1.6, 2.3); save(f, 'uoctang')

def banbe():
    f, ax = fig(8.6, 5.4)
    node(ax, (0, 2.9), 220, 'cur', r=0.45, fs=13); node(ax, (6.4, 2.9), 284, 'cur', r=0.45, fs=13)
    edge(ax, (0, 2.9), (6.4, 2.9), color=NAVY, directed=True, rad=-0.18, r=0.47)
    edge(ax, (6.4, 2.9), (0, 2.9), color=GREEN, directed=True, rad=-0.18, r=0.47)
    ax.text(3.2, 3.75, 's(220) = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284', ha='center', fontsize=10, color=NAVY, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none'))
    ax.text(3.2, 2.05, 's(284) = 1 + 2 + 4 + 71 + 142 = 220', ha='center', fontsize=10, color=GREEN, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none'))
    # sàng điều hòa với N = 12
    N = 12; w = 0.5; x0 = 0.9; y0 = 1.3
    ax.text(x0 - 0.45, y0, 'm', ha='right', va='center', fontsize=10, color=NAVY, fontweight='bold', style='italic')
    for m in range(1, N + 1):
        ax.text(x0 + (m - 1) * w, y0, str(m), ha='center', va='center', fontsize=10, color=NAVY, fontweight='bold')
    for d in range(1, N // 2 + 1):
        y = y0 - d * 0.42
        ax.text(x0 - 0.45, y, f'd = {d}', ha='right', va='center', fontsize=9.5, color=TXT)
        for m in range(1, N + 1):
            on = m % d == 0 and m > d; h3 = on and d == 3
            cellbox(ax, x0 + (m - 1) * w, y, d if on else '', fc='#FFE7B3' if h3 else ('#BDD7EE' if on else '#F4F4F4'),
                    ec=AMBER if h3 else (NAVY if on else '#D0D0D0'), w=w - 0.06, h=0.36, fs=9, lw=1.0)
    y = y0 - (N // 2 + 1) * 0.42 - 0.05
    ax.text(x0 - 0.45, y, 's(m)', ha='right', va='center', fontsize=10, color=RED, fontweight='bold')
    for m in range(1, N + 1):
        sm = sum(d for d in range(1, m) if m % d == 0)
        cellbox(ax, x0 + (m - 1) * w, y, sm, fc='#FFD966', ec=RED, w=w - 0.06, h=0.38, fs=9.5)
    tx = x0 + N * w + 0.2
    ax.text(tx, y0 - 0.75, 'Mỗi d cộng vào\n2d, 3d, 4d, ...', fontsize=10, color=TXT, va='center')
    ax.text(tx, y0 - 1.26, 'd = 3: ô 6, 9, 12', fontsize=10, color=AMBER, fontweight='bold', va='center')
    ax.text(tx, y0 - 2.3, 'Tổng số phép cộng\n≈ N · ln N', fontsize=10, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-0.9, 7.6); ax.set_ylim(y - 0.4, 4.0); save(f, 'banbe')

# ---------- Bài 3
def catgach():
    from math import gcd
    f, ax = fig(8.6, 3.0)
    a, b = 252, 105; g = gcd(a, b); k = 0.025
    for i in range(a // g):
        for j in range(b // g):
            hl = (i, j) == (0, b // g - 1)
            ax.add_patch(Rectangle((i * g * k, j * g * k), g * k, g * k, fc='#FFD966' if hl else ('#BDD7EE' if (i + j) % 2 == 0 else '#DDEBF7'),
                                   ec=RED if hl else NAVY, lw=1.8 if hl else 0.9, zorder=3 if hl else 2))
    ax.add_patch(Rectangle((0, 0), a * k, b * k, fc='none', ec=NAVY, lw=2.2, zorder=4))
    ax.text(a * k / 2, -0.25, 'a = 252  (252 / 21 = 12 miếng)', ha='center', va='top', fontsize=10, color=NAVY, fontweight='bold')
    ax.text(-0.2, b * k / 2, 'b = 105\n(5 miếng)', ha='right', va='center', fontsize=10, color=NAVY, fontweight='bold')
    ax.annotate('cạnh 21', xy=(g * k / 2, b * k - g * k / 2), xytext=(g * k / 2 + 0.6, b * k + 0.45), fontsize=10, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.3))
    tx = a * k + 0.5
    ax.text(tx, 2.1, 'g = gcd(252, 105) = 21', fontsize=11, color=RED, fontweight='bold')
    ax.text(tx, 1.5, 'số miếng = (a / g) · (b / g)', fontsize=10.5, color=TXT)
    ax.text(tx, 1.0, '= 12 · 5 = 60', fontsize=10.5, color=TXT)
    ax.text(tx, 0.25, 'a, b ≤ 10$^{18}$, g = 1:\nsố miếng tới 10$^{36}$!', fontsize=10, color=AMBER, fontweight='bold', va='center')
    ax.set_xlim(-1.6, tx + 3.6); ax.set_ylim(-0.75, b * k + 0.75); save(f, 'catgach')

def bomotso():
    from math import gcd
    f, ax = fig(8.4, 3.4)
    a = [12, 18, 7, 24, 30]; n = len(a)
    L = [0] * (n + 2); R = [0] * (n + 2)
    for i in range(1, n + 1): L[i] = gcd(L[i - 1], a[i - 1])
    for i in range(n, 0, -1): R[i] = gcd(R[i + 1], a[i - 1])
    res = [gcd(L[i - 1], R[i + 1]) for i in range(1, n + 1)]
    w = 0.95; rows = [('i', list(range(1, n + 1))), ('a[i]', a), ('L[i]', L[1:n + 1]), ('R[i]', R[1:n + 1]), ('bỏ a[i]', res)]
    ys = [2.2, 1.55, 0.75, -0.0, -0.95]
    for (lab, vals), y in zip(rows, ys):
        ax.text(-0.75, y, lab, ha='right', va='center', fontsize=10.5, color=RED if lab == 'bỏ a[i]' else NAVY, fontweight='bold')
        for i, v in enumerate(vals):
            if lab == 'i': ax.text(i * w, y, v, ha='center', va='center', fontsize=10, color='#606060'); continue
            st = dict(fc='#FFE7B3', ec=AMBER) if lab == 'a[i]' else dict(fc='#BDD7EE', ec=NAVY)
            if lab == 'a[i]' and i == 2: st = dict(fc='#EDEDED', ec='#9A9A9A')
            if lab == 'L[i]' and i == 1: st = dict(fc='#CDEBC5', ec=GREEN)
            if lab == 'R[i]' and i == 3: st = dict(fc='#CDEBC5', ec=GREEN)
            if lab == 'bỏ a[i]': st = dict(fc='#FFD966', ec=RED) if i == 2 else dict(fc='#F4F4F4', ec='#B0B0B0')
            cellbox(ax, i * w, y, v, w=w - 0.1, h=0.52, fs=11, **st)
    ax.annotate('', xy=(2 * w - 0.15, -0.72), xytext=(1 * w + 0.1, 0.48), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.6))
    ax.annotate('', xy=(2 * w + 0.15, -0.72), xytext=(3 * w - 0.1, -0.27), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.6))
    tx = n * w + 0.1
    ax.text(tx, 1.55, 'L[i] = gcd(a[1..i])   (tiền tố)', fontsize=10, color=TXT, va='center')
    ax.text(tx, 1.0, 'R[i] = gcd(a[i..n])   (hậu tố)', fontsize=10, color=TXT, va='center')
    ax.text(tx, 0.2, 'Bỏ a[3] = 7:\ngcd(L[2], R[4]) = gcd(6, 6) = 6', fontsize=10.5, color=RED, fontweight='bold', va='center')
    ax.text(tx, -0.95, 'kết quả: 6, bỏ phần tử thứ 3', fontsize=10, color=RED, va='center')
    ax.set_xlim(-1.9, tx + 4.4); ax.set_ylim(-1.35, 2.5); save(f, 'bomotso')

def dennhay():
    f, ax = fig(8.8, 3.9)
    t = [2, 3, 4]; T = 12; w = 0.42
    for x in range(1, T + 1):
        ax.text(x * w, 1.95, str(x), ha='center', va='center', fontsize=9.5, color=RED if x == T else '#505050', fontweight='bold' if x == T else 'normal')
    ax.add_patch(Rectangle((T * w - w / 2, 0.05), w, 1.75, fc='#FFF2CC', ec=RED, lw=1.6, zorder=1))
    for k, ti in enumerate(t):
        y = 1.45 - k * 0.6
        ax.text(0.0, y, f'đèn {k + 1} (t = {ti})', ha='right', va='center', fontsize=10, color=NAVY, fontweight='bold')
        ax.plot([0.5 * w, T * w + 0.4 * w], [y, y], color=LGRAY, lw=1.2, zorder=2)
        for x in range(ti, T + 1, ti):
            st = 'cur' if x == T else 'done'
            node(ax, (x * w, y), '', st, r=0.13, lw=1.6)
    ax.text(T * w / 2 - 0.3, -0.35, 'lần đầu cả ba đèn cùng nháy: lcm(2, 3, 4) = 12', ha='center', fontsize=10.5, color=RED, fontweight='bold')
    # bảng các giá trị khác nhau của lcm(t[l..r]) khi r = 4
    x0 = T * w + 2.3; tt = [2, 3, 4, 5]; ww = 0.72
    ax.text(x0 + 1.5 * ww, 1.95, 'r = 4, l giảm dần', ha='center', va='center', fontsize=10, color=NAVY, fontweight='bold')
    from math import lcm
    for l in range(4, 0, -1):
        xx = x0 + (4 - l) * ww
        ax.text(xx, 1.45, f'l = {l}', ha='center', va='center', fontsize=9.5, color='#505050')
        cellbox(ax, xx, 0.95, tt[l - 1], fc='#FFE7B3', ec=AMBER, w=ww - 0.08, h=0.46, fs=10.5)
        v = lcm(*tt[l - 1:4])
        cellbox(ax, xx, 0.25, v, fc='#BDD7EE' if l > 2 else '#FFD966', ec=NAVY if l > 2 else RED, w=ww - 0.08, h=0.46, fs=10.5)
    ax.text(x0 - 0.45, 0.95, 't', ha='right', va='center', fontsize=10, color=AMBER, fontweight='bold', style='italic')
    ax.text(x0 - 0.45, 0.25, 'lcm', ha='right', va='center', fontsize=10, color=NAVY, fontweight='bold')
    ax.text(x0 + 1.5 * ww, -0.35, 'chỉ 3 giá trị khác nhau: 5, 20, 60', ha='center', va='center', fontsize=10, color=TXT)
    ax.text(x0 + 1.5 * ww, -0.8, 'mỗi lần đổi: gấp ít nhất 2 lần', ha='center', va='center', fontsize=9.5, color=RED, fontweight='bold')
    ax.set_xlim(-2.2, x0 + 3 * ww + 1.0); ax.set_ylim(-1.05, 2.2); save(f, 'dennhay')

# ---------- Bài 4
def dongnuoc():
    f, ax = fig(8.6, 2.9)
    lo, hi = -4, 12
    numline(ax, lo, hi, y=0, labels=list(range(lo, hi + 1)), fs=9.5)
    for x in range(lo, hi + 1):
        if x % 2 == 0: node(ax, (x, 0), '', 'cur' if x == 2 else 'done', r=0.17, lw=1.6)
    ax.plot([7], [0], marker='x', ms=11, mew=2.5, color=GRAY, zorder=6)
    ax.text(7, -0.95, '7: không đong được', ha='center', fontsize=9.5, color='#707070')
    jump(ax, 0, 6, label='+6', color=NAVY, fs=10)
    jump(ax, 6, 2, color=GREEN)
    ax.text(4, 0.5, '−4', ha='center', fontsize=10, color=GREEN, fontweight='bold')
    ax.text(2, -0.95, '2 = 6 − 4', ha='center', fontsize=9.5, color=RED, fontweight='bold')
    ax.text(lo - 0.6, 2.45, 'Can 6 lít và can 4 lít: mọi lượng đong được đều là bội của gcd(6, 4) = 2', fontsize=10.5, color=NAVY, fontweight='bold')
    ax.set_xlim(lo - 0.8, hi + 1.0); ax.set_ylim(-1.2, 2.7); save(f, 'dongnuoc')

def muahang():
    f, ax = fig(8.0, 4.4)
    s = 0.36; X0, X1, Y0, Y1 = -5, 15, -3, 9
    ax.add_patch(Rectangle((0, 0), (X1 + 0.5) * s, (Y1 + 0.5) * s, fc='#EAF5E6', ec='none', zorder=0))
    for x in range(X0, X1 + 1):
        for y in range(Y0, Y1 + 1):
            ax.plot(x * s, y * s, '.', color='#C8C8C8', ms=2.5, zorder=1)
    ax.annotate('', xy=((X1 + 0.8) * s, 0), xytext=((X0 - 0.5) * s, 0), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.4))
    ax.annotate('', xy=(0, (Y1 + 0.8) * s), xytext=(0, (Y0 - 0.5) * s), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.4))
    ax.text((X1 + 0.9) * s, -0.3, 'x', fontsize=11, color=TXT, style='italic'); ax.text(0.15, (Y1 + 0.8) * s, 'y', fontsize=11, color=TXT, style='italic')
    xs = [X0 - 0.3, X1 + 0.3]
    ax.plot([x * s for x in xs], [(30 - 3 * x) / 5 * s for x in xs], color=NAVY, lw=1.6, zorder=2)
    for x in range(-5, 16, 5):
        y = (30 - 3 * x) // 5; ok = x >= 0 and y >= 0
        node(ax, (x * s, y * s), '', 'cur' if ok else 'gray', r=0.14, lw=1.6)
        ax.text(x * s + 0.2, y * s + 0.22, f'({x}, {y})', fontsize=9.5, color=RED if ok else '#808080', fontweight='bold' if ok else 'normal')
    ax.text(6 * s, 7.6 * s, '3x + 5y = 30', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(9.5 * s, 4.6 * s, 'x ≥ 0, y ≥ 0', fontsize=10, color=GREEN, fontweight='bold')
    ax.text((X1 + 1.6) * s, 6 * s, 'Các nghiệm cách đều:\nmỗi bước x tăng 5,\ny giảm 3.', fontsize=10, color=TXT, va='center')
    ax.text((X1 + 1.6) * s, 2.5 * s, 'Chỉ đếm các nghiệm\ntrong góc phần tư\nx ≥ 0, y ≥ 0: 3 cách', fontsize=10, color=RED, fontweight='bold', va='center')
    ax.set_xlim((X0 - 0.8) * s, (X1 + 9.5) * s); ax.set_ylim((Y0 - 0.8) * s, (Y1 + 1.2) * s); save(f, 'muahang')

def dongho():
    f, ax = fig(8.8, 3.8)
    m = 12; R = 1.5; p, a, q, b = 0, 5, 3, 2
    ax.add_patch(Circle((0, 0), R, fc='#F3F6FA', ec='#B4C6E7', lw=1.5))
    P = lambda k, rr=R: (rr * math.sin(2 * math.pi * k / m), rr * math.cos(2 * math.pi * k / m))
    for k in range(m):
        st = 'cur' if k == 5 else ('src' if k == 0 else ('amber' if k == 3 else 'w'))
        node(ax, P(k), k, st, r=0.24, fs=9.5, lw=1.6)
    ax.annotate('', xy=P(5, R - 0.3), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=PURPLE, lw=5, mutation_scale=16))
    ax.annotate('', xy=P(5, R - 0.62), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=AMBER, lw=2.2))
    ax.text(0, 0.35, 'tím: kim A\ncam: kim B', ha='center', fontsize=9, color='#505050')
    ax.text(0, -R - 0.55, 't = 1: cả hai kim ở nấc 5', ha='center', fontsize=10, color=RED, fontweight='bold')
    # bảng vị trí
    x0 = 2.9; w = 0.5; T = 10
    ax.text(x0 - 0.3, 1.3, 't', ha='right', va='center', fontsize=10, color='#505050', fontweight='bold')
    ax.text(x0 - 0.3, 0.65, 'kim A', ha='right', va='center', fontsize=10, color=PURPLE, fontweight='bold')
    ax.text(x0 - 0.3, 0.05, 'kim B', ha='right', va='center', fontsize=10, color=AMBER, fontweight='bold')
    for t in range(T + 1):
        A, B = (p + a * t) % m, (q + b * t) % m; hit = A == B; xx = x0 + 0.1 + t * w
        ax.text(xx, 1.3, str(t), ha='center', va='center', fontsize=9.5, color=RED if hit else '#505050', fontweight='bold' if hit else 'normal')
        cellbox(ax, xx, 0.65, A, fc='#FFD966' if hit else '#DCCCEC', ec=RED if hit else PURPLE, w=w - 0.06, h=0.46, fs=9.5, lw=1.2)
        cellbox(ax, xx, 0.05, B, fc='#FFD966' if hit else '#FFE7B3', ec=RED if hit else AMBER, w=w - 0.06, h=0.46, fs=9.5, lw=1.2)
    ax.text(x0, -0.75, 'A: 0 + 5t,  B: 3 + 2t  (mod 12)   ⇒   3t ≡ 3 (mod 12)', fontsize=10, color=NAVY, fontweight='bold')
    ax.text(x0, -1.3, 'gặp nhau khi t = 1, 5, 9, ... (cách nhau 12 / gcd(3, 12) = 4)', fontsize=10, color=RED)
    ax.set_xlim(-R - 0.4, x0 + 0.1 + T * w + 0.5); ax.set_ylim(-R - 0.8, R + 0.4); save(f, 'dongho')

ngaythu(); chusocuoi(); vietlien()
xephang(); uoctang(); banbe()
catgach(); bomotso(); dennhay()
dongnuoc(); muahang(); dongho()
