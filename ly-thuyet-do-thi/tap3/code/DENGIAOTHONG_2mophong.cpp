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
    vector<char> cur(n + 1, 0), nxt;
    cur[1] = 1;
    for (int t = 0; t <= n * P; t++) {          // mô phỏng từng phút: tập nút có thể đang đứng
        if (cur[n]) { printf("%d\n", t); return 0; }
        nxt = cur;
        for (int u = 1; u <= n; u++)
            if (cur[u] && s[u][t % P] == '1') for (int v : g[u]) nxt[v] = 1;
        cur = nxt;
    }
    printf("-1\n");
    return 0;
}
