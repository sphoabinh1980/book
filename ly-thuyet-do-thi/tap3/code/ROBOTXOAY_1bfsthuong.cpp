#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("ROBOTXOAY.INP", "r")) {
        freopen("ROBOTXOAY.INP", "r", stdin);
        freopen("ROBOTXOAY.OUT", "w", stdout);
    }
    int R, C; char h;
    cin >> R >> C >> h;
    vector<string> a(R);
    for (auto &s : a) cin >> s;
    const int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};
    string H = "NESW";
    // LỖI: BFS thường coi MỌI thao tác (kể cả tiến) đều tốn 1, rồi in số lần xoay của đường ít thao tác nhất
    vector<int> d((size_t)R * C * 4, -1), turns((size_t)R * C * 4, 0);
    queue<array<int,3>> q;
    for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) if (a[i][j] == 'S') { int k = H.find(h); d[(i * C + j) * 4 + k] = 0; q.push({i, j, k}); }
    while (!q.empty()) {
        auto [x, y, k] = q.front(); q.pop();
        int id = (x * C + y) * 4 + k;
        if (a[x][y] == 'T') { printf("%d\n", turns[id]); return 0; }
        int u = x + dx[k], v = y + dy[k];
        if (u >= 0 && u < R && v >= 0 && v < C && a[u][v] != '#' && d[(u * C + v) * 4 + k] < 0) {
            d[(u * C + v) * 4 + k] = d[id] + 1; turns[(u * C + v) * 4 + k] = turns[id]; q.push({u, v, k});
        }
        for (int t : {(k + 1) % 4, (k + 3) % 4})
            if (d[(x * C + y) * 4 + t] < 0) { d[(x * C + y) * 4 + t] = d[id] + 1; turns[(x * C + y) * 4 + t] = turns[id] + 1; q.push({x, y, t}); }
    }
    printf("-1\n");
    return 0;
}
