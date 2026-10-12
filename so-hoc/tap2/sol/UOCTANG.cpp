#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("UOCTANG.INP", "r")) { freopen("UOCTANG.INP", "r", stdin); freopen("UOCTANG.OUT", "w", stdout); }
    long long n; int q; scanf("%lld %d", &n, &q);
    vector<long long> lo, hi;                      // lo tăng dần, hi giảm dần
    for (long long d = 1; d * d <= n; d++)
        if (n % d == 0) { lo.push_back(d); if (d != n / d) hi.push_back(n / d); }
    vector<long long> dv(lo);
    for (int i = (int)hi.size() - 1; i >= 0; i--) dv.push_back(hi[i]);
    printf("%d\n", (int)dv.size());
    for (size_t i = 0; i < dv.size(); i++) printf("%lld%c", dv[i], i + 1 < dv.size() ? ' ' : '\n');
    while (q--) {
        long long x; scanf("%lld", &x);
        auto it = lower_bound(dv.begin(), dv.end(), x);   // ước nhỏ nhất >= x
        printf("%lld\n", it == dv.end() ? -1LL : *it);
    }
}
