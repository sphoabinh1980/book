#include <bits/stdc++.h>
using namespace std;

vector<int> p;
int root(int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }

int main() {
    if (fopen("NOIMANG.INP", "r")) {
        freopen("NOIMANG.INP", "r", stdin);
        freopen("NOIMANG.OUT", "w", stdout);
    }
    int n, k, m;
    scanf("%d %d %d", &n, &k, &m);
    for (int i = 0; i < k; i++) { int u, v; scanf("%d %d", &u, &v); }   // LỖI: bỏ qua cáp có sẵn
    vector<array<int,3>> e(m);
    for (auto &x : e) scanf("%d %d %d", &x[1], &x[2], &x[0]);
    sort(e.begin(), e.end());
    p.resize(n + 1); iota(p.begin(), p.end(), 0);
    int cnt = n; long long tot = 0;
    for (auto &x : e) { int a = root(x[1]), b = root(x[2]); if (a != b) { p[a] = b; cnt--; tot += x[0]; } }
    printf("%lld\n", cnt == 1 ? tot : -1LL);
    return 0;
}
