#include <bits/stdc++.h>
using namespace std;

vector<int> par;
int root(int x) {                          // DSU, nén đường đi không đệ quy
    while (par[x] != x) { par[x] = par[par[x]]; x = par[x]; }
    return x;
}

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
        par.assign(n + 1, 0);
        iota(par.begin(), par.end(), 0);
        int k = n;                         // số thành phần liên thông
        for (int i = 0; i < m; i++) {
            int u, v;
            scanf("%d %d", &u, &v);
            u = root(u); v = root(v);
            if (u != v) { par[u] = v; k--; }
        }
        // xóa m - (n - k) cạnh thừa, thêm k - 1 cạnh nối các thành phần
        printf("%lld\n", (long long)(m - (n - k)) + (k - 1));
    }
    return 0;
}
