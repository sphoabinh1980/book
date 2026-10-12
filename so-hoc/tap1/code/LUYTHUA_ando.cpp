#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// Nhân Ấn Độ: a · b mod m chỉ bằng phép cộng và nhân đôi.
// Mọi số trung gian < 2m ≤ 2 · 10^18 < 2^63: không tràn long long.
ll mulmod(ll a, ll b, ll m) {
    ll r = 0;
    a %= m;
    while (b > 0) {
        if (b & 1) r = (r + a) % m;       // cộng a·2^i khi bit i bằng 1
        a = (a + a) % m;                  // a, 2a, 4a, 8a, ...
        b >>= 1;
    }
    return r;
}

ll power(ll a, ll b, ll m) {
    ll r = 1 % m;
    a %= m;
    while (b > 0) {
        if (b & 1) r = mulmod(r, a, m);
        a = mulmod(a, a, m);
        b >>= 1;
    }
    return r;
}

int main() {
    if (fopen("LUYTHUA.INP", "r")) {
        freopen("LUYTHUA.INP", "r", stdin);
        freopen("LUYTHUA.OUT", "w", stdout);
    }
    ll a, b, m;
    cin >> a >> b >> m;
    cout << power(a, b, m) << "\n";
    return 0;
}
