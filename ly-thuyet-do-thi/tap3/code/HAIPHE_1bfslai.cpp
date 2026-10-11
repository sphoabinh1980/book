#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("HAIPHE.INP", "r")) {
        freopen("HAIPHE.INP", "r", stdin);
        freopen("HAIPHE.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<pair<int,int>>> g(n + 1);
    for (int i = 1; i <= m; i++) {
        int a, b, t;
        scanf("%d %d %d", &a, &b, &t);
        g[a].push_back({b, t}); g[b].push_back({a, t});
        // kiểm tra lại toàn bộ bằng cách tô màu: O(n + i)
        vector<int> col(n + 1, -1);
        for (int s = 1; s <= n; s++) {
            if (col[s] >= 0) continue;
            col[s] = 0; vector<int> st = {s};
            while (!st.empty()) {
                int u = st.back(); st.pop_back();
                for (auto [v, w] : g[u]) {
                    if (col[v] < 0) { col[v] = col[u] ^ w; st.push_back(v); }
                    else if (col[v] != (col[u] ^ w)) { printf("%d\n", i); return 0; }
                }
            }
        }
    }
    printf("0\n");
    return 0;
}
