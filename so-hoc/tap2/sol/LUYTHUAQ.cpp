#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
ll power(ll a, ll b) {                 // a^b mod MOD, bình phương liên tiếp
    ll r = 1; a %= MOD;                // a tới 10^18: phải lấy dư trước khi nhân
    while (b > 0) {
        if (b & 1) r = r * a % MOD;
        a = a * a % MOD; b >>= 1;
    }
    return r;                          // b = 0: r = 1 (kể cả 0^0)
}
int main() {
    if (fopen("LUYTHUAQ.INP", "r")) {
        freopen("LUYTHUAQ.INP", "r", stdin); freopen("LUYTHUAQ.OUT", "w", stdout);
    }
    int q; scanf("%d", &q);
    while (q--) {
        ll a, b; scanf("%lld %lld", &a, &b);
        printf("%lld\n", power(a, b));
    }
}
