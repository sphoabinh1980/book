#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int n, m;
vector<vector<pair<int,int>>> g;

vector<ll> dijkstra(int s) {
    vector<ll> d(n + 1, LLONG_MAX);
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<>> pq;
    d[s] = 0; pq.push({0, s});
    while (!pq.empty()) {
        auto [du, u] = pq.top(); pq.pop();
        if (du != d[u]) continue;
        for (auto [v, w] : g[u])
            if (d[u] + w < d[v]) { d[v] = d[u] + w; pq.push({d[v], v}); }
    }
    return d;
}

int main() {
    if (fopen("NUTGIAO.INP", "r")) {
        freopen("NUTGIAO.INP", "r", stdin);
        freopen("NUTGIAO.OUT", "w", stdout);
    }
    scanf("%d %d", &n, &m);
    g.assign(n + 1, {});
    for (int i = 0; i < m; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        g[u].push_back({v, w}); g[v].push_back({u, w});
    }
    auto d1 = dijkstra(1), dn = dijkstra(n);
    vector<int> ans;
    for (int v = 1; v <= n; v++)                // LỖI: chỉ kiểm tra v nằm trên MỘT đường ngắn nhất
        if (d1[v] != LLONG_MAX && dn[v] != LLONG_MAX && d1[v] + dn[v] == d1[n]) ans.push_back(v);
    printf("%d\n", (int)ans.size());
    for (size_t i = 0; i < ans.size(); i++) printf("%d%c", ans[i], i + 1 == ans.size() ? '\n' : ' ');
    return 0;
}
