#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("ROINHAU.INP", "r")) {
        freopen("ROINHAU.INP", "r", stdin);
        freopen("ROINHAU.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<pair<int,int>>> g(n + 1);     // (nút kề, số hiệu đường)
    for (int i = 1; i <= m; i++) { int u, v; scanf("%d %d", &u, &v); g[u].push_back({v, i}); }
    vector<char> used(m + 1, 0);
    vector<vector<int>> res;
    while (true) {                              // tìm một lộ trình ngắn nhất bằng BFS, rồi xóa các đường của nó
        vector<int> pe(n + 1, -1), pv(n + 1, 0);
        pe[1] = 0;
        queue<int> q; q.push(1);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto [v, id] : g[u]) if (!used[id] && pe[v] < 0) { pe[v] = id; pv[v] = u; q.push(v); }
        }
        if (pe[n] < 0) break;
        vector<int> path;
        for (int v = n; v != 1; v = pv[v]) { path.push_back(v); used[pe[v]] = 1; }
        path.push_back(1);
        reverse(path.begin(), path.end());
        res.push_back(path);
    }
    printf("%d\n", (int)res.size());
    for (auto &p : res) {
        printf("%d", (int)p.size());
        for (int x : p) printf(" %d", x);
        printf("\n");
    }
    return 0;
}
