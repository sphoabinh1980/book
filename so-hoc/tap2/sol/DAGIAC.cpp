#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("DAGIAC.INP", "r")) {
        freopen("DAGIAC.INP", "r", stdin); freopen("DAGIAC.OUT", "w", stdout);
    }
    int n; scanf("%d", &n);
    vector<long long> x(n), y(n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &x[i], &y[i]);
    long long S2 = 0, B = 0;              // S2 = 2 lần diện tích, B = số điểm trên biên
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        S2 += x[i] * y[j] - x[j] * y[i];        // công thức dây giày
        B += __gcd(llabs(x[j] - x[i]), llabs(y[j] - y[i]));
    }
    S2 = llabs(S2);                                       // đỉnh có thể cho theo chiều kim đồng hồ
    printf("%lld %lld\n", (S2 - B + 2) / 2, B);           // Pick: I = (2S - B + 2) / 2
}
