#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("XETAI.INP", "r")) {
        freopen("XETAI.INP", "r", stdin);
        freopen("XETAI.OUT", "w", stdout);
    }
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    // b[i][j]: tải trọng lớn nhất từ i tới j (0 = chưa có đường)
    vector<vector<int>> b(n + 1, vector<int>(n + 1, 0));
    for (int i = 0; i < m; i++) {
        int u, v, c;
        scanf("%d %d %d", &u, &v, &c);
        b[u][v] = max(b[u][v], c);              // nhiều đường: giữ đường chịu tải tốt nhất
        b[v][u] = max(b[v][u], c);
    }
    // Floyd với phép toán (max, min)
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++) {
            if (!b[i][k]) continue;
            for (int j = 1; j <= n; j++)
                b[i][j] = max(b[i][j], min(b[i][k], b[k][j]));
        }
    while (q--) {
        int s, t;
        scanf("%d %d", &s, &t);
        printf("%d\n", b[s][t]);
    }
    return 0;
}
