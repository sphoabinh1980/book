#include <bits/stdc++.h>
using namespace std;

vector<int> p;
int root(int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }

int main() {
    if (fopen("PHACAU.INP", "r")) {
        freopen("PHACAU.INP", "r", stdin);
        freopen("PHACAU.OUT", "w", stdout);
    }
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    vector<int> U(m + 1), V(m + 1);
    for (int i = 1; i <= m; i++) scanf("%d %d", &U[i], &V[i]);
    vector<char> alive(m + 1, 1);
    while (q--) {
        int k;
        scanf("%d", &k);
        alive[k] = 0;
        p.resize(n + 1); iota(p.begin(), p.end(), 0);   // dựng lại DSU từ đầu: O(n + m)
        int cnt = n;
        for (int i = 1; i <= m; i++)
            if (alive[i]) { int a = root(U[i]), b = root(V[i]); if (a != b) { p[a] = b; cnt--; } }
        printf("%d\n", cnt);
    }
    return 0;
}
