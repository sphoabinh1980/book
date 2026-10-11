#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
struct E { int v; ll w, a, p, b; };

int main() {
    if (fopen("XEBUYT.INP", "r")) {
        freopen("XEBUYT.INP", "r", stdin);
        freopen("XEBUYT.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<E>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v; ll w, a, p, b;
        scanf("%d %d %lld %lld %lld %lld", &u, &v, &w, &a, &p, &b);
        g[u].push_back({v, w, a, p, b});
    }
    vector<ll> d(n + 1, LLONG_MAX);
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<>> pq;
    d[1] = 0; pq.push({0, 1});
    while (!pq.empty()) {
        auto [t, u] = pq.top(); pq.pop();
        if (t != d[u]) continue;
        for (auto &e : g[u])                    // LỖI: coi như xe đi ngay khi Bình tới bến
            if (t <= e.b && t + e.w < d[e.v]) { d[e.v] = t + e.w; pq.push({d[e.v], e.v}); }
    }
    printf("%lld\n", d[n] == LLONG_MAX ? -1 : d[n]);
    return 0;
}
