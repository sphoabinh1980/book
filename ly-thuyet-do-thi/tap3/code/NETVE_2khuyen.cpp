#include <bits/stdc++.h>
using namespace std;

vector<int> p;
int root(int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }

int main() {
    if (fopen("NETVE.INP", "r")) {
        freopen("NETVE.INP", "r", stdin);
        freopen("NETVE.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        int n, m;
        scanf("%d %d", &n, &m);
        p.resize(n + 1); iota(p.begin(), p.end(), 0);
        vector<int> deg(n + 1, 0);
        for (int i = 0; i < m; i++) {
            int u, v; scanf("%d %d", &u, &v);
            deg[u]++; if (v != u) deg[v]++;     // SAI: vòng nhỏ chỉ được cộng 1
            p[root(u)] = root(v);
        }
        int odd = 0, r = -1;
        bool ok = true;
        for (int v = 1; v <= n; v++) if (deg[v]) {   // chỉ xét các điểm có đoạn nối vào
            odd += deg[v] % 2;
            if (r < 0) r = root(v);
            else if (root(v) != r) ok = false;   // các đoạn nằm trên hai mảnh rời nhau
        }
        puts(ok && (odd == 0 || odd == 2) ? "YES" : "NO");
    }
    return 0;
}
