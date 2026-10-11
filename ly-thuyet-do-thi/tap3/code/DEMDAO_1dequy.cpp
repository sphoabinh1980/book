#include <bits/stdc++.h>
using namespace std;

int R, C, area;
vector<string> a;

void dfs(int x, int y) {                   // loang đệ quy
    if (x < 0 || x >= R || y < 0 || y >= C || a[x][y] != '#') return;
    a[x][y] = 'x';
    area++;
    dfs(x - 1, y); dfs(x + 1, y); dfs(x, y - 1); dfs(x, y + 1);
}

int main() {
    if (fopen("DEMDAO.INP", "r")) {
        freopen("DEMDAO.INP", "r", stdin);
        freopen("DEMDAO.OUT", "w", stdout);
    }
    cin >> R >> C;
    a.resize(R);
    for (auto &s : a) cin >> s;
    int cnt = 0, best = 0;
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            if (a[i][j] == '#') {
                cnt++; area = 0;
                dfs(i, j);
                best = max(best, area);
            }
    printf("%d %d\n", cnt, best);
    return 0;
}
