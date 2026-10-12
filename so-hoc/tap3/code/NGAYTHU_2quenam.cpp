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
        // SAI: khi k < 0, phép % của C++ có thể cho số âm
        printf("%lld\n", (t - 2 + k) % 7 + 2);
    }
    return 0;
}
