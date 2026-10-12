#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 LL;
ll extgcd(ll a, ll b, ll &x, ll &y) {      // a*x + b*y = gcd(a, b)
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1, g = extgcd(b, a % b, x1, y1);
    x = y1; y = x1 - a / b * y1; return g;
}
ll md(ll a, ll m) { a %= m; return a < 0 ? a + m : a; }
int main() {
    if (fopen("PTDONGDU.INP", "r")) {
        freopen("PTDONGDU.INP", "r", stdin); freopen("PTDONGDU.OUT", "w", stdout);
    }
    int q; scanf("%d", &q);
    while (q--) {
        ll a, c, m, L, R; scanf("%lld %lld %lld %lld %lld", &a, &c, &m, &L, &R);
        a = md(a, m); c = md(c, m);
        ll x, y, g = extgcd(a, m, x, y);    // a = 0: g = m
        if (c % g != 0) { puts("0"); continue; }
        ll m2 = m / g;                      // nghiệm: x ≡ x0 (mod m2)
        ll x0 = (LL)(c / g) * md(x, m2) % m2;
        ll first = L + md(x0 - L, m2);      // nghiệm nhỏ nhất >= L
        if (first > R) { puts("0"); continue; }
        printf("%lld %lld\n", (R - first) / m2 + 1, first);
    }
}
