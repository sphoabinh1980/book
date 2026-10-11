#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("BIENAP.INP", "r")) {
        freopen("BIENAP.INP", "r", stdin);
        freopen("BIENAP.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++) { int u, v; scanf("%d %d", &u, &v); g[u].push_back(v); g[v].push_back(u); }
    vector<int> mark(n + 1, 0);
    vector<pair<int,int>> ans;
    for (int x = 1; x <= n; x++) {              // cho trạm x hỏng, đếm số phần bằng BFS
        mark[x] = x;
        int parts = 0;
        for (int s = 1; s <= n; s++) if (mark[s] != x) {
            parts++;
            queue<int> q; q.push(s); mark[s] = x;
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : g[u]) if (mark[v] != x) { mark[v] = x; q.push(v); }
            }
        }
        if (parts >= 2) ans.push_back({x, parts});
    }
    printf("%d\n", (int)ans.size());
    for (auto [v, c] : ans) printf("%d %d\n", v, c);
    return 0;
}
