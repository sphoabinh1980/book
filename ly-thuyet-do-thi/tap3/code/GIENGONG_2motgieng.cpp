#include <bits/stdc++.h>
using namespace std;

vector<int> p;
int root(int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }

int main() {
    if (fopen("GIENGONG.INP", "r")) {
        freopen("GIENGONG.INP", "r", stdin);
        freopen("GIENGONG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    vector<array<int,3>> e(m);
    for (auto &x : e) scanf("%d %d %d", &x[1], &x[2], &x[0]);
    sort(e.begin(), e.end());
    // LỖI: chỉ đào MỘT giếng rẻ nhất, phần còn lại nối ống bằng Kruskal
    long long tot = *min_element(a.begin() + 1, a.end());
    p.resize(n + 1); iota(p.begin(), p.end(), 0);
    int cnt = n;
    for (auto &x : e) { int u = root(x[1]), v = root(x[2]); if (u != v) { p[u] = v; cnt--; tot += x[0]; } }
    if (cnt > 1) {                              // nhóm nào chưa có nước thì đào thêm giếng rẻ nhất trong nhóm
        map<int, long long> cheap;
        for (int v = 1; v <= n; v++) { int r = root(v); if (!cheap.count(r) || a[v] < cheap[r]) cheap[r] = a[v]; }
        int first = root(min_element(a.begin() + 1, a.end()) - a.begin());
        for (auto [r, c] : cheap) if (r != first) tot += c;
    }
    printf("%lld\n", tot);
    return 0;
}
