#include <bits/stdc++.h>
using namespace std;

vector<int> p;
int cnt;                                        // số nhóm hiện tại

int root(int x) {
    while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
    return x;
}
void unite(int a, int b) {
    a = root(a); b = root(b);
    if (a != b) { p[a] = b; cnt--; }
}

int main() {
    if (fopen("PHACAU.INP", "r")) {
        freopen("PHACAU.INP", "r", stdin);
        freopen("PHACAU.OUT", "w", stdout);
    }
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    vector<int> U(m + 1), V(m + 1), k(q);
    vector<char> del(m + 1, 0);
    for (int i = 1; i <= m; i++) scanf("%d %d", &U[i], &V[i]);
    for (auto &x : k) { scanf("%d", &x); del[x] = 1; }
    p.resize(n + 1); iota(p.begin(), p.end(), 0);
    cnt = n;
    // Trạng thái cuối: chỉ còn các cầu không bao giờ sập
    for (int i = 1; i <= m; i++) if (!del[i]) unite(U[i], V[i]);
    // Đi ngược thời gian: ghi đáp số rồi XÂY lại cây cầu
    vector<int> ans(q);
    for (int t = q - 1; t >= 0; t--) {
        ans[t] = cnt;                           // số nhóm ngay sau khi cầu k[t] sập
        unite(U[k[t]], V[k[t]]);
    }
    for (int x : ans) printf("%d\n", x);
    return 0;
}
