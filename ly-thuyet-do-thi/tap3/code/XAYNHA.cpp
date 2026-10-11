#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("XAYNHA.INP", "r")) {
        freopen("XAYNHA.INP", "r", stdin);
        freopen("XAYNHA.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<ll> t(n + 1);
    vector<vector<int>> g(n + 1);               // cung p -> i: p phải làm trước i
    vector<int> in(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        int k;
        scanf("%lld %d", &t[i], &k);
        while (k--) { int p; scanf("%d", &p); g[p].push_back(i); in[i]++; }
    }
    vector<int> ord;                            // thứ tự tô pô (Kahn)
    queue<int> q;
    for (int v = 1; v <= n; v++) if (!in[v]) q.push(v);
    while (!q.empty()) {
        int u = q.front(); q.pop(); ord.push_back(u);
        for (int v : g[u]) if (--in[v] == 0) q.push(v);
    }
    // lượt xuôi: es[v] = thời điểm bắt đầu sớm nhất
    vector<ll> es(n + 1, 0);
    ll T = 0;
    for (int u : ord) {
        T = max(T, es[u] + t[u]);
        for (int v : g[u]) es[v] = max(es[v], es[u] + t[u]);
    }
    // lượt ngược: lf[v] = thời điểm kết thúc muộn nhất mà không làm dự án trễ
    vector<ll> lf(n + 1, T);
    for (int i = n - 1; i >= 0; i--) {
        int u = ord[i];
        for (int v : g[u]) lf[u] = min(lf[u], lf[v] - t[v]);
    }
    vector<int> c;                              // then chốt: không có thời gian dự trữ
    for (int v = 1; v <= n; v++) if (es[v] + t[v] == lf[v]) c.push_back(v);
    printf("%lld\n%d\n", T, (int)c.size());
    for (size_t i = 0; i < c.size(); i++) printf("%d%c", c[i], i + 1 == c.size() ? '\n' : ' ');
    return 0;
}
