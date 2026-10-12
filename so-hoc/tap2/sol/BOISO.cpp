#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll CAP = 2000000000000000000LL;              // 2·10^18 > R: không có bội nào trong [1, R]
ll lcmc(ll a, ll b) {                              // lcm, nhưng "chặn" ở CAP nếu vượt R
    if (a >= CAP || b >= CAP) return CAP;
    ll y = a / __gcd(a, b);
    if (y > CAP / b) return CAP;                   // y · b > CAP: không nhân để khỏi tràn
    return y * b;
}
int main() {
    if (fopen("BOISO.INP", "r")) {
        freopen("BOISO.INP", "r", stdin); freopen("BOISO.OUT", "w", stdout);
    }
    int q; scanf("%d", &q);
    while (q--) {
        ll L, R, a, b, c; scanf("%lld %lld %lld %lld %lld", &L, &R, &a, &b, &c);
        ll ab = lcmc(a, b), ac = lcmc(a, c), bc = lcmc(b, c), abc = lcmc(ab, c);
        // số x trong [1, N] chia hết cho a hoặc b nhưng không chia hết cho c
        auto f = [&](ll N) { return N / a + N / b - N / ab - N / ac - N / bc + N / abc; };
        printf("%lld\n", f(R) - f(L - 1));
    }
}
