#include <bits/stdc++.h>
using namespace std;
typedef long long ll; typedef __int128 L;
ll exgcd(ll a, ll b, ll &x, ll &y) {
    if (!b) { x = 1; y = 0; return a; }
    ll x1, y1, g = exgcd(b, a % b, x1, y1);
    x = y1; y = x1 - a / b * y1; return g;
}
int main() {
    if (fopen("DONGHO.INP", "r")) { freopen("DONGHO.INP", "r", stdin); freopen("DONGHO.OUT", "w", stdout); }
    int Q; scanf("%d", &Q);
    while (Q--) {
        ll m, p, a, q, b, T; scanf("%lld %lld %lld %lld %lld %lld", &m, &p, &a, &q, &b, &T);
        ll d = ((a - b) % m + m) % m, e = ((q - p) % m + m) % m;   // d·t ≡ e (mod m)
        ll x, y, g = exgcd(d, m, x, y);            // d = 0 thì g = m
        if (e % g) { puts("-1 0"); continue; }
        ll M = m / g;                              // các nghiệm t cách nhau M
        ll t0 = (ll)((L)((x % M + M) % M) * (e / g) % M);
        ll cnt = t0 > T ? 0 : (T - t0) / M + 1;
        printf("%lld %lld\n", t0, cnt);
    }
}
