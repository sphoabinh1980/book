#include <bits/stdc++.h>
using namespace std;

typedef unsigned __int128 u128;   // đáp số có thể vượt 2^64

void inso(u128 x) {               // cout không in được __int128
    if (x >= 10) inso(x / 10);
    putchar('0' + (int)(x % 10));
}

int main() {
    if (fopen("DEMBIT.INP", "r")) {
        freopen("DEMBIT.INP", "r", stdin);
        freopen("DEMBIT.OUT", "w", stdout);
    }
    long long n;
    cin >> n;
    u128 s = 0;
    for (int k = 0; (1LL << k) <= n; k++) {   // bit k của các số 0..n
        long long p = 1LL << k;     // nửa chu kì: 2^k số 0, 2^k số 1
        long long T = 2 * p;        // chu kì 2^(k+1)
        long long q = (n + 1) / T;  // số chu kì trọn vẹn
        long long r = (n + 1) % T;  // số phần tử của chu kì dở dang
        s += (u128)q * p + max(0LL, r - p);
    }
    inso(s);
    putchar('\n');
    return 0;
}
