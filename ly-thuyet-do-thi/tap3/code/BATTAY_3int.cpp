#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("BATTAY.INP", "r")) {
        freopen("BATTAY.INP", "r", stdin);
        freopen("BATTAY.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    int s = 0, mx = 0;                     // LỖI: tổng có thể vượt 2^31
    for (int i = 0; i < n; i++) {
        int d;
        scanf("%d", &d);
        s += d;
        mx = max(mx, d);
    }
    if (s % 2 != 0 || mx > s - mx) printf("-1\n");
    else printf("%d\n", s / 2);
    return 0;
}
