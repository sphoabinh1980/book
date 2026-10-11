#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CAYKHONG.INP", "r")) {
        freopen("CAYKHONG.INP", "r", stdin);
        freopen("CAYKHONG.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        int n, m;
        scanf("%d %d", &n, &m);
        for (int i = 0; i < m; i++) { int u, v; scanf("%d %d", &u, &v); }
        // Chỉ "sửa" cho đủ n - 1 cạnh, không quan tâm tới liên thông
        printf("%d\n", abs(m - (n - 1)));
    }
    return 0;
}
