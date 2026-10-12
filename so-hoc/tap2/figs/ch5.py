# Hình Chương 5 (Tập 2)
from shlib import *
import math

YEL, YEC = '#FFD966', RED          # ô vàng viền đỏ: đáp số / đang xét
BLU, BLC = '#BDD7EE', NAVY         # xanh dương: bình thường / đã xong
ORF, ORC = '#FFE7B3', AMBER        # cam nhạt: dữ liệu vào
GRF, GRC = '#EDEDED', '#9A9A9A'    # xám: bị loại

def digits_row(ax, s, xr, y, fc, ec, w=0.5, fs=12, colors=None, fcs=None):
    """vẽ xâu s căn phải tại cột xr (mỗi chữ số một ô)"""
    for k, ch in enumerate(reversed(s)):
        x = xr - k * w
        cellbox(ax, x, y, ch, fc=(fcs or {}).get(k, fc), ec=ec, w=w - 0.06, h=0.5, fs=fs, color=(colors or {}).get(k, TXT))

# ---------------------------------------------------------------- 17.1
def tonglon():
    f, ax = fig(9.4, 3.5); w = 0.5
    # trái: cộng
    a, b = '98765', '4789'; s = str(int(a) + int(b)); xr = 3.2
    c, carry = 0, {}
    for k in range(6):
        t = (int(a[-1 - k]) if k < len(a) else 0) + (int(b[-1 - k]) if k < len(b) else 0) + c
        c = t // 10
        if c: carry[k + 1] = 1
    ax.text(xr - 2.5 * w, 1.75, 'Cùng dấu: cộng', ha='center', fontsize=11.5, color=NAVY, fontweight='bold')
    for k, v in carry.items(): ax.text(xr - k * w, 1.2, str(v), ha='center', va='center', fontsize=10, color=RED, fontweight='bold')
    ax.text(xr - 6.3 * w, 1.2, 'nhớ', ha='center', va='center', fontsize=9.5, color=RED)
    digits_row(ax, a, xr, 0.6, ORF, ORC); digits_row(ax, b, xr, 0.0, ORF, ORC)
    ax.text(xr - 5.3 * w, 0.0, '+', ha='center', va='center', fontsize=15, color=NAVY, fontweight='bold')
    ax.plot([xr - 5.6 * w, xr + 0.3], [-0.35, -0.35], color=NAVY, lw=1.8)
    digits_row(ax, s, xr, -0.75, YEL, YEC, fcs=None)
    ax.text(xr - 2.5 * w, -1.45, 'số nhớ chỉ là 0 hoặc 1;\nkết quả có thể dài thêm một chữ số', ha='center', va='center', fontsize=9.5, color='#404040')
    # phải: trừ
    a, b = '100000', '1'; xr = 8.9
    ax.text(xr - 2.5 * w, 1.75, 'Khác dấu: lớn trừ nhỏ', ha='center', fontsize=11.5, color=NAVY, fontweight='bold')
    for k in range(1, 6): ax.text(xr - k * w, 1.2, '−1', ha='center', va='center', fontsize=9, color=RED, fontweight='bold')
    ax.text(xr - 6.5 * w, 1.2, 'mượn', ha='center', va='center', fontsize=9.5, color=RED)
    digits_row(ax, a, xr, 0.6, ORF, ORC); digits_row(ax, b, xr, 0.0, ORF, ORC)
    ax.text(xr - 6.3 * w, 0.0, '−', ha='center', va='center', fontsize=15, color=NAVY, fontweight='bold')
    ax.plot([xr - 6.6 * w, xr + 0.3], [-0.35, -0.35], color=NAVY, lw=1.8)
    digits_row(ax, '099999', xr, -0.75, YEL, YEC, fcs={5: GRF}, colors={5: '#9A9A9A'})
    ax.plot([xr - 5 * w - 0.2, xr - 5 * w + 0.2], [-0.95, -0.55], color=RED, lw=2)
    ax.text(xr - 2.5 * w, -1.45, 'mượn lan qua nhiều hàng;\nxóa chữ số 0 thừa ở đầu (ô xám)', ha='center', va='center', fontsize=9.5, color='#404040')
    ax.text(xr + 1.0, 0.3, 'dấu của kết quả\n= dấu của số có\ntrị tuyệt đối\nlớn hơn', ha='left', va='center', fontsize=10, color=PURPLE, fontweight='bold')
    ax.set_xlim(-0.2, 12.6); ax.set_ylim(-1.9, 2.05); save(f, 'tonglon')

# ---------------------------------------------------------------- 17.2
def luythualon():
    f, ax = fig(9.6, 4.2); B = 10**9
    x = 123456789; d = [x * x % B, x * x // B]
    # các bước nhân
    rows, c = [], 0
    for i in range(len(d)):
        t = d[i] * x + c; rows.append((i, d[i], t, t % B, t // B)); c = t // B
    rows.append((len(d), None, None, c, 0))
    ax.text(0, 3.25, f'Nhân d = 123456789² = [{d[0]}, {d[1]}] với x = 123456789 (cơ số 10⁹):', fontsize=12, color=NAVY, fontweight='bold')
    cols = [0.45, 2.15, 5.0, 7.75, 9.65]; head = ['i', 'd[i] cũ', 't = d[i] · x + c', 'd[i] mới', 'c mới']
    for xx, h in zip(cols, head): ax.text(xx, 2.7, h, ha='center', fontsize=12, color=NAVY, fontweight='bold')
    for r, (i, di, t, nd, nc) in enumerate(rows):
        y = 2.2 - r * 0.5
        ax.text(cols[0], y, f'{i}' + (' (mới)' if di is None else ''), ha='center', va='center', fontsize=11.5)
        ax.text(cols[1], y, '—' if di is None else f'{di}', ha='center', va='center', fontsize=11.5)
        ax.text(cols[2], y, 'c còn lại' if t is None else f'{t:,}'.replace(',', ' '), ha='center', va='center', fontsize=11.5)
        cellbox(ax, cols[3], y, nd, fc=YEL if r == len(rows) - 1 else BLU, ec=YEC if r == len(rows) - 1 else BLC, w=1.75, h=0.42, fs=11.5)
        ax.text(cols[4], y, f'{nc}', ha='center', va='center', fontsize=11.5, color=RED, fontweight='bold')
    # in ra
    y = -0.35
    ax.text(0, y + 0.55, 'In 3⁴⁰ = [56928801, 157665459, 12]: ô cao nhất in thường, các ô sau in đủ 9 chữ số', fontsize=12, color=NAVY, fontweight='bold')
    cells = [('12', '%lld'), ('157665459', '%09lld'), ('056928801', '%09lld')]; xx = 1.0
    for k, (s, fm) in enumerate(cells):
        wdt = 0.7 if k == 0 else 1.9
        cellbox(ax, xx + wdt / 2, y - 0.2, s if k < 2 else '', fc=YEL, ec=YEC, w=wdt - 0.08, h=0.5, fs=11.5)
        if k == 2:
            xs = xx + wdt / 2 - 0.62
            ax.text(xs, y - 0.2, '0', ha='right', va='center', fontsize=11.5, color=RED, fontweight='bold', zorder=6)
            ax.text(xs, y - 0.2, s[1:], ha='left', va='center', fontsize=11.5, color=TXT, fontweight='bold', zorder=6)
        ax.text(xx + wdt / 2, y - 0.75, fm, ha='center', va='center', fontsize=11.5, color=PURPLE, family='monospace')
        xx += wdt
    ax.text(xx + 0.3, y - 0.2, '→ 12157665459056928801', va='center', fontsize=11.5, color=RED, fontweight='bold')
    ax.text(xx + 0.3, y - 0.75, '(in "%lld" cả ba ô: mất chữ số 0, sai)', va='center', fontsize=11, color='#404040')
    ax.set_xlim(-0.2, 10.6); ax.set_ylim(-1.15, 3.5); save(f, 'luythualon')

# ---------------------------------------------------------------- 17.3
def tichlon():
    f, ax = fig(9.4, 4.3); B = 10**4
    X, Y = 123456789012, 98765432
    x = [X // B**i % B for i in range(3)]; y = [Y // B**j % B for j in range(2)]
    K = len(x) + len(y)
    c = [0] * (K + 1)
    for i in range(3):
        for j in range(2): c[i + j] += x[i] * y[j]
    cw = 1.9; xr = 9.0
    X0 = lambda k: xr - k * cw
    for k in range(K): ax.text(X0(k), 3.0, f'k = {k}', ha='center', fontsize=11.5, color=NAVY, fontweight='bold')
    for i in range(3): cellbox(ax, X0(i), 2.45, x[i], fc=ORF, ec=ORC, w=cw - 0.2, h=0.45, fs=11)
    for j in range(2): cellbox(ax, X0(j), 1.85, y[j], fc=ORF, ec=ORC, w=cw - 0.2, h=0.45, fs=11)
    ax.text(X0(K - 1) - 1.5, 2.45, 'x', ha='center', va='center', fontsize=13, color=AMBER, fontweight='bold', style='italic')
    ax.text(X0(K - 1) - 1.5, 1.85, 'y', ha='center', va='center', fontsize=13, color=AMBER, fontweight='bold', style='italic')
    ax.plot([X0(K - 1) - cw / 2, xr + cw / 2], [1.5, 1.5], color=NAVY, lw=1.6)
    for j in range(2):
        for i in range(3):
            ax.text(X0(i + j), 1.15 - j * 0.45, f'{x[i]} · {y[j]}', ha='center', va='center', fontsize=11.5, color=TXT)
        ax.text(X0(K - 1) - 1.5, 1.15 - j * 0.45, f'x · y[{j}]', ha='center', va='center', fontsize=11, color='#606060')
    ax.plot([X0(K - 1) - cw / 2, xr + cw / 2], [0.45, 0.45], color=NAVY, lw=1.6)
    for k in range(K): cellbox(ax, X0(k), 0.1, f'{c[k]:,}'.replace(',', ' '), fc=BLU, ec=BLC, w=cw - 0.1, h=0.45, fs=11.5)
    ax.text(X0(K - 1) - 1.5, 0.1, 'c[k]', ha='center', va='center', fontsize=12, color=NAVY, fontweight='bold')
    cc = c[:]; carry = 0
    for k in range(K): cc[k] += carry; carry = cc[k] // B; cc[k] %= B
    for k in range(K): cellbox(ax, X0(k), -0.6, f'{cc[k]:04d}' if k < K - 1 else str(cc[k]), fc=YEL, ec=YEC, w=cw - 0.2, h=0.45, fs=12)
    ax.text(X0(K - 1) - 1.5, -0.6, 'dồn nhớ', ha='center', va='center', fontsize=11.5, color=RED, fontweight='bold')
    ax.text(xr + cw / 2, -1.15, f'{X} · {Y} = {X * Y}', ha='right', va='center', fontsize=12.5, color=RED, fontweight='bold')
    ax.set_xlim(X0(K - 1) - 2.1, xr + cw / 2 + 0.1); ax.set_ylim(-1.4, 3.25); save(f, 'tichlon')

# ---------------------------------------------------------------- 18.1
def doicoso():
    f, ax = fig(9.4, 3.6)
    ax.text(1.9, 2.0, 'Horner: (7EA)₁₆ → giá trị', ha='center', fontsize=11.5, color=NAVY, fontweight='bold')
    steps = [('7', 7, '0 · 16 + 7 = 7'), ('E', 14, '7 · 16 + 14 = 126'), ('A', 10, '126 · 16 + 10 = 2026')]
    for r, (ch, v, txt) in enumerate(steps):
        y = 1.35 - r * 0.6
        cellbox(ax, 0.0, y, ch, fc=ORF, ec=ORC, w=0.5, h=0.45, fs=12)
        ax.text(0.4, y, f'= {v}', va='center', fontsize=10, color=AMBER)
        ax.text(1.4, y, txt, va='center', fontsize=10.5, color=TXT)
    cellbox(ax, 2.3, -0.75, '2026', fc=YEL, ec=YEC, w=1.1, h=0.5, fs=13)
    ax.annotate('', xy=(4.85, 1.2), xytext=(2.95, -0.75), arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=2, connectionstyle='arc3,rad=0.25'))
    ax.text(7.2, 2.0, 'Chia liên tiếp cho 8', ha='center', fontsize=11.5, color=NAVY, fontweight='bold')
    v, rows = 2026, []
    while v: rows.append((v, v // 8, v % 8)); v //= 8
    for r, (n, q, d) in enumerate(rows):
        y = 1.35 - r * 0.55
        ax.text(5.0, y, f'{n} = 8 · {q} + ', va='center', fontsize=10.5, color=TXT)
        cellbox(ax, 7.45, y, d, fc=BLU, ec=BLC, w=0.45, h=0.42, fs=12)
    ax.annotate('', xy=(8.0, 1.45), xytext=(8.0, 1.35 - 3 * 0.55 - 0.1), arrowprops=dict(arrowstyle='-|>', color=RED, lw=2))
    ax.text(8.2, 0.5, 'đọc\nngược', va='center', fontsize=10, color=RED, fontweight='bold')
    ax.text(9.05, 0.5, '→ (3752)₈', va='center', fontsize=13, color=RED, fontweight='bold')
    ax.set_xlim(-0.4, 11.1); ax.set_ylim(-1.15, 2.3); save(f, 'doicoso')

# ---------------------------------------------------------------- 18.2
def bitdoan():
    f, ax = fig(9.4, 3.4); N = 13; s = 0.58; L, R = 5, 7
    for x in range(N):
        cx = x * s
        st = 'q' if L <= x <= R else ('p' if x < L else 'o')
        ax.text(cx, 2.45, str(x), ha='center', va='center', fontsize=10.5, color=RED if st == 'q' else NAVY, fontweight='bold')
        for b in range(4):
            bit = (x >> (3 - b)) & 1
            fc = (YEL if bit else '#FFF6D5') if st == 'q' else ((BLU if bit else '#F3F6FA') if st == 'p' else ('#D0D0D0' if bit else 'white'))
            ec = YEC if st == 'q' else (BLC if st == 'p' else GRC)
            cellbox(ax, cx, 1.95 - b * s, bit, fc=fc, ec=ec, w=s - 0.05, h=s - 0.05, fs=10, bold=bool(bit), color=TXT if bit else '#8C8C8C', lw=1.2)
        ax.text(cx, 1.95 - 4 * s - 0.05, str(bin(x).count('1')), ha='center', va='center', fontsize=10.5, color=RED if st == 'q' else TXT, fontweight='bold')
    for b in range(4): ax.text(-0.75, 1.95 - b * s, f'bit {3 - b}', ha='center', va='center', fontsize=9.5, color='#404040')
    ax.text(-0.75, 1.95 - 4 * s - 0.05, 'số bit 1', ha='center', va='center', fontsize=9.5, color='#404040')
    ax.text(-0.75, 2.45, 'x', ha='center', va='center', fontsize=11, color=NAVY, fontweight='bold', style='italic')
    f7 = sum(bin(x).count('1') for x in range(R + 1)); f4 = sum(bin(x).count('1') for x in range(L))
    tx = N * s + 0.1
    ax.text(tx, 1.8, f'f(7) = {f7}', fontsize=11, color=NAVY, fontweight='bold', va='center')
    ax.text(tx, 1.25, f'f(4) = {f4}', fontsize=11, color=NAVY, va='center')
    ax.text(tx, 0.55, f'[5, 7]: {f7} − {f4} = {f7 - f4}', fontsize=11.5, color=RED, fontweight='bold', va='center')
    ax.text(tx, -0.15, 'f(n) = tổng số bit 1\ncủa 0, 1, ..., n', fontsize=9.5, color='#404040', va='center')
    ax.set_xlim(-1.3, tx + 3.0); ax.set_ylim(-0.75, 2.7); save(f, 'bitdoan')

# ---------------------------------------------------------------- 18.3
def kbit():
    f, ax = fig(9.2, 3.4); s = 0.55; n, k = 12, 2
    bits = [(n >> (3 - b)) & 1 for b in range(4)]
    x0 = 1.0
    ax.text(x0 - 0.9, 2.2, 'n = 12', ha='center', va='center', fontsize=11, color=NAVY, fontweight='bold')
    for b in range(4): cellbox(ax, x0 + b * s, 2.2, bits[b], fc=ORF, ec=ORC, w=s - 0.06, h=0.46, fs=12)
    for b in range(4): ax.text(x0 + b * s, 2.65, f'{3 - b}', ha='center', fontsize=9, color='#606060')
    rows = []
    ones = 0
    for b in range(4):
        i = 3 - b
        if bits[b]:
            pat = bits[:b] + [0] + ['*'] * i
            cnt = math.comb(i, k - ones) if k - ones >= 0 else 0
            ex = [v for v in range(n + 1) if bin(v).count('1') == k and v >> i == (n >> i) - 1]
            rows.append((pat, b, f'C({i}, {k - ones}) = {cnt}', ex)); ones += 1
    rows.append((bits, None, '1 (chính n)', [n]))
    for r, (pat, pos, txt, ex) in enumerate(rows):
        y = 1.45 - r * 0.62
        for b in range(4):
            v = pat[b]
            if v == '*': fc, ec = 'white', GRC
            elif pos is not None and b == pos: fc, ec = YEL, YEC
            elif pos is None: fc, ec = BLU, BLC
            else: fc, ec = BLU, BLC
            cellbox(ax, x0 + b * s, y, v, fc=fc, ec=ec, w=s - 0.06, h=0.46, fs=12, color='#8C8C8C' if v == '*' else TXT)
        ax.text(x0 + 4 * s, y, '→  ' + txt, va='center', fontsize=10.5, color=RED if pos is not None else PURPLE, fontweight='bold')
        ax.text(x0 + 4 * s + 2.5, y, 'số: ' + ', '.join(map(str, ex)), va='center', fontsize=10, color='#404040')
    tot = sum(1 for v in range(1, n + 1) if bin(v).count('1') == k)
    ax.text(x0 + 4 * s, 1.45 - 3 * 0.62 - 0.05, f'Tổng: 3 + 2 + 1 = {tot} số trong [1, 12] có đúng 2 bit 1', va='center', fontsize=10.5, color=NAVY, fontweight='bold')
    ax.text(x0 + 4 * s + 0.15, 2.2, 'ô vàng: bit 1 của n đổi thành 0;  ô xanh: giữ như n;\nô *: tự do, chọn sao cho đủ k = 2 bit 1', va='center', fontsize=9.5, color='#404040')
    ax.set_xlim(-0.3, 8.6); ax.set_ylim(-0.7, 2.85); save(f, 'kbit')

# ---------------------------------------------------------------- 19.1
def tong0():
    f, ax = fig(9.0, 3.6)
    a = [2, -7, 5, 4, -3, 1]; S = [0]
    for v in a: S.append(S[-1] + v)
    sx, sy = 1.1, 0.32
    P = [(i * sx, S[i] * sy) for i in range(7)]
    ax.plot([-0.5, 6 * sx + 0.5], [0, 0], color=LGRAY, lw=1.2, zorder=0)
    ax.plot([p[0] for p in P], [p[1] for p in P], color=GRAY, lw=1.6, zorder=1)
    pairs = [(0, 3, '[1, 3]', RED), (1, 6, '[2, 6]', PURPLE)]
    for t, (i, j, lab, col) in enumerate(pairs):
        ax.plot([P[i][0], P[j][0]], [P[i][1], P[j][1]], color=col, lw=2.2, ls=(0, (4, 3)), zorder=2)
        legend_line(ax, 6 * sx + 0.9, -0.75 - 0.55 * t, col, f'S{i} = S{j} = {S[i]}  →  đoạn {lab}', lw=2.2, dash=True, fs=10.5)
    hit = {0, 1, 3, 6}
    for i, p in enumerate(P):
        node(ax, p, str(S[i]).replace('-', '−'), 'cur' if i in hit else 'done', r=0.27, fs=10.5)
        ax.text(p[0], -2.35, f'S{i}', ha='center', fontsize=10, color=NAVY, fontweight='bold')
    for i, v in enumerate(a):
        ax.text((i + 0.5) * sx, -2.85, f'{v:+d}'.replace('-', '−'), ha='center', fontsize=10, color=AMBER, fontweight='bold')
    ax.text(-0.9, -2.85, 'a', ha='center', fontsize=10.5, color=AMBER, fontweight='bold', style='italic')
    ax.text(6 * sx + 0.9, 0.35, 'Hai tổng tiền tố bằng nhau\n⇔ đoạn ở giữa có tổng 0', va='center', fontsize=10.5, color=NAVY, fontweight='bold')
    ax.set_xlim(-1.2, 11.2); ax.set_ylim(-3.05, 1.65); save(f, 'tong0')

# ---------------------------------------------------------------- 19.2
def doandai():
    f, ax = fig(9.2, 3.0)
    a = [2, -7, 5, 4, -3, 1]; k = 3; S = [0]
    for v in a: S.append(S[-1] + v)
    m = [v % k for v in S]; s = 0.95
    first = {}
    for i, v in enumerate(m): first.setdefault(v, i)
    for i in range(7):
        x = i * s
        ax.text(x, 1.4, f'i = {i}', ha='center', va='center', fontsize=9.5, color=NAVY)
        ax.text(x, 0.9, str(S[i]).replace('-', '−'), ha='center', va='center', fontsize=10, color=TXT)
        isf = first[m[i]] == i
        cellbox(ax, x, 0.0, m[i], fc=BLU if isf else 'white', ec=BLC if isf else GRC, w=0.6, h=0.5, fs=12)
    ax.text(-0.9, 0.9, 'Sᵢ', ha='center', va='center', fontsize=10.5, color='#404040')
    ax.text(-0.9, 0.0, 'Sᵢ mod 3', ha='center', va='center', fontsize=9.5, color='#404040')
    # cung dài nhất
    i, j = first[m[6]], 6
    ax.annotate('', xy=(j * s, -0.3), xytext=(i * s, -0.3), arrowprops=dict(arrowstyle='-|>', color=RED, lw=2.2, connectionstyle='arc3,rad=0.2'))
    ax.text((i + j) / 2 * s, -1.2, 'first[2] = 1, r = 6: đoạn [2, 6], dài 5', ha='center', va='center', fontsize=10.5, color=RED, fontweight='bold')
    i2, j2 = 0, 3
    ax.annotate('', xy=(j2 * s, 0.3), xytext=(i2 * s, 0.3), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.8, connectionstyle='arc3,rad=-0.3'))
    ax.text(7 * s + 0.1, 0.3, 'ô xanh: lần đầu gặp số dư\n(first[0] = 0, first[2] = 1, first[1] = 2)\n\ncung xanh lá: [1, 3], dài 3', va='center', fontsize=9.5, color='#404040')
    ax.set_xlim(-1.6, 11.6); ax.set_ylim(-1.45, 1.6); save(f, 'doandai')

# ---------------------------------------------------------------- 19.3
def hcnchiahet():
    f, ax = fig(9.4, 3.8); s = 0.7
    A = [[1, 2, 3], [4, 5, 6]]; k = 3
    for i in range(2):
        for j in range(3): cellbox(ax, j * s, 2.2 - i * s, A[i][j], fc=ORF, ec=ORC, w=s - 0.05, h=s - 0.05, fs=13)
    ax.add_patch(Rectangle((-s / 2 - 0.06, 2.2 - s - s / 2 - 0.06), 3 * s + 0.12, 2 * s + 0.12, fc='none', ec=RED, lw=2.2, zorder=6))
    ax.text(-0.75, 2.2, 'hàng 1', ha='right', va='center', fontsize=9.5, color='#404040')
    ax.text(-0.75, 2.2 - s, 'hàng 2', ha='right', va='center', fontsize=9.5, color='#404040')
    ax.annotate('', xy=(s, 0.75), xytext=(s, 1.05), arrowprops=dict(arrowstyle='-|>', color=NAVY, lw=2))
    b = [A[0][j] + A[1][j] for j in range(3)]
    for j in range(3): cellbox(ax, j * s, 0.35, b[j], fc=BLU, ec=BLC, w=s - 0.05, h=s - 0.05, fs=13)
    ax.text(-0.75, 0.35, 'tổng cột b', ha='right', va='center', fontsize=9.5, color=NAVY, fontweight='bold')
    # tiền tố của b
    P = [0]
    for v in b: P.append((P[-1] + v) % k)
    x0 = 4.2
    ax.text(x0 + 1.5 * 0.9, 2.85, 'Tiền tố của b theo mô-đun 3', ha='center', fontsize=10.5, color=NAVY, fontweight='bold')
    for t in range(4):
        cellbox(ax, x0 + t * 0.9, 1.6, P[t], fc=YEL if P[t] == 0 else BLU, ec=YEC if P[t] == 0 else BLC, w=0.55, h=0.5, fs=12)
        ax.text(x0 + t * 0.9, 1.05, f'T{t}', ha='center', fontsize=9.5, color='#404040')
    segs = [(0, 2), (0, 3), (2, 3)]
    for u, v in segs:
        ax.annotate('', xy=(x0 + v * 0.9, 1.88), xytext=(x0 + u * 0.9, 1.88),
                    arrowprops=dict(arrowstyle='-', color=RED, lw=1.6, connectionstyle='arc3,rad=-0.45'))
    ax.text(x0 + 1.5 * 0.9, 0.45, 'ba số 0 → C(3, 2) = 3 đoạn:\n[5, 7], [5, 7, 9], [9]', ha='center', va='center', fontsize=10, color=RED, fontweight='bold')
    tx = 8.0
    ax.text(tx, 2.2, 'Mỗi cặp hàng (i₁, i₂):', fontsize=10.5, color=NAVY, fontweight='bold', va='center')
    ax.text(tx, 1.65, '(1, 1): 3 hình', fontsize=10.5, va='center')
    ax.text(tx, 1.2, '(2, 2): 3 hình', fontsize=10.5, va='center')
    ax.text(tx, 0.75, '(1, 2): 3 hình', fontsize=10.5, va='center', color=RED, fontweight='bold')
    ax.text(tx, 0.2, 'Tổng: 9 hình', fontsize=11, va='center', color=NAVY, fontweight='bold')
    ax.set_xlim(-2.0, 10.8); ax.set_ylim(-0.1, 3.1); save(f, 'hcnchiahet')

# ---------------------------------------------------------------- hình học
def lattice(ax, X, Y, s=0.5):
    for x in range(X[0], X[1] + 1): ax.plot([x * s, x * s], [Y[0] * s, Y[1] * s], color='#E3E3E3', lw=0.8, zorder=0)
    for y in range(Y[0], Y[1] + 1): ax.plot([X[0] * s, X[1] * s], [y * s, y * s], color='#E3E3E3', lw=0.8, zorder=0)
    for x in range(X[0], X[1] + 1):
        if x % 2 == 0 or x == X[1]: ax.text(x * s, Y[0] * s - 0.28, str(x), ha='center', va='center', fontsize=8.5, color='#707070')
    for y in range(Y[0], Y[1] + 1):
        if y % 2 == 0 or y == Y[1]: ax.text(X[0] * s - 0.3, y * s, str(y), ha='center', va='center', fontsize=8.5, color='#707070')
def cr(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def onseg(p, a, b): return cr(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
def inside(p, P):
    c = False
    for i in range(len(P)):
        a, b = P[i], P[(i + 1) % len(P)]
        if (a[1] > p[1]) != (b[1] > p[1]):
            if p[0] < a[0] + (p[1] - a[1]) * (b[0] - a[0]) / (b[1] - a[1]): c = not c
    return c

def trongcay():
    f, ax = fig(8.6, 4.4); s = 0.5
    P = [(1, 1), (13, 9), (13, 2)]
    lattice(ax, (0, 14), (0, 10), s)
    for i in range(2): ax.plot([P[i][0] * s, P[i + 1][0] * s], [P[i][1] * s, P[i + 1][1] * s], color=NAVY, lw=2.4, zorder=2)
    pts = [(x, y) for x in range(0, 15) for y in range(0, 11) if any(onseg((x, y), P[i], P[i + 1]) for i in range(2))]
    for p in pts:
        st = 'cur' if p == P[1] else ('wait' if p not in P else 'done')
        node(ax, (p[0] * s, p[1] * s), '', st, r=0.13, lw=1.8)
    ax.text(6.5 * s, 6.3 * s, 'gcd(12, 8) = 4\n→ 5 điểm', ha='center', va='center', fontsize=10, color=NAVY, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none'))
    ax.text(13.6 * s, 5.5 * s, 'gcd(0, 7) = 7\n→ 8 điểm', ha='left', va='center', fontsize=10, color=NAVY, fontweight='bold')
    ax.text(13 * s, 9.75 * s, '(13, 9): đếm 2 lần!', ha='center', va='bottom', fontsize=10, color=RED, fontweight='bold')
    ax.text(16.6 * s, 2.0 * s, '5 + 8 − 1 = 12 cây', ha='left', va='center', fontsize=11.5, color=RED, fontweight='bold')
    ax.set_xlim(-0.6, 11.4); ax.set_ylim(-0.5, 5.4); save(f, 'trongcay')

def poly_points(P, X, Y):
    inn, bd = [], []
    for x in range(X[0], X[1] + 1):
        for y in range(Y[0], Y[1] + 1):
            if any(onseg((x, y), P[i], P[(i + 1) % len(P)]) for i in range(len(P))): bd.append((x, y))
            elif inside((x, y), P): inn.append((x, y))
    return inn, bd

def dagiac():
    f, ax = fig(8.4, 4.0); s = 0.55
    P = [(0, 0), (6, 0), (6, 4), (2, 6), (0, 3)]
    lattice(ax, (0, 7), (0, 6), s)
    ax.add_patch(Polygon([(x * s, y * s) for x, y in P], closed=True, fc='#F3F6FA', ec=NAVY, lw=2.4, zorder=1))
    inn, bd = poly_points(P, (0, 7), (0, 6))
    for p in inn: node(ax, (p[0] * s, p[1] * s), '', 'done', r=0.1, lw=1.6)
    for p in bd: node(ax, (p[0] * s, p[1] * s), '', 'cur', r=0.12, lw=1.8)
    tx = 8.4 * s
    ax.text(tx, 3.0, '2S = 0 + 24 + 28 + 6 + 0 = 58', fontsize=10.5, va='center', color=NAVY)
    ax.text(tx, 2.45, 'B = 6 + 4 + 2 + 1 + 3 = 16', fontsize=10.5, va='center', color=RED, fontweight='bold')
    ax.text(tx, 1.9, f'I = (58 − 16 + 2) / 2 = {len(inn)}', fontsize=10.5, va='center', color=NAVY, fontweight='bold')
    legend_node(ax, tx, 1.1, 'cur', f'trên biên: {len(bd)} điểm', fs=10, r=0.1)
    legend_node(ax, tx, 0.6, 'done', f'bên trong: {len(inn)} điểm', fs=10, r=0.1)
    ax.set_xlim(-0.6, tx + 4.4); ax.set_ylim(-0.45, 3.5); save(f, 'dagiac')

def tamgiac():
    f, ax = fig(8.8, 4.4); s = 0.5
    P = [(1, 1), (13, 9), (13, 2)]
    lattice(ax, (0, 14), (0, 10), s)
    ax.add_patch(Polygon([(x * s, y * s) for x, y in P], closed=True, fc='#F3F6FA', ec=NAVY, lw=2.2, zorder=1))
    inn, bd = poly_points(P, (0, 14), (0, 10))
    for p in inn: node(ax, (p[0] * s, p[1] * s), '', 'done', r=0.09, lw=1.4)
    for p in bd: node(ax, (p[0] * s, p[1] * s), '', 'cur', r=0.11, lw=1.6)
    tx = 15.6 * s
    ax.text(tx, 4.6, 'Tam giác (1, 1), (13, 9), (13, 2)', fontsize=10.5, color=NAVY, fontweight='bold', va='center')
    ax.text(tx, 4.05, '2S = |12 · 1 − 12 · 8| = 84', fontsize=10.5, va='center')
    ax.text(tx, 3.5, 'B = 4 + 7 + 1 = 12', fontsize=10.5, va='center', color=RED, fontweight='bold')
    ax.text(tx, 2.95, f'I = (84 − 12 + 2) / 2 = {len(inn)}', fontsize=10.5, va='center', color=NAVY, fontweight='bold')
    ax.text(tx, 1.9, 'Với tọa độ tới 10¹⁸:', fontsize=10.5, color=PURPLE, fontweight='bold', va='center')
    ax.text(tx, 1.35, '|dx|, |dy| ≤ 2 · 10¹⁸  → long long', fontsize=10, va='center')
    ax.text(tx, 0.85, 'dx · dy ≤ 4 · 10³⁶  → __int128', fontsize=10, va='center')
    ax.text(tx, 0.35, 'I < 2 · 10³⁶ (2⁶⁴ ≈ 1,8 · 10¹⁹)', fontsize=10, va='center')
    ax.set_xlim(-0.6, tx + 5.4); ax.set_ylim(-0.5, 5.0); save(f, 'tamgiac')

tonglon(); luythualon(); tichlon(); doicoso(); bitdoan(); kbit()
tong0(); doandai(); hcnchiahet(); trongcay(); dagiac(); tamgiac()
