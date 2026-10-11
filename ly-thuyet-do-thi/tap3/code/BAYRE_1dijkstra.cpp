#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("BAYRE.INP", "r")) {
        freopen("BAYRE.INP", "r", stdin);
        freopen("BAYRE.OUT", "w", stdout);
    }
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    vector<vector<pair<int,int>>> g(n + 1);
    for (int i = 0; i < m; i++) { int u, v, c; scanf("%d %d %d", &u, &v, &c); g[u].push_back({v, c}); }
    vector<ll> d(n + 1, LLONG_MAX);             // Dijkstra thường: bỏ qua giới hạn k chuyến
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<>> pq;
    d[1] = 0; pq.push({0, 1});
    while (!pq.empty()) {
        auto [du, u] = pq.top(); pq.pop();
        if (du != d[u]) continue;
        for (auto [v, c] : g[u]) if (d[u] + c < d[v]) { d[v] = d[u] + c; pq.push({d[v], v}); }
    }
    printf("%lld\n", d[n] == LLONG_MAX ? -1 : d[n]);
    return 0;
}
