#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("PHATUONG.INP", "r")) {
        freopen("PHATUONG.INP", "r", stdin);
        freopen("PHATUONG.OUT", "w", stdout);
    }
    int R, C, K;
    cin >> R >> C >> K;
    vector<string> a(R);
    for (auto &s : a) cin >> s;
    const int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
    // trạng thái (x, y, k): ở ô (x, y), đã phá k bức tường
    vector<int> d((size_t)R * C * (K + 1), -1);
    auto id = [&](int x, int y, int k) { return (x * C + y) * (K + 1) + k; };
    queue<array<int,3>> q;
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            if (a[i][j] == 'S') { d[id(i, j, 0)] = 0; q.push({i, j, 0}); }
    while (!q.empty()) {
        auto [x, y, k] = q.front(); q.pop();
        if (a[x][y] == 'T') { printf("%d\n", d[id(x, y, k)]); return 0; }
        for (int t = 0; t < 4; t++) {
            int u = x + dx[t], v = y + dy[t];
            if (u < 0 || u >= R || v < 0 || v >= C) continue;
            int k2 = k + (a[u][v] == '#');      // bước vào tường: dùng thêm một lần búa
            if (k2 > K || d[id(u, v, k2)] >= 0) continue;
            d[id(u, v, k2)] = d[id(x, y, k)] + 1;
            q.push({u, v, k2});
        }
    }
    printf("-1\n");
    return 0;
}
