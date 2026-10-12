#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("CHUSO0.INP", "r")) {
        freopen("CHUSO0.INP", "r", stdin); freopen("CHUSO0.OUT", "w", stdout);
    }
    int t; scanf("%d", &t);
    while (t--) {
        long long n, b; scanf("%lld %lld", &n, &b);
        long long ans = LLONG_MAX;
        auto xet = [&](long long p, int k) {       // b chứa p^k
            long long e = 0, m = n;
            while (m) { m /= p; e += m; }          // Legendre: số mũ của p trong n!
            ans = min(ans, e / k);
        };
        for (long long p = 2; p * p <= b; p++)     // phân tích b bằng thử chia tới √b
            if (b % p == 0) {
                int k = 0;
                while (b % p == 0) b /= p, k++;
                xet(p, k);
            }
        if (b > 1) xet(b, 1);                      // phần còn lại là một số nguyên tố
        printf("%lld\n", ans);
    }
}
