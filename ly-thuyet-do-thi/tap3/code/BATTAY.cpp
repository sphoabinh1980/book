#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("BATTAY.INP", "r")) {
        freopen("BATTAY.INP", "r", stdin);
        freopen("BATTAY.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    long long s = 0, mx = 0;               // tổng tới 1e14: phải dùng long long
    for (int i = 0; i < n; i++) {
        long long d;
        scanf("%lld", &d);
        s += d;
        mx = max(mx, d);
    }
    // Điều kiện cần và đủ: tổng chẵn, và người nhiều nhất không vượt tổng của những người còn lại
    if (s % 2 != 0 || mx > s - mx) printf("-1\n");
    else printf("%lld\n", s / 2);
    return 0;
}
