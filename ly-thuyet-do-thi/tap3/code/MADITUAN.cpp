#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("MADITUAN.INP", "r")) {
        freopen("MADITUAN.INP", "r", stdin);
        freopen("MADITUAN.OUT", "w", stdout);
    }
    int N, sx, sy, Q;
    scanf("%d %d %d %d", &N, &sx, &sy, &Q);
    const int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1}, dy[8] = {2, 1, -1, -2, -2, -1, 1, 2};
    // d[x][y]: số nước ít nhất từ ô xuất phát (đánh số từ 0), -1 nếu chưa tới
    vector<vector<int>> d(N, vector<int>(N, -1));
    queue<pair<int,int>> q;
    d[sx - 1][sy - 1] = 0;
    q.push({sx - 1, sy - 1});
    while (!q.empty()) {                    // BFS một lần duy nhất
        auto [x, y] = q.front(); q.pop();
        for (int k = 0; k < 8; k++) {
            int u = x + dx[k], v = y + dy[k];
            if (u >= 0 && u < N && v >= 0 && v < N && d[u][v] < 0) {
                d[u][v] = d[x][y] + 1;
                q.push({u, v});
            }
        }
    }
    while (Q--) {                           // mỗi câu hỏi O(1)
        int x, y;
        scanf("%d %d", &x, &y);
        printf("%d\n", d[x - 1][y - 1]);
    }
    return 0;
}
