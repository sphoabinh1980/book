# Vẽ sơ đồ khối theo phong cách của mẫu Tập 3
from figlib import *
from matplotlib.patches import FancyBboxPatch, Polygon
STY_F = {'term': ('#DDEBF7', NAVY), 'proc': ('#FBE2D5', RED), 'io': ('#E2EFDA', GREEN), 'dec': ('#FFF2CC', AMBER), 'loop': ('#FFF2CC', AMBER)}
FS = 9.5
def _w(t): return max(0.9, 0.086 * max(len(x) for x in t.split('\n')) + 0.35)
def _h(t): return 0.34 + 0.17 * (t.count('\n'))

def box(ax, kind, x, y, text):
    fc, ec = STY_F[kind]; w = _w(text); h = _h(text)
    if kind == 'term':
        ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle='round,pad=0,rounding_size=0.2', fc=fc, ec=ec, lw=1.8, zorder=3))
    elif kind == 'proc':
        ax.add_patch(Rectangle((x - w/2, y - h/2), w, h, fc=fc, ec=ec, lw=1.6, zorder=3))
    elif kind == 'io':
        s = 0.18; ax.add_patch(Polygon([(x - w/2 + s, y + h/2), (x + w/2 + s, y + h/2), (x + w/2 - s, y - h/2), (x - w/2 - s, y - h/2)], fc=fc, ec=ec, lw=1.6, zorder=3))
    else:
        w = w * 1.5; h = h * 1.55
        ax.add_patch(Polygon([(x, y + h/2), (x + w/2, y), (x, y - h/2), (x - w/2, y)], fc=fc, ec=ec, lw=1.6, zorder=3))
    ax.text(x, y, text, ha='center', va='center', fontsize=FS, color=TXT, zorder=4, fontweight='bold' if kind == 'term' else 'normal')
    return w, h

def arrow(ax, pts, color=NAVY, label=None, lc=None, lpos=None):
    for a, b in zip(pts[:-2], pts[1:-1]): ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=1.6, zorder=2)
    ax.annotate('', xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle='-|>', color=color, lw=1.6, mutation_scale=12), zorder=2)
    if label:
        p = lpos or pts[0]
        ax.text(p[0], p[1], label, fontsize=8.5, color=lc or color, fontweight='bold', ha='left', va='bottom', zorder=5)

def flow(name, steps, gap=0.3):
    """steps: danh sách (kind, text, extra). kind: term/proc/io/dec/loop/end.
    dec: extra = (chữ ở nhánh Đúng bên phải, kiểu hộp); loop: các bước sau cho tới 'end' là thân vòng lặp."""
    f, ax = plt.subplots(figsize=(6, 6)); ax.set_aspect('equal'); ax.axis('off')
    y = 0; pos = []; loops = []; xmin, xmax = -1, 1; right = {}
    prev_bottom = None
    for k, st in enumerate(steps):
        kind, text = st[0], st[1]
        if kind == 'end':
            lk, ly, lw_, lh = loops.pop()
            bodyw = max([_w(t[1]) for t in steps[lk + 1:k] if t[0] != 'end'] + [0])
            # mũi tên quay lại từ đáy thân vòng lặp lên đỉnh thoi, đi vòng bên trái
            xl = -max(lw_ / 2, bodyw / 2) - 0.3
            arrow(ax, [(0, prev_bottom), (0, prev_bottom - 0.18), (xl, prev_bottom - 0.18), (xl, ly), (-lw_ / 2, ly)])
            xmin = min(xmin, xl - 0.2)
            exit_y = prev_bottom - 0.4
            xr = max([lw_ / 2, bodyw / 2] + [right[j] for j in range(lk + 1, k) if j in right]) + 0.35
            arrow(ax, [(lw_ / 2, ly), (xr, ly), (xr, exit_y), (0.05, exit_y)], label='Sai', lc=RED, lpos=(lw_ / 2 + 0.05, ly + 0.03))
            xmax = max(xmax, xr + 0.2)
            prev_bottom = exit_y; y = exit_y - 0.05
            continue
        h = _h(text) * (1.55 if kind in ('dec', 'loop') else 1)
        cy = y - gap - h / 2 if prev_bottom is not None else 0
        if prev_bottom is not None: arrow(ax, [(0, prev_bottom), (0, cy + h / 2)])
        w, h = box(ax, kind, 0, cy, text)
        xmin = min(xmin, -w / 2 - 0.3); xmax = max(xmax, w / 2 + 0.3)
        if kind == 'dec':
            side, skind = st[2]
            sw, sh = _w(side), _h(side)
            sx = w / 2 + 0.55 + sw / 2
            box(ax, skind, sx, cy, side)
            arrow(ax, [(w / 2, cy), (sx - sw / 2, cy)], label='Đúng', lc=GREEN, lpos=(w / 2 + 0.03, cy + 0.05))
            xmax = max(xmax, sx + sw / 2 + 0.2); right[k] = sx + sw / 2
            ax.text(0.08, cy - h / 2 - 0.05, 'Sai', fontsize=8.5, color=RED, fontweight='bold', va='top')
        if kind == 'loop':
            loops.append((k, cy, w, h))
            ax.text(0.08, cy - h / 2 - 0.05, 'Đúng', fontsize=8.5, color=GREEN, fontweight='bold', va='top')
        prev_bottom = cy - h / 2; y = prev_bottom
    ax.set_xlim(xmin, xmax); ax.set_ylim(y - 0.2, 0.5)
    W = xmax - xmin; H = 0.5 - y + 0.2
    f.set_size_inches(W, H)
    save(f, name, pad=0.03)

if __name__ == '__main__':
    flow('test_flow', [('term', 'Hàm f(n)'), ('dec', 'n ≤ 1 ?', ('trả về 1', 'term')), ('proc', 'a ← f(n − 1)'), ('proc', 'b ← f(n − 2)'), ('term', 'trả về a + 2·b')])
    flow('test_flow2', [('term', 'Bắt đầu'), ('io', 'Đọc n; f(0) = f(1) = 1'), ('proc', 'i ← 2'), ('loop', 'i ≤ n ?'), ('proc', 'f(i) ← f(i − 1) + 2·f(i − 2)\ni ← i + 1'), ('end', ''), ('io', 'In f(n)'), ('term', 'Kết thúc')])
