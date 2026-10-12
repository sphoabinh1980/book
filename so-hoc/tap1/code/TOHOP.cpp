#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
const int N = 1000000;
long long fact[N + 1], ifact[N + 1];

long long power(long long a, long long b) {   // a^b mod MOD (Bài 9)
    long long r = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) r = r * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return r;
}

long long C(int n, int k) {
    if (k < 0 || k > n) return 0;
    return fact[n] * ifact[k] % MOD * ifact[n - k] % MOD;
}

int main() {
    if (fopen("TOHOP.INP", "r")) {
        freopen("TOHOP.INP", "r", stdin);
        freopen("TOHOP.OUT", "w", stdout);
    }
    fact[0] = 1;
    for (int i = 1; i <= N; i++) fact[i] = fact[i - 1] * i % MOD;
    ifact[N] = power(fact[N], MOD - 2);        // Fermat nhỏ (Bài 10)
    for (int i = N; i >= 1; i--)               // đi ngược: 1/(i-1)!
        ifact[i - 1] = ifact[i] * i % MOD;     //   = 1/i! * i
    int q;
    scanf("%d", &q);
    while (q--) {
        int n, k;
        scanf("%d %d", &n, &k);
        printf("%lld\n", C(n, k));
    }
    return 0;
}
