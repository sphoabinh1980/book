#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
    if (fopen("DONGNUOC.INP", "r")) { freopen("DONGNUOC.INP", "r", stdin); freopen("DONGNUOC.OUT", "w", stdout); }
    int n, q; scanf("%d %d", &n, &q);
    ll g = 0;
    for (int i = 0; i < n; i++) { ll a; scanf("%lld", &a); g = __gcd(g, a); }   // gcd(0, a) = a
    printf("%lld\n", g);                           // lượng dương nhỏ nhất đong được
    while (q--) {
        ll c; scanf("%lld", &c);
        puts(c % g == 0 ? "CO" : "KHONG");         // Bézout: đong được <=> g | c
    }
}
