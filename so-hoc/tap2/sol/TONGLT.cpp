#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 LL;
ll a, m;
// trả về S = 1 + a + ... + a^(n-1) mod m, đồng thời P = a^n mod m
void geo(ll n, ll &S, ll &P) {
    if (n == 0) { S = 0; P = 1 % m; return; }
    if (n & 1) {                                 // S(n) = 1 + a * S(n - 1)
        geo(n - 1, S, P);
        S = (1 + (LL)a * S) % m; P = (LL)P * a % m; return;
    }
    geo(n / 2, S, P);                            // S(2k) = S(k) * (1 + a^k)
    S = (LL)S * ((1 + P) % m) % m; P = (LL)P * P % m;
}
int main() {
    if (fopen("TONGLT.INP", "r")) {
        freopen("TONGLT.INP", "r", stdin); freopen("TONGLT.OUT", "w", stdout);
    }
    int T; scanf("%d", &T);
    while (T--) {
        ll n; scanf("%lld %lld %lld", &a, &n, &m);
        a %= m;
        ll S, P; geo(n + 1, S, P);               // n + 1 số hạng: a^0, ..., a^n
        printf("%lld\n", S);
    }
}
