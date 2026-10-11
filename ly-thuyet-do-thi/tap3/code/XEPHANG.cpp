#include <bits/stdc++.h>
using namespace std;

const int N = 2001;
bitset<N> r[N];                                 // r[a][b] = 1: chắc chắn a mạnh hơn b

int main() {
    if (fopen("XEPHANG.INP", "r")) {
        freopen("XEPHANG.INP", "r", stdin);
        freopen("XEPHANG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        r[a][b] = 1;
    }
    // bao đóng bắc cầu: nếu i mạnh hơn k thì i mạnh hơn mọi người k mạnh hơn
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            if (r[i][k]) r[i] |= r[k];          // n/64 phép tính
    vector<int> ans;
    for (int v = 1; v <= n; v++) {
        int c = r[v].count();                   // số người chắc chắn yếu hơn v
        for (int u = 1; u <= n; u++) if (r[u][v]) c++;   // cộng số người mạnh hơn v
        if (c == n - 1) ans.push_back(v);
    }
    printf("%d\n", (int)ans.size());
    for (size_t i = 0; i < ans.size(); i++) printf("%d%c", ans[i], i + 1 == ans.size() ? '\n' : ' ');
    return 0;
}
