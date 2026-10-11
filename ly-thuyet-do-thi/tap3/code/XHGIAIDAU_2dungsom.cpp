#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("XHGIAIDAU.INP", "r")) {
        freopen("XHGIAIDAU.INP", "r", stdin);
        freopen("XHGIAIDAU.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> g(n + 1);
    vector<int> in(n + 1, 0);
    for (int i = 0; i < m; i++) { int a, b; scanf("%d %d", &a, &b); g[a].push_back(b); in[b]++; }
    queue<int> q;
    for (int v = 1; v <= n; v++) if (in[v] == 0) q.push(v);
    vector<int> ord;
    while (!q.empty()) {
        if (q.size() > 1) { printf("0\n"); return 0; }   // SAI: dừng sớm, chưa biết có vòng hay không
        int u = q.front(); q.pop();
        ord.push_back(u);
        for (int v : g[u]) if (--in[v] == 0) q.push(v);
    }
    if ((int)ord.size() < n) printf("-1\n");
    else for (int i = 0; i < n; i++) printf("%d%c", ord[i], i == n - 1 ? '\n' : ' ');
    return 0;
}
