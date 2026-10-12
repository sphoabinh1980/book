#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1, g = extgcd(b, a % b, x1, y1);
    x = y1; y = x1 - a / b * y1; return g;
}
int main() {
    if (fopen("DIEMBINH.INP", "r")) {
        freopen("DIEMBINH.INP", "r", stdin); freopen("DIEMBINH.OUT", "w", stdout);
    }
    int k; ll L; scanf("%d %lld", &k, &L);
    ll r = 0, M = 1;                        // tập nghiệm hiện tại: x ≡ r (mod M)
    for (int i = 0; i < k; i++) {
        ll m, a; scanf("%lld %lld", &m, &a);
        // giải M*t ≡ a - r (mod m); gcd(M, m) = 1 nên luôn có nghiệm
        ll x, y; extgcd(M % m, m, x, y);    // x = M^-1 mod m
        ll d = ((a - r) % m + m) % m;
        ll t = d * ((x % m + m) % m) % m;   // d, x < m <= 10^9: tích < 10^18
        r += M * t; M *= m;                 // r < M*m <= 10^18
    }
    if (r < L) r += (L - r + M - 1) / M * M; // số nhỏ nhất >= L trong lớp r (mod M)
    printf("%lld\n", r);
}
