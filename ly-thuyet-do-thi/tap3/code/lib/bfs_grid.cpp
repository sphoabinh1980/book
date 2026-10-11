const int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};

// khoảng cách từ ô (sx, sy) tới mọi ô trên lưới R x C; '#' là ô cấm, -1 là không tới được
vector<vector<int>> bfsGrid(const vector<string> &a, int sx, int sy) {
    int R = a.size(), C = a[0].size();
    vector<vector<int>> d(R, vector<int>(C, -1));
    queue<pair<int,int>> q;
    d[sx][sy] = 0; q.push({sx, sy});
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        for (int k = 0; k < 4; k++) {
            int u = x + dx[k], v = y + dy[k];
            if (u < 0 || u >= R || v < 0 || v >= C || a[u][v] == '#' || d[u][v] >= 0) continue;
            d[u][v] = d[x][y] + 1; q.push({u, v});
        }
    }
    return d;
}
