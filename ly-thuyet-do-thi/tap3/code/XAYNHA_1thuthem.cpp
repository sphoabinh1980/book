#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int n;
vector<ll> t;
vector<vector<int>> g;
vector<int> ord;

ll total() {                                    // thời điểm hoàn thành dự án
    vector<ll> es(n + 1, 0);
    ll T = 0;
    for (int u : ord) {
        T = max(T, es[u] + t[u]);
        for (int v : g[u]) es[v] = max(es[v], es[u] + t[u]);
    }
    return T;
}

int main() {
    if (fopen("XAYNHA.INP", "r")) {
        freopen("XAYNHA.INP", "r", stdin);
        freopen("XAYNHA.OUT", "w", stdout);
    }
    scanf("%d", &n);
    t.resize(n + 1); g.resize(n + 1);
    vector<int> in(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        int k; scanf("%lld %d", &t[i], &k);
        while (k--) { int p; scanf("%d", &p); g[p].push_back(i); in[i]++; }
    }
    queue<int> q;
    for (int v = 1; v <= n; v++) if (!in[v]) q.push(v);
    while (!q.empty()) { int u = q.front(); q.pop(); ord.push_back(u); for (int v : g[u]) if (--in[v] == 0) q.push(v); }
    ll T = total();
    vector<int> c;
    for (int i = 1; i <= n; i++) {              // thử kéo dài từng việc thêm 1 ngày
        t[i]++;
        if (total() > T) c.push_back(i);
        t[i]--;
    }
    printf("%lld\n%d\n", T, (int)c.size());
    for (size_t i = 0; i < c.size(); i++) printf("%d%c", c[i], i + 1 == c.size() ? '\n' : ' ');
    return 0;
}
