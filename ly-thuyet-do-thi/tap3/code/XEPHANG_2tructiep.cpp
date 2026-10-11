#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("XEPHANG.INP", "r")) {
        freopen("XEPHANG.INP", "r", stdin);
        freopen("XEPHANG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<set<int>> rel(n + 1);
    for (int i = 0; i < m; i++) { int a, b; scanf("%d %d", &a, &b); rel[a].insert(b); rel[b].insert(a); }
    vector<int> ans;                            // LỖI: chỉ dùng kết quả trực tiếp
    for (int v = 1; v <= n; v++) if ((int)rel[v].size() == n - 1) ans.push_back(v);
    printf("%d\n", (int)ans.size());
    for (size_t i = 0; i < ans.size(); i++) printf("%d%c", ans[i], i + 1 == ans.size() ? '\n' : ' ');
    return 0;
}
