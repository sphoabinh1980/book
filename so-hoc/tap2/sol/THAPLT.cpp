#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll CAP = 4000000000LL;               // > mọi φ(m); "cap" = min(giá trị thật, CAP)
int k; vector<ll> a, cap;
ll phi(ll n) {
    ll res = n;
    for (ll p = 2; p * p <= n; p++)
        if (n % p == 0) { res -= res / p; while (n % p == 0) n /= p; }
    if (n > 1) res -= res / n;
    return res;
}
ll power(ll a, ll b, ll m) {
    ll r = 1 % m; a %= m;
    for (; b > 0; b >>= 1, a = a * a % m) if (b & 1) r = r * a % m;
    return r;
}
ll capPow(ll x, ll e) {                    // min(x^e, CAP), e đã bị chặn bởi CAP
    if (x == 0) return e == 0 ? 1 : 0;
    if (x == 1) return 1;
    if (e >= 64) return CAP;
    ll r = 1;
    for (int i = 0; i < e; i++) { r *= x; if (r >= CAP) return CAP; }
    return r;
}
ll solve(int i, ll m) {                    // a[i]^(a[i+1]^(...)) mod m
    if (m == 1) return 0;
    if (i == k - 1) return a[i] % m;
    ll ph = phi(m), e = cap[i + 1];
    if (e < ph) return power(a[i], e, m);  // số mũ nhỏ: dùng đúng giá trị thật
    return power(a[i], solve(i + 1, ph) + ph, m);   // Euler mở rộng: E >= φ(m)
}
int main() {
    if (fopen("THAPLT.INP", "r")) {
        freopen("THAPLT.INP", "r", stdin); freopen("THAPLT.OUT", "w", stdout);
    }
    int T; scanf("%d", &T);
    while (T--) {
        ll m; scanf("%d %lld", &k, &m);
        a.assign(k, 0); cap.assign(k, 0);
        for (auto &x : a) scanf("%lld", &x);
        cap[k - 1] = min(a[k - 1], CAP);
        for (int i = k - 2; i >= 0; i--) cap[i] = capPow(a[i], cap[i + 1]);
        printf("%lld\n", solve(0, m));
    }
}
