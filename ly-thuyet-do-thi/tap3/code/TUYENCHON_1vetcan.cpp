#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TUYENCHON.INP", "r")) {
        freopen("TUYENCHON.INP", "r", stdin);
        freopen("TUYENCHON.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> X(m), Y(m);
    for (int i = 0; i < m; i++) scanf("%d %d", &X[i], &Y[i]);
    auto sat = [](int mask, int x) {            // mong muốn x có được thực hiện không?
        bool take = mask >> (abs(x) - 1) & 1;
        return x > 0 ? take : !take;
    };
    for (int mask = 0; mask < (1 << n); mask++) {   // thử mọi phương án nhận/loại
        bool ok = true;
        for (int i = 0; i < m && ok; i++) ok = sat(mask, X[i]) || sat(mask, Y[i]);
        if (ok) {
            printf("YES\n");
            for (int i = 0; i < n; i++) putchar('0' + (mask >> i & 1));
            printf("\n");
            return 0;
        }
    }
    printf("NO\n");
    return 0;
}
