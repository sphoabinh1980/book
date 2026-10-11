#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
struct Route { int v; ll w, a, p, b; };

int main() {
    if (fopen("XEBUYT.INP", "r")) {
        freopen("XEBUYT.INP", "r", stdin);
        freopen("XEBUYT.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<Route>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v; ll w, a, p, b;
        scanf("%d %d %lld %lld %lld %lld", &u, &v, &w, &a, &p, &b);
        g[u].push_back({v, w, a, p, b});
    }
    // d[v]: thời điểm sớm nhất có mặt ở bến v
    vector<ll> d(n + 1, LLONG_MAX);
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<>> pq;
    d[1] = 0;
    pq.push({0, 1});
    while (!pq.empty()) {
        auto [t, u] = pq.top(); pq.pop();
        if (t != d[u]) continue;
        for (auto &r : g[u]) {
            // chuyến sớm nhất xuất bến không trước thời điểm t
            ll dep = t <= r.a ? r.a : r.a + (t - r.a + r.p - 1) / r.p * r.p;
            if (dep > r.b) continue;            // đã hết chuyến
            if (dep + r.w < d[r.v]) {
                d[r.v] = dep + r.w;
                pq.push({d[r.v], r.v});
            }
        }
    }
    printf("%lld\n", d[n] == LLONG_MAX ? -1 : d[n]);
    return 0;
}
