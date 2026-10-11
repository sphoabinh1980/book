#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int n, m;
vector<vector<pair<int,int>>> g;

vector<ll> dijkstra(int s) {
    vector<ll> d(n + 1, LLONG_MAX);
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<>> pq;
    d[s] = 0; pq.push({0, s});
    while (!pq.empty()) {
        auto [du, u] = pq.top(); pq.pop();
        if (du != d[u]) continue;
        for (auto [v, w] : g[u])
            if (d[u] + w < d[v]) { d[v] = d[u] + w; pq.push({d[v], v}); }
    }
    return d;
}

int main() {
    if (fopen("NUTGIAO.INP", "r")) {
        freopen("NUTGIAO.INP", "r", stdin);
        freopen("NUTGIAO.OUT", "w", stdout);
    }
    scanf("%d %d", &n, &m);
    g.assign(n + 1, {});
    vector<array<int,3>> e(m);
    for (auto &x : e) {
        scanf("%d %d %d", &x[0], &x[1], &x[2]);
        g[x[0]].push_back({x[1], x[2]}); g[x[1]].push_back({x[0], x[2]});
    }
    auto d1 = dijkstra(1), dn = dijkstra(n);
    ll D = d1[n];
    auto on = [&](int v) { return d1[v] != LLONG_MAX && dn[v] != LLONG_MAX && d1[v] + dn[v] == D; };
    // Các "mốc" d1 của những đỉnh nằm trên ít nhất một đường ngắn nhất
    vector<ll> val;
    for (int v = 1; v <= n; v++) if (on(v)) val.push_back(d1[v]);
    sort(val.begin(), val.end());
    map<ll,int> same;                           // số đỉnh có cùng mốc
    for (ll x : val) same[x]++;
    val.erase(unique(val.begin(), val.end()), val.end());
    int K = val.size();
    // Cạnh a -> b trên đường ngắn nhất "nhảy qua" mọi mốc nằm hẳn giữa d1[a] và d1[b]
    vector<int> cover(K + 1, 0);                // mảng hiệu
    for (auto &x : e)
        for (int t = 0; t < 2; t++) {
            int a = t ? x[1] : x[0], b = t ? x[0] : x[1];
            if (!on(a) || !on(b) || d1[a] + x[2] + dn[b] != D) continue;
            int l = upper_bound(val.begin(), val.end(), d1[a]) - val.begin();
            int r = lower_bound(val.begin(), val.end(), d1[b]) - val.begin();
            if (l < r) { cover[l]++; cover[r]--; }
        }
    vector<char> key(K);
    for (int i = 0, c = 0; i < K; i++) {
        c += cover[i];
        key[i] = (c == 0 && same[val[i]] == 1);  // không bị nhảy qua, và chỉ có một đỉnh
    }
    vector<int> ans;
    for (int v = 1; v <= n; v++)
        if (on(v) && key[lower_bound(val.begin(), val.end(), d1[v]) - val.begin()]) ans.push_back(v);
    printf("%d\n", (int)ans.size());
    for (size_t i = 0; i < ans.size(); i++) printf("%d%c", ans[i], i + 1 == ans.size() ? '\n' : ' ');
    return 0;
}
