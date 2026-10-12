# Hình bìa Tập 3: ba bậc điểm từ cách ngây thơ tới cách tối ưu
from shlib import *
f, ax = fig(7.4, 3.0)
steps = [(0, 0.0, 1.0, '30 điểm', 'Cách ngây thơ', '#F8CBAD', RED), (2.7, 0.0, 1.7, '60 điểm', 'Bế tắc → quan sát', '#FFE7B3', AMBER), (5.4, 0.0, 2.6, '100 điểm', 'Cách tối ưu', '#CDEBC5', GREEN)]
for x, y, h, t, lab, fc, ec in steps:
    ax.add_patch(FancyBboxPatch((x, y), 2.2, h, boxstyle='round,pad=0.02,rounding_size=0.12', fc=fc, ec=ec, lw=2.2))
    ax.text(x + 1.1, h + 0.28, t, ha='center', fontsize=15, color=ec, fontweight='bold')
    ax.text(x + 1.1, -0.35, lab, ha='center', fontsize=11, color=TXT, fontweight='bold')
ax.annotate('', xy=(2.6, 1.55), xytext=(1.6, 1.55), arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=2.2, connectionstyle='arc3,rad=-0.3', mutation_scale=16))
ax.annotate('', xy=(5.3, 2.4), xytext=(4.3, 2.3), arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=2.2, connectionstyle='arc3,rad=-0.3', mutation_scale=16))
for k, (t, c) in enumerate([('O(n)', RED), ('O(√n)', AMBER), ('O(log n)', GREEN)]):
    ax.text(1.1 + 2.7 * k, [0.5, 0.85, 1.3][k], t, ha='center', va='center', fontsize=13, color=c, fontweight='bold', family='DejaVu Sans Mono')
ax.set_xlim(-0.3, 7.9); ax.set_ylim(-0.7, 3.3); save(f, 'cover3')
