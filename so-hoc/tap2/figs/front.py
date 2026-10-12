# Hình bìa và hình "ba mức độ"
from shlib import *
import math

def cover():
    f, ax = fig(12, 3.6)
    chap = {l: (l - 1) // 4 for l in range(1, 21)}
    sts = ['done', 'teal', 'amber', 'pink', 'src']
    pos = {l: ((l - 1) * 0.85, 1.9 + 0.95 * math.sin((l - 1) * 0.55)) for l in range(1, 21)}
    for l in range(1, 20): edge(ax, pos[l], pos[l + 1], color=RED if chap[l] == chap[l + 1] else NAVY, lw=3.2, r=0.28)
    lv = [('#CDEBC5', GREEN), ('#FFE7B3', AMBER), ('#F8CBAD', RED)]
    for l in range(1, 21):
        x, y = pos[l]; up = math.cos((l - 1) * 0.55) < 0
        for k in range(3):
            a = math.radians(90 - (k - 1) * 38 if up else 270 + (k - 1) * 38)
            q = (x + 0.58 * math.cos(a), y + 0.58 * math.sin(a))
            ax.plot([x + 0.28 * math.cos(a), q[0] - 0.12 * math.cos(a)], [y + 0.28 * math.sin(a), q[1] - 0.12 * math.sin(a)], color='#A0A0A0', lw=1.3, zorder=1)
            ax.add_patch(Circle(q, 0.12, fc=lv[k][0], ec=lv[k][1], lw=1.7, zorder=4))
        node(ax, pos[l], l, sts[chap[l]], r=0.28, fs=11)
    names = ['Chia hết và ước số', 'Số nguyên tố', 'Số học đồng dư', 'Tổ hợp và đếm', 'Kĩ thuật số học']
    for c in range(5):
        Ls = [l for l in range(1, 21) if chap[l] == c]
        cx = sum(pos[l][0] for l in Ls) / len(Ls)
        fc, ec = STY[sts[c]]
        ax.text(cx, 0.05, f'Chương {c + 1}', ha='center', fontsize=11, color=ec, fontweight='bold')
        ax.text(cx, -0.3, names[c], ha='center', fontsize=9.5, color=TXT)
    for x, t, (fc, ec) in [(2.6, 'cơ bản', lv[0]), (4.2, 'trung bình', lv[1]), (6.2, 'nâng cao', lv[2])]:
        ax.add_patch(Circle((x, 3.95), 0.1, fc=fc, ec=ec, lw=1.6)); ax.text(x + 0.2, 3.95, t, va='center', fontsize=10, color=ec, fontweight='bold')
    ax.text(8.2, 3.95, 'Mỗi bài học (đỉnh lớn) có ba bài tập (đỉnh nhỏ)', va='center', fontsize=10, color=NAVY)
    ax.set_xlim(-0.6, 16.8); ax.set_ylim(-0.55, 4.2); save(f, 'cover')

def levels():
    f, ax = fig(9, 1.3)
    for k, (st, t, c) in enumerate([('wait', '★☆☆  Cơ bản', GREEN), ('amber', '★★☆  Trung bình', AMBER), ('ans', '★★★  Nâng cao', RED)]):
        x = k * 3.1
        ax.add_patch(FancyBboxPatch((x, 0), 2.7, 0.8, boxstyle='round,pad=0.02,rounding_size=0.15', fc=STY[st][0], ec=c, lw=2))
        ax.text(x + 1.35, 0.4, t, ha='center', va='center', fontsize=14, color=c, fontweight='bold')
        if k < 2: ax.annotate('', xy=(x + 3.05, 0.4), xytext=(x + 2.75, 0.4), arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=2, mutation_scale=16))
    ax.set_xlim(-0.1, 9.0); ax.set_ylim(-0.1, 0.9); save(f, 'levels')

cover(); levels()
