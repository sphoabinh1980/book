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
    const ll INF = LLONG_MAX / 4;               // INF + INF vẫn không tràn
    vector<vector<ll>> d(n + 1, vector<ll>(n + 1, INF));
    for (int i = 1; i <= n; i++) d[i][i] = 0;
    for (int i = 0; i < m; i++) {
        int u, v; ll w;
        scanf("%d %d %lld", &u, &v, &w);
        d[u][v] = min(d[u][v], w);              // giữ con đường ngắn nhất giữa một cặp
        d[v][u] = min(d[v][u], w);
    }
    for (int k = 1; k <= n; k++)                // k ở ngoài cùng
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
    int best = 1; ll bs = INF;
    for (int i = 1; i <= n; i++) {
        ll s = 0;
        for (int j = 1; j <= n; j++) s += d[i][j];
        if (s < bs) { bs = s; best = i; }       // "<" giữ số hiệu nhỏ nhất khi bằng nhau
    }
    printf("%d %lld\n", best, bs);
    return 0;
}
