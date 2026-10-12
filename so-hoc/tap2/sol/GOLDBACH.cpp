#include <bits/stdc++.h>
using namespace std;
bool nt(long long n) {
    if (n < 2) return false;
    if (n < 4) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0) return false;
    return true;
}
int main() {
    if (fopen("GOLDBACH.INP", "r")) {
        freopen("GOLDBACH.INP", "r", stdin); freopen("GOLDBACH.OUT", "w", stdout);
    }
    int q; scanf("%d", &q);
    while (q--) {
        long long n; scanf("%lld", &n);
        if (n % 2 == 1) {                          // n lẻ: một số hạng phải là 2
            if (nt(n - 2)) printf("2 %lld\n", n - 2); else puts("-1");
            continue;
        }
        long long ans = -1;
        for (long long p = 2; p <= n / 2; p++)     // p tăng dần: thử nhanh p trước, n − p sau
            if (nt(p) && nt(n - p)) { ans = p; break; }
        if (ans < 0) puts("-1"); else printf("%lld %lld\n", ans, n - ans);
    }
}
