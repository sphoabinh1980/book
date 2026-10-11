#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CAMERA.INP", "r")) {
        freopen("CAMERA.INP", "r", stdin);
        freopen("CAMERA.OUT", "w", stdout);
    }
    int R, C, K;
    scanf("%d %d %d", &R, &C, &K);
    vector<int> rr(K), cc(K);
    for (int i = 0; i < K; i++) scanf("%d %d", &rr[i], &cc[i]);
    int best = INT_MAX; long long bestMask = 0;
    for (long long mask = 0; mask < (1LL << R); mask++) {   // chọn tập hàng; cột: lấy hết những cột còn thiếu
        set<int> cols;
        for (int i = 0; i < K; i++) if (!(mask >> (rr[i] - 1) & 1)) cols.insert(cc[i]);
        int t = __builtin_popcountll(mask) + cols.size();
        if (t < best) { best = t; bestMask = mask; }
    }
    set<int> cols;
    for (int i = 0; i < K; i++) if (!(bestMask >> (rr[i] - 1) & 1)) cols.insert(cc[i]);
    printf("%d\n", best);
    for (int r = 1; r <= R; r++) if (bestMask >> (r - 1) & 1) printf("H %d\n", r);
    for (int c : cols) printf("C %d\n", c);
    return 0;
}
