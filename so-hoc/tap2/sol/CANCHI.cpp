#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 LL;
const ll MOD = 1000000007, LIM = 1000000000000000000LL;
ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1, g = extgcd(b, a % b, x1, y1);
    x = y1; y = x1 - a / b * y1; return g;
}
int main() {
    if (fopen("CANCHI.INP", "r")) {
        freopen("CANCHI.INP", "r", stdin); freopen("CANCHI.OUT", "w", stdout);
    }
    int k, q; scanf("%d %d", &k, &q);
    vector<ll> m(k), c(k);
    map<ll, int> ex;                            // lcm = tích p^(số mũ lớn nhất)
    for (auto &x : m) {
        scanf("%lld", &x); ll v = x;
        for (ll p = 2; p * p <= v; p++) {
            int e = 0; while (v % p == 0) v /= p, e++;
            if (e) ex[p] = max(ex[p], e);
        }
        if (v > 1) ex[v] = max(ex[v], 1);
    }
    ll cnt = 1;
    for (auto &pe : ex) for (int i = 0; i < pe.second; i++) cnt = cnt * pe.first % MOD;
    printf("%lld\n", cnt);
    while (q--) {
        for (auto &x : c) scanf("%lld", &x);
        ll L, R; scanf("%lld %lld", &L, &R);
        LL r = 0, M = 1; bool ok = true, big = false;   // x ≡ r (mod M)
        for (int i = 0; i < k && ok; i++) {
            if (big) { ok = (r % m[i] == c[i]); continue; } // chỉ còn một ứng viên r
            ll x, y, g = extgcd((ll)(M % m[i]), m[i], x, y);
            ll d = ((c[i] - (ll)(r % m[i])) % m[i] + m[i]) % m[i];
            if (d % g) { ok = false; break; }
            ll m2 = m[i] / g, t = d / g * ((x % m2 + m2) % m2) % m2;
            r += M * t; M *= m2;                // M <= 10^18 * 10^6: vừa __int128
            if (M > LIM) big = true;            // M > R: trong [0, R] có tối đa một năm
        }
        if (!ok) { puts("0"); continue; }
        if (big) { if (L <= r && r <= R) printf("1 %lld\n", (ll)r); else puts("0"); continue; }
        ll MM = (ll)M, first = L + (((ll)r - L) % MM + MM) % MM;
        if (first > R) puts("0"); else printf("%lld %lld\n", (R - first) / MM + 1, first);
    }
}
