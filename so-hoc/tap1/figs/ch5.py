# Hình Chương 5. KĨ THUẬT SỐ HỌC TRONG LẬP TRÌNH
from shlib import *
import math

YEL, BLUE, ORG, GRY = ('#FFD966', RED), ('#BDD7EE', NAVY), ('#FFE7B3', AMBER), ('#EDEDED', '#9A9A9A')
def cb(ax, x, y, t, sty, **k):
    cellbox(ax, x, y, t, fc=sty[0], ec=sty[1], **k)
def arr(ax, a, b, color=NAVY, lw=1.6, rad=0.0, ms=12):
    ax.annotate('', xy=b, xytext=a, arrowprops=dict(arrowstyle='-|>', color=color, lw=lw, mutation_scale=ms,
                connectionstyle=f'arc3,rad={rad}'))

# ---------------- Bài 17
def f17_mang():
    f, ax = fig(8.0, 3.6)
    # số 5040 viết thường -> mảng đảo ngược
    ax.text(-0.3, 3.15, 'Số 5040 viết trên giấy', fontsize=11.5, color=NAVY, fontweight='bold', ha='left')
    names = ['nghìn', 'trăm', 'chục', 'đơn vị']
    for j, d in enumerate('5040'):
        cb(ax, 0.3 + j * 1.0, 2.3, d, ORG)
        ax.text(0.3 + j * 1.0, 1.75, names[j], ha='center', va='top', fontsize=9.5, color='#404040')
    ax.text(5.0, 3.15, 'Mảng a trong máy (đảo ngược)', fontsize=11.5, color=NAVY, fontweight='bold', ha='left')
    for i, d in enumerate([0, 4, 0, 5]):
        cb(ax, 5.6 + i * 1.0, 2.3, d, BLUE)
        ax.text(5.6 + i * 1.0, 1.75, f'a[{i}]', ha='center', va='top', fontsize=10, color=RED, fontweight='bold')
    arr(ax, (4.0, 2.3), (5.05, 2.3), color=AMBER, lw=2)
    ax.text(4.5, 2.55, 'đảo', ha='center', fontsize=9.5, color=AMBER, fontweight='bold')
    ax.text(5.1, 1.05, 'a[i] là chữ số hàng 10ⁱ: chữ số mới (hàng cao hơn)\nchỉ cần push_back vào cuối mảng.',
            fontsize=10, color='#404040', va='center', ha='left')
    # 14! trong cơ số 10^9
    y = -0.35
    ax.text(-0.3, y + 0.75, '14! = 87 178 291 200 trong cơ số 10⁹ (mỗi ô giữ 9 chữ số)', fontsize=11.5, color=NAVY,
            fontweight='bold', ha='left')
    cb(ax, 1.2, y, '87', BLUE, w=1.3)
    cb(ax, 3.6, y, '178291200', BLUE, w=3.0)
    ax.text(1.2, y - 0.5, 'a[1]', ha='center', va='top', fontsize=10, color=RED, fontweight='bold')
    ax.text(3.6, y - 0.5, 'a[0]', ha='center', va='top', fontsize=10, color=RED, fontweight='bold')
    ax.text(5.6, y, '14! = a[1] · 10⁹ + a[0]', fontsize=11, color=TXT, va='center', ha='left')
    ax.set_xlim(-0.5, 10.2); ax.set_ylim(-1.2, 3.5)
    save(f, 'f17_mang')

def f17_nhantay():
    f, ax = fig(8.6, 3.9)
    # bên trái: phép nhân trên giấy
    X = [0.6, 1.3, 2.0, 2.7]
    ax.text(1.6, 3.25, 'Trên giấy', fontsize=11.5, color=NAVY, fontweight='bold', ha='center')
    for x, d in zip(X[1:], '720'): ax.text(x, 2.3, d, fontsize=17, ha='center', va='center', fontweight='bold')
    ax.text(X[0] - 0.1, 1.6, '×', fontsize=17, ha='center', va='center', color=NAVY)
    ax.text(X[3], 1.6, '7', fontsize=17, ha='center', va='center', fontweight='bold')
    ax.plot([0.2, 3.1], [1.15, 1.15], color=TXT, lw=1.6)
    for x, d in zip(X, '5040'): ax.text(x, 0.6, d, fontsize=17, ha='center', va='center', fontweight='bold', color=RED)
    for x, c in ((X[0], '5'), (X[1], '1')): ax.text(x, 2.85, c, fontsize=11, ha='center', va='center', color=RED, fontweight='bold')
    ax.text(1.6, -0.15, 'số nhớ ghi nhỏ, màu đỏ', fontsize=9.5, ha='center', color=RED)
    # bên phải: trên mảng
    x0 = 6.5; dx = 1.75
    ax.text(x0 + 1.5 * dx, 3.25, 'Trên mảng a (a[0] ở bên trái)', fontsize=11.5, color=NAVY, fontweight='bold', ha='center')
    lab = [('i', 2.7), ('a[i] cũ', 2.05), ('t = a[i] · 7 + c', 1.15), ('a[i] = t mod 10', -0.05)]
    for t, y in lab: ax.text(x0 - 0.7, y, t, fontsize=10, ha='right', va='center', color=NAVY, fontweight='bold')
    old = [0, 2, 7, None]; ts = ['0·7 + 0\n= 0', '2·7 + 0\n= 14', '7·7 + 1\n= 50', 'c còn lại\n= 5']
    new = [0, 4, 0, 5]; cs = [0, 1, 5]
    for i in range(4):
        x = x0 + i * dx
        ax.text(x, 2.7, str(i), fontsize=10.5, ha='center', va='center', color=RED, fontweight='bold')
        if old[i] is not None: cb(ax, x, 2.05, old[i], ORG)
        else: cb(ax, x, 2.05, '', GRY)
        ax.text(x, 1.15, ts[i], fontsize=10, ha='center', va='center', color=TXT)
        cb(ax, x, -0.05, new[i], YEL if i == 3 else BLUE)
        if i < 3:
            arr(ax, (x + 0.42, 0.95), (x + dx - 0.42, 0.95), color=RED, lw=1.6)
            ax.text(x + dx / 2, 0.68, f'nhớ {cs[i]}', fontsize=9.5, ha='center', va='center', color=RED, fontweight='bold')
    ax.text(x0 + 3 * dx, -0.62, 'ô mới\n(push_back)', fontsize=9, ha='center', va='top', color=RED)
    ax.set_xlim(-0.2, x0 + 3 * dx + 0.7); ax.set_ylim(-1.3, 3.5)
    save(f, 'f17_nhantay')

def f17_giaithua():
    # số chữ số của n! theo n, so với giới hạn 2^64
    f, ax = plt.subplots(figsize=(7.2, 3.0))
    ns = list(range(0, 41)); L = [len(str(math.factorial(n))) for n in ns]
    cols = [NAVY if n <= 20 else RED for n in ns]
    ax.bar(ns, L, color=cols, width=0.75)
    ax.axhline(19.27, color=AMBER, lw=1.8, ls='--')
    ax.text(0.0, 26.5, 'giới hạn của unsigned long long:\n2⁶⁴ ≈ 1,8 · 10¹⁹ (khoảng 19 chữ số)', fontsize=10, color=AMBER, fontweight='bold')
    ax.annotate('21! có 20 chữ số: bắt đầu tràn', xy=(20.8, 20.6), xytext=(0.0, 40), fontsize=10, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.4, connectionstyle='arc3,rad=-0.2'))
    ax.set_xlabel('n', fontsize=11); ax.set_ylabel('số chữ số của n!', fontsize=10.5)
    ax.set_xlim(-1, 41); ax.set_ylim(0, 50)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=10)
    save(f, 'f17_giaithua')

# ---------------- Bài 18
def f18_bangbit():
    f, ax = fig(8.0, 4.6)
    s = 0.36
    colsk = [3, 2, 1, 0]
    for i in range(16):
        y = -i * s
        ax.text(-0.45, y, str(i), ha='right', va='center', fontsize=10, color=TXT)
        for j, k in enumerate(colsk):
            b = (i >> k) & 1
            x = j * 0.62
            ax.add_patch(Rectangle((x - 0.31, y - s / 2), 0.62, s, fc=('#BDD7EE' if b else 'white'), ec='#A0A0A0', lw=0.8))
            ax.text(x, y, str(b), ha='center', va='center', fontsize=10, color=NAVY if b else '#9A9A9A', fontweight='bold' if b else 'normal')
    for j, k in enumerate(colsk):
        ax.text(j * 0.62, s * 0.95, f'{k}', ha='center', va='bottom', fontsize=10.5, color=RED, fontweight='bold')
    ax.text(-0.45, s * 0.95, 'i', ha='right', va='bottom', fontsize=10.5, color=RED, fontweight='bold', style='italic')
    ax.text(0.93, s * 0.95 + 0.42, 'bit k', ha='center', va='bottom', fontsize=10, color=RED, fontweight='bold')
    ax.add_patch(Rectangle((-0.31, -15 * s - s / 2), 4 * 0.62, 16 * s, fc='none', ec=NAVY, lw=1.8))
    # ngoặc chu kì cho từng cột, vẽ bên phải
    for j, k in enumerate(colsk):
        T = 2 << k; x = 2.9 + j * 1.05
        for st in range(0, 16, T):
            ytop = -st * s + s / 2 - 0.03; ybot = -(st + T - 1) * s - s / 2 + 0.03
            ymid = -(st + (1 << k)) * s + s / 2
            ax.add_patch(Rectangle((x - 0.13, ymid), 0.26, ytop - ymid, fc='white', ec=GRAY, lw=1.0))
            ax.add_patch(Rectangle((x - 0.13, ybot), 0.26, ymid - ybot, fc='#9DC3E6', ec=GRAY, lw=1.0))
        ax.text(x, s * 0.95, f'{T}', ha='center', va='bottom', fontsize=10, color=NAVY, fontweight='bold')
    ax.text(4.45, s * 0.95 + 0.42, 'chu kì của bit 3, 2, 1, 0', ha='center', va='bottom', fontsize=10, color=NAVY, fontweight='bold')
    ax.text(7.2, -1.6, 'Cột bit k lặp lại\nvới chu kì 2ᵏ⁺¹:\n2ᵏ số 0 (trắng)\nrồi 2ᵏ số 1 (xanh).', fontsize=10.5, color=TXT, va='center', ha='left')
    ax.text(7.2, -3.6, 'Bit 0: 0 1 0 1 ...\nBit 1: 0 0 1 1 ...\nBit 2: 0 0 0 0 1 1 1 1 ...', fontsize=10, color='#404040', va='center', ha='left')
    ax.set_xlim(-0.8, 10.2); ax.set_ylim(-16 * s, s * 2.6)
    save(f, 'f18_bangbit')

def f18_chuki():
    # n = 12: các số 0..12, mỗi hàng là một bit, chia theo chu kì
    n = 12
    f, ax = fig(8.6, 3.6)
    w = 0.52
    for i in range(n + 1):
        ax.text(i * w, 0.55, str(i), ha='center', va='center', fontsize=10, color=TXT)
    tot = []
    for k in range(4):
        y = -k * 0.72
        T = 2 << k; p = 1 << k
        ax.text(-0.45, y, f'bit {k}', ha='right', va='center', fontsize=10.5, color=RED, fontweight='bold')
        ones = 0
        for i in range(n + 1):
            b = (i >> k) & 1; ones += b
            full = (i // T) < (n + 1) // T
            fc = ('#BDD7EE' if full else '#FFD966') if b else 'white'
            ax.add_patch(Rectangle((i * w - w / 2, y - 0.25), w, 0.5, fc=fc, ec='#A0A0A0', lw=0.8))
            ax.text(i * w, y, str(b), ha='center', va='center', fontsize=10, color=NAVY if b else '#9A9A9A', fontweight='bold' if b else 'normal')
        for st in range(T, n + 1, T):
            ax.plot([st * w - w / 2] * 2, [y - 0.33, y + 0.33], color=RED, lw=2.4)
        q, r = (n + 1) // T, (n + 1) % T
        ax.text((n + 1) * w - 0.05, y, f'{q} chu kì · {p} + max(0, {r} − {p}) = {ones}', ha='left', va='center', fontsize=10, color=NAVY)
        tot.append(ones)
    ax.text((n + 1) * w - 0.05, -2.75, f'Tổng: {" + ".join(map(str, tot))} = {sum(tot)}', ha='left', va='center', fontsize=11, color=RED, fontweight='bold')
    ax.text(-0.25, -3.35, 'vạch đỏ: ranh giới chu kì;  xanh: bit 1 trong chu kì trọn vẹn;  vàng: bit 1 trong phần dở dang', ha='left', va='center', fontsize=9.5, color='#404040')
    ax.set_xlim(-1.3, 13.4); ax.set_ylim(-3.65, 0.85)
    save(f, 'f18_chuki')

def f18_chia2():
    # chia liên tiếp 2026 cho 2
    f, ax = fig(7.4, 3.0)
    x = 2026; seq = []
    while x: seq.append((x, x % 2)); x //= 2
    dx = 0.62 * 1.0
    for j, (v, r) in enumerate(seq):
        X = j * 1.3
        ax.text(X, 1.2, str(v), ha='center', va='center', fontsize=10.5, color=TXT, fontweight='bold')
        if j + 1 < len(seq): arr(ax, (X + 0.42, 1.2), (X + 1.3 - 0.42, 1.2), color=GRAY, lw=1.2, ms=9)
        cb(ax, X, 0.2, r, YEL if r else GRY, w=0.55, h=0.55, fs=12)
        ax.text(X, -0.32, f'bit {j}', ha='center', va='top', fontsize=9, color=RED)
    ax.text(-0.6, 1.2, 'n', ha='right', va='center', fontsize=11, color=NAVY, fontweight='bold', style='italic')
    ax.text(-0.6, 0.2, 'n mod 2', ha='right', va='center', fontsize=10.5, color=NAVY, fontweight='bold')
    ax.text(6.5, 1.85, '÷ 2 mỗi bước (bỏ bit thấp nhất)', ha='center', fontsize=10, color=GRAY)
    L = (len(seq) - 1) * 1.3
    arr(ax, (L, -0.95), (0, -0.95), color=RED, lw=1.8)
    ax.text(L / 2, -1.15, 'đọc ngược: 2026 = 11111101010 (cơ số 2)', ha='center', va='top', fontsize=11, color=RED, fontweight='bold')
    ax.set_xlim(-2.1, L + 0.5); ax.set_ylim(-1.75, 2.2)
    save(f, 'f18_chia2')

# ---------------- Bài 19
def f19_tiento():
    a = [2, -7, 5, 4, -3, 1]; k = 3
    S = [0]
    for v in a: S.append(S[-1] + v)
    SUB = '₀₁₂₃₄₅₆₇₈₉'
    col = {0: ('#BDD7EE', NAVY), 1: ('#FFD966', RED), 2: ('#CDEBC5', GREEN)}
    f, ax = fig(8.6, 4.6)
    dx = 1.25
    ax.text(-0.7, 2.6, 'a', ha='right', va='center', fontsize=12, color=NAVY, fontweight='bold', style='italic')
    for i, v in enumerate(a):
        cb(ax, (i + 0.5) * dx, 2.6, str(v).replace('-', '−'), ORG)
        ax.text((i + 0.5) * dx, 3.05, 'a' + SUB[i + 1], ha='center', va='bottom', fontsize=10, color='#404040')
    ax.text(-0.7, 1.35, 'S', ha='right', va='center', fontsize=12, color=NAVY, fontweight='bold', style='italic')
    ax.text(-0.7, 0.4, 'S mod 3', ha='right', va='center', fontsize=10.5, color=NAVY, fontweight='bold')
    for j, s in enumerate(S):
        r = s % k; fc, ec = col[r]
        cellbox(ax, j * dx, 1.35, str(s).replace('-', '−'), fc='white', ec=NAVY)
        ax.text(j * dx, 1.8, 'S' + SUB[j], ha='center', va='bottom', fontsize=10, color='#404040')
        node(ax, (j * dx, 0.4), r, r=0.3, fs=13)
        ax.patches[-1].set_facecolor(fc); ax.patches[-1].set_edgecolor(ec)
    # cung nối các cặp cùng số dư, độ sâu chọn tay để nhãn không đè nhau
    H = {(4, 5): 0.4, (2, 4): 0.7, (0, 3): 1.0, (2, 5): 1.3, (1, 6): 1.65}
    for (i, j), h in H.items():
        assert S[i] % k == S[j] % k
        ec = col[S[i] % k][1]
        xs = [i * dx + t / 40 * (j - i) * dx for t in range(41)]
        ys = [0.08 - h * math.sin(math.pi * t / 40) for t in range(41)]
        ax.plot(xs, ys, color=ec, lw=1.8, zorder=1)
        ax.text((i + j) / 2 * dx, 0.08 - h, f'a{SUB[i + 1]}..a{SUB[j]}', ha='center', va='center', fontsize=10.5, color=ec, zorder=6,
                bbox=dict(boxstyle='round,pad=0.12', fc='white', ec=ec, lw=0.8))
    ax.set_xlim(-1.9, 8.0); ax.set_ylim(-1.85, 3.4)
    save(f, 'f19_tiento')

def f19_ngan():
    f, ax = fig(7.6, 2.5)
    data = [(0, ['S0', 'S3'], ('#BDD7EE', NAVY)), (1, ['S2', 'S4', 'S5'], ('#FFD966', RED)), (2, ['S1', 'S6'], ('#CDEBC5', GREEN))]
    for j, (r, items, (fc, ec)) in enumerate(data):
        X = j * 2.9
        ax.add_patch(FancyBboxPatch((X - 1.05, -0.55), 2.1, 1.3, boxstyle='round,pad=0.02,rounding_size=0.12', fc=fc, ec=ec, lw=2, alpha=0.9))
        ax.text(X, 1.0, f'ngăn {r}', ha='center', va='center', fontsize=11, color=ec, fontweight='bold')
        for t, it in enumerate(items):
            ax.text(X - 0.62 + t * 0.62 + (0.31 if len(items) == 2 else 0), 0.1, it, ha='center', va='center', fontsize=11, color=TXT, fontweight='bold')
        c = len(items)
        ax.text(X, -0.85, f'c = {c}: C({c}, 2) = {c * (c - 1) // 2}', ha='center', va='top', fontsize=10.5, color=TXT)
    ax.text(7.9, 0.1, '1 + 3 + 1 = 5', ha='left', va='center', fontsize=12, color=RED, fontweight='bold')
    ax.set_xlim(-1.4, 10.0); ax.set_ylim(-1.35, 1.3)
    save(f, 'f19_ngan')

def f19_rho():
    seq = [0, 2, 6, 4, 1, 3, 11]   # x0 = 0, c = 2, m = 17; 11 -> 4
    f, ax = fig(7.0, 3.0)
    tail = [(0, 0), (1.3, 0), (2.6, 0)]
    cx, cy, R = 4.9, 0, 1.15
    cyc = [(cx + R * math.cos(t), cy + R * math.sin(t)) for t in (math.pi, math.pi / 2, 0, -math.pi / 2)]
    pos = tail + cyc
    for i, v in enumerate(seq):
        node(ax, pos[i], v, 'done' if i < 3 else 'cur', r=0.32, fs=12)
        ax.text(pos[i][0], pos[i][1] + (0.45 if i != 6 else -0.45), 'x' + '₀₁₂₃₄₅₆₇'[i], ha='center', va='center', fontsize=10.5, color='#404040') if i < 3 else None
    for i in range(6): edge(ax, pos[i], pos[i + 1], color=NAVY, directed=True, r=0.34, rad=(-0.35 if i >= 3 else 0), lw=1.8)
    edge(ax, pos[6], pos[3], color=RED, directed=True, r=0.34, rad=-0.35, lw=2)
    labs = {3: (-0.35, -0.48, 'x₃'), 4: (0, 0.5, 'x₄'), 5: (0.62, 0, 'x₅'), 6: (0.6, -0.3, 'x₆')}
    for i, (ox, oy, t) in labs.items(): ax.text(pos[i][0] + ox, pos[i][1] + oy, t, ha='center', va='center', fontsize=10.5, color='#404040')
    ax.text(1.3, -0.85, 'đuôi: μ = 3', ha='center', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(cx, -1.95, 'vòng: λ = 4', ha='center', fontsize=11, color=RED, fontweight='bold')
    ax.text(7.0, 0.55, 'xᵢ₊₁ = (xᵢ² + 2) mod 17\nx₇ = 11² + 2 = 123 ≡ 4\n= x₃: gặp lại!', ha='left', va='center', fontsize=10, color=TXT)
    ax.set_xlim(-0.5, 10.2); ax.set_ylim(-2.3, 1.7)
    save(f, 'f19_rho')

# ---------------- Bài 20
def lattice(ax, X0, X1, Y0, Y1, s=1.0):
    for x in range(X0, X1 + 1): ax.plot([x, x], [Y0 - 0.3, Y1 + 0.3], color='#E3E3E3', lw=0.9, zorder=0)
    for y in range(Y0, Y1 + 1): ax.plot([X0 - 0.3, X1 + 0.3], [y, y], color='#E3E3E3', lw=0.9, zorder=0)
    for x in range(X0, X1 + 1):
        for y in range(Y0, Y1 + 1): ax.plot([x], [y], 'o', ms=2.6, color='#B0B0B0', zorder=1)

def f20_doan():
    f, ax = fig(7.6, 5.0)
    lattice(ax, 0, 14, 0, 10)
    ax.plot([1, 13], [1, 9], color=NAVY, lw=2.4, zorder=2)
    pts = [(1 + 3 * t, 1 + 2 * t) for t in range(5)]
    for i, (x, y) in enumerate(pts):
        ax.plot([x], [y], 'o', ms=11, mfc='#FFD966', mec=RED, mew=2, zorder=5)
        ax.text(x - 0.25, y + 0.4, f'({x}, {y})', ha='right', va='bottom', fontsize=10, color=RED, fontweight='bold')
    # bước (3, 2)
    x, y = pts[1]
    ax.plot([x, x + 3], [y, y], color=GREEN, lw=2, zorder=3); ax.plot([x + 3, x + 3], [y, y + 2], color=GREEN, lw=2, zorder=3)
    ax.text(x + 1.5, y - 0.35, '+3 = 12 / 4', ha='center', va='top', fontsize=10, color=GREEN, fontweight='bold')
    ax.text(x + 3.2, y + 1, '+2 = 8 / 4', ha='left', va='center', fontsize=10, color=GREEN, fontweight='bold')
    ax.text(7.6, 1.6, 'dx = 12, dy = 8\ngcd(12, 8) = 4\n→ 4 bước bằng nhau (3, 2)\n→ 4 + 1 = 5 điểm nguyên', ha='left', va='center', fontsize=11, color=NAVY, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.35', fc='white', ec=NAVY, lw=1.2))
    for x in range(0, 15, 2): ax.text(x, -0.6, str(x), ha='center', va='top', fontsize=9.5, color='#555555')
    for y in range(0, 11, 2): ax.text(-0.6, y, str(y), ha='right', va='center', fontsize=9.5, color='#555555')
    ax.set_xlim(-1.2, 14.6); ax.set_ylim(-1.2, 10.5)
    save(f, 'f20_doan')

def f20_pick():
    P = [(0, 0), (6, 0), (6, 4), (2, 6), (0, 3)]
    f, ax = fig(7.4, 4.6)
    lattice(ax, -1, 7, -1, 7)
    ax.add_patch(Polygon(P, closed=True, fc='#EAF1FA', ec=NAVY, lw=2.2, zorder=2))
    def onb(x, y):
        for i in range(len(P)):
            (ax_, ay), (bx, by) = P[i], P[(i + 1) % len(P)]
            if (bx - ax_) * (y - ay) - (by - ay) * (x - ax_) == 0 and min(ax_, bx) <= x <= max(ax_, bx) and min(ay, by) <= y <= max(ay, by): return True
        return False
    from matplotlib.path import Path
    path = Path(P)
    B = I = 0
    for x in range(-1, 8):
        for y in range(-1, 8):
            if onb(x, y): ax.plot([x], [y], 'o', ms=10, mfc='#FFD966', mec=RED, mew=2, zorder=5); B += 1
            elif path.contains_point((x, y)): ax.plot([x], [y], 'o', ms=9, mfc='#BDD7EE', mec=NAVY, mew=1.6, zorder=5); I += 1
    for (x, y) in P: ax.text(x + (0.2 if x > 3 else -0.2), y + (0.3 if y > 3 else -0.3), f'({x}, {y})', ha='left' if x > 3 else 'right', va='center', fontsize=10, color=NAVY, fontweight='bold')
    tx = 8.4
    ax.plot([tx], [5.6], 'o', ms=10, mfc='#FFD966', mec=RED, mew=2); ax.text(tx + 0.35, 5.6, f'trên biên: B = {B}', va='center', fontsize=11, color=RED, fontweight='bold')
    ax.plot([tx], [4.7], 'o', ms=9, mfc='#BDD7EE', mec=NAVY, mew=1.6); ax.text(tx + 0.35, 4.7, f'bên trong: I = {I}', va='center', fontsize=11, color=NAVY, fontweight='bold')
    ax.text(tx - 0.2, 3.3, 'Diện tích S = 29\n= I + B/2 − 1\n= 22 + 8 − 1', fontsize=11.5, color=TXT, va='center', ha='left')
    assert (B, I) == (16, 22)
    ax.set_xlim(-1.6, 12.6); ax.set_ylim(-1.5, 7.4)
    save(f, 'f20_pick')

f17_mang(); f17_nhantay(); f17_giaithua()
f18_bangbit(); f18_chuki(); f18_chia2()
f19_tiento(); f19_ngan(); f19_rho()
f20_doan(); f20_pick()

from flow import flow
flow('f17_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc n'), ('proc', 'f ← 1; i ← 2'), ('loop', 'i ≤ n ?'),
     ('proc', 'f ← f · i   (64 bit: tràn khi n ≥ 21!)\ni ← i + 1'), ('end', ''), ('io', 'In f'), ('term', 'Kết thúc')])
flow('f17_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc n'), ('proc', 'a ← [1]   (mảng chữ số đảo ngược)'), ('loop', 'còn x ≤ n ?'),
     ('proc', 'c ← 0; với mỗi i:\nt ← a[i] · x + c\na[i] ← t mod 10; c ← t div 10'), ('proc', 'c > 0: thêm các chữ số của c\nvào cuối mảng'), ('end', ''),
     ('io', 'In a từ cuối về đầu'), ('term', 'Kết thúc')])
flow('f18_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc n'), ('proc', 's ← 0'), ('loop', 'còn i ≤ n ?'),
     ('proc', 'x ← i; khi x > 0:\ns ← s + (x and 1); x ← x >> 1'), ('end', ''), ('io', 'In s'), ('term', 'Kết thúc')])
flow('f18_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc n'), ('proc', 's ← 0; k ← 0'), ('loop', '2ᵏ ≤ n ?'),
     ('proc', 'p ← 2ᵏ; T ← 2p\nq ← (n + 1) div T; r ← (n + 1) mod T'), ('proc', 's ← s + q · p + max(0, r − p)\nk ← k + 1'), ('end', ''),
     ('io', 'In s (128 bit)'), ('term', 'Kết thúc')])
flow('f19_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc n, k, a[1..n]'), ('proc', 'ans ← 0'), ('loop', 'còn l ≤ n ?'),
     ('proc', 's ← 0; với r = l..n:\ns ← s + a[r]\nnếu s mod k = 0: ans ← ans + 1'), ('end', ''), ('io', 'In ans'), ('term', 'Kết thúc')])
flow('f19_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc n, k'), ('proc', 'cnt[0] ← 1; s ← 0; ans ← 0'), ('loop', 'còn a[r] ?'),
     ('proc', 's ← (s + a[r]) mod k   (không âm)'), ('proc', 'ans ← ans + cnt[s]\ncnt[s] ← cnt[s] + 1'), ('end', ''), ('io', 'In ans'), ('term', 'Kết thúc')])
flow('f20_ngaytho', [('term', 'Bắt đầu'), ('io', 'Đọc x1, y1, x2, y2'), ('dec', 'x1 = x2 ?', ('In |y2 − y1| + 1', 'io')),
     ('proc', 'cnt ← 0'), ('loop', 'còn x từ x1 tới x2 ?'), ('proc', 'nếu dx | (x − x1) · dy:\ncnt ← cnt + 1'), ('end', ''), ('io', 'In cnt'), ('term', 'Kết thúc')])
flow('f20_toiuu', [('term', 'Bắt đầu'), ('io', 'Đọc x1, y1, x2, y2'), ('proc', 'dx ← |x2 − x1|; dy ← |y2 − y1|'),
     ('proc', 'g ← gcd(dx, dy)   (Euclid)'), ('io', 'In g + 1'), ('term', 'Kết thúc')])
