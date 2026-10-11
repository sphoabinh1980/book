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
    // LỖI: đánh dấu đã thăm theo ô, nhớ kèm số tường đã phá của LẦN TỚI ĐẦU TIÊN
    vector<vector<int>> d(R, vector<int>(C, -1)), used(R, vector<int>(C, 0));
    queue<pair<int,int>> q;
    for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) if (a[i][j] == 'S') { d[i][j] = 0; q.push({i, j}); }
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        if (a[x][y] == 'T') { printf("%d\n", d[x][y]); return 0; }
        for (int t = 0; t < 4; t++) {
            int u = x + dx[t], v = y + dy[t];
            if (u < 0 || u >= R || v < 0 || v >= C || d[u][v] >= 0) continue;
            int k = used[x][y] + (a[u][v] == '#');
            if (k > K) continue;
            d[u][v] = d[x][y] + 1; used[u][v] = k; q.push({u, v});
        }
    }
    printf("-1\n");
    return 0;
}
