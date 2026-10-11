#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TAMGIAC.INP", "r")) {
        freopen("TAMGIAC.INP", "r", stdin);
        freopen("TAMGIAC.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> g(n + 1);
    vector<pair<int,int>> e(m);
    for (auto &[u, v] : e) {
        scanf("%d %d", &u, &v);
        g[u].push_back(v); g[v].push_back(u);
    }
    vector<int> mark(n + 1, 0);
    long long cnt = 0;
    for (int i = 0; i < m; i++) {
        auto [u, v] = e[i];
        for (int w : g[u]) mark[w] = i + 1;       // đánh dấu bạn của u
        for (int w : g[v]) if (mark[w] == i + 1) cnt++;
    }
    printf("%lld\n", cnt / 3);
    return 0;
}
