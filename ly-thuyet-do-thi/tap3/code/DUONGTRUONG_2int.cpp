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
    vector<int> d(n + 1, INT_MAX);          // LỖI: khoảng cách có thể vượt 2^31
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    d[s] = 0; pq.push({0, s});
    while (!pq.empty()) {
        auto [du, u] = pq.top(); pq.pop();
        if (du != d[u]) continue;
        for (auto [v, w] : g[u])
            if (d[u] + w < d[v]) { d[v] = d[u] + w; pq.push({d[v], v}); }
    }
    for (int v = 1; v <= n; v++) printf("%d%c", d[v] == INT_MAX ? -1 : d[v], v == n ? '\n' : ' ');
    return 0;
}
