#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("PHIEULER.INP", "r")) {
        freopen("PHIEULER.INP", "r", stdin);
        freopen("PHIEULER.OUT", "w", stdout);
    }
    ll n;
    cin >> n;
    ll cnt = 0;
    for (ll k = 1; k <= n; k++)             // xét từng k = 1, 2, ..., n
        if (__gcd(k, n) == 1) cnt++;        // k nguyên tố cùng nhau với n
    cout << cnt << "\n";
    return 0;
}
