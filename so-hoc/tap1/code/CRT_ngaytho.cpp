#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("CRT.INP", "r")) {
        freopen("CRT.INP", "r", stdin);
        freopen("CRT.OUT", "w", stdout);
    }
    int k;
    cin >> k;
    vector<ll> a(k), m(k);
    ll L = 1;                               // L = lcm(m1, ..., mk)
    for (int i = 0; i < k; i++) {
        cin >> a[i] >> m[i];
        L = L / __gcd(L, m[i]) * m[i];
    }
    // nghiệm nhỏ nhất (nếu có) nhỏ hơn L; chỉ thử các x ≡ a1 (mod m1)
    for (ll x = a[0]; x < L; x += m[0]) {
        bool good = true;
        for (int i = 1; i < k && good; i++)
            if (x % m[i] != a[i]) good = false;
        if (good) { cout << x << "\n"; return 0; }
    }
    cout << -1 << "\n";
    return 0;
}
