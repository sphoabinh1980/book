#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TINDON.INP", "r")) {
        freopen("TINDON.INP", "r", stdin);
        freopen("TINDON.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> in(n + 1, 0);
    for (int i = 0; i < m; i++) { int a, b; scanf("%d %d", &a, &b); in[b]++; }
    int cnt = 0;                                // đếm những người không ai kể cho
    for (int v = 1; v <= n; v++) if (in[v] == 0) cnt++;
    printf("%d\n", cnt);
    return 0;
}
