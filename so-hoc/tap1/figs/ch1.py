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
