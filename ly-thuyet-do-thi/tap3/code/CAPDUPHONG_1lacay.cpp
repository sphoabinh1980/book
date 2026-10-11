#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CAPDUPHONG.INP", "r")) {
        freopen("CAPDUPHONG.INP", "r", stdin);
        freopen("CAPDUPHONG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> deg(n + 1, 0);
    for (int i = 0; i < m; i++) { int u, v; scanf("%d %d", &u, &v); deg[u]++; deg[v]++; }
    int leaves = 0;                             // coi mạng như một cây: đếm lá
    for (int v = 1; v <= n; v++) if (deg[v] == 1) leaves++;
    printf("%d\n", n == 1 ? 0 : (leaves + 1) / 2);
    return 0;
}
