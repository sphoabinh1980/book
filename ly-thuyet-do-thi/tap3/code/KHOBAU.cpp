#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("KHOBAU.INP", "r")) {
        freopen("KHOBAU.INP", "r", stdin);
        freopen("KHOBAU.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<ll> a(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    vector<vector<int>> g(n + 1);
    vector<pair<int,int>> e(m);
    for (auto &x : e) { scanf("%d %d", &x.first, &x.second); g[x.first].push_back(x.second); }
    // Tarjan không đệ quy (như bài TINDON)
    vector<int> num(n + 1, 0), low(n + 1, 0), comp(n + 1, -1), it(n + 1, 0), S, cs;
    vector<char> onS(n + 1, 0);
    int timer = 0, c = 0;
    for (int s = 1; s <= n; s++) if (!num[s]) {
        cs.push_back(s); num[s] = low[s] = ++timer; S.push_back(s); onS[s] = 1;
        while (!cs.empty()) {
            int u = cs.back();
            if (it[u] < (int)g[u].size()) {
                int v = g[u][it[u]++];
                if (!num[v]) { num[v] = low[v] = ++timer; S.push_back(v); onS[v] = 1; cs.push_back(v); }
                else if (onS[v]) low[u] = min(low[u], num[v]);
            } else {
                cs.pop_back();
                if (!cs.empty()) low[cs.back()] = min(low[cs.back()], low[u]);
                if (low[u] == num[u]) {
                    int v;
                    do { v = S.back(); S.pop_back(); onS[v] = 0; comp[v] = c; } while (v != u);
                    c++;
                }
            }
        }
    }
    // nén: mỗi thành phần là một "siêu địa điểm" có w = tổng vàng
    vector<ll> w(c, 0);
    for (int v = 1; v <= n; v++) w[comp[v]] += a[v];
    vector<vector<int>> h(c);
    for (auto &x : e) if (comp[x.first] != comp[x.second]) h[comp[x.first]].push_back(comp[x.second]);
    // Tarjan đánh số theo thứ tự tô pô NGƯỢC: cung luôn đi từ số lớn sang số nhỏ
    vector<ll> best(c, -1);                     // best[x]: vàng nhiều nhất khi tới thành phần x
    int s = comp[1];
    best[s] = w[s];
    ll ans = 0;
    for (int x = s; x >= 0; x--) if (best[x] >= 0) {
        ans = max(ans, best[x]);
        for (int y : h[x]) best[y] = max(best[y], best[x] + w[y]);
    }
    printf("%lld\n", ans);
    return 0;
}
