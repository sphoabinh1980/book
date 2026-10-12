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
        long long d = t - 2;                // thứ Hai = 0, ..., CN = 6
        long long r = (d + k % 7) % 7;      // có thể âm khi k < 0
        r = (r + 7) % 7;                    // đưa về đoạn [0, 6]
        printf("%lld\n", r + 2);
    }
    return 0;
}
