#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("HUYETMACH.INP", "r")) {
        freopen("HUYETMACH.INP", "r", stdin);
        freopen("HUYETMACH.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<pair<int,int>>> g(n + 1);     // (đỉnh kề, số hiệu đường)
    for (int i = 1; i <= m; i++) {
        int u, v; scanf("%d %d", &u, &v);
        g[u].push_back({v, i}); g[v].push_back({u, i});
    }
    vector<int> num(n + 1, 0), low(n + 1, 0), pe(n + 1, 0), it(n + 1, 0), br;
    int timer = 0;
    for (int s = 1; s <= n; s++) if (!num[s]) {
        // DFS không đệ quy: st giữ đường đi từ gốc tới đỉnh đang xét
        vector<int> st = {s};
        num[s] = low[s] = ++timer;
        while (!st.empty()) {
            int u = st.back();
            if (it[u] < (int)g[u].size()) {
                auto [v, id] = g[u][it[u]++];
                if (id == pe[u]) continue;      // bỏ đúng CON ĐƯỜNG vừa đi tới, không bỏ đỉnh cha
                if (num[v]) low[u] = min(low[u], num[v]);
                else { num[v] = low[v] = ++timer; pe[v] = id; st.push_back(v); }
            } else {                            // u xong: báo kết quả cho cha
                st.pop_back();
                if (!st.empty()) {
                    int p = st.back();
                    low[p] = min(low[p], low[u]);
                    if (low[u] > num[p]) br.push_back(pe[u]);   // cây con của u không "trèo" qua được
                }
            }
        }
    }
    sort(br.begin(), br.end());
    printf("%d\n", (int)br.size());
    for (size_t i = 0; i < br.size(); i++) printf("%d%c", br[i], i + 1 == br.size() ? '\n' : ' ');
    return 0;
}
