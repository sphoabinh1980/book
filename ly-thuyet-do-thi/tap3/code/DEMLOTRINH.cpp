#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;
int n, m;

vector<char> reach(int s, vector<vector<int>> &G) {   // các đỉnh tới được từ s
    vector<char> vis(n + 1, 0);
    vector<int> st = {s}; vis[s] = 1;
    while (!st.empty()) {
        int u = st.back(); st.pop_back();
        for (int v : G[u]) if (!vis[v]) { vis[v] = 1; st.push_back(v); }
    }
    return vis;
}

int main() {
    if (fopen("DEMLOTRINH.INP", "r")) {
        freopen("DEMLOTRINH.INP", "r", stdin);
        freopen("DEMLOTRINH.OUT", "w", stdout);
    }
    scanf("%d %d", &n, &m);
    vector<vector<int>> g(n + 1), rg(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v; scanf("%d %d", &u, &v);
        g[u].push_back(v); rg[v].push_back(u);
    }
    vector<char> A = reach(1, g), B = reach(n, rg);   // A: từ 1 tới được; B: tới được n
    if (!A[n]) { printf("0\n"); return 0; }
    // chỉ giữ các nút "có ích": vừa thuộc A vừa thuộc B
    vector<int> in(n + 1, 0);
    int tot = 0;
    for (int u = 1; u <= n; u++) if (A[u] && B[u]) {
        tot++;
        for (int v : g[u]) if (A[v] && B[v]) in[v]++;
    }
    if (in[1]) { printf("-1\n"); return 0; }   // có vòng quay về 1
    vector<long long> f(n + 1, 0);              // f[v]: số lộ trình 1 -> v (mod)
    f[1] = 1;
    queue<int> q; q.push(1);
    int done = 0;
    while (!q.empty()) {                        // Kahn trên đồ thị con có ích
        int u = q.front(); q.pop(); done++;
        for (int v : g[u]) if (A[v] && B[v]) {
            f[v] = (f[v] + f[u]) % MOD;
            if (--in[v] == 0) q.push(v);
        }
    }
    if (done < tot) printf("-1\n");             // còn nút chưa lấy ra: có vòng trên lộ trình
    else printf("%lld\n", f[n]);
    return 0;
}
