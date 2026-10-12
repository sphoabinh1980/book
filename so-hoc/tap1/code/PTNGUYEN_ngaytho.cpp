#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("PTNGUYEN.INP", "r")) {
        freopen("PTNGUYEN.INP", "r", stdin);
        freopen("PTNGUYEN.OUT", "w", stdout);
    }
    int q;
    cin >> q;
    while (q--) {
        ll a, b, c;
        cin >> a >> b >> c;
        ll ans = -1;
        for (ll x = 0; x < b; x++)              // thử x = 0, 1, ..., b − 1
            if (((c - a * x) % b + b) % b == 0) { ans = x; break; }
        if (ans < 0) cout << -1 << "\n";
        else cout << ans << " " << (c - a * ans) / b << "\n";
    }
    return 0;
}
