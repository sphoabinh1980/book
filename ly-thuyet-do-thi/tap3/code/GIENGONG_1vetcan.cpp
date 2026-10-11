#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> p;
int root(int x) { while (p[x] != x) x = p[x]; return x; }

int main() {
    if (fopen("GIENGONG.INP", "r")) {
        freopen("GIENGONG.INP", "r", stdin);
        freopen("GIENGONG.OUT", "w", stdout);
    }
    scanf("%d %d", &n, &m);
    vector<long long> a(n);
    for (auto &x : a) scanf("%lld", &x);
    vector<array<int,3>> e(m);
    for (auto &x : e) scanf("%d %d %d", &x[0], &x[1], &x[2]);
    if (n + m > 24) return 0;                   // 2^(n+m) quá lớn
    long long best = LLONG_MAX;
    for (int wm = 1; wm < (1 << n); wm++)       // tập nhà đào giếng
        for (int em = 0; em < (1 << m); em++) { // tập ống được nối
            p.assign(n + 2, 0); iota(p.begin(), p.end(), 0);
            long long c = 0;
            for (int i = 0; i < n; i++) if (wm >> i & 1) { c += a[i]; p[root(i + 1)] = root(0); }
            for (int j = 0; j < m; j++) if (em >> j & 1) { c += e[j][2]; p[root(e[j][0])] = root(e[j][1]); }
            bool ok = true;
            for (int v = 1; v <= n; v++) if (root(v) != root(0)) ok = false;
            if (ok) best = min(best, c);
        }
    printf("%lld\n", best);
    return 0;
}
