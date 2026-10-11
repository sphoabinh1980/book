#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CHIADOI.INP", "r")) {
        freopen("CHIADOI.INP", "r", stdin);
        freopen("CHIADOI.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++) { int u, v; scanf("%d %d", &u, &v); g[u].push_back(v); g[v].push_back(u); }
    vector<int> col(n + 1, -1), diffs;
    for (int s = 1; s <= n; s++) if (col[s] < 0) {
        int c[2] = {0, 0}; col[s] = 0; vector<int> q = {s};
        for (size_t h = 0; h < q.size(); h++) {
            int u = q[h]; c[col[u]]++;
            for (int v : g[u]) {
                if (col[v] < 0) { col[v] = col[u] ^ 1; q.push_back(v); }
                else if (col[v] == col[u]) { printf("-1\n"); return 0; }
            }
        }
        diffs.push_back(abs(c[0] - c[1]));
    }
    // Tham lam: xét các hiệu từ lớn tới nhỏ, đưa phía đông hơn về đội đang ít người hơn
    sort(diffs.rbegin(), diffs.rend());
    long long cur = 0;
    for (int d : diffs) cur = (cur >= 0 ? cur - d : cur + d);
    printf("%lld\n", llabs(cur));
    return 0;
}
