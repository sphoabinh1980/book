#include <bits/stdc++.h>
using namespace std;
const int MOD = 1000000007;

int main() {
    if (fopen("TOHOP.INP", "r")) {
        freopen("TOHOP.INP", "r", stdin);
        freopen("TOHOP.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    vector<int> qn(q), qk(q);
    int mx = 0;
    for (int i = 0; i < q; i++) {
        scanf("%d %d", &qn[i], &qk[i]);
        mx = max(mx, qn[i]);
    }
    // c[n][k] = C(n, k) mod MOD: dựng cả tam giác Pascal tới hàng mx
    vector<vector<int>> c(mx + 1);
    for (int n = 0; n <= mx; n++) {
        c[n].assign(n + 1, 1);                 // hai đầu hàng bằng 1
        for (int k = 1; k < n; k++)
            c[n][k] = (c[n - 1][k - 1] + c[n - 1][k]) % MOD;
    }
    for (int i = 0; i < q; i++) {
        int n = qn[i], k = qk[i];
        printf("%d\n", (k < 0 || k > n) ? 0 : c[n][k]);
    }
    return 0;
}
