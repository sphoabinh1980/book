#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("NOITIENG.INP", "r")) {
        freopen("NOITIENG.INP", "r", stdin);
        freopen("NOITIENG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> a(m), b(m);
    for (int i = 0; i < m; i++) scanf("%d %d", &a[i], &b[i]);
    int ans = -1;
    for (int v = 1; v <= n; v++) {         // thử từng người, đếm lại trên toàn bộ danh sách
        int in = 0, out = 0;
        for (int i = 0; i < m; i++) {
            if (b[i] == v) in++;
            if (a[i] == v) out++;
        }
        if (in == n - 1 && out == 0) ans = v;
    }
    printf("%d\n", ans);
    return 0;
}
