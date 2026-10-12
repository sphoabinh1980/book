# Kiểm tra các chương trình của Chương 1
def ints(s): return list(map(int, s.split()))

def gen_SODU(r):
    L = r.choice([1, 2, 5, 18, 19, 25, 300, 5000])
    s = str(r.randint(1, 9)) + ''.join(str(r.randint(0, 9)) for _ in range(L - 1)) if r.random() < 0.95 else '0'
    m = r.choice([1, 2, 7, 10, r.randint(1, 1000), r.randint(1, 10**9), 10**9])
    return f'{s}\n{m}\n'
def brute_SODU(inp):
    s, m = inp.split(); return str(int(s) % int(m))

SPEC = {
    'SODU': {'gen': gen_SODU, 'brute': brute_SODU},
}
