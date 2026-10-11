typedef long long ll;
const ll INF = LLONG_MAX / 4;

// g[u] = danh sách (v, w); trả về khoảng cách ngắn nhất từ s
vector<ll> dijkstra(const vector<vector<pair<int,int>>> &g, int s) {
    vector<ll> d(g.size(), INF);
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<>> pq;
    d[s] = 0; pq.push({0, s});
    while (!pq.empty()) {
        auto [du, u] = pq.top(); pq.pop();
        if (du != d[u]) continue;               // bản cũ: bỏ qua
        for (auto [v, w] : g[u])
            if (d[u] + w < d[v]) { d[v] = d[u] + w; pq.push({d[v], v}); }
    }
    return d;
}
