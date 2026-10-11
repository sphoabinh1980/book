def edges_txt(E): return ''.join(f'{u} {v}\n' for u, v in E)
def rand_simple_edges(r, n, m, base=None):
    """m cạnh vô hướng phân biệt, không khuyên."""
    S = set(); E = []
    if base:
        for u, v in base:
            k = (min(u, v), max(u, v))
            if k not in S and u != v: S.add(k); E.append((u, v))
    while len(E) < m:
        u, v = r.randint(1, n), r.randint(1, n)
        if u == v: continue
        k = (min(u, v), max(u, v))
        if k in S: continue
        S.add(k); E.append((u, v))
    r.shuffle(E); return E
def rand_tree(r, n, deep=False):
    """cạnh của cây n đỉnh (deep: gần như đường thẳng)."""
    p = list(range(1, n + 1)); r.shuffle(p); E = []
    for i in range(1, n):
        j = i - 1 if deep and r.random() < 0.97 else r.randint(max(0, i - 50) if deep else 0, i - 1)
        E.append((p[i], p[j]))
    r.shuffle(E); return E
