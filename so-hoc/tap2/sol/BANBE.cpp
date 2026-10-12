#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("BANBE.INP", "r")) {
        freopen("BANBE.INP", "r", stdin); freopen("BANBE.OUT", "w", stdout);
    }
    int N; long long k; scanf("%d %lld", &N, &k);
    vector<unsigned> s(N + 1, 0);                  // s[i] = tổng các ước thực sự của i
    for (int d = 1; d <= N / 2; d++)               // sàng điều hòa: d là ước của 2d, 3d, ...
        for (int m = 2 * d; m <= N; m += d) s[m] += d;
    vector<pair<int, int>> ans;
    for (int a = 1; a <= N; a++) {
        long long b = (long long)s[a] - k;
        if (b > a && b <= N && (long long)s[b] - k == a) ans.push_back({a, (int)b});
    }
    printf("%d\n", (int)ans.size());
    for (auto &p : ans) printf("%d %d\n", p.first, p.second);
}
