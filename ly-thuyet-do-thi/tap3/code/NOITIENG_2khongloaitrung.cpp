#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("NOITIENG.INP", "r")) {
        freopen("NOITIENG.INP", "r", stdin);
        freopen("NOITIENG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> in(n + 1, 0), out(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        out[u]++; in[v]++;                 // LỖI: dòng bị lặp được đếm nhiều lần
    }
    int ans = -1;
    for (int v = 1; v <= n; v++)
        if (in[v] == n - 1 && out[v] == 0) ans = v;
    printf("%d\n", ans);
    return 0;
}
