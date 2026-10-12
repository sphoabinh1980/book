#include <bits/stdc++.h>
using namespace std;
typedef __int128 i128;
void print(i128 x) { if (x >= 10) print(x / 10); putchar('0' + (int)(x % 10)); }
unsigned long long g(long long a, long long b) {          // gcd(|a|, |b|), |a|, |b| <= 2 * 10^18
    unsigned long long u = a < 0 ? -(unsigned long long)a : a;
    unsigned long long v = b < 0 ? -(unsigned long long)b : b;
    while (v) { unsigned long long t = u % v; u = v; v = t; }
    return u;
}
int main() {
    if (fopen("TAMGIAC.INP", "r")) {
        freopen("TAMGIAC.INP", "r", stdin); freopen("TAMGIAC.OUT", "w", stdout);
    }
    int q; scanf("%d", &q);
    while (q--) {
        long long x[3], y[3];
        for (int i = 0; i < 3; i++) scanf("%lld %lld", &x[i], &y[i]);
        long long ux = x[1] - x[0], uy = y[1] - y[0], vx = x[2] - x[0], vy = y[2] - y[0];
        i128 S2 = (i128)ux * vy - (i128)uy * vx;          // ép kiểu TRƯỚC khi nhân
        if (S2 < 0) S2 = -S2;
        i128 B = (i128)g(ux, uy) + g(vx, vy) + g(x[2] - x[1], y[2] - y[1]);
        print((S2 - B + 2) / 2); putchar('\n');
    }
}
