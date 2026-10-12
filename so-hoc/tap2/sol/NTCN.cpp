#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
    if (fopen("NTCN.INP", "r")) {
        freopen("NTCN.INP", "r", stdin); freopen("NTCN.OUT", "w", stdout);
    }
    const int LIM = 1000000;                       // √(10^12)
    vector<int> pr; vector<bool> comp(LIM + 1);
    for (int i = 2; i <= LIM; i++) if (!comp[i]) {
        pr.push_back(i);
        for (ll j = (ll)i * i; j <= LIM; j += i) comp[j] = true;
    }
    int q; scanf("%d", &q);
    while (q--) {
        ll n, N; scanf("%lld %lld", &n, &N);
        vector<ll> p;                              // các ước nguyên tố phân biệt của n (≤ 11 số)
        for (int x : pr) {
            if ((ll)x * x > n) break;
            if (n % x == 0) { p.push_back(x); while (n % x == 0) n /= x; }
        }
        if (n > 1) p.push_back(n);
        int k = p.size(); ll bad = 0;              // số x ≤ N chia hết cho ít nhất một p[i]
        for (int S = 1; S < (1 << k); S++) {
            ll d = 1;
            for (int i = 0; i < k; i++) if (S >> i & 1) {
                if (d > N / p[i]) { d = N + 1; break; }   // tích vượt N: số hạng bằng 0
                d *= p[i];
            }
            bad += (__builtin_popcount(S) & 1 ? 1 : -1) * (N / d);
        }
        printf("%lld\n", N - bad);
    }
}
