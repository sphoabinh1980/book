#include <bits/stdc++.h>
using namespace std;

vector<int> par;
int root(int x) { while (par[x] != x) { par[x] = par[par[x]]; x = par[x]; } return x; }

int main() {
    if (fopen("XETAI.INP", "r")) {
        freopen("XETAI.INP", "r", stdin);
        freopen("XETAI.OUT", "w", stdout);
    }
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    vector<array<int,3>> e(m);
    for (auto &x : e) scanf("%d %d %d", &x[1], &x[2], &x[0]);
    sort(e.rbegin(), e.rend());                 // cây khung LỚN nhất: cạnh nặng trước
    par.resize(n + 1); iota(par.begin(), par.end(), 0);
    vector<vector<pair<int,int>>> t(n + 1);
    for (auto &x : e) {
        int a = root(x[1]), b = root(x[2]);
        if (a != b) { par[a] = b; t[x[1]].push_back({x[2], x[0]}); t[x[2]].push_back({x[1], x[0]}); }
    }
    // với mỗi đỉnh nguồn, DFS trên cây một lần để có cạnh yếu nhất tới mọi đỉnh
    vector<vector<int>> best(n + 1, vector<int>(n + 1, 0));
    for (int s = 1; s <= n; s++) {
        vector<int> st = {s}; vector<char> vis(n + 1, 0); vis[s] = 1;
        best[s][s] = INT_MAX;
        while (!st.empty()) {
            int u = st.back(); st.pop_back();
            for (auto [v, c] : t[u]) if (!vis[v]) { vis[v] = 1; best[s][v] = min(best[s][u], c); st.push_back(v); }
        }
    }
    while (q--) { int s, x; scanf("%d %d", &s, &x); printf("%d\n", best[s][x]); }
    return 0;
}
