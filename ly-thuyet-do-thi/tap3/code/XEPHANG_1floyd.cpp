#include <bits/stdc++.h>
using namespace std;

const int N = 2005;
bool r[N][N];

int main() {
    if (fopen("XEPHANG.INP", "r")) {
        freopen("XEPHANG.INP", "r", stdin);
        freopen("XEPHANG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) { int a, b; scanf("%d %d", &a, &b); r[a][b] = true; }
    for (int k = 1; k <= n; k++)                // bao đóng bắc cầu kiểu Floyd: O(n^3)
        for (int i = 1; i <= n; i++)
            if (r[i][k])
                for (int j = 1; j <= n; j++)
                    if (r[k][j]) r[i][j] = true;
    vector<int> ans;
    for (int v = 1; v <= n; v++) {
        int c = 0;
        for (int u = 1; u <= n; u++) if (r[u][v] || r[v][u]) c++;
        if (c == n - 1) ans.push_back(v);
    }
    printf("%d\n", (int)ans.size());
    for (size_t i = 0; i < ans.size(); i++) printf("%d%c", ans[i], i + 1 == ans.size() ? '\n' : ' ');
    return 0;
}
