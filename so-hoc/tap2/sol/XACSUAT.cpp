#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
ll power(ll a, ll b) {
    ll r = 1; a %= MOD;
    for (; b > 0; b >>= 1, a = a * a % MOD) if (b & 1) r = r * a % MOD;
    return r;
}
int main() {
    if (fopen("XACSUAT.INP", "r")) {
        freopen("XACSUAT.INP", "r", stdin); freopen("XACSUAT.OUT", "w", stdout);
    }
    int n; scanf("%d", &n);
    ll red = 1, blue = 1, all = 1;         // tích số bi đỏ, tích số bi xanh, tích tổng số bi
    for (int i = 0; i < n; i++) {
        ll x, y; scanf("%lld %lld", &x, &y);
        red = red * x % MOD; blue = blue * y % MOD; all = all * (x + y) % MOD;
    }
    ll inv = power(all, MOD - 2);          // chỉ cần MỘT lần nghịch đảo (Fermat)
    ll p1 = red * inv % MOD;               // mọi viên đều đỏ
    ll p2 = (1 - blue * inv % MOD + MOD) % MOD;   // 1 - P(mọi viên đều xanh)
    printf("%lld\n%lld\n", p1, p2);
}
