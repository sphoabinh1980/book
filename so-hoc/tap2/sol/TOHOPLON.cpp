#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll pw(ll a, ll b, ll m) {
    ll r = 1 % m; a %= m;
    for (; b; b >>= 1, a = a * a % m) if (b & 1) r = r * a % m;
    return r;
}
struct Prime {                                     // giai thừa theo mô-đun một số nguyên tố nhỏ p
    ll p; vector<ll> f, inv;
    void init() {
        f.assign(p, 1); inv.assign(p, 1);
        for (ll i = 1; i < p; i++) f[i] = f[i - 1] * i % p;
        inv[p - 1] = pw(f[p - 1], p - 2, p);
        for (ll i = p - 1; i > 0; i--) inv[i - 1] = inv[i] * i % p;
    }
    ll lucas(ll n, ll k) {                         // C(n, k) mod p theo định lí Lucas
        ll r = 1;
        while (k > 0 && r) {
            ll a = n % p, b = k % p;
            if (b > a) return 0;
            r = r * f[a] % p * inv[b] % p * inv[a - b] % p;
            n /= p; k /= p;
        }
        return r;
    }
};
int main() {
    if (fopen("TOHOPLON.INP", "r")) {
        freopen("TOHOPLON.INP", "r", stdin); freopen("TOHOPLON.OUT", "w", stdout);
    }
    int q; ll m; scanf("%d %lld", &q, &m);
    vector<Prime> ps; ll x = m;
    for (ll d = 2; d * d <= x; d++) if (x % d == 0) { ps.push_back({d}); x /= d; }
    if (x > 1) ps.push_back({x});                  // m không có ước chính phương
    vector<ll> e;                       // hệ số Trung Hoa: e ≡ 1 (mod p), e ≡ 0 (mod m / p)
    for (auto &P : ps) {
        P.init();
        ll M = m / P.p;
        e.push_back(M * pw(M % P.p, P.p - 2, P.p) % m);
    }
    while (q--) {
        ll n, k; scanf("%lld %lld", &n, &k);
        ll ans = 0;
        if (k <= n)
            for (size_t i = 0; i < ps.size(); i++) ans = (ans + ps[i].lucas(n, k) * e[i]) % m;
        printf("%lld\n", ans % m);
    }
}
