# Hàm dùng chung cho bộ sinh test Tập 3
def S(gen, ntests, check=None):
    """gen(subtask, i, rng) -> input; ntests[k] = số test của subtask k + 1; check(inp, out, ans) -> bool (nếu bài nhiều đáp án)"""
    return {'gen': gen, 'ntests': ntests, 'check': check}
def lines(*rows): return ''.join(' '.join(map(str, r)) + '\n' for r in rows)
