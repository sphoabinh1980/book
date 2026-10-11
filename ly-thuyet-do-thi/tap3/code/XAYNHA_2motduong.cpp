#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("XAYNHA.INP", "r")) {
        freopen("XAYNHA.INP", "r", stdin);
        freopen("XAYNHA.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<ll> t(n + 1);
    vector<vector<int>> g(n + 1), pre(n + 1);
    vector<int> in(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        int k; scanf("%lld %d", &t[i], &k);
        while (k--) { int p; scanf("%d", &p); g[p].push_back(i); pre[i].push_back(p); in[i]++; }
    }
    vector<int> ord; queue<int> q;
    for (int v = 1; v <= n; v++) if (!in[v]) q.push(v);
    while (!q.empty()) { int u = q.front(); q.pop(); ord.push_back(u); for (int v : g[u]) if (--in[v] == 0) q.push(v); }
    vector<ll> es(n + 1, 0);
    ll T = 0; int last = 0;
    for (int u : ord) {
        if (es[u] + t[u] > T) { T = es[u] + t[u]; last = u; }
        for (int v : g[u]) es[v] = max(es[v], es[u] + t[u]);
    }
    vector<int> c;                              // SAI: chỉ lần ngược MỘT đường dài nhất
    for (int u = last; u; ) {
        c.push_back(u);
        int nx = 0;
        for (int p : pre[u]) if (es[p] + t[p] == es[u]) { nx = p; break; }
        u = nx;
    }
    sort(c.begin(), c.end());
    printf("%lld\n%d\n", T, (int)c.size());
    for (size_t i = 0; i < c.size(); i++) printf("%d%c", c[i], i + 1 == c.size() ? '\n' : ' ');
    return 0;
}
