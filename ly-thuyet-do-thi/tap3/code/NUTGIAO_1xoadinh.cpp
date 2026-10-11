#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int n, m;
vector<vector<pair<int,int>>> g;

ll dijkstra(int banned) {                       // khoảng cách 1 -> n khi cấm đỉnh banned
    vector<ll> d(n + 1, LLONG_MAX);
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<>> pq;
    d[1] = 0; pq.push({0, 1});
    while (!pq.empty()) {
        auto [du, u] = pq.top(); pq.pop();
        if (du != d[u]) continue;
        for (auto [v, w] : g[u])
            if (v != banned && d[u] + w < d[v]) { d[v] = d[u] + w; pq.push({d[v], v}); }
    }
    return d[n];
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
    ll D = dijkstra(0);
    vector<int> ans = {1};
    for (int v = 2; v < n; v++)                 // xóa thử từng đỉnh: n lần Dijkstra
        if (dijkstra(v) > D) ans.push_back(v);
    ans.push_back(n);
    printf("%d\n", (int)ans.size());
    for (size_t i = 0; i < ans.size(); i++) printf("%d%c", ans[i], i + 1 == ans.size() ? '\n' : ' ');
    return 0;
}
