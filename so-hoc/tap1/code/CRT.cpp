#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll extgcd(ll a, ll b, ll &x, ll &y) {   // a·x + b·y = gcd(a, b)
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1;
    ll g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    if (fopen("CRT.INP", "r")) {
        freopen("CRT.INP", "r", stdin);
        freopen("CRT.OUT", "w", stdout);
    }
    int k;
    cin >> k;
    ll r = 0, M = 1;            // các phương trình đã gộp: x ≡ r (mod M)
    bool ok = true;
    for (int i = 0; i < k; i++) {
        ll a, m;
        cin >> a >> m;
        if (!ok) continue;
        // x = r + M·t, cần M·t ≡ a - r (mod m)
        ll x, y;
        ll g = extgcd(M % m, m, x, y);      // g = gcd(M, m)
        ll d = ((a - r) % m + m) % m;
        if (d % g != 0) { ok = false; continue; }   // vô nghiệm
        ll m2 = m / g;                      // t xác định theo mod m/g
        ll t = (d / g) % m2 * ((x % m2 + m2) % m2) % m2;
        r = r + M * t;                      // r mới < M·m2 = lcm(M, m)
        M = M * m2;
    }
    cout << (ok ? r : -1) << "\n";
    return 0;
}
