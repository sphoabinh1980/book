#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TINDON.INP", "r")) {
        freopen("TINDON.INP", "r", stdin);
        freopen("TINDON.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> g(n + 1);
    vector<pair<int,int>> e(m);
    for (auto &x : e) { scanf("%d %d", &x.first, &x.second); g[x.first].push_back(x.second); }
    // Tarjan không đệ quy: comp[v] = số hiệu thành phần liên thông mạnh của v
    vector<int> num(n + 1, 0), low(n + 1, 0), comp(n + 1, -1), it(n + 1, 0), S, cs;
    vector<char> onS(n + 1, 0);
    int timer = 0, c = 0;
    for (int s = 1; s <= n; s++) if (!num[s]) {
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
                if (low[u] == num[u]) {         // u là "gốc" của một thành phần: lấy cả thành phần ra
                    int v;
                    do { v = S.back(); S.pop_back(); onS[v] = 0; comp[v] = c; } while (v != u);
                    c++;
                }
            }
        }
    }
    // SAI: đếm các thành phần không có cung đi RA (nhầm chiều lan truyền)
    vector<int> out(c, 0);
    for (auto &x : e) if (comp[x.first] != comp[x.second]) out[comp[x.first]]++;
    printf("%d\n", (int)count(out.begin(), out.end(), 0));
    return 0;
}
