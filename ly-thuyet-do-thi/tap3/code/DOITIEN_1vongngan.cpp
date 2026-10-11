#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DOITIEN.INP", "r")) {
        freopen("DOITIEN.INP", "r", stdin);
        freopen("DOITIEN.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> u(m), v(m); vector<double> r(m);
    for (int i = 0; i < m; i++) scanf("%d %d %lf", &u[i], &v[i], &r[i]);
    bool ok = false;
    for (int i = 0; i < m; i++)                 // vòng 2 quầy và vòng 3 quầy
        for (int j = 0; j < m; j++) {
            if (v[i] != u[j]) continue;
            if (v[j] == u[i] && r[i] * r[j] > 1 + 1e-9) ok = true;
            for (int k = 0; k < m && !ok; k++)
                if (v[j] == u[k] && v[k] == u[i] && r[i] * r[j] * r[k] > 1 + 1e-9) ok = true;
        }
    puts(ok ? "YES" : "NO");
    return 0;
}
