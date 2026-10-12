#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;

long long power(long long a, long long b) {
    long long r = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) r = r * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return r;
}

// C(n, k) = n(n-1)...(n-k+1) / k!, mỗi truy vấn O(k + log MOD)
// dùng được cả khi n rất lớn (tới 10^18), miễn là k < MOD
long long C(long long n, long long k) {
    if (k < 0 || k > n) return 0;
    long long tu = 1, mau = 1;
    for (long long i = 0; i < k; i++) {
        tu = tu * ((n - i) % MOD) % MOD;
        mau = mau * ((i + 1) % MOD) % MOD;
    }
    return tu * power(mau, MOD - 2) % MOD;
}

int main() {
    if (fopen("TOHOP.INP", "r")) {
        freopen("TOHOP.INP", "r", stdin);
        freopen("TOHOP.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        long long n, k;
        scanf("%lld %lld", &n, &k);
        if (k >= 0 && k <= n) k = min(k, n - k);   // C(n,k) = C(n,n-k)
        printf("%lld\n", C(n, k));
    }
    return 0;
}
