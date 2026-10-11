#include <bits/stdc++.h>
using namespace std;

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
        vector<int> deg(n + 1, 0);
        for (int i = 0; i < m; i++) { int u, v; scanf("%d %d", &u, &v); deg[u]++; deg[v]++; }
        int odd = 0;                            // chỉ đếm điểm bậc lẻ, quên kiểm tra liên thông
        for (int v = 1; v <= n; v++) odd += deg[v] % 2;
        puts(odd == 0 || odd == 2 ? "YES" : "NO");
    }
    return 0;
}
