#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
ll S1(ll r) { return (ll)((__int128)r * (r + 1) / 2 % MOD); }                 // 1 + 2 + ... + r
ll S2(ll r) { return (ll)((__int128)r * (r + 1) * (2 * r + 1) / 6 % MOD); }   // 1² + ... + r²
int main() {
    if (fopen("HAITHUONG.INP", "r")) {
        freopen("HAITHUONG.INP", "r", stdin); freopen("HAITHUONG.OUT", "w", stdout);
    }
    ll n, m; scanf("%lld %lld", &n, &m);
    ll lim = min(n, m), nm = (n % MOD) * (m % MOD) % MOD, s = 0;
    for (ll i = 1, j; i <= lim; i = j + 1) {
        ll a = n / i, b = m / i;
        j = min(n / a, m / b);                     // cả hai thương cùng không đổi trên [i, j]
        ll len = (j - i + 1) % MOD;
        ll s1 = (S1(j) - S1(i - 1) + MOD) % MOD, s2 = (S2(j) - S2(i - 1) + MOD) % MOD;
        a %= MOD; b %= MOD;
        // (n - i·a)(m - i·b) = n·m - i·(n·b + m·a) + i²·a·b
        ll lin = ((n % MOD) * b + (m % MOD) * a) % MOD;
        s = (s + nm * len) % MOD;
        s = (s - lin * s1 % MOD + MOD) % MOD;
        s = (s + a * b % MOD * s2) % MOD;
    }
    printf("%lld\n", s);
}
