#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DUPHONG.INP", "r")) {
        freopen("DUPHONG.INP", "r", stdin);
        freopen("DUPHONG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        g[u].push_back(v); g[v].push_back(u);
    }
    vector<long long> sz(n + 1);
    vector<int> seen(n + 1, 0);
    for (int s = 1; s <= n; s++) {         // BFS riêng từ từng máy: O(n·(n + m))
        vector<int> q = {s};
        seen[s] = s;
        for (size_t h = 0; h < q.size(); h++)
            for (int v : g[q[h]]) if (seen[v] != s) { seen[v] = s; q.push_back(v); }
        sz[s] = q.size();
    }
    long long pairs = 0;
    for (int v = 1; v <= n; v++) { printf("%lld%c", sz[v], v == n ? '\n' : ' '); pairs += sz[v] - 1; }
    pairs /= 2;
    // hai nhóm lớn nhất: duyệt các kích thước nhóm (mỗi nhóm s máy xuất hiện s lần)
    map<long long, long long> times;
    for (int v = 1; v <= n; v++) times[sz[v]]++;
    vector<long long> comp;
    for (auto [s, t] : times) for (long long k = 0; k < t / s; k++) comp.push_back(s);
    sort(comp.rbegin(), comp.rend());
    long long best = pairs + (comp.size() >= 2 ? comp[0] * comp[1] : 0);
    printf("%lld\n%lld\n", pairs, best);
    return 0;
}
