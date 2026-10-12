#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll power(ll a, ll b, ll m) {        // lũy thừa nhanh (Bài 9)
    ll r = 1 % m;
    a %= m;
    while (b > 0) {
        if (b & 1) r = r * a % m;   // p ≤ 2 · 10^9: tích < 4 · 10^18
        a = a * a % m;
        b >>= 1;
    }
    return r;
}

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
        ll inv = power(b % p, p - 2, p);    // Fermat: b^(p-2) = 1/b
        printf("%lld\n", a % p * inv % p);
    }
    return 0;
}
