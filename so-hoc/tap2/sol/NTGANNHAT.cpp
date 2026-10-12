#include <bits/stdc++.h>
using namespace std;
bool nt(long long n) {                             // thử 2, 3 rồi các cặp 6k ± 1 tới √n
    if (n < 2) return false;
    if (n < 4) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0) return false;
    return true;
}
int main() {
    if (fopen("NTGANNHAT.INP", "r")) {
        freopen("NTGANNHAT.INP", "r", stdin); freopen("NTGANNHAT.OUT", "w", stdout);
    }
    int q; scanf("%d", &q);
    while (q--) {
        long long n; scanf("%lld", &n);
        for (long long d = 0;; d++) {              // xét n, n − 1, n + 1, n − 2, n + 2, ...
            if (nt(n - d)) { printf("%lld\n", n - d); break; }   // bên trái trước: số nhỏ hơn
            if (nt(n + d)) { printf("%lld\n", n + d); break; }
        }
    }
}
