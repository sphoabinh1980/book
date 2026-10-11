#include <bits/stdc++.h>
using namespace std;

int R, C, stamp = 0;
vector<vector<int>> g;                          // g[ô trắng] = các ô đen trống kề cạnh
vector<int> mt, vis;                            // mt[ô đen] = ô trắng đang ghép với nó (-1: chưa)

bool kuhn(int u) {
    for (int v : g[u]) if (vis[v] != stamp) {
        vis[v] = stamp;
        if (mt[v] < 0 || kuhn(mt[v])) { mt[v] = u; return true; }
    }
    return false;
}

int main() {
    if (fopen("DATDOMINO.INP", "r")) {
        freopen("DATDOMINO.INP", "r", stdin);
        freopen("DATDOMINO.OUT", "w", stdout);
    }
    cin >> R >> C;
    vector<string> a(R);
    for (auto &s : a) cin >> s;
    int N = R * C;
    g.resize(N); mt.assign(N, -1); vis.assign(N, 0);
    const int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
    // tô bàn cờ: ô (i, j) "trắng" nếu i + j chẵn; mỗi quân domino phủ một ô trắng và một ô đen
    for (int i = 0; i < R; i++) for (int j = 0; j < C; j++)
        if (a[i][j] == '.' && (i + j) % 2 == 0)
            for (int d = 0; d < 4; d++) {
                int x = i + dx[d], y = j + dy[d];
                if (x >= 0 && x < R && y >= 0 && y < C && a[x][y] == '.') g[i * C + j].push_back(x * C + y);
            }
    int ans = 0;
    for (int u = 0; u < N; u++) if (!g[u].empty()) { stamp++; if (kuhn(u)) ans++; }
    printf("%d\n", ans);
    return 0;
}
