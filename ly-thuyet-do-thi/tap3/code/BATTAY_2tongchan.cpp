#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("BATTAY.INP", "r")) {
        freopen("BATTAY.INP", "r", stdin);
        freopen("BATTAY.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    long long s = 0;
    for (int i = 0; i < n; i++) {
        long long d;
        scanf("%lld", &d);
        s += d;
    }
    if (s % 2 != 0) printf("-1\n");        // chỉ dùng định lí bắt tay
    else printf("%lld\n", s / 2);
    return 0;
}
