#include <bits/stdc++.h>
using namespace std;

int R, C, stamp = 0;
vector<vector<int>> g;                          // g[hàng r] = các cột c có ô quan trọng (r, c)
vector<int> mc, mr, vis;                        // mc[c]: hàng ghép với cột c; mr[r]: cột ghép với hàng r

bool kuhn(int r) {
    for (int c : g[r]) if (vis[c] != stamp) {
        vis[c] = stamp;
        if (!mc[c] || kuhn(mc[c])) { mc[c] = r; mr[r] = c; return true; }
    }
    return false;
}

int main() {
    if (fopen("CAMERA.INP", "r")) {
        freopen("CAMERA.INP", "r", stdin);
        freopen("CAMERA.OUT", "w", stdout);
    }
    int K;
    scanf("%d %d %d", &R, &C, &K);
    g.resize(R + 1); mc.assign(C + 1, 0); mr.assign(R + 1, 0); vis.assign(C + 1, 0);
    for (int i = 0; i < K; i++) { int r, c; scanf("%d %d", &r, &c); g[r].push_back(c); }
    int t = 0;
    for (int r = 1; r <= R; r++) { stamp++; if (kuhn(r)) t++; }
    // König: Z = các đỉnh tới được từ hàng CHƯA ghép theo đường đan xen
    // (hàng -> cột bằng cạnh bất kì, cột -> hàng bằng cạnh ghép).
    // Phủ đỉnh nhỏ nhất = (hàng KHÔNG thuộc Z) + (cột THUỘC Z).
    vector<char> zr(R + 1, 0), zc(C + 1, 0);
    queue<int> q;
    for (int r = 1; r <= R; r++) if (!mr[r]) { zr[r] = 1; q.push(r); }
    while (!q.empty()) {
        int r = q.front(); q.pop();
        for (int c : g[r]) if (!zc[c]) {
            zc[c] = 1;
            int r2 = mc[c];
            if (r2 && !zr[r2]) { zr[r2] = 1; q.push(r2); }
        }
    }
    printf("%d\n", t);
    for (int r = 1; r <= R; r++) if (!zr[r]) printf("H %d\n", r);
    for (int c = 1; c <= C; c++) if (zc[c]) printf("C %d\n", c);
    return 0;
}
