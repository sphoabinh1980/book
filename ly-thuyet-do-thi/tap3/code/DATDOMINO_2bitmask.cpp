#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DATDOMINO.INP", "r")) {
        freopen("DATDOMINO.INP", "r", stdin);
        freopen("DATDOMINO.OUT", "w", stdout);
    }
    int R, C;
    cin >> R >> C;
    vector<string> a(R);
    for (auto &s : a) cin >> s;
    if (C > R) {                                // cho cạnh ngắn làm chiều rộng
        vector<string> b(C, string(R, '.'));
        for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) b[j][i] = a[i][j];
        a = b; swap(R, C);
    }
    // QHĐ "hồ sơ gãy": duyệt từng ô; bit j của mask cho biết ô ở cột j (hàng đang xét
    // với j >= c, hàng dưới với j < c) đã bị một quân domino chiếm chỗ hay chưa
    vector<int> dp(1LL << min(C, 40), -1), nd(1LL << min(C, 40));   // 2^C trạng thái: C lớn thì không đủ bộ nhớ
    dp[0] = 0;
    for (int r = 0; r < R; r++) for (int c = 0; c < C; c++) {
        fill(nd.begin(), nd.end(), -1);
        for (int mask = 0; mask < (1 << C); mask++) if (dp[mask] >= 0) {
            int v = dp[mask], m0 = mask & ~(1 << c);
            auto upd = [&](int mk, int val) { nd[mk] = max(nd[mk], val); };
            if ((mask >> c & 1) || a[r][c] == '#') { upd(m0, v); continue; }
            upd(m0, v);                                                    // bỏ trống ô (r, c)
            if (r + 1 < R && a[r + 1][c] == '.') upd(m0 | 1 << c, v + 1);   // quân dọc
            if (c + 1 < C && a[r][c + 1] == '.' && !(mask >> (c + 1) & 1))
                upd(m0 | 1 << (c + 1), v + 1);                              // quân ngang
        }
        swap(dp, nd);
    }
    printf("%d\n", *max_element(dp.begin(), dp.end()));
    return 0;
}
