#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CAPK.INP", "r")) {
        freopen("CAPK.INP", "r", stdin);
        freopen("CAPK.OUT", "w", stdout);
    }
    int n, q;
    scanf("%d %d", &n, &q);
    vector<int> par(n + 1, 0);
    for (int i = 2; i <= n; i++) scanf("%d", &par[i]);
    while (q--) {
        int v, k;
        scanf("%d %d", &v, &k);
        while (k > 0 && v != 0) { v = par[v]; k--; }   // leo từng bậc
        printf("%d\n", v ? v : -1);
    }
    return 0;
}
