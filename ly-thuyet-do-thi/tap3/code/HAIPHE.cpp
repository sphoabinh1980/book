#include <bits/stdc++.h>
using namespace std;

vector<int> p, w;                               // w[x] = 1 nếu x khác phe với p[x]

// trả về (gốc, chẵn lẻ từ x tới gốc); nén đường đi không đệ quy
pair<int,int> root(int x) {
    int r = x, par = 0;
    while (p[r] != r) { par ^= w[r]; r = p[r]; }
    int cur = x, acc = par;                     // acc: chẵn lẻ từ cur tới gốc
    while (p[cur] != cur) {
        int nx = p[cur], wc = w[cur];
        p[cur] = r; w[cur] = acc;               // treo thẳng vào gốc
        acc ^= wc; cur = nx;
    }
    return {r, par};
}

int main() {
    if (fopen("HAIPHE.INP", "r")) {
        freopen("HAIPHE.INP", "r", stdin);
        freopen("HAIPHE.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    p.resize(n + 1); w.assign(n + 1, 0);
    iota(p.begin(), p.end(), 0);
    for (int i = 1; i <= m; i++) {
        int a, b, t;
        scanf("%d %d %d", &a, &b, &t);
        auto [ra, pa] = root(a);
        auto [rb, pb] = root(b);
        if (ra == rb) {                         // đã biết quan hệ giữa a và b
            if ((pa ^ pb) != t) { printf("%d\n", i); return 0; }
        } else {                                // nối ra vào rb sao cho quan hệ a, b đúng bằng t
            p[ra] = rb;
            w[ra] = pa ^ pb ^ t;
        }
    }
    printf("0\n");
    return 0;
}
