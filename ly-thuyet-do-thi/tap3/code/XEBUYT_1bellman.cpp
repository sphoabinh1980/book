#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("XEBUYT.INP", "r")) {
        freopen("XEBUYT.INP", "r", stdin);
        freopen("XEBUYT.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<array<ll,6>> e(m);
    for (auto &x : e) for (int k = 0; k < 6; k++) scanf("%lld", &x[k]);
    const ll INF = LLONG_MAX;
    vector<ll> d(n + 1, INF);
    d[1] = 0;
    bool changed = true;
    while (changed) {                           // nới lỏng mọi tuyến tới khi không đổi
        changed = false;
        for (auto &x : e) {
            int u = x[0], v = x[1]; ll w = x[2], a = x[3], p = x[4], b = x[5];
            if (d[u] == INF) continue;
            ll dep = d[u] <= a ? a : a + (d[u] - a + p - 1) / p * p;
            if (dep <= b && dep + w < d[v]) { d[v] = dep + w; changed = true; }
        }
    }
    printf("%lld\n", d[n] == INF ? -1 : d[n]);
    return 0;
}
