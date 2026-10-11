#include <bits/stdc++.h>
using namespace std;

vector<int> p;
int root(int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }

int main() {
    if (fopen("HAIPHE.INP", "r")) {
        freopen("HAIPHE.INP", "r", stdin);
        freopen("HAIPHE.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    p.resize(n + 1); iota(p.begin(), p.end(), 0);
    for (int i = 1; i <= m; i++) {
        int a, b, t;
        scanf("%d %d %d", &a, &b, &t);
        // LỖI: chỉ gộp những người "cùng phe", bỏ qua thông tin "khác phe"
        if (t == 0) p[root(a)] = root(b);
        else if (root(a) == root(b)) { printf("%d\n", i); return 0; }
    }
    printf("0\n");
    return 0;
}
