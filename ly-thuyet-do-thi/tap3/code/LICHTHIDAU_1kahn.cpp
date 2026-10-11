#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("LICHTHIDAU.INP", "r")) {
        freopen("LICHTHIDAU.INP", "r", stdin);
        freopen("LICHTHIDAU.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<pair<int,ll>>> g(n + 1);
    vector<int> in(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int t, a, b; ll c;
        scanf("%d %d %d %lld", &t, &a, &b, &c);
        if (t == 1) { g[b].push_back({a, c}); in[a]++; }   // bỏ qua ràng buộc loại 2
    }
    // đường đi dài nhất trên DAG theo thứ tự tô pô
    vector<ll> d(n + 1, 1);
    queue<int> q; int cnt = 0;
    for (int v = 1; v <= n; v++) if (!in[v]) q.push(v);
    while (!q.empty()) {
        int u = q.front(); q.pop(); cnt++;
        for (auto [v, c] : g[u]) { d[v] = max(d[v], d[u] + c); if (--in[v] == 0) q.push(v); }
    }
    if (cnt < n) { printf("-1\n"); return 0; }
    for (int v = 1; v <= n; v++) printf("%lld%c", d[v], v == n ? '\n' : ' ');
    return 0;
}
