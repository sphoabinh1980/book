#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
int main() {
    if (fopen("TONGSIGMA.INP", "r")) {
        freopen("TONGSIGMA.INP", "r", stdin); freopen("TONGSIGMA.OUT", "w", stdout);
    }
    ll n; scanf("%lld", &n);
    ll s = 0;
    for (ll i = 1, j; i <= n; i = j + 1) {
        ll q = n / i;
        j = n / q;                                 // khối [i, j] cùng thương q
        __int128 t = (__int128)(i + j) * (j - i + 1) / 2;   // i + (i+1) + ... + j, tới 10^24
        s = (s + (ll)(t % MOD) * (q % MOD)) % MOD;
    }
    printf("%lld\n", s);
}
