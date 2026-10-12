#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// a · b mod m với a, b < m ≤ 10^18: tích tới 10^36 nên nhân bằng __int128
ll mulmod(ll a, ll b, ll m) {
    return (__int128)a * b % m;
}

ll power(ll a, ll b, ll m) {
    ll r = 1 % m;               // m = 1 thì mọi số dư đều bằng 0
    a %= m;
    while (b > 0) {
        if (b & 1) r = mulmod(r, a, m);   // bit cuối của b là 1
        a = mulmod(a, a, m);              // a^1, a^2, a^4, a^8, ...
        b >>= 1;                          // bỏ bit cuối của b
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
