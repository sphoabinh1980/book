# Hình Chương 1. CHIA HẾT VÀ ƯỚC SỐ
from shlib import *
import math

# ---------------- Bài 1
def f_trucso():
    f, ax = plt.subplots(figsize=(8.6, 4.6)); ax.set_aspect('equal'); ax.axis('off')
    def remainder(x0, x1, y):
        yy = y - 0.98
        ax.plot([x0, x1], [yy, yy], color=RED, lw=3, solid_capstyle='butt', zorder=4)
        for x in (x0, x1): ax.plot([x, x], [yy - 0.12, yy + 0.12], color=RED, lw=2, zorder=4)
        ax.text((x0 + x1) / 2, yy - 0.2, 'r = 2', ha='center', va='top', fontsize=10.5, color=RED, fontweight='bold')
        ax.plot([x1], [y], 'o', ms=9, mfc='#FFD966', mec=RED, mew=2, zorder=6)
    # a = 17, b = 5
    y = 3.0
    numline(ax, 0, 19, y, major=5)
    for k in range(3): jump(ax, 5 * k, 5 * k + 5, y, color=NAVY, label='+5')
    remainder(15, 17, y)
    ax.text(-1.2, y + 2.15, 'a = 17, b = 5:   17 = 5 · 3 + 2   (q = 3, r = 2)', fontsize=11, color=NAVY, fontweight='bold', ha='left')
    # a = -7, b = 3
    y = -1.2
    numline(ax, -10, 2, y, major=3)
    for k in range(3): jump(ax, -3 * k, -3 * k - 3, y, color=NAVY, label='−3')
    remainder(-9, -7, y)
    ax.text(-11.2, y + 1.75, 'a = −7, b = 3:   −7 = 3 · (−3) + 2   (q = −3, r = 2)', fontsize=11, color=NAVY, fontweight='bold', ha='left')
    ax.text(4.2, y - 0.1, 'Đi tới bội số của b gần nhất\nKHÔNG VƯỢT QUÁ a (bên trái a),\nrồi bước sang phải một đoạn r ≥ 0', fontsize=9.5, color='#404040', va='center')
    ax.set_xlim(-11.5, 20.5); ax.set_ylim(-2.9, 5.6)
    save(f, 'f1_trucso')

def f_dongho():
    f, ax = fig(7.6, 3.9)
    R = 1.55; cx, cy = 0, 0
    ax.add_patch(Circle((cx, cy), R, fc='#F3F6FA', ec=NAVY, lw=2.2))
    groups = {0: '0, 7, 14, 21', 1: '1, 8, 15', 2: '2, 9, 16', 3: '3, 10, 17\n−4, −11', 4: '4, 11, 18', 5: '5, 12, 19', 6: '6, 13, 20\n−1, −8'}
    for k in range(7):
        ang = math.pi / 2 - 2 * math.pi * k / 7
        p = (cx + R * math.cos(ang), cy + R * math.sin(ang))
        node(ax, p, k, 'cur' if k == 3 else 'done', r=0.3, fs=14)
        q = (cx + (R + 0.95) * math.cos(ang), cy + (R + 0.75) * math.sin(ang))
        ax.text(q[0], q[1], groups[k], ha='center', va='center', fontsize=9, color=RED if k == 3 else '#404040', fontweight='bold' if k == 3 else 'normal')
    ax.text(cx, cy + 0.15, 'mod 7', ha='center', va='center', fontsize=15, color=NAVY, fontweight='bold')
    ax.text(cx, cy - 0.35, '(7 "ngăn")', ha='center', va='center', fontsize=10, color='#404040')
    tx = 3.7
    ax.text(tx, 1.2, '17 ≡ 3 (mod 7)', fontsize=13, color=RED, fontweight='bold')
    ax.text(tx, 0.7, '10 ≡ 3 (mod 7)', fontsize=13, color=RED, fontweight='bold')
    ax.text(tx, 0.2, '−4 ≡ 3 (mod 7)', fontsize=13, color=RED, fontweight='bold')
    ax.text(tx, -0.55, 'Cùng rơi vào ngăn 3:\nhiệu của chúng chia hết cho 7\n(17 − 10 = 7, 17 − (−4) = 21)', fontsize=10, color='#404040', va='top')
    ax.set_xlim(-3.0, 7.4); ax.set_ylim(-2.7, 2.7)
    save(f, 'f1_dongho')

def f_horner():
    f, ax = fig(8.4, 2.9)
    digs = '2026'; m = 7; r = 0; xs = []
    ax.text(-0.9, 1.25, 'Chữ số', fontsize=10.5, color=NAVY, fontweight='bold', ha='right', va='center')
    ax.text(-0.9, -0.55, 'r', fontsize=12, color=RED, fontweight='bold', ha='right', va='center', style='italic')
    cellbox(ax, 0, -0.55, 0, fc='#EDEDED', ec='#9A9A9A')
    ax.text(0, -1.05, 'ban đầu', ha='center', va='top', fontsize=8.5, color='#404040')
    for i, c in enumerate(digs):
        x = 2.3 * (i + 1)
        cellbox(ax, x - 1.15, 1.25, c, fc='#FFE7B3', ec=AMBER)
        nr = (r * 10 + int(c)) % m
        cellbox(ax, x, -0.55, nr, fc='#FFD966' if i == len(digs) - 1 else '#BDD7EE', ec=RED if i == len(digs) - 1 else NAVY)
        ax.annotate('', xy=(x - 0.48, -0.55), xytext=(x - 2.3 + 0.48, -0.55), arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=1.6))
        ax.annotate('', xy=(x - 0.95, -0.33), xytext=(x - 1.15, 0.88), arrowprops=dict(arrowstyle='-|>', color=AMBER, lw=1.4))
        ax.text(x, -1.05, f'({r}·10 + {c})\nmod 7', ha='center', va='top', fontsize=8.5, color='#404040')
        r = nr
    ax.text(2.3 * 4 + 0.7, -0.55, '= 2026 mod 7', fontsize=11, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-2.2, 12.6); ax.set_ylim(-1.9, 1.8)
    save(f, 'f1_horner')

f_trucso(); f_dongho(); f_horner()

from flow import flow
flow('f1_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc xâu s và m'), ('proc', 'N ← 0'), ('loop', 'còn chữ số c\ntrong s?'), ('proc', 'N ← N · 10 + c\n(N dài dần: tràn số!)'), ('end', ''), ('io', 'In N mod m'), ('term', 'Kết thúc')])
flow('f1_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc xâu s và m'), ('proc', 'r ← 0'), ('loop', 'còn chữ số c\ntrong s?'), ('proc', 'r ← (r · 10 + c) mod m\n(luôn có 0 ≤ r < m)'), ('end', ''), ('io', 'In r'), ('term', 'Kết thúc')])

# ---------------- Bài 2
def f_hcn():
    f, ax = fig(8.2, 2.9)
    x0 = 0
    for (w, h), lab in zip([(12, 1), (6, 2), (4, 3)], ['1 × 12', '2 × 6', '3 × 4']):
        for i in range(w):
            for j in range(h):
                ax.add_patch(Rectangle((x0 + i * 0.42, j * 0.42), 0.42, 0.42, fc='#BDD7EE', ec=NAVY, lw=1.0))
        ax.text(x0 + w * 0.21, h * 0.42 + 0.25, lab, ha='center', fontsize=12, color=RED, fontweight='bold')
        x0 += w * 0.42 + 0.9
    ax.text(x0 - 0.2, 0.55, 'Mỗi cặp ước (d, 12 / d)\n= một hình chữ nhật\ngồm 12 ô vuông', fontsize=10, color='#404040', va='center')
    ax.set_xlim(-0.3, x0 + 3.6); ax.set_ylim(-0.3, 1.9)
    save(f, 'f2_hcn')

def f_capuoc():
    f, ax = fig(8.4, 2.9)
    ds = [1, 2, 3, 4, 6, 9, 12, 18, 36]
    xs = {d: i * 1.0 for i, d in enumerate(ds)}
    for d in ds:
        st = 'cur' if d == 6 else ('done' if d < 6 else 'amber')
        node(ax, (xs[d], 0), d, st, r=0.33, fs=12)
    for d in ds:
        e = 36 // d
        if d < e:
            mid = (xs[d] + xs[e]) / 2; span = xs[e] - xs[d]
            ax.add_patch(Arc((mid, 0.35), span, span * 0.42, theta1=0, theta2=180, color=NAVY, lw=1.6))
            ax.text(mid, 0.35 + span * 0.21 + 0.08, f'{d} · {e}', ha='center', fontsize=9, color=NAVY, fontweight='bold')
    ax.plot([xs[6], xs[6]], [-0.55, -1.0], color=RED, lw=1.6, ls='--')
    ax.text(xs[6], -1.25, '√36 = 6', ha='center', fontsize=11, color=RED, fontweight='bold')
    ax.text(xs[2], -0.8, 'd ≤ √n  (tìm bằng vòng lặp)', ha='center', fontsize=10, color=NAVY)
    ax.text(xs[12] + 0.5, -0.8, 'n / d ≥ √n  (suy ra, không cần tìm)', ha='center', fontsize=10, color=AMBER)
    ax.set_xlim(-0.6, 8.6); ax.set_ylim(-1.5, 2.4)
    save(f, 'f2_capuoc')

# ---------------- Bài 3
def f_euclid():
    f, ax = fig(8.2, 3.6)
    s = 0.03; a, b = 252, 105
    ax.add_patch(Rectangle((0, 0), a * s, b * s, fc='white', ec=NAVY, lw=2))
    cols = ['#BDD7EE', '#FFE7B3', '#FFD966']; x = 0; y = 0; W_, H_ = a, b; k = 0
    # các hình vuông: 2 hình 105, rồi 2 hình 42 (dựng đứng), rồi 2 hình 21
    sq = [(0, 0, 105), (105, 0, 105), (210, 0, 42), (210, 42, 42), (210, 84, 21), (231, 84, 21)]
    fc = ['#BDD7EE', '#BDD7EE', '#FFE7B3', '#FFE7B3', '#FFD966', '#FFD966']
    ec = [NAVY, NAVY, AMBER, AMBER, RED, RED]
    for (x, y, t), c, e in zip(sq, fc, ec):
        ax.add_patch(Rectangle((x * s, y * s), t * s, t * s, fc=c, ec=e, lw=1.8))
        ax.text((x + t / 2) * s, (y + t / 2) * s, str(t), ha='center', va='center', fontsize=12 if t > 30 else 9, color=TXT, fontweight='bold')
    ax.text(a * s / 2, -0.35, '252', ha='center', va='top', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(-0.25, b * s / 2, '105', ha='right', va='center', fontsize=11, color=NAVY, fontweight='bold')
    tx = a * s + 0.6
    for i, t in enumerate(['252 = 2 · 105 + 42', '105 = 2 · 42 + 21', '  42 = 2 · 21 + 0']):
        ax.text(tx, 2.6 - i * 0.62, t, fontsize=12, color=[NAVY, AMBER, RED][i], fontweight='bold', family='DejaVu Sans Mono')
    ax.text(tx, 0.45, 'Hình vuông nhỏ nhất (21 × 21)\nlát kín cả hình chữ nhật:\ngcd(252, 105) = 21', fontsize=10.5, color=RED, va='center')
    ax.set_xlim(-0.9, tx + 4.6); ax.set_ylim(-0.8, 3.4)
    save(f, 'f3_euclid')

def f_ucchung():
    f, ax = fig(7.4, 3.3)
    from matplotlib.patches import Ellipse
    ax.add_patch(Ellipse((0, 0), 5.4, 3.4, fc='#BDD7EE', ec=NAVY, lw=2, alpha=0.55))
    ax.add_patch(Ellipse((2.9, 0), 4.2, 3.0, fc='#FFE7B3', ec=AMBER, lw=2, alpha=0.6))
    ax.text(-1.9, 1.85, 'Ước của 252', fontsize=11, color=NAVY, fontweight='bold', ha='center')
    ax.text(4.0, 1.7, 'Ước của 105', fontsize=11, color=AMBER, fontweight='bold', ha='center')
    left = ['2', '4', '6', '9', '12', '14', '18', '28', '36', '42', '63', '84', '126', '252']
    for i, t in enumerate(left):
        ax.text(-2.15 + (i % 4) * 0.62, 0.9 - (i // 4) * 0.55, t, ha='center', va='center', fontsize=9.5, color=TXT)
    for i, t in enumerate(['1', '3', '7', '21']):
        ax.text(1.45, 0.85 - i * 0.55, t, ha='center', va='center', fontsize=12, color=RED, fontweight='bold')
    for i, t in enumerate(['5', '15', '35', '105']):
        ax.text(3.6 + (i % 2) * 0.7, 0.4 - (i // 2) * 0.7, t, ha='center', va='center', fontsize=9.5, color=TXT)
    ax.text(1.45, -1.95, 'ước chung lớn nhất: 21', ha='center', fontsize=11, color=RED, fontweight='bold')
    ax.set_xlim(-2.9, 5.2); ax.set_ylim(-2.3, 2.2)
    save(f, 'f3_ucchung')

# ---------------- Bài 4
def f_nghiem():
    f, ax = plt.subplots(figsize=(7.6, 4.2)); ax.set_aspect('equal')
    xs = range(-8, 13); ys = range(-6, 7)
    for x in xs: ax.plot([x, x], [-6, 6], color='#E3E8F0', lw=0.8, zorder=0)
    for y in ys: ax.plot([-8, 12], [y, y], color='#E3E8F0', lw=0.8, zorder=0)
    ax.axhline(0, color=GRAY, lw=1.2); ax.axvline(0, color=GRAY, lw=1.2)
    X = [-8, 12]; ax.plot(X, [(7 - 3 * x) / 5 for x in X], color=NAVY, lw=2)
    pts = [(-6, 5), (-1, 2), (4, -1), (9, -4)]
    for p in pts:
        ax.plot(*p, 'o', ms=9, mfc='#FFD966' if p == (4, -1) else '#F8CBAD', mec=RED, mew=2, zorder=5)
        ax.text(p[0] + 0.35, p[1] + 0.35, f'({p[0]}, {p[1]})'.replace('-', '−'), fontsize=9.5, color=RED, fontweight='bold')
    for a, b in zip(pts, pts[1:]):
        ax.annotate('', xy=(b[0], b[1] - 0.35), xytext=(a[0], a[1] - 0.35), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.4, connectionstyle='arc3,rad=0.25'))
    ax.text(6.5, 3.3, '3x + 5y = 7', fontsize=13, color=NAVY, fontweight='bold')
    ax.text(6.5, 1.5, 'các nghiệm cách nhau\nđúng (+5, −3)', fontsize=10.5, color=GREEN, fontweight='bold')
    ax.set_xlim(-8, 12); ax.set_ylim(-6, 6); ax.set_xticks(range(-8, 13, 2)); ax.set_yticks(range(-6, 7, 2))
    ax.tick_params(labelsize=8.5, colors='#555555')
    for sp_ in ax.spines.values(): sp_.set_visible(False)
    save(f, 'f4_nghiem')

f_hcn(); f_capuoc(); f_euclid(); f_ucchung(); f_nghiem()
flow('f2_ngaytho', [('term', 'Bắt đầu'), ('proc', 'cnt ← 0; sum ← 0'), ('loop', 'd = 1, 2, ..., n'), ('dec', 'n mod d = 0 ?', ('cnt ← cnt + 1\nsum ← sum + d', 'proc')), ('end', ''), ('io', 'In cnt, sum'), ('term', 'Kết thúc')])
flow('f2_toiuu', [('term', 'Bắt đầu'), ('proc', 'cnt ← 0; sum ← 0'), ('loop', 'd = 1, 2, ...\nchừng nào d · d ≤ n'), ('dec', 'n mod d = 0 ?', ('thêm d; nếu n / d ≠ d\nthì thêm cả n / d', 'proc')), ('end', ''), ('io', 'In cnt, sum'), ('term', 'Kết thúc')])
flow('f3_ngaytho', [('term', 'Bắt đầu'), ('proc', 'g ← min(a, b)'), ('loop', 'g không chia hết\ncả a lẫn b?'), ('proc', 'g ← g − 1'), ('end', ''), ('io', 'In g'), ('term', 'Kết thúc')])
flow('f3_toiuu', [('term', 'Bắt đầu'), ('loop', 'b ≠ 0 ?'), ('proc', 'r ← a mod b'), ('proc', 'a ← b; b ← r'), ('end', ''), ('io', 'In a (= ƯCLN)'), ('term', 'Kết thúc')])
flow('f4_ngaytho', [('term', 'Một truy vấn (a, b, c)'), ('loop', 'x = 0, 1, ..., b − 1'), ('dec', '(c − a·x) chia hết\ncho b ?', ('In x và\ny = (c − a·x) / b', 'io')), ('end', ''), ('io', 'In −1'), ('term', 'Kết thúc')])
flow('f4_toiuu', [('term', 'Một truy vấn (a, b, c)'), ('proc', 'Euclid mở rộng:\ng, x, y với a·x + b·y = g'), ('dec', 'g không chia hết c ?', ('In −1', 'io')), ('proc', 'x ← x · (c / g)\nđưa x về [0, b / g)'), ('io', 'In x và y = (c − a·x) / b'), ('term', 'Kết thúc')])
