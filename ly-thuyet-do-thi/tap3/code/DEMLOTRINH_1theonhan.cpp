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
    vector<long long> f(n + 1, 0);
    f[1] = 1;
    for (int u = 1; u <= n; u++)                // giả sử mọi đường đều có u < v
        for (int v : g[u]) f[v] = (f[v] + f[u]) % MOD;
    printf("%lld\n", f[n]);
    return 0;
}
