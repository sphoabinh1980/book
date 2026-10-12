#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// Euclid mở rộng (Bài 4): trả về g = gcd(a, b) và x, y với a·x + b·y = g
ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1;
    ll g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

// nghịch đảo của b theo mô-đun m bất kì; -1 nếu không tồn tại
ll inverse(ll b, ll m) {
    ll x, y;
    ll g = extgcd(b % m, m, x, y);
    if (g != 1) return -1;              // gcd(b, m) > 1: không có
    return (x % m + m) % m;             // x có thể âm
}

int main() {
    if (fopen("CHIAMOD.INP", "r")) {
        freopen("CHIAMOD.INP", "r", stdin);
        freopen("CHIAMOD.OUT", "w", stdout);
    }
    int q;
    ll m;
    scanf("%d %lld", &q, &m);
    while (q--) {
        ll a, b;
        scanf("%lld %lld", &a, &b);
        ll inv = inverse(b, m);
        if (inv < 0) printf("-1\n");
        else printf("%lld\n", a % m * inv % m);
    }
    return 0;
}
