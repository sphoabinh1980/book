#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> U, V, p;
int root(int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }

bool connectedWithout(int skip) {
    p.resize(n + 1); iota(p.begin(), p.end(), 0);
    int c = n;
    for (int i = 1; i <= m; i++) if (i != skip) {
        int a = root(U[i]), b = root(V[i]);
        if (a != b) { p[a] = b; c--; }
    }
    return c == 1;
}

int main() {
    if (fopen("CAPDUPHONG.INP", "r")) {
        freopen("CAPDUPHONG.INP", "r", stdin);
        freopen("CAPDUPHONG.OUT", "w", stdout);
    }
    scanf("%d %d", &n, &m);
    U.resize(m + 1); V.resize(m + 1);
    for (int i = 1; i <= m; i++) scanf("%d %d", &U[i], &V[i]);
    vector<char> isb(m + 1, 0);
    for (int i = 1; i <= m; i++) isb[i] = !connectedWithout(i);   // cầu: bỏ đi thì mất liên thông
    p.resize(n + 1); iota(p.begin(), p.end(), 0);
    for (int i = 1; i <= m; i++) if (!isb[i]) p[root(U[i])] = root(V[i]);
    vector<int> deg(n + 1, 0);
    int comps = 0, leaves = 0;
    for (int v = 1; v <= n; v++) if (root(v) == v) comps++;
    for (int i = 1; i <= m; i++) if (isb[i]) { deg[root(U[i])]++; deg[root(V[i])]++; }
    for (int v = 1; v <= n; v++) if (root(v) == v && deg[v] == 1) leaves++;
    printf("%d\n", comps == 1 ? 0 : (leaves + 1) / 2);
    return 0;
}
