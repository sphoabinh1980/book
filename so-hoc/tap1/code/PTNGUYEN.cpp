#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

// Trả về g = gcd(a, b) và tìm x, y với a·x + b·y = g
ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) { x = 1; y = 0; return a; }     // a·1 + 0·0 = a
    ll x1, y1;
    ll g = extgcd(b, a % b, x1, y1);            // b·x1 + (a mod b)·y1 = g
    x = y1;                                     // a mod b = a − (a/b)·b
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    if (fopen("PTNGUYEN.INP", "r")) {
        freopen("PTNGUYEN.INP", "r", stdin);
        freopen("PTNGUYEN.OUT", "w", stdout);
    }
    int q;
    cin >> q;
    while (q--) {
        ll a, b, c, x, y;
        cin >> a >> b >> c;
        ll g = extgcd(a, b, x, y);
        if (c % g != 0) { cout << -1 << "\n"; continue; }   // Bézout
        ll bg = b / g;                          // x tăng giảm theo bước b/g
        ll x0 = (ll)((__int128)x * (c / g) % bg);
        if (x0 < 0) x0 += bg;                   // x nhỏ nhất không âm
        ll y0 = (ll)(((__int128)c - (__int128)a * x0) / b);
        cout << x0 << " " << y0 << "\n";
    }
    return 0;
}
