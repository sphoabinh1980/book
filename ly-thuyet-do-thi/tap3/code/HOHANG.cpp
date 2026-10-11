#include <bits/stdc++.h>
using namespace std;

const int LG = 18;                              // 2^18 > 2e5

int main() {
    if (fopen("HOHANG.INP", "r")) {
        freopen("HOHANG.INP", "r", stdin);
        freopen("HOHANG.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<vector<int>> ch(n + 1);              // danh sách con
    int rt = 0;
    for (int i = 1; i <= n; i++) {
        int p;
        scanf("%d", &p);
        if (p) ch[p].push_back(i); else rt = i; // ông tổ có cha = 0
    }
    // BFS từ ông tổ: độ sâu và up[v][j] = tổ tiên thứ 2^j
    vector<array<int, LG + 1>> up(n + 1);
    vector<int> dep(n + 1, 0), q = {rt};
    up[rt].fill(rt);
    for (size_t h = 0; h < q.size(); h++) {
        int u = q[h];
        for (int v : ch[u]) {
            dep[v] = dep[u] + 1;
            up[v][0] = u;
            for (int j = 1; j <= LG; j++) up[v][j] = up[up[v][j - 1]][j - 1];
            q.push_back(v);
        }
    }
    int Q;
    scanf("%d", &Q);
    while (Q--) {
        int u, v;
        scanf("%d %d", &u, &v);
        int diff = abs(dep[u] - dep[v]);
        if (dep[u] < dep[v]) swap(u, v);
        for (int j = LG; j >= 0; j--)           // nâng u lên cùng độ sâu với v
            if (dep[u] - (1 << j) >= dep[v]) u = up[u][j];
        if (u != v) {                           // nhảy cả hai lên khi tổ tiên còn khác nhau
            for (int j = LG; j >= 0; j--)
                if (up[u][j] != up[v][j]) { u = up[u][j]; v = up[v][j]; }
            u = up[u][0];
        }
        printf("%d %d\n", u, diff);
    }
    return 0;
}
