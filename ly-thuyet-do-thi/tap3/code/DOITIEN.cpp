#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DOITIEN.INP", "r")) {
        freopen("DOITIEN.INP", "r", stdin);
        freopen("DOITIEN.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> U(m), V(m);
    vector<double> W(m);
    for (int i = 0; i < m; i++) {
        double r;
        scanf("%d %d %lf", &U[i], &V[i], &r);
        W[i] = -log(r);                         // tích > 1  <=>  tổng -log < 0
    }
    // Mọi đỉnh đều là nguồn: tương đương thêm đỉnh ảo nối tới mọi đỉnh với trọng số 0
    vector<double> d(n + 1, 0);
    bool neg = false;
    for (int it = 0; it < n; it++) {
        bool changed = false;
        for (int i = 0; i < m; i++)
            if (d[U[i]] + W[i] < d[V[i]] - 1e-9) {
                d[V[i]] = d[U[i]] + W[i];
                changed = true;
            }
        if (!changed) break;
        if (it == n - 1) neg = true;            // lượt thứ n vẫn còn giảm: có chu trình âm
    }
    puts(neg ? "YES" : "NO");
    return 0;
}
