#include <bits/stdc++.h>
using namespace std;

const int LG = 17;                              // 2^17 > 1e5
vector<int> p;
int root(int x) {
    while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
    return x;
}

int main() {
    if (fopen("ITDOC.INP", "r")) {
        freopen("ITDOC.INP", "r", stdin);
        freopen("ITDOC.OUT", "w", stdout);
    }
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    vector<array<int,3>> e(m);
    for (auto &x : e) scanf("%d %d %d", &x[1], &x[2], &x[0]);
    // 1) Kruskal: rừng khung nhỏ nhất
    sort(e.begin(), e.end());
    p.resize(n + 1); iota(p.begin(), p.end(), 0);
    vector<vector<pair<int,int>>> g(n + 1);
    for (auto &x : e) {
        int a = root(x[1]), b = root(x[2]);
        if (a == b) continue;
        p[a] = b;
        g[x[1]].push_back({x[2], x[0]}); g[x[2]].push_back({x[1], x[0]});
    }
    // 2) Treo từng cây, tính up[v][j] và mx[v][j] = độ dốc lớn nhất khi nhảy 2^j bước
    vector<array<int, LG + 1>> up(n + 1), mx(n + 1);
    vector<int> dep(n + 1, -1), tree(n + 1);
    for (int s = 1; s <= n; s++) {
        if (dep[s] >= 0) continue;
        dep[s] = 0; tree[s] = s; up[s].fill(s); mx[s].fill(0);
        vector<int> st = {s};
        while (!st.empty()) {
            int u = st.back(); st.pop_back();
            for (auto [v, h] : g[u]) {
                if (dep[v] >= 0) continue;
                dep[v] = dep[u] + 1; tree[v] = s;
                up[v][0] = u; mx[v][0] = h;
                for (int j = 1; j <= LG; j++) {
                    up[v][j] = up[up[v][j - 1]][j - 1];
                    mx[v][j] = max(mx[v][j - 1], mx[up[v][j - 1]][j - 1]);
                }
                st.push_back(v);
            }
        }
    }
    // 3) Mỗi câu hỏi: cạnh lớn nhất trên đường đi trong cây = nhảy tới LCA
    while (q--) {
        int u, v;
        scanf("%d %d", &u, &v);
        if (tree[u] != tree[v]) { printf("-1\n"); continue; }
        int r = 0;
        if (dep[u] < dep[v]) swap(u, v);
        for (int j = LG; j >= 0; j--)
            if (dep[u] - (1 << j) >= dep[v]) { r = max(r, mx[u][j]); u = up[u][j]; }
        if (u != v) {
            for (int j = LG; j >= 0; j--)
                if (up[u][j] != up[v][j]) {
                    r = max({r, mx[u][j], mx[v][j]});
                    u = up[u][j]; v = up[v][j];
                }
            r = max({r, mx[u][0], mx[v][0]});
        }
        printf("%d\n", r);
    }
    return 0;
}
