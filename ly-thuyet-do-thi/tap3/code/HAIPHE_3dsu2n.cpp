#include <bits/stdc++.h>
using namespace std;

vector<int> p;
int root(int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }
void unite(int a, int b) { p[root(a)] = root(b); }

int main() {
    if (fopen("HAIPHE.INP", "r")) {
        freopen("HAIPHE.INP", "r", stdin);
        freopen("HAIPHE.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    // đỉnh a: "a ở phe A", đỉnh a + n: "a ở phe B"
    p.resize(2 * n + 1); iota(p.begin(), p.end(), 0);
    for (int i = 1; i <= m; i++) {
        int a, b, t;
        scanf("%d %d %d", &a, &b, &t);
        if (t == 0) {
            if (root(a) == root(b + n)) { printf("%d\n", i); return 0; }
            unite(a, b); unite(a + n, b + n);
        } else {
            if (root(a) == root(b)) { printf("%d\n", i); return 0; }
            unite(a, b + n); unite(a + n, b);
        }
    }
    printf("0\n");
    return 0;
}
