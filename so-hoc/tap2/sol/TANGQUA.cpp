#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
ll pw(ll a, ll b) {
    ll r = 1; a %= MOD;
    for (; b; b >>= 1, a = a * a % MOD) if (b & 1) r = r * a % MOD;
    return r;
}
int main() {
    if (fopen("TANGQUA.INP", "r")) {
        freopen("TANGQUA.INP", "r", stdin); freopen("TANGQUA.OUT", "w", stdout);
    }
    ll n, m; scanf("%lld %lld", &n, &m);
    ll k = n - m;                                  // số bạn KHÔNG nhận lại quà của mình, k ≤ 10^7
    // D(k): hoán vị không điểm cố định, D(0) = 1, D(1) = 0, D(i) = (i - 1)(D(i - 1) + D(i - 2))
    ll d0 = 1, d1 = 0;
    for (ll i = 2; i <= k; i++) { ll d2 = (i - 1) * ((d0 + d1) % MOD) % MOD; d0 = d1; d1 = d2; }
    ll D = (k == 0 ? d0 : d1);
    // C(n, m) = C(n, k) = n (n - 1) ... (n - k + 1) / k!   (nhân dần, k < MOD)
    ll num = 1, den = 1;
    for (ll i = 0; i < k; i++) {
        num = num * ((n - i) % MOD) % MOD;
        den = den * ((i + 1) % MOD) % MOD;
    }
    printf("%lld\n", num * pw(den, MOD - 2) % MOD * D % MOD);
}
