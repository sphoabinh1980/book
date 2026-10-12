#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("LUYTHUA.INP", "r")) {
        freopen("LUYTHUA.INP", "r", stdin);
        freopen("LUYTHUA.OUT", "w", stdout);
    }
    ll a, b, m;
    cin >> a >> b >> m;
    a %= m;
    ll r = 1 % m;
    for (ll i = 1; i <= b; i++)             // nhân b lần
        r = (__int128)r * a % m;            // r = a^i mod m
    cout << r << "\n";
    return 0;
}
