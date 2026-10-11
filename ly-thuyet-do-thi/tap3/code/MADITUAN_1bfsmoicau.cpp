#include <bits/stdc++.h>
using namespace std;

int N;
const int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1}, dy[8] = {2, 1, -1, -2, -2, -1, 1, 2};

int bfs(int sx, int sy, int tx, int ty) {  // một lần BFS cho một câu hỏi
    vector<int> d(N * N, -1);
    queue<int> q;
    d[(sx - 1) * N + sy - 1] = 0; q.push((sx - 1) * N + sy - 1);
    while (!q.empty()) {
        int c = q.front(); q.pop();
        int x = c / N, y = c % N;
        if (x == tx - 1 && y == ty - 1) return d[c];
        for (int k = 0; k < 8; k++) {
            int u = x + dx[k], v = y + dy[k];
            if (u >= 0 && u < N && v >= 0 && v < N && d[u * N + v] < 0) {
                d[u * N + v] = d[c] + 1; q.push(u * N + v);
            }
        }
    }
    return -1;
}

int main() {
    if (fopen("MADITUAN.INP", "r")) {
        freopen("MADITUAN.INP", "r", stdin);
        freopen("MADITUAN.OUT", "w", stdout);
    }
    int sx, sy, Q;
    scanf("%d %d %d %d", &N, &sx, &sy, &Q);
    while (Q--) {
        int x, y;
        scanf("%d %d", &x, &y);
        printf("%d\n", bfs(sx, sy, x, y));
    }
    return 0;
}
