#include <bits/stdc++.h>
using namespace std;

vector<int> p;
int root(int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }

int main() {
    if (fopen("CAPDUPHONG.INP", "r")) {
        freopen("CAPDUPHONG.INP", "r", stdin);
        freopen("CAPDUPHONG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<pair<int,int>>> g(n + 1);
    vector<int> U(m + 1), V(m + 1);
    for (int i = 1; i <= m; i++) {
        scanf("%d %d", &U[i], &V[i]);
        g[U[i]].push_back({V[i], i}); g[V[i]].push_back({U[i], i});
    }
    // Bước 1: tìm mọi cầu (num/low, không đệ quy)
    vector<int> num(n + 1, 0), low(n + 1, 0), pe(n + 1, 0), it(n + 1, 0);
    vector<char> isb(m + 1, 0);
    int timer = 0;
    vector<int> st = {1};
    num[1] = low[1] = ++timer;
    while (!st.empty()) {
        int u = st.back();
        if (it[u] < (int)g[u].size()) {
            auto [v, id] = g[u][it[u]++];
            if (id == pe[u]) continue;
            if (num[v]) low[u] = min(low[u], num[v]);
            else { num[v] = low[v] = ++timer; pe[v] = id; st.push_back(v); }
        } else {
            st.pop_back();
            if (!st.empty()) {
                int q = st.back();
                low[q] = min(low[q], low[u]);
                if (low[u] > num[q]) isb[pe[u]] = 1;
            }
        }
    }
    // Bước 2: nén mỗi "khối không cầu" thành một đỉnh (DSU trên các cạnh không phải cầu)
    p.resize(n + 1); iota(p.begin(), p.end(), 0);
    for (int i = 1; i <= m; i++) if (!isb[i]) p[root(U[i])] = root(V[i]);
    // Bước 3: các cầu tạo thành một cây; đếm lá của cây đó
    vector<int> deg(n + 1, 0);
    int comps = 0, leaves = 0;
    for (int v = 1; v <= n; v++) if (root(v) == v) comps++;
    for (int i = 1; i <= m; i++) if (isb[i]) { deg[root(U[i])]++; deg[root(V[i])]++; }
    for (int v = 1; v <= n; v++) if (root(v) == v && deg[v] == 1) leaves++;
    printf("%d\n", comps == 1 ? 0 : (leaves + 1) / 2);
    return 0;
}
