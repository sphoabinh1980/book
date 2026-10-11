#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TRUCNHAT.INP", "r")) {
        freopen("TRUCNHAT.INP", "r", stdin);
        freopen("TRUCNHAT.OUT", "w", stdout);
    }
    int n, d;
    scanf("%d %d", &n, &d);
    vector<int> a(n + 1), b(d + 1);
    for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
    for (int j = 1; j <= d; j++) scanf("%d", &b[j]);
    vector<vector<int>> can(d + 1);             // can[j]: những học sinh trực được ngày j
    for (int i = 1; i <= n; i++) { int k; scanf("%d", &k); while (k--) { int j; scanf("%d", &j); can[j].push_back(i); } }
    vector<vector<int>> day(d + 1);
    for (int j = 1; j <= d; j++) {              // mỗi ngày chọn những bạn còn "nhiều lượt" nhất
        sort(can[j].begin(), can[j].end(), [&](int x, int y) { return a[x] > a[y]; });
        for (int i : can[j]) if ((int)day[j].size() < b[j] && a[i] > 0) { day[j].push_back(i); a[i]--; }
        if ((int)day[j].size() < b[j]) { printf("NO\n"); return 0; }
    }
    printf("YES\n");
    for (int j = 1; j <= d; j++) {
        for (int i : day[j]) printf("%d ", i);
        printf("\n");
    }
    return 0;
}
