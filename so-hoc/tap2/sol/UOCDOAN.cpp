#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("UOCDOAN.INP", "r")) {
        freopen("UOCDOAN.INP", "r", stdin); freopen("UOCDOAN.OUT", "w", stdout);
    }
    long long L, R; scanf("%lld %lld", &L, &R);
    int n = R - L + 1;
    vector<long long> con(n);                      // con[i]: phần còn lại của L + i sau khi chia
    vector<int> d(n, 1);                           // d[i]: tích các (e + 1) đã tìm được
    for (int i = 0; i < n; i++) con[i] = L + i;
    long long S = 1;
    while ((S + 1) * (S + 1) <= R) S++;            // S = ⌊√R⌋
    vector<char> g(S + 1, 0);
    for (long long p = 2; p <= S; p++) if (!g[p]) {
        for (long long j = p * p; j <= S; j += p) g[j] = 1;
        for (long long x = (L + p - 1) / p * p; x <= R; x += p) {   // mọi bội của p trong đoạn
            int i = x - L, e = 0;
            while (con[i] % p == 0) con[i] /= p, e++;
            d[i] *= e + 1;
        }
    }
    long long tong = 0, best = L; int bd = 0;
    for (int i = 0; i < n; i++) {
        if (con[i] > 1) d[i] *= 2;                 // phần còn lại > 1 là một số nguyên tố > √R
        tong += d[i];
        if (d[i] > bd) bd = d[i], best = L + i;
    }
    printf("%lld\n%lld %d\n", tong, best, bd);
}
