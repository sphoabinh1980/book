#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("NTDOAN.INP", "r")) {
        freopen("NTDOAN.INP", "r", stdin); freopen("NTDOAN.OUT", "w", stdout);
    }
    const int S = 1000000;                         // √(10^12)
    vector<char> g(S + 1, 0); vector<long long> pr;
    for (long long p = 2; p <= S; p++) if (!g[p]) {
        pr.push_back(p);
        for (long long j = p * p; j <= S; j += p) g[j] = 1;
    }
    int t; scanf("%d", &t);
    while (t--) {
        long long L, R; scanf("%lld %lld", &L, &R);
        vector<char> gach(R - L + 1, 0);           // ô x − L ứng với số x
        for (long long p : pr) {
            if (p * p > R) break;
            long long j = max(p * p, (L + p - 1) / p * p);
            for (; j <= R; j += p) gach[j - L] = 1;
        }
        if (L == 1) gach[0] = 1;                   // số 1 không nguyên tố
        long long dem = 0, tong = 0;
        for (long long x = L; x <= R; x++) if (!gach[x - L]) dem++, tong += x;
        printf("%lld %lld\n", dem, tong);
    }
}
