#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

ull mul(ull a, ull b, ull m) { return (unsigned __int128)a * b % m; }
ull pw(ull a, ull e, ull m) {               // a^e mod m (Bài 9)
    ull r = 1;
    for (a %= m; e; e >>= 1, a = mul(a, a, m))
        if (e & 1) r = mul(r, a, m);
    return r;
}
// Miller–Rabin với 12 cơ sở cố định: đúng với mọi n < 2^64
bool laNT(ull n) {
    const ull A[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    if (n < 2) return false;
    for (ull p : A)
        if (n % p == 0) return n == p;
    ull d = n - 1;
    int s = 0;
    while (d % 2 == 0) d /= 2, s++;         // n − 1 = d · 2^s, d lẻ
    for (ull a : A) {
        ull x = pw(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool ok = false;
        for (int r = 1; r < s && !ok; r++) {
            x = mul(x, x, n);
            ok = (x == n - 1);
        }
        if (!ok) return false;              // a là "nhân chứng": hợp số
    }
    return true;
}

int main() {
    if (fopen("KTNT.INP", "r")) {
        freopen("KTNT.INP", "r", stdin);
        freopen("KTNT.OUT", "w", stdout);
    }
    int q;
    cin >> q;
    while (q--) {
        ull n;
        cin >> n;
        cout << (laNT(n) ? "YES" : "NO") << "\n";
    }
    return 0;
}
