#include <bits/stdc++.h>
using namespace std;

int R, C, K;
vector<string> a;
const int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};

long long countAll() {                     // đếm lại toàn bộ bản đồ: O(R·C)
    long long c = 0;
    for (int x = 0; x < R; x++)
        for (int y = 0; y < C; y++) {
            if (a[x][y] != '.') continue;
            int k = 0;
            for (int d = 0; d < 4; d++) {
                int u = x + dx[d], v = y + dy[d];
                if (u >= 0 && u < R && v >= 0 && v < C && a[u][v] == '.') k++;
            }
            if (k == K) c++;
        }
    return c;
}

int main() {
    if (fopen("BANDO.INP", "r")) {
        freopen("BANDO.INP", "r", stdin);
        freopen("BANDO.OUT", "w", stdout);
    }
    int q;
    cin >> R >> C >> K >> q;
    a.resize(R);
    for (auto &s : a) cin >> s;
    printf("%lld\n", countAll());
    while (q--) {
        int x, y;
        scanf("%d %d", &x, &y); x--; y--;
        a[x][y] = (a[x][y] == '.' ? '#' : '.');
        printf("%lld\n", countAll());
    }
    return 0;
}
