# Hình Chương 3 (Tập 2)
from shlib import *
import math

P7 = 10**9 + 7
YEL, YEC = '#FFD966', RED          # ô đáp số / đang xét
BLU, BLC = '#BDD7EE', NAVY         # bình thường / đã xong
INP, INC = '#FFE7B3', AMBER        # dữ liệu vào
GRY, GRC = '#EDEDED', '#9A9A9A'    # bị loại

# ---------- 9.1 LUYTHUAQ: 2^10 = 2^8 · 2^2
def luythuaq():
    f, ax = fig(9.2, 3.0)
    a, b, m = 2, 10, 1000
    bits = [(b >> i) & 1 for i in range(4)]
    ax.text(-0.5, 1.2, 'bit của b = 10 = 1010₂', ha='right', va='center', fontsize=10, color=AMBER, fontweight='bold')
    ax.text(-0.5, 0.35, '$a^{2^i}$', ha='right', va='center', fontsize=10, color=NAVY, fontweight='bold')
    ax.text(-0.5, -0.5, 'r sau lượt', ha='right', va='center', fontsize=10, color=RED, fontweight='bold')
    r = 1; x = a
    for i in range(4):
        cx = i * 1.85 + 0.75
        on = bits[i]
        ax.text(cx, 1.75, f'lượt {i + 1}', ha='center', va='center', fontsize=10, color='#505050')
        cellbox(ax, cx, 1.2, on, fc=INP, ec=INC, w=1.2, h=0.5, fs=11)
        cellbox(ax, cx, 0.35, f'$2^{{{1 << i}}}$ = {x}', fc=YEL if on else GRY, ec=YEC if on else GRC, w=1.5, h=0.5, fs=10.5,
                color=TXT if on else '#808080')
        if on: r = r * x
        cellbox(ax, cx, -0.5, r, fc=YEL if i == 3 else BLU, ec=YEC if i == 3 else BLC, w=1.2, h=0.5, fs=11)
        if i < 3: ax.annotate('', xy=(cx + 1.08, 0.35), xytext=(cx + 0.77, 0.35), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.2))
        x = x * x
    ax.text(3 * 1.85 + 0.75, -1.05, 'mỗi lượt: bình phương hàng giữa, nhân vào r nếu bit bằng 1', ha='right', va='center', fontsize=10, color=GRAY, style='italic')
    tx = 7.5
    ax.text(tx, 1.15, '$2^{10} = 2^{8} \\cdot 2^{2}$ = 1024', fontsize=11, color=RED, fontweight='bold', va='center')
    ax.text(tx, 0.5, 'chỉ nhân vào r ở các bit 1', fontsize=10, color=TXT, va='center')
    ax.text(tx, -0.1, 'b ≤ $10^{18}$ có không quá 60 bit:', fontsize=10, color=TXT, va='center')
    ax.text(tx, -0.6, '≤ 60 lượt cho mỗi câu hỏi', fontsize=10, color=NAVY, fontweight='bold', va='center')
    ax.set_xlim(-3.1, 12.2); ax.set_ylim(-1.3, 2.0); save(f, 'luythuaq')

# ---------- 9.2 SOMULON: Horner trên số mũ, 2^12345 mod 1000
def somulon():
    f, ax = fig(9.0, 2.9)
    b, m = '12345', 1000
    r = 1; pre = ''
    ax.text(-0.35, 1.0, 'chữ số d', ha='right', va='center', fontsize=10, color=AMBER, fontweight='bold')
    ax.text(-0.35, 0.2, 'phần đầu x', ha='right', va='center', fontsize=10, color='#505050', fontweight='bold')
    ax.text(-0.35, -0.6, 'r = $2^x$ mod 1000', ha='right', va='center', fontsize=10, color=RED, fontweight='bold')
    for i, ch in enumerate(b):
        d = int(ch); pre += ch; r = pow(r, 10, m) * pow(2, d, m) % m
        cx = i * 1.45 + 0.6
        cellbox(ax, cx, 1.0, d, fc=INP, ec=INC, w=0.6, h=0.5, fs=11)
        ax.text(cx, 0.2, pre, ha='center', va='center', fontsize=10.5, color=TXT)
        last = i == len(b) - 1
        cellbox(ax, cx, -0.6, r, fc=YEL if last else BLU, ec=YEC if last else BLC, w=1.0, h=0.5, fs=11)
        if i:
            ax.annotate('', xy=(cx - 0.55, -0.6), xytext=(cx - 0.9, -0.6), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.4))
    ax.text(0.6 + 1.45 * 0.5, -1.15, 'r ← $r^{10} \\cdot 2^{d}$ (mod 1000)', ha='left', va='center', fontsize=10, color=GREEN, fontweight='bold')
    ax.text(7.7, 0.55, '$a^{10x + d} = (a^{x})^{10} \\cdot a^{d}$', fontsize=11, color=NAVY, fontweight='bold', va='center')
    ax.text(7.7, -0.1, 'mỗi chữ số của b: khoảng', fontsize=10, color=TXT, va='center')
    ax.text(7.7, -0.55, '5 phép nhân theo mô-đun m', fontsize=10, color=TXT, va='center')
    ax.set_xlim(-3.0, 12.6); ax.set_ylim(-1.4, 1.4); save(f, 'somulon')

# ---------- 9.3 TONGLT: chia đôi S(10) với a = 2, m = 1000
def tonglt():
    f, ax = fig(9.4, 3.2)
    a, m = 2, 1000
    def geo(n):
        if n == 0: return 0, 1
        if n % 2: S, P = geo(n - 1); return (1 + a * S) % m, P * a % m
        S, P = geo(n // 2); return S * (1 + P) % m, P * P % m
    chain = [0, 1, 2, 4, 5, 10]
    rule = {1: 'bớt 1', 2: 'chia đôi', 4: 'chia đôi', 5: 'bớt 1', 10: 'chia đôi'}
    form = {1: '1 + a·S(0)', 2: 'S(1)·(1 + $a^{1}$)', 4: 'S(2)·(1 + $a^{2}$)', 5: '1 + a·S(4)', 10: 'S(5)·(1 + $a^{5}$)'}
    for i, n in enumerate(chain):
        x = i * 1.75
        S, P = geo(n); last = n == 10
        cellbox(ax, x, 0.55, f'S({n}) = {S}', fc=YEL if last else BLU, ec=YEC if last else BLC, w=1.45, h=0.5, fs=10)
        cellbox(ax, x, -0.1, f'$a^{{{n}}}$ ≡ {P}', fc='#F3F6FA', ec='#B4C6E7', w=1.45, h=0.45, fs=9.5, bold=False)
        if n:
            ax.text(x, -0.65, form[n], ha='center', va='center', fontsize=9.5, color='#404040')
            ax.annotate('', xy=(x - 0.76, 0.55), xytext=(x - 1.0, 0.55), arrowprops=dict(arrowstyle='-|>', color=GREEN if rule[n] == 'chia đôi' else PURPLE, lw=1.6))
            ax.text(x - 0.875, 1.05, rule[n], ha='center', va='center', fontsize=9.5, color=GREEN if rule[n] == 'chia đôi' else PURPLE, fontweight='bold')
    ax.text(chain.index(10) * 1.75, -1.05, '1023 mod 1000 = 23', ha='center', va='center', fontsize=10, color=RED, fontweight='bold')
    ax.text(-0.75, 1.45, 'S(n) = 1 + a + ... + $a^{n-1}$ (n số hạng), tính theo mô-đun m = 1000;  đề bài hỏi S(n + 1)', fontsize=10, color=NAVY, fontweight='bold')
    ax.set_xlim(-0.9, 9.7); ax.set_ylim(-1.4, 1.7); save(f, 'tonglt')

# ---------- 10.1 XACSUAT
def xacsuat():
    f, ax = fig(8.6, 2.8)
    bags = [(1, 1), (1, 2)]
    for k, (x, y) in enumerate(bags):
        cx = k * 2.1
        ax.add_patch(FancyBboxPatch((cx - 0.8, -0.75), 1.6, 1.5, boxstyle='round,pad=0.05', fc='#F7F7F7', ec=GRAY, lw=1.5))
        ax.text(cx, 1.0, f'túi {k + 1}', ha='center', fontsize=10, color=NAVY, fontweight='bold')
        balls = ['r'] * x + ['b'] * y
        for j, c in enumerate(balls):
            px = cx + (j - (len(balls) - 1) / 2) * 0.48
            ax.add_patch(Circle((px, 0.0), 0.2, fc='#E06666' if c == 'r' else '#6FA8DC', ec='#7F1F1F' if c == 'r' else NAVY, lw=1.4))
        ax.text(cx, -1.05, f'P(đỏ) = {x}/{x + y}', ha='center', fontsize=9.5, color=TXT)
    tx = 3.6
    ax.text(tx, 0.75, 'P(cả hai đỏ) = 1/2 · 1/3 = 1/6', fontsize=10.5, color=TXT, va='center')
    ax.text(tx + 0.3, 0.3, '→ 1 · 6⁻¹ mod p = 166666668', fontsize=10.5, color=RED, fontweight='bold', va='center')
    ax.text(tx, -0.3, 'P(ít nhất một đỏ) = 1 − 1/2 · 2/3 = 2/3', fontsize=10.5, color=TXT, va='center')
    ax.text(tx + 0.3, -0.75, '→ 2 · 3⁻¹ mod p = 666666672', fontsize=10.5, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-1.0, 9.6); ax.set_ylim(-1.3, 1.3); save(f, 'xacsuat')

# ---------- 10.2 NGHICHDAO: bảng truy hồi với p = 11
def nghichdao():
    f, ax = fig(9.0, 2.9)
    p = 11; inv = [0, 1]
    for i in range(2, p): inv.append((p - p // i) * inv[p % i] % p)
    rows = [('i', lambda i: i, INP, INC), ('q = ⌊11/i⌋', lambda i: p // i, '#F3F6FA', '#B4C6E7'),
            ('r = 11 mod i', lambda i: p % i, '#F3F6FA', '#B4C6E7'), ('inv[r]', lambda i: inv[p % i], BLU, BLC),
            ('inv[i]', lambda i: inv[i], YEL, YEC)]
    w = 0.62
    for ri, (lab, fn, fc, ec) in enumerate(rows):
        y = -ri * 0.55
        ax.text(-0.2, y, lab, ha='right', va='center', fontsize=10, color=NAVY, fontweight='bold')
        for i in range(1, p):
            cellbox(ax, i * w, y, fn(i) if (i > 1 or ri in (0, 4)) else '–', fc=fc, ec=ec, w=w - 0.06, h=0.46, fs=10.5, bold=ri in (0, 4))
    # mũi tên minh hoạ cột i = 7 lấy inv[4]
    ax.annotate('', xy=(4 * w, -4 * 0.55 + 0.25), xytext=(7 * w, -2 * 0.55 - 0.25),
                arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.5, connectionstyle='arc3,rad=0.25'))
    ax.text(p * w + 0.1, -0.55, 'Cột i = 7: r = 4,', fontsize=10, color=RED, va='center')
    ax.text(p * w + 0.1, -1.0, 'inv[7] = (11 − 1) · inv[4]', fontsize=10, color=RED, va='center')
    ax.text(p * w + 0.1, -1.45, '= 10 · 3 = 30 ≡ 8', fontsize=10, color=RED, va='center', fontweight='bold')
    ax.text(p * w + 0.1, -2.1, 'hàng cuối là hoán vị của 1..10', fontsize=9.5, color='#404040', va='center')
    ax.set_xlim(-2.4, p * w + 4.0); ax.set_ylim(-2.55, 0.35); save(f, 'nghichdao')

# ---------- 10.3 PTDONGDU: 6x ≡ 4 (mod 10) trên [0, 20]
def ptdongdu():
    f, ax = fig(9.4, 2.2)
    L, R = 0, 20
    sols = [x for x in range(L - 3, R + 4) if (6 * x - 4) % 10 == 0]
    numline(ax, L - 3, R + 3, y=0, labels=set(range(L - 3, R + 4)), fs=9.5)
    for x in sols:
        inside = L <= x <= R
        node(ax, (x, 0), '', 'cur' if x == min(s for s in sols if s >= L) else ('done' if inside else 'gray'), r=0.2, fs=10, lw=2.2)
    for z in (L, R): ax.plot([z - 0.5, z - 0.5], [-0.15, 0.6], color=PURPLE, lw=1.8, ls='--') if z == L else ax.plot([z + 0.5, z + 0.5], [-0.15, 0.6], color=PURPLE, lw=1.8, ls='--')
    ax.text(L, 0.85, 'L = 0', ha='center', fontsize=10, color=PURPLE, fontweight='bold')
    ax.text(R, 0.85, 'R = 20', ha='center', fontsize=10, color=PURPLE, fontweight='bold')
    for x0, x1 in [(4, 9), (9, 14), (14, 19)]: jump(ax, x0, x1, y=0.3, h=0.4, color=GREEN, label='+5' if x0 == 4 else None, fs=10)
    ax.text(10, -1.45, '6x ≡ 4 (mod 10)  ⇔  3x ≡ 2 (mod 5)  ⇔  x ≡ 4 (mod 5):   4 nghiệm trong [0, 20], nhỏ nhất là 4',
            ha='center', fontsize=10, color=NAVY, fontweight='bold')
    ax.set_xlim(L - 4, R + 4.5); ax.set_ylim(-1.75, 2.6); save(f, 'ptdongdu')

# ---------- 11.1 PHI: đồng hồ 12 vạch, bước 5 và bước 4
def phi():
    f, ax = fig(8.6, 3.9)
    n = 12
    for c, (k, title) in enumerate([(5, 'bước k = 5: đi qua đủ 12 vạch'), (4, 'bước k = 4: chỉ thăm 0, 4, 8')]):
        cx = c * 4.6; R = 1.35
        pos = lambda v: (cx + R * math.sin(2 * math.pi * v / n), R * math.cos(2 * math.pi * v / n))
        ax.add_patch(Circle((cx, 0), R, fc='#F3F6FA', ec='#B4C6E7', lw=1.4))
        seen = []; v = 0
        while v not in seen: seen.append(v); v = (v + k) % n
        for i in range(len(seen)):
            p, q = pos(seen[i]), pos(seen[(i + 1) % len(seen)])
            edge(ax, p, q, color=GREEN if k == 5 else RED, lw=1.4, directed=True, r=0.24, head=9)
        for v in range(n):
            node(ax, pos(v), v, 'cur' if v == 0 else ('done' if v in seen else 'gray'), r=0.22, fs=10)
        ax.text(cx, -1.95, title, ha='center', fontsize=10, color=GREEN if k == 5 else RED, fontweight='bold')
    ax.text(2.3, 2.05, 'Đi qua đủ n vạch ⇔ gcd(k, n) = 1.   Với n = 12: k ∈ {1, 5, 7, 11}, đáp số φ(12) = 4',
            ha='center', fontsize=10, color=NAVY, fontweight='bold')
    ax.set_xlim(-1.8, 6.4); ax.set_ylim(-2.25, 2.35); save(f, 'phi')

# ---------- 11.2 PHANSO: phân số a/b, b ≤ 8
def phanso():
    f, ax = fig(8.4, 4.0)
    N = 8; s = 0.62
    ax.text(-0.75, 0.55, 'mẫu b', ha='center', fontsize=9.5, color=NAVY, fontweight='bold')
    ax.text(3.5 * s + 0.3, 0.55, 'tử a = 1, 2, ..., b − 1', ha='center', fontsize=9.5, color=NAVY, fontweight='bold')
    tot = 0
    for b in range(2, N + 1):
        y = -(b - 2) * 0.5
        ax.text(-0.75, y, str(b), ha='center', va='center', fontsize=10.5, color=NAVY, fontweight='bold')
        cnt = 0
        for a in range(1, b):
            ok = math.gcd(a, b) == 1; cnt += ok
            cellbox(ax, a * s, y, f'{a}/{b}', fc=BLU if ok else GRY, ec=BLC if ok else GRC, w=s - 0.05, h=0.42, fs=9.5,
                    bold=ok, color=TXT if ok else '#9A9A9A')
        tot += cnt
        ax.text(N * s + 0.2, y, f'φ({b}) = {cnt}', va='center', fontsize=9.5, color=GREEN)
    ax.text(N * s + 1.9, -1.5, f'Cộng lại:\n{tot} phân số\ntối giản\nmẫu ≤ {N}', fontsize=10.5, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-1.2, N * s + 3.7); ax.set_ylim(-3.35, 0.85); save(f, 'phanso')

# ---------- 11.3 THAPLT: dãy 2^e mod 12
def thaplt():
    f, ax = fig(9.0, 2.6)
    E = 12; m = 12; w = 0.62
    ax.text(-0.25, 0.55, 'e', ha='right', va='center', fontsize=10.5, color=NAVY, fontweight='bold', style='italic')
    ax.text(-0.45, 0.0, '$2^{e}$ mod 12', ha='right', va='center', fontsize=10, color=NAVY, fontweight='bold')
    for e in range(E):
        v = pow(2, e, m)
        st = (GRY, GRC) if e < 2 else ((YEL, YEC) if e in (4,) else (BLU, BLC))
        ax.text(e * w, 0.55, str(e), ha='center', va='center', fontsize=9.5, color=TXT)
        cellbox(ax, e * w, 0.0, v, fc=st[0], ec=st[1], w=w - 0.06, h=0.45, fs=10.5, color=TXT if e >= 2 else '#808080')
    ax.annotate('', xy=(-0.2, -0.45), xytext=(1.4 * w, -0.45), arrowprops=dict(arrowstyle='<->', color=GRAY, lw=1.2))
    ax.text(0.5 * w, -0.78, 'chưa\ntuần hoàn', ha='center', va='top', fontsize=9.5, color='#707070', linespacing=0.95)
    ax.annotate('', xy=(1.65 * w, -0.45), xytext=((E - 0.6) * w, -0.45), arrowprops=dict(arrowstyle='<->', color=NAVY, lw=1.2))
    ax.text((E / 2 + 0.8) * w, -0.78, 'lặp lại 4, 8, 4, 8, ... (chu kì 2 là ước của φ(12) = 4)', ha='center', va='top', fontsize=9.5, color=NAVY)
    tx = E * w + 0.2
    ax.text(tx, 0.45, '$10^{18}$ mod 4 = 0:', fontsize=10, color=TXT, va='center')
    ax.text(tx, 0.0, 'sai: $2^{0}$ = 1', fontsize=10, color='#808080', va='center')
    ax.text(tx, -0.45, 'đúng: $2^{0 + 4}$ ≡ 4', fontsize=10, color=RED, fontweight='bold', va='center')
    ax.set_xlim(-2.3, tx + 2.6); ax.set_ylim(-1.35, 0.85); save(f, 'thaplt')

# ---------- 12.1 DIEMBINH: gộp từng phương trình
def diembinh():
    f, ax = fig(9.4, 2.4)
    steps = [('(0, 1)', None), ('(2, 3)', 'x ≡ 2 (mod 3)'), ('(8, 15)', 'x ≡ 3 (mod 5)'), ('(23, 105)', 'x ≡ 2 (mod 7)'), ('128', 'x ≥ L = 100')]
    for i, (val, lab) in enumerate(steps):
        x = i * 2.15
        last = i == len(steps) - 1
        cellbox(ax, x, 0, val, fc=YEL if last else (BLU if i else '#F3F6FA'), ec=YEC if last else BLC, w=1.45, h=0.55, fs=11)
        if lab:
            ax.annotate('', xy=(x - 0.76, 0), xytext=(x - 1.39, 0), arrowprops=dict(arrowstyle='-|>', color=GREEN if not last else PURPLE, lw=1.6))
            ax.text(x - 1.075, 0.55, lab, ha='center', va='center', fontsize=10, color=GREEN if not last else PURPLE, fontweight='bold')
    ax.text(0, -0.6, '(r, M): x ≡ r (mod M)', ha='center', fontsize=10, color='#505050')
    ax.text(4 * 2.15, -0.6, '23 + 105 = 128', ha='center', fontsize=9.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.85, 9.5); ax.set_ylim(-0.85, 0.9); save(f, 'diembinh')

# ---------- 12.2 HAIDEN: hai trục thời gian
def haiden():
    f, ax = fig(9.4, 4.0)
    cases = [((2, 3), (3, 5), 0, 'Câu hỏi 1'), ((10, 4), (0, 6), -2.9, 'Câu hỏi 3')]
    T = 22
    for (a1, p1), (a2, p2), y0, name in cases:
        ans = next(t for t in range(max(a1, a2), 200) if (t - a1) % p1 == 0 and (t - a2) % p2 == 0)
        ax.text(-1.0, y0 + 0.2, name, ha='right', va='center', fontsize=11.5, color=NAVY, fontweight='bold')
        for row, (a, p, col, lab) in enumerate([(a1, p1, AMBER, f'đèn 1 (a={a1}, p={p1})'), (a2, p2, TEAL, f'đèn 2 (a={a2}, p={p2})')]):
            y = y0 + 0.55 - row * 0.75
            ax.plot([-0.4, T + 0.4], [y, y], color=LGRAY, lw=1)
            ax.text(T + 0.9, y, lab, va='center', fontsize=11, color=col, fontweight='bold')
            for t in range(a, T + 1, p):
                hit = t == ans
                ax.add_patch(Circle((t, y), 0.24, fc=YEL if hit else ('#FFE7B3' if row == 0 else '#B2E5E0'), ec=RED if hit else col, lw=1.6, zorder=3))
        for t in range(0, T + 1, 2): ax.text(t, y0 - 0.9, str(t), ha='center', va='center', fontsize=10.5, color='#606060')
        # lớp đồng dư nhưng đèn chưa bật (câu 3: t = 6)
        if a1 == 10:
            ax.add_patch(Circle((6, y0 + 0.55), 0.22, fc='white', ec=GRC, lw=1.4, ls='--', zorder=3))
            ax.text(6, y0 + 0.95, 't = 6: đúng số dư nhưng đèn 1 chưa bật', ha='center', fontsize=9.5, color='#707070')
        ax.text(ans, y0 + 1.1, f't = {ans}', ha='center', fontsize=11.5, color=RED, fontweight='bold')
    ax.set_xlim(-3.6, T + 6.6); ax.set_ylim(-4.0, 1.45); save(f, 'haiden')

# ---------- 12.3 CANCHI: bảng 10 × 12
def canchi():
    f, ax = fig(9.4, 5.0)
    can = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
    chi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
    s = 0.66; cell = {}
    for x in range(60): cell[(x % 10, x % 12)] = x
    for j in range(12):
        ax.text(j * s, 0.45, f'{j}', ha='center', va='center', fontsize=9.5, color=NAVY, fontweight='bold')
        ax.text(j * s, 0.75, chi[j], ha='center', va='center', fontsize=9.5, color=NAVY)
    for i in range(10):
        y = -i * 0.42
        ax.text(-0.45, y, f'{can[i]} {i}', ha='right', va='center', fontsize=9.5, color=NAVY, fontweight='bold')
        for j in range(12):
            x = cell.get((i, j))
            if x is None: fc, ec, t = GRY, '#C8C8C8', ''
            elif (i, j) == (2, 6): fc, ec, t = YEL, YEC, x
            else: fc, ec, t = BLU, BLC, x
            ax.add_patch(Rectangle((j * s - s / 2, y - 0.21), s, 0.42, fc=fc, ec=ec if (i, j) == (2, 6) else 'white', lw=1.6 if (i, j) == (2, 6) else 1.0, zorder=2 if (i, j) != (2, 6) else 4))
            if t != '': ax.text(j * s, y, str(t), ha='center', va='center', fontsize=9.5, color=TXT, fontweight='bold' if (i, j) == (2, 6) else 'normal', zorder=5)
    tx = 12 * s + 0.1
    ax.text(tx, -0.6, 'Ô ghi số x: năm thứ x\n(tính từ năm 1984 Giáp Tý)', fontsize=9.5, color=TXT, va='center')
    ax.text(tx, -1.55, 'Bính Ngọ = (2, 6): x = 42,\n42 + 60 = 102, ...\n(1984 + 42 = 2026)', fontsize=9.5, color=RED, fontweight='bold', va='center')
    ax.text(tx, -2.75, 'Ô xám: tên không bao giờ\nxuất hiện, vì Can và Chi\nphải cùng chẵn hoặc cùng lẻ\n(gcd(10, 12) = 2)', fontsize=9.5, color='#505050', va='center')
    ax.text(tx, -3.75, 'Chỉ 60 = lcm(10, 12)\ntrong 120 ô có tên năm', fontsize=9.5, color=NAVY, fontweight='bold', va='center')
    ax.set_xlim(-1.9, tx + 3.6); ax.set_ylim(-4.15, 1.0); save(f, 'canchi')

luythuaq(); somulon(); tonglt(); xacsuat(); nghichdao(); ptdongdu()
phi(); phanso(); thaplt(); diembinh(); haiden(); canchi()
