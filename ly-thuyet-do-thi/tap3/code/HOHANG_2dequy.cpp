#include <bits/stdc++.h>
using namespace std;

const int LG = 18;
vector<vector<int>> ch;
vector<array<int, LG + 1>> up;
vector<int> dep;

void dfs(int u) {                               // DFS đệ quy để tính độ sâu và bảng nhảy
    for (int v : ch[u]) {
        dep[v] = dep[u] + 1; up[v][0] = u;
        for (int j = 1; j <= LG; j++) up[v][j] = up[up[v][j - 1]][j - 1];
        dfs(v);
    }
}

int main() {
    if (fopen("HOHANG.INP", "r")) {
        freopen("HOHANG.INP", "r", stdin);
        freopen("HOHANG.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    ch.assign(n + 1, {}); up.resize(n + 1); dep.assign(n + 1, 0);
    int rt = 0;
    for (int i = 1; i <= n; i++) { int p; scanf("%d", &p); if (p) ch[p].push_back(i); else rt = i; }
    up[rt].fill(rt);
    dfs(rt);
    int q;
    scanf("%d", &q);
    while (q--) {
        int u, v;
        scanf("%d %d", &u, &v);
        int diff = abs(dep[u] - dep[v]);
        if (dep[u] < dep[v]) swap(u, v);
        for (int j = LG; j >= 0; j--) if (dep[u] - (1 << j) >= dep[v]) u = up[u][j];
        if (u != v) {
            for (int j = LG; j >= 0; j--) if (up[u][j] != up[v][j]) { u = up[u][j]; v = up[v][j]; }
            u = up[u][0];
        }
        printf("%d %d\n", u, diff);
    }
    return 0;
}
