#include <bits/stdc++.h>
using namespace std;
long long C[64][64];
long long cnt(long long n, int k) {          // số x trong [0, n] có đúng k bit 1 (n >= -1)
    if (n < 0) return 0;
    long long res = 0; int ones = 0;
    for (int i = 61; i >= 0; i--)
        if ((n >> i) & 1) {                  // đặt bit i bằng 0, i bit thấp hơn tự do
            if (k - ones >= 0) res += C[i][k - ones];
            ones++;
        }
    if (ones == k) res++;                    // chính n
    return res;
}
long long kth(int k, long long m) {          // số dương nhỏ thứ m có đúng k bit 1 (k >= 1)
    long long x = 0;
    for (int i = 61; i >= 0; i--) {
        long long c0 = C[i][k];              // số cách khi bit i bằng 0
        if (m > c0) { m -= c0; x |= 1LL << i; k--; }
    }
    return x;
}
int main() {
    if (fopen("KBIT.INP", "r")) {
        freopen("KBIT.INP", "r", stdin); freopen("KBIT.OUT", "w", stdout);
    }
    for (int i = 0; i < 64; i++) {
        C[i][0] = 1;
        for (int j = 1; j <= i; j++) C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
    }
    int q; scanf("%d", &q);
    while (q--) {
        int t; scanf("%d", &t);
        if (t == 1) {
            long long L, R; int k; scanf("%lld %lld %d", &L, &R, &k);
            printf("%lld\n", cnt(R, k) - cnt(L - 1, k));
        } else {
            int k; long long m; scanf("%d %lld", &k, &m);
            printf("%lld\n", kth(k, m));
        }
    }
}
