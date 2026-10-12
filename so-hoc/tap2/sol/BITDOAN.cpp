#include <bits/stdc++.h>
using namespace std;
typedef unsigned __int128 u128;
u128 f(long long n) {                     // tổng số bit 1 của 0, 1, ..., n (n >= -1)
    u128 s = 0;
    for (int k = 0; k < 62 && (1LL << k) <= n; k++) {
        long long p = 1LL << k, T = p << 1;
        long long q = (n + 1) / T, r = (n + 1) % T;
        s += (u128)q * p + max(0LL, r - p);   // cột bit k: chu kì 2^(k+1)
    }
    return s;
}
void print(u128 x) { if (x >= 10) print(x / 10); putchar('0' + (int)(x % 10)); }
int main() {
    if (fopen("BITDOAN.INP", "r")) {
        freopen("BITDOAN.INP", "r", stdin); freopen("BITDOAN.OUT", "w", stdout);
    }
    int q; scanf("%d", &q);
    while (q--) {
        long long L, R; scanf("%lld %lld", &L, &R);
        print(f(R) - f(L - 1)); putchar('\n');   // đáp số có thể vượt 2^64
    }
}
