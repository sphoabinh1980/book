from figlib import *
import math

def cover():
    f, ax = fig(12, 3.6)
    chap = {**{l: 0 for l in (1, 2, 3, 4)}, **{l: 1 for l in (5, 6, 7, 8)}, **{l: 2 for l in (9, 10, 11)}, **{l: 3 for l in (12, 13, 14, 15)}, **{l: 4 for l in (16, 17)}}
    sts = ['done', 'teal', 'amber', 'pink', 'src']
    pos = {}
    for l in range(1, 18):
        x = (l - 1)*1.0; y = 1.9 + 0.95*math.sin((l - 1)*0.62)
        pos[l] = (x, y)
    for l in range(1, 17): edge(ax, pos[l], pos[l + 1], color=RED if chap[l] == chap[l + 1] else NAVY, lw=3.4, r=0.3)
    lv = [('#CDEBC5', GREEN), ('#FFE7B3', AMBER), ('#F8CBAD', RED)]
    for l in range(1, 18):
        x, y = pos[l]; up = math.cos((l - 1)*0.62) < 0
        for k in range(3):
            a = math.radians(90 - (k - 1)*38 if up else 270 + (k - 1)*38)
            q = (x + 0.62*math.cos(a), y + 0.62*math.sin(a))
            ax.plot([x + 0.3*math.cos(a), q[0] - 0.13*math.cos(a)], [y + 0.3*math.sin(a), q[1] - 0.13*math.sin(a)], color='#A0A0A0', lw=1.4, zorder=1)
            ax.add_patch(Circle(q, 0.13, fc=lv[k][0], ec=lv[k][1], lw=1.8, zorder=4))
        node(ax, pos[l], l, sts[chap[l]], r=0.3, fs=12)
    names = ['Làm quen với đồ thị', 'Đường đi ngắn nhất', 'Cây và cây khung', 'Cấu trúc của đồ thị', 'Ghép cặp và luồng']
    for c in range(5):
        Ls = [l for l in range(1, 18) if chap[l] == c]
        cx = sum(pos[l][0] for l in Ls)/len(Ls)
        fc, ec = STY[sts[c]]
        ax.text(cx, 0.05, f'Chương {c + 1}', ha='center', fontsize=11, color=ec, fontweight='bold')
        ax.text(cx, -0.3, names[c], ha='center', fontsize=9.5, color=TXT)
    ax.add_patch(Circle((3.0, 3.85), 0.1, fc='#CDEBC5', ec=GREEN, lw=1.6)); ax.text(3.2, 3.85, 'cơ bản', va='center', fontsize=10, color=GREEN, fontweight='bold')
    ax.add_patch(Circle((4.6, 3.85), 0.1, fc='#FFE7B3', ec=AMBER, lw=1.6)); ax.text(4.8, 3.85, 'trung bình', va='center', fontsize=10, color=AMBER, fontweight='bold')
    ax.add_patch(Circle((6.6, 3.85), 0.1, fc='#F8CBAD', ec=RED, lw=1.6)); ax.text(6.8, 3.85, 'nâng cao', va='center', fontsize=10, color=RED, fontweight='bold')
    ax.text(8.6, 3.85, 'Mỗi bài học (đỉnh lớn) có ba bài tập (đỉnh nhỏ)', va='center', fontsize=10, color=NAVY)
    ax.set_xlim(-0.6, 16.6); ax.set_ylim(-0.55, 4.1); save(f, 'cover')

def levels():
    f, ax = fig(9, 1.3)
    for k, (st, t, c) in enumerate([('wait', '★☆☆  Cơ bản', GREEN), ('amber', '★★☆  Trung bình', AMBER), ('ans', '★★★  Nâng cao', RED)]):
        x = k*3.1
        ax.add_patch(FancyBboxPatch((x, 0), 2.7, 0.8, boxstyle='round,pad=0.02,rounding_size=0.15', fc=STY[st][0], ec=c, lw=2))
        ax.text(x + 1.35, 0.4, t, ha='center', va='center', fontsize=14, color=c, fontweight='bold')
        if k < 2: ax.annotate('', xy=(x + 3.05, 0.4), xytext=(x + 2.75, 0.4), arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=2, mutation_scale=16))
    ax.set_xlim(-0.1, 9.0); ax.set_ylim(-0.1, 0.9); save(f, 'levels')

cover(); levels()
