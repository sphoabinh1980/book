#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll power(ll a, ll b, ll m) {
    ll r = 1 % m; a %= m;
    for (; b > 0; b >>= 1, a = a * a % m) if (b & 1) r = r * a % m;
    return r;
}
int main() {
    if (fopen("SOMULON.INP", "r")) {
        freopen("SOMULON.INP", "r", stdin); freopen("SOMULON.OUT", "w", stdout);
    }
    int T; cin >> T;
    while (T--) {
        ll a, m; string b; cin >> a >> b >> m;  // m <= 10^9: tích hai số dư vừa long long
        ll pw[10];                               // pw[d] = a^d mod m
        for (int d = 0; d < 10; d++) pw[d] = power(a, d, m);
        ll r = 1 % m;                            // r = a^(phần đầu đã đọc của b) mod m
        for (char c : b) r = power(r, 10, m) * pw[c - '0'] % m;   // a^(10x+d) = (a^x)^10 * a^d
        printf("%lld\n", r);
    }
}
