#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TAMGIAC.INP", "r")) {
        freopen("TAMGIAC.INP", "r", stdin);
        freopen("TAMGIAC.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> eu(m), ev(m), deg(n + 1, 0);
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &eu[i], &ev[i]);
        deg[eu[i]]++; deg[ev[i]]++;
    }
    // "u thấp hơn v" nếu bậc nhỏ hơn, bằng bậc thì số hiệu nhỏ hơn
    auto low = [&](int u, int v) { return deg[u] < deg[v] || (deg[u] == deg[v] && u < v); };
    vector<vector<int>> out(n + 1);        // mỗi cạnh chỉ giữ chiều từ đỉnh thấp sang đỉnh cao
    for (int i = 0; i < m; i++) {
        int u = eu[i], v = ev[i];
        if (low(u, v)) out[u].push_back(v); else out[v].push_back(u);
    }
    vector<int> mark(n + 1, 0);
    long long cnt = 0;
    for (int u = 1; u <= n; u++) {
        for (int v : out[u]) mark[v] = u;  // đánh dấu các đỉnh cao hơn kề u
        for (int v : out[u])
            for (int w : out[v])
                if (mark[w] == u) cnt++;   // tam giác u < v < w được đếm đúng một lần
    }
    printf("%lld\n", cnt);
    return 0;
}
