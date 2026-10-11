#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DUONGTRUONG.INP", "r")) {
        freopen("DUONGTRUONG.INP", "r", stdin);
        freopen("DUONGTRUONG.OUT", "w", stdout);
    }
    int n, m, s;
    scanf("%d %d %d", &n, &m, &s);
    vector<vector<pair<int,int>>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        g[u].push_back({v, w});
    }
    const long long INF = LLONG_MAX;
    vector<long long> d(n + 1, INF);
    vector<bool> done(n + 1, false);
    d[s] = 0;
    for (int it = 0; it < n; it++) {
        int u = -1;                         // tìm đỉnh chưa chốt có nhãn nhỏ nhất: O(n)
        for (int v = 1; v <= n; v++)
            if (!done[v] && d[v] != INF && (u < 0 || d[v] < d[u])) u = v;
        if (u < 0) break;
        done[u] = true;
        for (auto [v, w] : g[u]) d[v] = min(d[v], d[u] + w);
    }
    for (int v = 1; v <= n; v++) printf("%lld%c", d[v] == INF ? -1 : d[v], v == n ? '\n' : ' ');
    return 0;
}
