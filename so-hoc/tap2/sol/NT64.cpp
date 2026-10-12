#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
ull mulmod(ull a, ull b, ull m) { return (unsigned __int128)a * b % m; }
ull powmod(ull a, ull e, ull m) {
    ull r = 1; a %= m;
    for (; e; e >>= 1, a = mulmod(a, a, m)) if (e & 1) r = mulmod(r, a, m);
    return r;
}
bool nt(ull n) {
    if (n < 2) return false;
    static const ull P[12] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (ull p : P) { if (n % p == 0) return n == p; }
    ull d = n - 1; int s = 0;
    while (d % 2 == 0) d /= 2, s++;                // n − 1 = d · 2^s, d lẻ
    for (ull a : P) {
        ull x = powmod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool ok = false;
        for (int r = 1; r < s && !ok; r++) { x = mulmod(x, x, n); ok = (x == n - 1); }
        if (!ok) return false;                     // a là "nhân chứng": n là hợp số
    }
    return true;                                   // đúng với mọi n < 2^64 (12 cơ sở đầu tiên)
}
int main() {
    if (fopen("NT64.INP", "r")) {
        freopen("NT64.INP", "r", stdin); freopen("NT64.OUT", "w", stdout);
    }
    int q; scanf("%d", &q);
    string out;
    while (q--) {
        ull n; scanf("%llu", &n);
        out += nt(n) ? "YES\n" : "NO\n";
    }
    fputs(out.c_str(), stdout);
}
