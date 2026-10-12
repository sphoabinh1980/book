# Thư viện vẽ hình cho Tập 2 — cùng bảng màu với Tập 1
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle, FancyBboxPatch
import math, os
plt.rcParams['font.family'] = 'DejaVu Sans'
NAVY = '#1F3864'; RED = '#C0504D'; GRAY = '#8C8C8C'; LGRAY = '#D9D9D9'; TXT = '#1A1A1A'
ORANGE = '#C55A11'; GREEN = '#2E7D32'; PURPLE = '#6A4C93'; TEAL = '#1B7F79'; PINK = '#A23B6B'; AMBER = '#B26A00'
STY = {  # kiểu đỉnh: (nền, viền)
    'w': ('#FFFFFF', NAVY), 'cur': ('#FFD966', RED), 'wait': ('#CDEBC5', GREEN), 'done': ('#BDD7EE', NAVY),
    'src': ('#DCCCEC', PURPLE), 'ans': ('#F8CBAD', RED), 'teal': ('#B2E5E0', TEAL), 'pink': ('#F4C7D9', PINK),
    'amber': ('#FFE7B3', AMBER), 'gray': ('#EDEDED', '#9A9A9A'),
}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'png')
os.makedirs(OUT, exist_ok=True)

def fig(w, h):
    f, ax = plt.subplots(figsize=(w, h)); ax.set_aspect('equal'); ax.axis('off'); return f, ax
def save(f, name, pad=0.06):
    f.savefig(os.path.join(OUT, name + '.png'), dpi=220, bbox_inches='tight', pad_inches=pad, facecolor='white'); plt.close(f)

def node(ax, p, label, st='w', r=0.32, fs=15, bold=True, lw=2.6, z=5):
    fc, ec = STY[st]
    ax.add_patch(Circle(p, r, facecolor=fc, edgecolor=ec, lw=lw, zorder=z))
    ax.text(p[0], p[1], str(label), ha='center', va='center', fontsize=fs, color=TXT, fontweight='bold' if bold else 'normal', zorder=z+1)

def tag(ax, p, text, color=NAVY, fs=11, bg='white', z=8, bold=True):
    ax.text(p[0], p[1], text, ha='center', va='center', fontsize=fs, color=color, fontweight='bold' if bold else 'normal', zorder=z,
            bbox=dict(boxstyle='round,pad=0.22', fc=bg, ec=color, lw=1.3))

def _short(p, q, r):
    dx, dy = q[0]-p[0], q[1]-p[1]; L = math.hypot(dx, dy) or 1
    return (p[0]+dx*r/L, p[1]+dy*r/L), (q[0]-dx*r/L, q[1]-dy*r/L)

def edge(ax, p, q, color=GRAY, lw=2.2, directed=False, label=None, lcolor=None, lfs=11, rad=0.0, r=0.32, dash=False,
         lpos=0.5, loff=(0, 0), z=2, head=14):
    a, b = _short(p, q, r)
    ls = (0, (4, 3)) if dash else '-'
    if directed or rad:
        arr = FancyArrowPatch(a, b, arrowstyle='-|>' if directed else '-', mutation_scale=head, color=color, lw=lw,
                              connectionstyle=f'arc3,rad={rad}', linestyle=ls, zorder=z, shrinkA=0, shrinkB=1 if directed else 0)
        ax.add_patch(arr)
    else:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, zorder=z, linestyle=ls, solid_capstyle='round')
    if label is not None:
        mx, my = p[0]+(q[0]-p[0])*lpos, p[1]+(q[1]-p[1])*lpos
        if rad:
            dx, dy = q[0]-p[0], q[1]-p[1]; mx += dy*rad*0.5; my -= dx*rad*0.5
        ax.text(mx+loff[0], my+loff[1], str(label), ha='center', va='center', fontsize=lfs, color=lcolor or (color if color != GRAY else TXT),
                fontweight='bold' if color != GRAY else 'normal', zorder=z+3,
                bbox=dict(boxstyle='round,pad=0.12', fc='white', ec='none'))

def loop(ax, p, color=GRAY, lw=2.2, r=0.32, ang=90, size=0.42):
    a = math.radians(ang); c = (p[0]+math.cos(a)*(r+size*0.55), p[1]+math.sin(a)*(r+size*0.55))
    ax.add_patch(Circle(c, size*0.62, facecolor='none', edgecolor=color, lw=lw, zorder=1))

def caption(ax, x, y, text, fs=12, color=NAVY, bold=True, ha='center'):
    ax.text(x, y, text, ha=ha, va='center', fontsize=fs, color=color, fontweight='bold' if bold else 'normal')

def legend_line(ax, x, y, color, text, lw=4, dash=False, fs=11, L=0.6):
    ax.plot([x, x+L], [y, y], color=color, lw=lw, linestyle=(0, (4, 3)) if dash else '-', solid_capstyle='butt')
    ax.text(x+L+0.15, y, text, va='center', fontsize=fs, color=TXT)
def legend_node(ax, x, y, st, text, fs=11, r=0.16):
    fc, ec = STY[st]; ax.add_patch(Circle((x+0.18, y), r, facecolor=fc, edgecolor=ec, lw=2))
    ax.text(x+0.5, y, text, va='center', fontsize=fs, color=TXT)

def grid(ax, rows, x0=0, y0=0, s=0.6, colors=None, texts=None, fs=12, lw=1.2, tcolor=None):
    """Vẽ lưới; rows là danh sách xâu; colors[(i,j)] = màu nền; texts[(i,j)] = chữ."""
    R, C = len(rows), len(rows[0])
    for i in range(R):
        for j in range(C):
            ch = rows[i][j]
            fc = (colors or {}).get((i, j)) or ('#595959' if ch == '#' else 'white')
            ax.add_patch(Rectangle((x0+j*s, y0-(i+1)*s), s, s, facecolor=fc, edgecolor='#A0A0A0', lw=lw, zorder=1))
            t = (texts or {}).get((i, j))
            if t is not None:
                col = (tcolor or {}).get((i, j), TXT) if isinstance(tcolor, dict) else (tcolor or TXT)
                ax.text(x0+j*s+s/2, y0-i*s-s/2, str(t), ha='center', va='center', fontsize=fs, color=col, fontweight='bold', zorder=3)
    ax.add_patch(Rectangle((x0, y0-R*s), C*s, R*s, facecolor='none', edgecolor=NAVY, lw=2, zorder=4))
def cell_center(i, j, x0=0, y0=0, s=0.6): return (x0+j*s+s/2, y0-i*s-s/2)
