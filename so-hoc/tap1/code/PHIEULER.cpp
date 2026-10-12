#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// φ(n) = n · (1 - 1/p1) · (1 - 1/p2) · ... với p1, p2, ... là các
// ước nguyên tố khác nhau của n, tìm bằng cách thử chia tới √n
ll phi(ll n) {
    ll res = n;
    for (ll p = 2; p * p <= n; p++)
        if (n % p == 0) {                   // p là ước nguyên tố của n
            while (n % p == 0) n /= p;      // chia hết mọi thừa số p
            res -= res / p;                 // res = res · (1 - 1/p)
        }
    if (n > 1) res -= res / n;      // còn lại một số nguyên tố > √n
    return res;
}

int main() {
    if (fopen("PHIEULER.INP", "r")) {
        freopen("PHIEULER.INP", "r", stdin);
        freopen("PHIEULER.OUT", "w", stdout);
    }
    ll n;
    cin >> n;
    cout << phi(n) << "\n";
    return 0;
}
