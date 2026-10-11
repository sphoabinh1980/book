#include <bits/stdc++.h>
using namespace std;

vector<int> p, sz;
int root(int x) { while (p[x] != x) x = p[x]; return x; }   // không nén đường đi

int main() {
    if (fopen("MANGBANBE.INP", "r")) {
        freopen("MANGBANBE.INP", "r", stdin);
        freopen("MANGBANBE.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    p.resize(n + 1); sz.assign(n + 1, 1);
    iota(p.begin(), p.end(), 0);
    int cnt = n, best = 1;
    while (m--) {
        int u, v;
        scanf("%d %d", &u, &v);
        u = root(u); v = root(v);
        if (u != v) {                           // gộp tùy tiện: u treo vào v
            p[u] = v; sz[v] += sz[u]; cnt--;
            best = max(best, sz[v]);
        }
        printf("%d %d\n", cnt, best);
    }
    return 0;
}
