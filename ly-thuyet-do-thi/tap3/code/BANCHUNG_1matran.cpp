#include <bits/stdc++.h>
using namespace std;

const int N = 505;
bool a[N][N];

int main() {
    if (fopen("BANCHUNG.INP", "r")) {
        freopen("BANCHUNG.INP", "r", stdin);
        freopen("BANCHUNG.OUT", "w", stdout);
    }
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    if (n >= N) return 0;                   // ma trận không đủ chỗ
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        a[u][v] = a[v][u] = true;
    }
    while (q--) {
        int u, v;
        scanf("%d %d", &u, &v);
        int c = 0;
        for (int w = 1; w <= n; w++) if (a[u][w] && a[v][w]) c++;
        printf("%d\n", c);
    }
    return 0;
}
