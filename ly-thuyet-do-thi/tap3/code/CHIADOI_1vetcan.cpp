#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CHIADOI.INP", "r")) {
        freopen("CHIADOI.INP", "r", stdin);
        freopen("CHIADOI.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> u(m), v(m);
    for (int i = 0; i < m; i++) { scanf("%d %d", &u[i], &v[i]); u[i]--; v[i]--; }
    if (n > 25) return 0;                  // 2^n quá lớn
    int best = -1;
    for (int mask = 0; mask < (1 << n); mask++) {   // bit i = 1: bạn i ở đội A
        bool ok = true;
        for (int i = 0; i < m && ok; i++)
            if (((mask >> u[i]) & 1) == ((mask >> v[i]) & 1)) ok = false;
        if (!ok) continue;
        int d = abs(n - 2 * __builtin_popcount(mask));
        if (best < 0 || d < best) best = d;
    }
    printf("%d\n", best);
    return 0;
}
