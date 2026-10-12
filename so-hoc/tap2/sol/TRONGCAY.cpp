#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("TRONGCAY.INP", "r")) {
        freopen("TRONGCAY.INP", "r", stdin); freopen("TRONGCAY.OUT", "w", stdout);
    }
    int n; scanf("%d", &n);
    vector<long long> x(n), y(n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &x[i], &y[i]);
    long long ans = 1;                                    // điểm đầu tiên
    for (int i = 0; i + 1 < n; i++)          // mỗi đoạn góp gcd điểm mới (đầu đoạn đã được đếm)
        ans += __gcd(llabs(x[i + 1] - x[i]), llabs(y[i + 1] - y[i]));
    printf("%lld\n", ans);
}
