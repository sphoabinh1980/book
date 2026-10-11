#include <bits/stdc++.h>
using namespace std;

int n, m, stamp = 0;
vector<vector<int>> g;                          // g[i]: các phòng thí sinh i thi được
vector<int> who, vis;                           // who[p]: thí sinh đang ở phòng p (0: trống)

bool kuhn(int u) {                              // tìm đường tăng xuất phát từ thí sinh u
    for (int p : g[u]) if (vis[p] != stamp) {
        vis[p] = stamp;
        if (!who[p] || kuhn(who[p])) { who[p] = u; return true; }   // phòng trống, hoặc người cũ đổi được phòng
    }
    return false;
}

int main() {
    if (fopen("XEPPHONG.INP", "r")) {
        freopen("XEPPHONG.INP", "r", stdin);
        freopen("XEPPHONG.OUT", "w", stdout);
    }
    scanf("%d %d", &n, &m);
    g.resize(n + 1); who.assign(m + 1, 0); vis.assign(m + 1, 0);
    for (int i = 1; i <= n; i++) {
        int k; scanf("%d", &k);
        g[i].resize(k);
        for (int &x : g[i]) scanf("%d", &x);
    }
    int ans = 0;
    for (int i = 1; i <= n; i++) { stamp++; if (kuhn(i)) ans++; }
    printf("%d\n", ans);
    return 0;
}
