#include <bits/stdc++.h>
using namespace std;

int R, C, K, best = INT_MAX;
vector<string> a;
vector<pair<int,int>> walls;
const int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};

int bfs() {                                     // BFS thường trên bản đồ hiện tại
    vector<vector<int>> d(R, vector<int>(C, -1));
    queue<pair<int,int>> q;
    for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) if (a[i][j] == 'S') { d[i][j] = 0; q.push({i, j}); }
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        if (a[x][y] == 'T') return d[x][y];
        for (int t = 0; t < 4; t++) {
            int u = x + dx[t], v = y + dy[t];
            if (u >= 0 && u < R && v >= 0 && v < C && a[u][v] != '#' && d[u][v] < 0) { d[u][v] = d[x][y] + 1; q.push({u, v}); }
        }
    }
    return INT_MAX;
}

void tryBreak(int from, int left) {             // thử mọi tập không quá K bức tường
    best = min(best, bfs());
    if (left == 0) return;
    for (int i = from; i < (int)walls.size(); i++) {
        auto [x, y] = walls[i];
        a[x][y] = '.'; tryBreak(i + 1, left - 1); a[x][y] = '#';
    }
}

int main() {
    if (fopen("PHATUONG.INP", "r")) {
        freopen("PHATUONG.INP", "r", stdin);
        freopen("PHATUONG.OUT", "w", stdout);
    }
    cin >> R >> C >> K;
    a.resize(R);
    for (auto &s : a) cin >> s;
    for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) if (a[i][j] == '#') walls.push_back({i, j});
    tryBreak(0, K);
    printf("%d\n", best == INT_MAX ? -1 : best);
    return 0;
}
