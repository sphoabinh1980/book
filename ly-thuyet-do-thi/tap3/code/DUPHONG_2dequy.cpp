#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> g;
vector<int> comp;
long long cur;

void dfs(int u, int k) {                   // DFS đệ quy
    comp[u] = k; cur++;
    for (int v : g[u]) if (!comp[v]) dfs(v, k);
}

int main() {
    if (fopen("DUPHONG.INP", "r")) {
        freopen("DUPHONG.INP", "r", stdin);
        freopen("DUPHONG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    g.assign(n + 1, {}); comp.assign(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        g[u].push_back(v); g[v].push_back(u);
    }
    vector<long long> sz(1, 0);
    for (int s = 1; s <= n; s++)
        if (!comp[s]) { cur = 0; dfs(s, sz.size()); sz.push_back(cur); }
    long long pairs = 0;
    for (size_t k = 1; k < sz.size(); k++) pairs += sz[k] * (sz[k] - 1) / 2;
    for (int v = 1; v <= n; v++) printf("%lld%c", sz[comp[v]], v == n ? '\n' : ' ');
    vector<long long> s(sz.begin() + 1, sz.end());
    sort(s.rbegin(), s.rend());
    printf("%lld\n%lld\n", pairs, pairs + (s.size() >= 2 ? s[0] * s[1] : 0));
    return 0;
}
