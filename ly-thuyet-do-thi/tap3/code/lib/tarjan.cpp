// g: đồ thị có hướng, đỉnh 1..n. comp[v] = số hiệu thành phần, đánh số theo
// thứ tự tô pô NGƯỢC (cung giữa hai thành phần đi từ số lớn sang số nhỏ). Trả về số thành phần.
int tarjan(int n, const vector<vector<int>> &g, vector<int> &comp) {
    vector<int> num(n + 1, 0), low(n + 1, 0), it(n + 1, 0), S, cs;
    vector<char> onS(n + 1, 0);
    comp.assign(n + 1, -1);
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
                if (low[u] == num[u]) {
                    int v;
                    do { v = S.back(); S.pop_back(); onS[v] = 0; comp[v] = c; } while (v != u);
                    c++;
                }
            }
        }
    }
    return c;
}
