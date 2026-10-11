#include <bits/stdc++.h>
using namespace std;

int R, C, K;
vector<string> a;
const int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};

bool inside(int x, int y) { return x >= 0 && x < R && y >= 0 && y < C; }

// 1 nếu ô (x, y) là ô khả nghi, 0 nếu không
int good(int x, int y) {
    if (a[x][y] != '.') return 0;
    int k = 0;
    for (int d = 0; d < 4; d++) {
        int u = x + dx[d], v = y + dy[d];
        if (inside(u, v) && a[u][v] == '.') k++;
    }
    return k == K;
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
    long long cnt = 0;
    for (int x = 0; x < R; x++)
        for (int y = 0; y < C; y++) cnt += good(x, y);
    printf("%lld\n", cnt);
    while (q--) {
        int x, y;
        scanf("%d %d", &x, &y); x--; y--;
        // chỉ ô (x, y) và bốn ô kề bị ảnh hưởng
        vector<pair<int,int>> cells = {{x, y}};
        for (int d = 0; d < 4; d++)
            if (inside(x + dx[d], y + dy[d])) cells.push_back({x + dx[d], y + dy[d]});
        for (auto [u, v] : cells) cnt -= good(u, v);   // bỏ đóng góp cũ
        a[x][y] = (a[x][y] == '.' ? '#' : '.');
        for (auto [u, v] : cells) cnt += good(u, v);   // cộng đóng góp mới
        printf("%lld\n", cnt);
    }
    return 0;
}
