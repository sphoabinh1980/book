#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("THUDO.INP", "r")) {
        freopen("THUDO.INP", "r", stdin);
        freopen("THUDO.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<array<int,3>> e(m);
    for (auto &x : e) scanf("%d %d %d", &x[0], &x[1], &x[2]);
    const ll INF = LLONG_MAX / 4;
    int best = 1; ll bs = INF;
    for (int s = 1; s <= n; s++) {              // Bellman-Ford từ từng thành phố
        vector<ll> d(n + 1, INF);
        d[s] = 0;
        for (int it = 0; it < n - 1; it++) {
            bool ch = false;
            for (auto &x : e) {
                if (d[x[0]] + x[2] < d[x[1]]) { d[x[1]] = d[x[0]] + x[2]; ch = true; }
                if (d[x[1]] + x[2] < d[x[0]]) { d[x[0]] = d[x[1]] + x[2]; ch = true; }
            }
            if (!ch) break;
        }
        ll sum = 0;
        for (int v = 1; v <= n; v++) sum += d[v];
        if (sum < bs) { bs = sum; best = s; }
    }
    printf("%d %lld\n", best, bs);
    return 0;
}
