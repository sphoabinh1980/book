#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll mulmod(ll a, ll b, ll m) { return (__int128)a * b % m; }

ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1;
    ll g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

// Công thức Tôn Tử, chỉ dùng khi các m_i đôi một nguyên tố cùng nhau
int main() {
    if (fopen("CRT.INP", "r")) {
        freopen("CRT.INP", "r", stdin);
        freopen("CRT.OUT", "w", stdout);
    }
    int k;
    cin >> k;
    vector<ll> a(k), m(k);
    ll M = 1;
    for (int i = 0; i < k; i++) { cin >> a[i] >> m[i]; M *= m[i]; }
    ll x = 0;
    for (int i = 0; i < k; i++) {
        ll Mi = M / m[i], y, z;
        extgcd(Mi % m[i], m[i], y, z);      // y = Mi^(-1) mod m[i]
        y = (y % m[i] + m[i]) % m[i];
        // số hạng a_i·M_i·y_i: ≡ a_i (mod m_i), ≡ 0 (mod m_j), j ≠ i
        x = (x + mulmod(mulmod(a[i], Mi, M), y, M)) % M;
    }
    cout << x << "\n";
    return 0;
}
