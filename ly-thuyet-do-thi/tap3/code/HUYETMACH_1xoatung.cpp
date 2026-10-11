#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> U, V, p;
int root(int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }

int comps(int skip) {                           // số thành phần khi bỏ con đường skip
    p.resize(n + 1); iota(p.begin(), p.end(), 0);
    int c = n;
    for (int i = 1; i <= m; i++) if (i != skip) {
        int a = root(U[i]), b = root(V[i]);
        if (a != b) { p[a] = b; c--; }
    }
    return c;
}

int main() {
    if (fopen("HUYETMACH.INP", "r")) {
        freopen("HUYETMACH.INP", "r", stdin);
        freopen("HUYETMACH.OUT", "w", stdout);
    }
    scanf("%d %d", &n, &m);
    U.resize(m + 1); V.resize(m + 1);
    for (int i = 1; i <= m; i++) scanf("%d %d", &U[i], &V[i]);
    int base = comps(0);
    vector<int> br;
    for (int i = 1; i <= m; i++) if (comps(i) > base) br.push_back(i);   // chặn thử từng đường
    printf("%d\n", (int)br.size());
    for (size_t i = 0; i < br.size(); i++) printf("%d%c", br[i], i + 1 == br.size() ? '\n' : ' ');
    return 0;
}
