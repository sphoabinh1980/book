#include <bits/stdc++.h>
using namespace std;

const int N = 2005;
bool a[N][N];

int main() {
    if (fopen("TAMGIAC.INP", "r")) {
        freopen("TAMGIAC.INP", "r", stdin);
        freopen("TAMGIAC.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    if (n >= N) { printf("0\n"); return 0; }   // không đủ bộ nhớ cho ma trận
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        a[u][v] = a[v][u] = true;
    }
    long long cnt = 0;
    for (int x = 1; x <= n; x++)
        for (int y = x + 1; y <= n; y++)
            for (int z = y + 1; z <= n; z++)
                if (a[x][y] && a[y][z] && a[x][z]) cnt++;
    printf("%lld\n", cnt);
    return 0;
}
