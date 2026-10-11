#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    if (fopen("DEMLOTRINH.INP", "r")) {
        freopen("DEMLOTRINH.INP", "r", stdin);
        freopen("DEMLOTRINH.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++) { int u, v; scanf("%d %d", &u, &v); g[u].push_back(v); }
    vector<char> A(n + 1, 0);                   // chỉ lọc các nút tới được từ 1
    vector<int> st = {1}; A[1] = 1;
    while (!st.empty()) { int u = st.back(); st.pop_back(); for (int v : g[u]) if (!A[v]) { A[v] = 1; st.push_back(v); } }
    vector<int> in(n + 1, 0); int tot = 0;
    for (int u = 1; u <= n; u++) if (A[u]) { tot++; for (int v : g[u]) in[v]++; }
    vector<long long> f(n + 1, 0); f[1] = 1;
    queue<int> q; if (!in[1]) q.push(1);
    int done = 0;
    while (!q.empty()) {
        int u = q.front(); q.pop(); done++;
        for (int v : g[u]) { f[v] = (f[v] + f[u]) % MOD; if (--in[v] == 0) q.push(v); }
    }
    if (done < tot) printf("-1\n");             // SAI: mọi vòng đều bị coi là "vô số"
    else printf("%lld\n", f[n]);
    return 0;
}
