#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("CHIAMOD.INP", "r")) {
        freopen("CHIAMOD.INP", "r", stdin);
        freopen("CHIAMOD.OUT", "w", stdout);
    }
    int q;
    ll p;
    scanf("%d %lld", &q, &p);
    while (q--) {
        ll a, b;
        scanf("%lld %lld", &a, &b);
        b %= p;
        ll inv = 0;
        for (ll x = 1; x < p; x++)          // thử mọi x = 1, 2, ..., p - 1
            if (b * x % p == 1) { inv = x; break; }
        printf("%lld\n", a % p * inv % p);
    }
    return 0;
}
