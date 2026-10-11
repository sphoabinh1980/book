#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TUYENCHON.INP", "r")) {
        freopen("TUYENCHON.INP", "r", stdin);
        freopen("TUYENCHON.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    // đỉnh 2i: "nhận i", đỉnh 2i+1: "loại i"; phủ định của đỉnh x là x ^ 1
    auto node = [](int x) { return x > 0 ? 2 * x : 2 * (-x) + 1; };
    int N = 2 * n + 2;
    vector<vector<int>> g(N);
    for (int i = 0; i < m; i++) {
        int x, y; scanf("%d %d", &x, &y);
        int a = node(x), b = node(y);
        g[a ^ 1].push_back(b);                  // (a hoặc b): không a thì phải b
        g[b ^ 1].push_back(a);                  //             không b thì phải a
    }
    // Tarjan không đệ quy
    vector<int> num(N, 0), low(N, 0), comp(N, -1), it(N, 0), S, cs;
    vector<char> onS(N, 0);
    int timer = 0, c = 0;
    for (int s = 2; s < N; s++) if (!num[s]) {
        cs.push_back(s); num[s] = low[s] = ++timer; S.push_back(s); onS[s] = 1;
        while (!cs.empty()) {
            int u = cs.back();
            if (it[u] < (int)g[u].size()) {
                int v = g[u][it[u]++];
                if (!num[v]) { num[v] = low[v] = ++timer; S.push_back(v); onS[v] = 1; cs.push_back(v); }
                else if (onS[v]) low[u] = min(low[u], num[v]);
            } else {
                cs.pop_back();
                if (!cs.empty()) low[cs.back()] = min(low[cs.back()], low[u]);
                if (low[u] == num[u]) {
                    int v;
                    do { v = S.back(); S.pop_back(); onS[v] = 0; comp[v] = c; } while (v != u);
                    c++;
                }
            }
        }
    }
    string s(n, '0');
    for (int i = 1; i <= n; i++) {
        if (comp[2 * i] == comp[2 * i + 1]) { printf("NO\n"); return 0; }
        s[i - 1] = comp[2 * i] > comp[2 * i + 1] ? '1' : '0';   // SAI: chọn ngược chiều
    }
    printf("YES\n%s\n", s.c_str());
    return 0;
}
