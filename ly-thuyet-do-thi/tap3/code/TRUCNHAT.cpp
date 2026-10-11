#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

struct Dinic {                                  // luồng cực đại, thuật toán Dinic
    struct E { int to; ll cap; };
    vector<E> e;
    vector<vector<int>> g;
    vector<int> lv, it;
    Dinic(int n) : g(n + 1), lv(n + 1), it(n + 1) {}
    int add(int u, int v, ll c) {               // cung u -> v và cung ngược v -> u (dung lượng 0)
        e.push_back({v, c}); g[u].push_back(e.size() - 1);
        e.push_back({u, 0}); g[v].push_back(e.size() - 1);
        return e.size() - 2;
    }
    bool bfs(int s, int t) {                    // chia tầng theo khoảng cách trên đồ thị thặng dư
        fill(lv.begin(), lv.end(), -1); lv[s] = 0;
        queue<int> q; q.push(s);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int id : g[u]) if (e[id].cap > 0 && lv[e[id].to] < 0) { lv[e[id].to] = lv[u] + 1; q.push(e[id].to); }
        }
        return lv[t] >= 0;
    }
    ll dfs(int u, int t, ll f) {                // đẩy luồng theo các cung đi lên đúng một tầng
        if (u == t) return f;
        for (int &i = it[u]; i < (int)g[u].size(); i++) {
            int id = g[u][i], v = e[id].to;
            if (e[id].cap > 0 && lv[v] == lv[u] + 1) {
                ll d = dfs(v, t, min(f, e[id].cap));
                if (d > 0) { e[id].cap -= d; e[id ^ 1].cap += d; return d; }
            }
        }
        return 0;
    }
    ll maxflow(int s, int t) {
        ll F = 0;
        while (bfs(s, t)) {
            fill(it.begin(), it.end(), 0);
            while (ll f = dfs(s, t, LLONG_MAX)) F += f;
        }
        return F;
    }
};

int main() {
    if (fopen("TRUCNHAT.INP", "r")) {
        freopen("TRUCNHAT.INP", "r", stdin);
        freopen("TRUCNHAT.OUT", "w", stdout);
    }
    int n, d;
    scanf("%d %d", &n, &d);
    // nguồn s -> học sinh i (dung lượng a[i]) -> ngày j (1) -> đích t (b[j])
    int s = n + d + 1, t = n + d + 2;
    Dinic D(t);
    ll need = 0;
    for (int i = 1; i <= n; i++) { int a; scanf("%d", &a); D.add(s, i, a); }
    for (int j = 1; j <= d; j++) { int b; scanf("%d", &b); D.add(n + j, t, b); need += b; }
    vector<array<int,3>> e;                     // (học sinh, ngày, số hiệu cung)
    for (int i = 1; i <= n; i++) {
        int k; scanf("%d", &k);
        while (k--) { int j; scanf("%d", &j); e.push_back({i, j, D.add(i, n + j, 1)}); }
    }
    if (D.maxflow(s, t) != need) { printf("NO\n"); return 0; }   // không lấp đầy mọi ngày
    vector<vector<int>> day(d + 1);
    for (auto &x : e) if (D.e[x[2]].cap == 0) day[x[1]].push_back(x[0]);   // cung có luồng: i trực ngày j
    printf("YES\n");
    for (int j = 1; j <= d; j++) {
        for (size_t i = 0; i < day[j].size(); i++) printf("%d ", day[j][i]);
        printf("\n");
    }
    return 0;
}
