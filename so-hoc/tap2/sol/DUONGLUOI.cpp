#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
const int N = 2000000;
long long fact[N + 1], ifact[N + 1];
long long pw(long long a, long long b) {
    long long r = 1; a %= MOD;
    for (; b; b >>= 1, a = a * a % MOD) if (b & 1) r = r * a % MOD;
    return r;
}
// số đường đi từ (x1, y1) tới (x2, y2), chỉ sang phải hoặc lên trên
long long P(long long x1, long long y1, long long x2, long long y2) {
    long long dx = x2 - x1, dy = y2 - y1;
    if (dx < 0 || dy < 0) return 0;
    return fact[dx + dy] * ifact[dx] % MOD * ifact[dy] % MOD;
}
int main() {
    if (fopen("DUONGLUOI.INP", "r")) {
        freopen("DUONGLUOI.INP", "r", stdin); freopen("DUONGLUOI.OUT", "w", stdout);
    }
    fact[0] = 1;
    for (int i = 1; i <= N; i++) fact[i] = fact[i - 1] * i % MOD;
    ifact[N] = pw(fact[N], MOD - 2);
    for (int i = N; i > 0; i--) ifact[i - 1] = ifact[i] * i % MOD;
    long long m, n; int K; scanf("%lld %lld %d", &m, &n, &K);
    long long x[2], y[2];
    for (int i = 0; i < K; i++) scanf("%lld %lld", &x[i], &y[i]);
    long long ans = P(0, 0, m, n);
    for (int i = 0; i < K; i++)                    // trừ các đường đi qua ô cấm thứ i
        ans -= P(0, 0, x[i], y[i]) * P(x[i], y[i], m, n) % MOD;
    if (K == 2) {                                  // cộng lại các đường đi qua cả hai ô
        for (int a = 0; a < 2; a++) {
            int b = 1 - a;                         // đi qua ô a trước rồi tới ô b
            ans += P(0, 0, x[a], y[a]) * P(x[a], y[a], x[b], y[b]) % MOD
                   * P(x[b], y[b], m, n) % MOD;
        }
    }
    printf("%lld\n", ((ans % MOD) + MOD) % MOD);
}
