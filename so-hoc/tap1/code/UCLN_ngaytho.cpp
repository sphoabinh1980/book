#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("UCLN.INP", "r")) {
        freopen("UCLN.INP", "r", stdin);
        freopen("UCLN.OUT", "w", stdout);
    }
    ll a, b;
    cin >> a >> b;
    ll g = min(a, b);
    while (a % g != 0 || b % g != 0) g--;       // thử giảm dần từ min(a, b)
    const ll LIM = 1000000000000000000LL;
    ll x = a / g;
    cout << g << "\n";
    if (x > LIM / b) cout << -1 << "\n";
    else cout << x * b << "\n";
    return 0;
}
