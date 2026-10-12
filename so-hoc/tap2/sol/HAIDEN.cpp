#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1, g = extgcd(b, a % b, x1, y1);
    x = y1; y = x1 - a / b * y1; return g;
}
int main() {
    if (fopen("HAIDEN.INP", "r")) {
        freopen("HAIDEN.INP", "r", stdin); freopen("HAIDEN.OUT", "w", stdout);
    }
    int q; scanf("%d", &q);
    while (q--) {
        ll a1, p1, a2, p2; scanf("%lld %lld %lld %lld", &a1, &p1, &a2, &p2);
        ll r1 = a1 % p1, r2 = a2 % p2;
        ll x, y, g = extgcd(p1, p2, x, y);       // p1*x + p2*y = g
        ll d = r2 - r1;                           // cần p1*t ≡ d (mod p2)
        if (d % g != 0) { puts("-1"); continue; }
        ll m = p2 / g;                            // t duy nhất theo mô-đun p2/g
        ll t = (d / g % m + m) % m * ((x % m + m) % m) % m;
        ll lcm = p1 * m, r = r1 + p1 * t;         // t, x < m <= 10^9; r < lcm <= 10^18
        ll T0 = max(a1, a2);                      // cả hai đèn đã bắt đầu nháy
        ll first = T0 + ((r - T0) % lcm + lcm) % lcm;
        printf("%lld\n", first);
    }
}
