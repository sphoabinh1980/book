#include <bits/stdc++.h>
using namespace std;
int a[405][405], col[405], cnt[1000005];
int main() {
    if (fopen("HCNCHIAHET.INP", "r")) {
        freopen("HCNCHIAHET.INP", "r", stdin); freopen("HCNCHIAHET.OUT", "w", stdout);
    }
    int m, n, k; scanf("%d %d %d", &m, &n, &k);
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) { long long x; scanf("%lld", &x); a[i][j] = (x % k + k) % k; }
    long long ans = 0;
    for (int top = 0; top < m; top++) {
        fill(col, col + n, 0);
        for (int bot = top; bot < m; bot++) {           // cố định cặp hàng (top, bot)
            for (int j = 0; j < n; j++) { col[j] += a[bot][j]; if (col[j] >= k) col[j] -= k; }
            int s = 0; cnt[0] = 1;                      // DOANCHIA trên dãy tổng cột
            for (int j = 0; j < n; j++) {
                s += col[j]; if (s >= k) s -= k;
                ans += cnt[s]++;
            }
            s = 0; cnt[0] = 0;                          // chỉ xóa các ô đã dùng, không xóa cả mảng
            for (int j = 0; j < n; j++) { s += col[j]; if (s >= k) s -= k; cnt[s] = 0; }
        }
    }
    printf("%lld\n", ans);
}
