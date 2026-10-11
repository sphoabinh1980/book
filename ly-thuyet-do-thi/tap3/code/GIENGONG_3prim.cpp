#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("GIENGONG.INP", "r")) {
        freopen("GIENGONG.INP", "r", stdin);
        freopen("GIENGONG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<pair<int,ll>>> g(n + 1);
    for (int i = 1; i <= n; i++) { ll a; scanf("%lld", &a); g[0].push_back({i, a}); g[i].push_back({0, a}); }
    for (int i = 0; i < m; i++) { int u, v; ll c; scanf("%d %d %lld", &u, &v, &c); g[u].push_back({v, c}); g[v].push_back({u, c}); }
    vector<ll> d(n + 1, LLONG_MAX); vector<char> in(n + 1, 0);
    d[0] = 0; ll tot = 0;
    for (int it = 0; it <= n; it++) {           // Prim O(n^2) trên n + 1 đỉnh (kể cả đỉnh ảo 0)
        int u = -1;
        for (int v = 0; v <= n; v++) if (!in[v] && (u < 0 || d[v] < d[u])) u = v;
        in[u] = 1; tot += d[u];
        for (auto [v, c] : g[u]) if (!in[v] && c < d[v]) d[v] = c;
    }
    printf("%lld\n", tot);
    return 0;
}
