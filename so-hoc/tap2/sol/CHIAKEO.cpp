#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
const int N = 2000000;                             // n - k·t + k - 1 < 2·10^6
long long fact[N + 1], ifact[N + 1];
long long pw(long long a, long long b) {
    long long r = 1; a %= MOD;
    for (; b; b >>= 1, a = a * a % MOD) if (b & 1) r = r * a % MOD;
    return r;
}
long long C(int n, int k) {
    if (k < 0 || k > n) return 0;
    return fact[n] * ifact[k] % MOD * ifact[n - k] % MOD;
}
int main() {
    if (fopen("CHIAKEO.INP", "r")) {
        freopen("CHIAKEO.INP", "r", stdin); freopen("CHIAKEO.OUT", "w", stdout);
    }
    fact[0] = 1;
    for (int i = 1; i <= N; i++) fact[i] = fact[i - 1] * i % MOD;
    ifact[N] = pw(fact[N], MOD - 2);               // một lần lũy thừa, rồi đi ngược
    for (int i = N; i > 0; i--) ifact[i - 1] = ifact[i] * i % MOD;
    int q; scanf("%d", &q);
    while (q--) {
        long long n, k, t; scanf("%lld %lld %lld", &n, &k, &t);
        if (k * t > n) { puts("0"); continue; }   // k·t tới 10^12: phải dùng long long
        long long r = n - k * t;                   // phát trước mỗi bạn t cái, còn r cái
        printf("%lld\n", C(r + k - 1, k - 1));    // chia kẹo Euler
    }
}
