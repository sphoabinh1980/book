#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("HOHANG.INP", "r")) {
        freopen("HOHANG.INP", "r", stdin);
        freopen("HOHANG.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<int> par(n + 1), dep(n + 1, -1);
    for (int i = 1; i <= n; i++) scanf("%d", &par[i]);
    for (int i = 1; i <= n; i++) {              // độ sâu: leo tới khi gặp đỉnh đã biết
        vector<int> path;
        int v = i;
        while (v && dep[v] < 0) { path.push_back(v); v = par[v]; }
        int d = v ? dep[v] : -1;
        for (int k = path.size() - 1; k >= 0; k--) dep[path[k]] = ++d;
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        int u, v;
        scanf("%d %d", &u, &v);
        int diff = abs(dep[u] - dep[v]);
        while (dep[u] > dep[v]) u = par[u];     // leo từng bậc: O(n) mỗi câu hỏi
        while (dep[v] > dep[u]) v = par[v];
        while (u != v) { u = par[u]; v = par[v]; }
        printf("%d %d\n", u, diff);
    }
    return 0;
}
