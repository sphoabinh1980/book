#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
    if (fopen("NGHICHDAO.INP", "r")) {
        freopen("NGHICHDAO.INP", "r", stdin); freopen("NGHICHDAO.OUT", "w", stdout);
    }
    ll n, p; scanf("%lld %lld", &n, &p);
    vector<unsigned> inv(n + 1);           // p < 2^31: mỗi nghịch đảo vừa 4 byte
    inv[1] = 1;
    ll sum = 1, x = 1;
    for (ll i = 2; i <= n; i++) {
        // p = q*i + r  =>  i^-1 = (p - q) * r^-1  (mod p), với r = p mod i < i
        inv[i] = (p - p / i) * inv[p % i] % p;
        sum += inv[i]; if (sum >= p) sum -= p;
        x ^= inv[i];
    }
    printf("%lld\n%lld\n", sum % p, x);
}
