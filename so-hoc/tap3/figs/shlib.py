# Các hình dùng chung cho sách Số học (cùng bảng màu bộ Lý thuyết đồ thị)
from figlib import *
from matplotlib.patches import Arc, FancyBboxPatch, Polygon, Wedge

def cellbox(ax, x, y, text, fc='#FFFFFF', ec=NAVY, w=0.9, h=0.7, fs=13, bold=True, color=TXT, lw=1.6, z=3):
    ax.add_patch(Rectangle((x - w/2, y - h/2), w, h, fc=fc, ec=ec, lw=lw, zorder=z))
    ax.text(x, y, str(text), ha='center', va='center', fontsize=fs, fontweight='bold' if bold else 'normal', color=color, zorder=z + 1)

def jump(ax, x0, x1, y=0, h=0.55, color=NAVY, label=None, fs=10, lw=1.8):
    """cung nhảy từ x0 tới x1 phía trên trục số"""
    ax.annotate('', xy=(x1, y + 0.05), xytext=(x0, y + 0.05),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=lw, connectionstyle=f'arc3,rad={-0.5 if x1 > x0 else 0.5}', mutation_scale=12), zorder=4)
    if label: ax.text((x0 + x1) / 2, y + abs(x1 - x0) * 0.25 + 0.15, label, ha='center', va='bottom', fontsize=fs, color=color, fontweight='bold')

def numline(ax, lo, hi, y=0, step=1, labels=None, fs=9.5, color=GRAY, major=None):
    ax.plot([lo - 0.6, hi + 0.6], [y, y], color=color, lw=1.6, zorder=1)
    ax.annotate('', xy=(hi + 0.9, y), xytext=(hi + 0.5, y), arrowprops=dict(arrowstyle='-|>', color=color, lw=1.6))
    for x in range(lo, hi + 1, step):
        big = major and x % major == 0
        ax.plot([x, x], [y - (0.13 if big else 0.08), y + (0.13 if big else 0.08)], color=color, lw=1.4 if big else 1.0, zorder=1)
        if labels is None or x in labels:
            ax.text(x, y - 0.28, str(x), ha='center', va='top', fontsize=fs, color=TXT if big or labels else '#555555')
