#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("DOANDAI.INP", "r")) {
        freopen("DOANDAI.INP", "r", stdin); freopen("DOANDAI.OUT", "w", stdout);
    }
    int n, k; scanf("%d %d", &n, &k);
    vector<int> first(k, -1);                 // first[d] = chỉ số i nhỏ nhất có S_i mod k = d
    first[0] = 0;                             // S_0 = 0
    long long s = 0; int best = 0, bl = 0;
    for (int r = 1; r <= n; r++) {
        long long a; scanf("%lld", &a);
        s = ((s + a) % k + k) % k;            // số dư không âm
        if (first[s] < 0) first[s] = r;
        else if (r - first[s] > best) {        // chỉ nhận khi dài hơn hẳn: giữ l nhỏ nhất
            best = r - first[s]; bl = first[s] + 1;
        }
    }
    if (best == 0) puts("0"); else printf("%d %d\n", best, bl);
}
