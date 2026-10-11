#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("MANGBANBE.INP", "r")) {
        freopen("MANGBANBE.INP", "r", stdin);
        freopen("MANGBANBE.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> g(n + 1);
    while (m--) {
        int u, v;
        scanf("%d %d", &u, &v);
        g[u].push_back(v); g[v].push_back(u);
        vector<char> seen(n + 1, 0);            // đếm lại các nhóm từ đầu: O(n + m)
        int cnt = 0, best = 0;
        for (int s = 1; s <= n; s++) {
            if (seen[s]) continue;
            cnt++; int sz = 0;
            vector<int> st = {s}; seen[s] = 1;
            while (!st.empty()) {
                int x = st.back(); st.pop_back(); sz++;
                for (int y : g[x]) if (!seen[y]) { seen[y] = 1; st.push_back(y); }
            }
            best = max(best, sz);
        }
        printf("%d %d\n", cnt, best);
    }
    return 0;
}
