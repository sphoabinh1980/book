#include <bits/stdc++.h>
using namespace std;

const int LG = 20;                              // 2^20 > 1e6

int main() {
    if (fopen("CAPK.INP", "r")) {
        freopen("CAPK.INP", "r", stdin);
        freopen("CAPK.OUT", "w", stdout);
    }
    int n, q;
    scanf("%d %d", &n, &q);
    // up[j][v]: cấp trên thứ 2^j của v (0 nếu không có) — 21 · (n + 1) số nguyên
    vector<vector<int>> up(LG + 1, vector<int>(n + 1, 0));
    for (int i = 2; i <= n; i++) scanf("%d", &up[0][i]);
    for (int j = 1; j <= LG; j++)
        for (int v = 1; v <= n; v++) up[j][v] = up[j - 1][up[j - 1][v]];
    while (q--) {
        int v, k;
        scanf("%d %d", &v, &k);
        if (k > n) { printf("-1\n"); continue; }
        for (int j = 0; j <= LG && v; j++) if (k >> j & 1) v = up[j][v];
        printf("%d\n", v ? v : -1);
    }
    return 0;
}
