#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CHUYENDOI.INP", "r")) {
        freopen("CHUYENDOI.INP", "r", stdin);
        freopen("CHUYENDOI.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<vector<int>> g(n + 1);          // danh sách kề
    vector<pair<int,int>> e;               // danh sách cạnh
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) {
            int x;
            scanf("%d", &x);
            if (!x) continue;
            g[i].push_back(j);             // j tăng dần nên g[i] tự sắp xếp
            if (i < j) e.push_back({i, j});// mỗi cạnh chỉ lấy một lần
        }
    printf("%d\n", (int)e.size());
    for (auto [u, v] : e) printf("%d %d\n", u, v);
    for (int i = 1; i <= n; i++) {
        printf("%d", (int)g[i].size());
        for (int v : g[i]) printf(" %d", v);
        printf("\n");
    }
    return 0;
}
