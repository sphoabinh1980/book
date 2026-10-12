#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("XEPHANG.INP", "r")) { freopen("XEPHANG.INP", "r", stdin); freopen("XEPHANG.OUT", "w", stdout); }
    int T; scanf("%d", &T);
    while (T--) {
        long long n; scanf("%lld", &n);
        long long cnt = 0, best = 1;               // best = ước lớn nhất không vượt quá √n
        for (long long d = 1; d * d <= n; d++)
            if (n % d == 0) { cnt += (d == n / d) ? 1 : 2; best = d; }
        if (best == 1) { puts("0"); continue; }    // n = 1 hoặc n nguyên tố: không có cách nào
        printf("%lld %lld %lld\n", cnt - 2, best, n / best);  // bỏ hai cách 1 × n và n × 1
    }
}
