#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("NGAYTHU.INP", "r")) {
        freopen("NGAYTHU.INP", "r", stdin);
        freopen("NGAYTHU.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        long long t, k;
        scanf("%lld %lld", &t, &k);
        int d = t - 2;
        long long step = (k > 0) ? 1 : -1;  // tiến hoặc lùi
        for (long long i = 0; i != k; i += step)
            d = (d + step + 7) % 7;         // mỗi lần đi một ngày
        printf("%d\n", d + 2);
    }
    return 0;
}
