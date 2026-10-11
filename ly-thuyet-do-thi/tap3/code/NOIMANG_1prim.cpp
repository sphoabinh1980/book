#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("NOIMANG.INP", "r")) {
        freopen("NOIMANG.INP", "r", stdin);
        freopen("NOIMANG.OUT", "w", stdout);
    }
    int n, k, m;
    scanf("%d %d %d", &n, &k, &m);
    vector<vector<pair<int,int>>> g(n + 1);
    for (int i = 0; i < k; i++) { int u, v; scanf("%d %d", &u, &v); g[u].push_back({v, 0}); g[v].push_back({u, 0}); }
    for (int i = 0; i < m; i++) { int u, v, c; scanf("%d %d %d", &u, &v, &c); g[u].push_back({v, c}); g[v].push_back({u, c}); }
    const ll INF = LLONG_MAX;
    vector<ll> d(n + 1, INF); vector<char> in(n + 1, 0);
    d[1] = 0; ll tot = 0;
    for (int it = 0; it < n; it++) {            // Prim O(n^2): tìm đỉnh gần cây nhất bằng vòng lặp
        int u = -1;
        for (int v = 1; v <= n; v++) if (!in[v] && d[v] != INF && (u < 0 || d[v] < d[u])) u = v;
        if (u < 0) { printf("-1\n"); return 0; }
        in[u] = 1; tot += d[u];
        for (auto [v, c] : g[u]) if (!in[v] && c < d[v]) d[v] = c;
    }
    printf("%lld\n", tot);
    return 0;
}
