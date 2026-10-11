#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DUPHONG.INP", "r")) {
        freopen("DUPHONG.INP", "r", stdin);
        freopen("DUPHONG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        g[u].push_back(v); g[v].push_back(u);
    }
    vector<int> comp(n + 1, 0);            // comp[v]: số hiệu nhóm của máy v
    vector<long long> sz(1, 0);            // sz[k]: số máy của nhóm k
    for (int s = 1; s <= n; s++) {
        if (comp[s]) continue;
        int k = sz.size();
        sz.push_back(0);
        vector<int> st = {s};              // DFS bằng ngăn xếp tự quản lí
        comp[s] = k;
        while (!st.empty()) {
            int u = st.back(); st.pop_back();
            sz[k]++;
            for (int v : g[u]) if (!comp[v]) { comp[v] = k; st.push_back(v); }
        }
    }
    for (int v = 1; v <= n; v++) printf("%lld%c", sz[comp[v]], v == n ? '\n' : ' ');
    long long pairs = 0;                   // có thể tới 1,25e11
    for (size_t k = 1; k < sz.size(); k++) pairs += sz[k] * (sz[k] - 1) / 2;
    // cáp mới nối hai nhóm lớn nhất a, b tạo thêm a·b cặp
    vector<long long> s(sz.begin() + 1, sz.end());
    sort(s.rbegin(), s.rend());
    long long best = pairs + (s.size() >= 2 ? s[0] * s[1] : 0);
    printf("%lld\n%lld\n", pairs, best);
    return 0;
}
