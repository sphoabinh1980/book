# Hình bìa
from shlib import *
def isp(n): return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))
f, ax = fig(7.2, 3.6)
N = 10
for i in range(N):
    for j in range(N):
        v = i * N + j + 1
        x, y = j * 0.62, -i * 0.62
        if isp(v): fc, ec, col = '#FFD966', RED, TXT
        elif v == 1: fc, ec, col = '#EDEDED', '#9A9A9A', '#7F7F7F'
        else: fc, ec, col = '#F3F6FA', '#B4C6E7', '#7F8FA6'
        ax.add_patch(Rectangle((x - 0.29, y - 0.29), 0.58, 0.58, fc=fc, ec=ec, lw=1.2))
        ax.text(x, y, str(v), ha='center', va='center', fontsize=9, color=col, fontweight='bold' if isp(v) else 'normal')
tx = 7.0
for k, (t, c) in enumerate([('a = b · q + r', NAVY), ('gcd(a, b) = gcd(b, a mod b)', TEAL), ('a^(p−1) ≡ 1  (mod p)', RED), ('C(n, k) = n! / (k! (n − k)!)', PURPLE), ('ax + by = gcd(a, b)', AMBER)]):
    ax.text(tx, -0.3 - k * 1.2, t, fontsize=13, color=c, fontweight='bold', va='center')
ax.set_xlim(-0.5, 13.6); ax.set_ylim(-6.0, 0.4)
save(f, 'cover1')
