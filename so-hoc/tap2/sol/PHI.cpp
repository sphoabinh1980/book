#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll phi(ll n) {                             // công thức tích, thử chia tới √n
    ll res = n;
    if (n % 2 == 0) { res -= res / 2; while (n % 2 == 0) n /= 2; }
    for (ll p = 3; p * p <= n; p += 2)     // chỉ thử số lẻ
        if (n % p == 0) { res -= res / p; while (n % p == 0) n /= p; }
    if (n > 1) res -= res / n;             // ước nguyên tố lớn còn lại
    return res;
}
int main() {
    if (fopen("PHI.INP", "r")) {
        freopen("PHI.INP", "r", stdin); freopen("PHI.OUT", "w", stdout);
    }
    int q; scanf("%d", &q);
    while (q--) { ll n; scanf("%lld", &n); printf("%lld\n", phi(n)); }
}
