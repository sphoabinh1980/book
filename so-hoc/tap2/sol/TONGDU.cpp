#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
int main() {
    if (fopen("TONGDU.INP", "r")) {
        freopen("TONGDU.INP", "r", stdin); freopen("TONGDU.OUT", "w", stdout);
    }
    ll n, k; scanf("%lld %lld", &n, &k);
    // n mod i = n - i·(n / i); với i > n thì n / i = 0, số dư bằng n
    ll s = (n % MOD) * (k % MOD) % MOD;            // tổng n·k
    ll lim = min(n, k);
    for (ll i = 1, j; i <= lim; i = j + 1) {
        ll q = n / i;
        j = min(n / q, lim);                       // khối không được vượt quá k
        __int128 t = (__int128)(i + j) * (j - i + 1) / 2;
        s = (s - (ll)(t % MOD) * (q % MOD) % MOD + MOD) % MOD;
    }
    printf("%lld\n", s);
}
