#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CAPQUANG.INP", "r")) {
        freopen("CAPQUANG.INP", "r", stdin);
        freopen("CAPQUANG.OUT", "w", stdout);
    }
    int n, q;
    scanf("%d %d", &n, &q);
    vector<vector<pair<int,int>>> g(n + 1);
    for (int i = 1; i < n; i++) { int u, v, c; scanf("%d %d %d", &u, &v, &c); g[u].push_back({v, c}); g[v].push_back({u, c}); }
    vector<int> mn(n + 1);
    while (q--) {                               // DFS từ u cho mỗi câu hỏi: O(n)
        int u, v;
        scanf("%d %d", &u, &v);
        fill(mn.begin(), mn.end(), -1);
        mn[u] = INT_MAX; vector<int> st = {u};
        while (!st.empty()) {
            int x = st.back(); st.pop_back();
            for (auto [y, c] : g[x]) if (mn[y] < 0) { mn[y] = min(mn[x], c); st.push_back(y); }
        }
        printf("%d\n", mn[v]);
    }
    return 0;
}
