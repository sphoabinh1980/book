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
    const int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
    vector<vector<int>> p(R, vector<int>(C, -1));
    queue<pair<int,int>> q;
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++) if (a[i][j] == 'J') { p[i][j] = 0; q.push({i, j}); }
    while (!q.empty()) {                    // BFS cho An, bỏ qua lửa
        auto [x, y] = q.front(); q.pop();
        if (x == 0 || y == 0 || x == R - 1 || y == C - 1) { printf("%d\n", p[x][y] + 1); return 0; }
        for (int d = 0; d < 4; d++) {
            int u = x + dx[d], v = y + dy[d];
            if (a[u][v] != '#' && p[u][v] < 0) { p[u][v] = p[x][y] + 1; q.push({u, v}); }
        }
    }
    printf("-1\n");
    return 0;
}
