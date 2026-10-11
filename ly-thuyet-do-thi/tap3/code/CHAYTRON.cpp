#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CHAYTRON.INP", "r")) {
        freopen("CHAYTRON.INP", "r", stdin);
        freopen("CHAYTRON.OUT", "w", stdout);
    }
    int R, C;
    cin >> R >> C;
    vector<string> a(R);
    for (auto &s : a) cin >> s;
    const int INF = INT_MAX, dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
    // Lần 1: BFS nhiều nguồn từ mọi ô 'F', f[x][y] = phút lửa tới ô (x, y)
    vector<vector<int>> f(R, vector<int>(C, INF));
    queue<pair<int,int>> q;
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++) if (a[i][j] == 'F') { f[i][j] = 0; q.push({i, j}); }
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int u = x + dx[d], v = y + dy[d];
            if (u >= 0 && u < R && v >= 0 && v < C && a[u][v] != '#' && f[u][v] == INF) {
                f[u][v] = f[x][y] + 1;
                q.push({u, v});
            }
        }
    }
    // Lần 2: BFS cho An, chỉ bước vào ô mà lửa tới SAU An
    vector<vector<int>> p(R, vector<int>(C, -1));
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++) if (a[i][j] == 'J') { p[i][j] = 0; q.push({i, j}); }
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        if (x == 0 || y == 0 || x == R - 1 || y == C - 1) {   // ô biên: phút sau ra ngoài
            printf("%d\n", p[x][y] + 1);
            return 0;
        }
        for (int d = 0; d < 4; d++) {
            int u = x + dx[d], v = y + dy[d];  // (x, y) không ở biên nên (u, v) trong bảng
            if (a[u][v] != '#' && p[u][v] < 0 && p[x][y] + 1 < f[u][v]) {
                p[u][v] = p[x][y] + 1;
                q.push({u, v});
            }
        }
    }
    printf("-1\n");
    return 0;
}
