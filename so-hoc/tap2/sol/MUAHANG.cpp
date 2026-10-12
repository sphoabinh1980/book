#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll exgcd(ll a, ll b, ll &x, ll &y) {               // a·x + b·y = gcd(a, b)
    if (!b) { x = 1; y = 0; return a; }
    ll x1, y1, g = exgcd(b, a % b, x1, y1);
    x = y1; y = x1 - a / b * y1; return g;
}
int main() {
    if (fopen("MUAHANG.INP", "r")) { freopen("MUAHANG.INP", "r", stdin); freopen("MUAHANG.OUT", "w", stdout); }
    int q; scanf("%d", &q);
    while (q--) {
        ll a, b, c; scanf("%lld %lld %lld", &a, &b, &c);
        ll x, y, g = exgcd(a, b, x, y);
        if (c % g) { puts("0"); continue; }
        a /= g; b /= g; c /= g;                    // giờ gcd(a, b) = 1, a·x ≡ 1 (mod b)
        ll x0 = (ll)((__int128)((x % b + b) % b) * (c % b) % b);   // x nhỏ nhất không âm
        if (a * x0 > c) { puts("0"); continue; }  // a·x0 ≤ 10^18: không tràn
        printf("%lld\n", (c - a * x0) / (a * b) + 1);   // x = x0, x0 + b, ... cho tới khi y < 0
    }
}
