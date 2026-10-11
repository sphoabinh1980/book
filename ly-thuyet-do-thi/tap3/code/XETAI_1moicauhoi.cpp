#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<pair<int,int>>> g;

bool reach(int s, int t, int W) {               // đi được từ s tới t chỉ dùng cạnh chịu >= W tấn?
    vector<char> vis(n + 1, 0);
    vector<int> st = {s}; vis[s] = 1;
    while (!st.empty()) {
        int u = st.back(); st.pop_back();
        if (u == t) return true;
        for (auto [v, c] : g[u]) if (c >= W && !vis[v]) { vis[v] = 1; st.push_back(v); }
    }
    return false;
}

int main() {
    if (fopen("XETAI.INP", "r")) {
        freopen("XETAI.INP", "r", stdin);
        freopen("XETAI.OUT", "w", stdout);
    }
    int q;
    scanf("%d %d %d", &n, &m, &q);
    g.assign(n + 1, {});
    for (int i = 0; i < m; i++) { int u, v, c; scanf("%d %d %d", &u, &v, &c); g[u].push_back({v, c}); g[v].push_back({u, c}); }
    while (q--) {
        int s, t;
        scanf("%d %d", &s, &t);
        int lo = 0, hi = 1000000000;            // tìm nhị phân tải trọng lớn nhất
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (reach(s, t, mid)) lo = mid; else hi = mid - 1;
        }
        printf("%d\n", lo);
    }
    return 0;
}
