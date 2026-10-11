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
    if (fopen("DUONGONG.INP", "r")) {
        freopen("DUONGONG.INP", "r", stdin);
        freopen("DUONGONG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    Dinic D(n);
    vector<int> U(m + 1), V(m + 1), id(m + 1);
    for (int i = 1; i <= m; i++) { ll c; scanf("%d %d %lld", &U[i], &V[i], &c); id[i] = D.add(U[i], V[i], c); }
    ll F = D.maxflow(1, n);
    vector<int> cut;                            // SAI: in mọi ống đã chảy đầy
    for (int i = 1; i <= m; i++) if (D.e[id[i]].cap == 0) cut.push_back(i);
    printf("%lld\n%d\n", F, (int)cut.size());
    for (size_t i = 0; i < cut.size(); i++) printf("%d%c", cut[i], i + 1 == cut.size() ? '\n' : ' ');
    return 0;
}
