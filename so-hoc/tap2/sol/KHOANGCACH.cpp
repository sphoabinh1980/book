#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("KHOANGCACH.INP", "r")) {
        freopen("KHOANGCACH.INP", "r", stdin); freopen("KHOANGCACH.OUT", "w", stdout);
    }
    long long L, R; scanf("%lld %lld", &L, &R);
    long long S = sqrtl((long double)R);
    while (S * S > R) S--;
    while ((S + 1) * (S + 1) <= R) S++;
    vector<char> g(S + 1, 0), gach(R - L + 1, 0);
    for (long long p = 2; p <= S; p++) if (!g[p]) {
        for (long long j = p * p; j <= S; j += p) g[j] = 1;
        for (long long j = max(p * p, (L + p - 1) / p * p); j <= R; j += p) gach[j - L] = 1;
    }
    if (L == 1) gach[0] = 1;
    long long prev = -1, lp = -1, lq = -1, np = -1, nq = -1;
    for (long long x = L; x <= R; x++) if (!gach[x - L]) {
        if (prev > 0) {                            // (prev, x) là hai số nguyên tố liên tiếp
            if (lp < 0 || x - prev > lq - lp) lp = prev, lq = x;   // dấu > : giữ cặp bên trái
            if (np < 0 || x - prev < nq - np) np = prev, nq = x;
        }
        prev = x;
    }
    if (lp < 0) { puts("-1"); return 0; }
    printf("%lld %lld\n%lld %lld\n", lp, lq, np, nq);
}
