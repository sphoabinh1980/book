#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
    if (fopen("BOMOTSO.INP", "r")) { freopen("BOMOTSO.INP", "r", stdin); freopen("BOMOTSO.OUT", "w", stdout); }
    int n; scanf("%d", &n);
    vector<ll> a(n + 2, 0), L(n + 2, 0), R(n + 2, 0);  // gcd(0, x) = x
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    for (int i = 1; i <= n; i++) L[i] = __gcd(L[i - 1], a[i]);      // gcd tiền tố
    for (int i = n; i >= 1; i--) R[i] = __gcd(R[i + 1], a[i]);      // gcd hậu tố
    ll best = -1; int pos = 0;
    for (int i = 1; i <= n; i++) {
        ll g = __gcd(L[i - 1], R[i + 1]);          // bỏ a[i]
        if (g > best) best = g, pos = i;           // dấu > : giữ chỉ số nhỏ nhất
    }
    printf("%lld %d\n", best, pos);
}
