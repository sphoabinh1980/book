#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll power(ll a, ll b, ll m) {
    ll r = 1 % m;
    a %= m;
    while (b > 0) {
        if (b & 1) r = r * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return r;
}

int main() {                // tính a^(b^c) mod p, p nguyên tố, b, c ≥ 1
    if (fopen("THAPLT.INP", "r")) {
        freopen("THAPLT.INP", "r", stdin);
        freopen("THAPLT.OUT", "w", stdout);
    }
    ll a, b, c, p;
    cin >> a >> b >> c >> p;
    if (a % p == 0) { cout << 0 << "\n"; return 0; }   // b^c ≥ 1
    ll e = power(b, c, p - 1);      // Fermat: số mũ chỉ cần mod p - 1
    cout << power(a, e, p) << "\n";
    return 0;
}
