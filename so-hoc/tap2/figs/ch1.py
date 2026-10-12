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

ngaythu(); chusocuoi(); vietlien()
