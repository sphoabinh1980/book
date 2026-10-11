#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("KHOBAU.INP", "r")) {
        freopen("KHOBAU.INP", "r", stdin);
        freopen("KHOBAU.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<ll> a(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    vector<vector<int>> g(n + 1);
    vector<int> in(n + 1, 0);
    for (int i = 0; i < m; i++) { int u, v; scanf("%d %d", &u, &v); g[u].push_back(v); in[v]++; }
    // quy hoạch động theo thứ tự tô pô (Kahn), coi như đồ thị không có chu trình
    vector<ll> best(n + 1, -1);
    best[1] = a[1];
    queue<int> q;
    for (int v = 1; v <= n; v++) if (!in[v]) q.push(v);
    ll ans = a[1];
    while (!q.empty()) {
        int u = q.front(); q.pop();
        if (best[u] >= 0) ans = max(ans, best[u]);
        for (int v : g[u]) {
            if (best[u] >= 0) best[v] = max(best[v], best[u] + a[v]);
            if (--in[v] == 0) q.push(v);
        }
    }
    printf("%lld\n", ans);
    return 0;
}
