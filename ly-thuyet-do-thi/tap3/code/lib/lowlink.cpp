// g[u] = danh sách (v, số hiệu cạnh); đỉnh 1..n, cạnh 1..m, cho phép cạnh song song.
// isBridge[id] = cạnh id là cầu; cut[u] = số phần còn lại khi bỏ đỉnh u (1 nếu u không là khớp)
void lowlink(int n, int m, const vector<vector<pair<int,int>>> &g, vector<char> &isBridge, vector<int> &cut) {
    vector<int> num(n + 1, 0), low(n + 1, 0), pe(n + 1, 0), it(n + 1, 0), cnt(n + 1, 0);
    isBridge.assign(m + 1, 0); cut.assign(n + 1, 1);
    int timer = 0;
    for (int s = 1; s <= n; s++) if (!num[s]) {
        vector<int> st = {s};
        num[s] = low[s] = ++timer;
        while (!st.empty()) {
            int u = st.back();
            if (it[u] < (int)g[u].size()) {
                auto [v, id] = g[u][it[u]++];
                if (id == pe[u]) continue;      // bỏ đúng cạnh vừa đi tới
                if (num[v]) low[u] = min(low[u], num[v]);
                else { num[v] = low[v] = ++timer; pe[v] = id; st.push_back(v); }
            } else {
                st.pop_back();
                if (st.empty()) break;
                int p = st.back();
                low[p] = min(low[p], low[u]);
                if (low[u] > num[p]) isBridge[pe[u]] = 1;
                if (low[u] >= num[p]) cnt[p]++;
            }
        }
        cnt[s]--;                               // gốc: không có "phần phía trên", bù trước cho +1 dưới đây
    }
    for (int v = 1; v <= n; v++) cut[v] = max(1, cnt[v] + 1);
}
