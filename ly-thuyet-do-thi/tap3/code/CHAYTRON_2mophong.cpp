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
    // fire[x][y], here[x][y]: ô đang cháy / An có thể đang đứng ở ô đó
    vector<vector<char>> fire(R, vector<char>(C, 0)), here(R, vector<char>(C, 0));
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++) { fire[i][j] = a[i][j] == 'F'; here[i][j] = a[i][j] == 'J'; }
    for (int t = 0; ; t++) {                // mô phỏng từng phút trên toàn bảng
        bool any = false;
        for (int i = 0; i < R; i++)
            for (int j = 0; j < C; j++) if (here[i][j]) {
                any = true;
                if (i == 0 || j == 0 || i == R - 1 || j == C - 1) { printf("%d\n", t + 1); return 0; }
            }
        if (!any) break;
        auto nf = fire, nh = here;
        for (int i = 0; i < R; i++)
            for (int j = 0; j < C; j++) if (fire[i][j])
                for (int d = 0; d < 4; d++) {
                    int u = i + dx[d], v = j + dy[d];
                    if (u >= 0 && u < R && v >= 0 && v < C && a[u][v] != '#') nf[u][v] = 1;
                }
        for (int i = 0; i < R; i++)
            for (int j = 0; j < C; j++) {
                nh[i][j] = 0;
                if (a[i][j] == '#' || nf[i][j]) continue;
                for (int d = 0; d < 4; d++) {
                    int u = i + dx[d], v = j + dy[d];
                    if (u >= 0 && u < R && v >= 0 && v < C && here[u][v]) nh[i][j] = 1;
                }
            }
        fire = nf; here = nh;
    }
    printf("-1\n");
    return 0;
}
