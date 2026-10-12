#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll gcd_(ll a, ll b) {                           // thuật toán Euclid
    while (b != 0) {
        ll r = a % b;                           // (a, b) -> (b, a mod b)
        a = b; b = r;
    }
    return a;
}

int main() {
    if (fopen("UCLN.INP", "r")) {
        freopen("UCLN.INP", "r", stdin);
        freopen("UCLN.OUT", "w", stdout);
    }
    ll a, b;
    cin >> a >> b;
    ll g = gcd_(a, b);
    const ll LIM = 1000000000000000000LL;       // 10^18
    ll x = a / g;                               // chia trước, nhân sau
    cout << g << "\n";
    if (x > LIM / b) cout << -1 << "\n";        // x · b > 10^18: không in
    else cout << x * b << "\n";
    return 0;
}
