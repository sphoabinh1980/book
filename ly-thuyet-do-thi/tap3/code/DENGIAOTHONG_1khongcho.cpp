#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DENGIAOTHONG.INP", "r")) {
        freopen("DENGIAOTHONG.INP", "r", stdin);
        freopen("DENGIAOTHONG.OUT", "w", stdout);
    }
    int n, m, P;
    cin >> n >> m >> P;
    vector<string> s(n + 1);
    for (int i = 1; i <= n; i++) cin >> s[i];
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++) { int u, v; cin >> u >> v; g[u].push_back(v); g[v].push_back(u); }
    // LỖI: BFS thường, đánh dấu theo nút; tới nút đèn đỏ thì coi như không đi tiếp được ngay
    vector<int> d(n + 1, -1);
    queue<int> q; d[1] = 0; q.push(1);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        int t = d[u];
        while (s[u][t % P] != '1' && t < d[u] + P) t++;  // chờ tới khi đèn xanh
        if (s[u][t % P] != '1') continue;
        for (int v : g[u]) if (d[v] < 0) { d[v] = t + 1; q.push(v); }
    }
    printf("%d\n", n == 1 ? 0 : d[n]);
    return 0;
}
