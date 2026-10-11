#include <bits/stdc++.h>
using namespace std;

vector<int> p;
int root(int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }

int main() {
    if (fopen("ITDOC.INP", "r")) {
        freopen("ITDOC.INP", "r", stdin);
        freopen("ITDOC.OUT", "w", stdout);
    }
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    vector<array<int,3>> e(m);
    for (auto &x : e) scanf("%d %d %d", &x[1], &x[2], &x[0]);
    sort(e.begin(), e.end());
    p.resize(n + 1); iota(p.begin(), p.end(), 0);
    vector<vector<pair<int,int>>> t(n + 1);     // cây khung nhỏ nhất (rừng)
    for (auto &x : e) {
        int a = root(x[1]), b = root(x[2]);
        if (a != b) { p[a] = b; t[x[1]].push_back({x[2], x[0]}); t[x[2]].push_back({x[1], x[0]}); }
    }
    vector<int> mx(n + 1);
    while (q--) {                               // DFS trên cây cho từng câu hỏi: O(n)
        int s, g;
        scanf("%d %d", &s, &g);
        fill(mx.begin(), mx.end(), -1);
        mx[s] = 0; vector<int> st = {s};
        while (!st.empty()) {
            int u = st.back(); st.pop_back();
            for (auto [v, h] : t[u]) if (mx[v] < 0) { mx[v] = max(mx[u], h); st.push_back(v); }
        }
        printf("%d\n", mx[g]);
    }
    return 0;
}
