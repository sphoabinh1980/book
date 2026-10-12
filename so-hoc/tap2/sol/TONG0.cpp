#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("TONG0.INP", "r")) {
        freopen("TONG0.INP", "r", stdin); freopen("TONG0.OUT", "w", stdout);
    }
    int n; scanf("%d", &n);
    vector<long long> S(n + 1, 0);                    // S[0] = 0: tiền tố rỗng
    for (int i = 1; i <= n; i++) { long long a; scanf("%lld", &a); S[i] = S[i - 1] + a; }
    sort(S.begin(), S.end());
    long long ans = 0;
    for (int i = 0, j; i <= n; i = j) {               // nhóm các tổng tiền tố bằng nhau
        for (j = i; j <= n && S[j] == S[i]; j++) {}
        long long c = j - i; ans += c * (c - 1) / 2;
    }
    printf("%lld\n", ans);
}
