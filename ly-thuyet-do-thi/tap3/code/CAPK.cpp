#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CAPK.INP", "r")) {
        freopen("CAPK.INP", "r", stdin);
        freopen("CAPK.OUT", "w", stdout);
    }
    int n, q;
    scanf("%d %d", &n, &q);
    // Danh sách con lưu dạng "đầu - kế tiếp" để tiết kiệm bộ nhớ
    vector<int> head(n + 1, -1), nxt(n + 1);
    for (int i = 2; i <= n; i++) {
        int p;
        scanf("%d", &p);
        nxt[i] = head[p]; head[p] = i;
    }
    // Đọc hết câu hỏi, gom theo đỉnh v (cũng dạng đầu - kế tiếp)
    vector<int> qk(q), qhead(n + 1, -1), qnxt(q), ans(q);
    for (int i = 0; i < q; i++) {
        int v;
        scanf("%d %d", &v, &qk[i]);
        qnxt[i] = qhead[v]; qhead[v] = i;
    }
    // DFS không đệ quy; path = các đỉnh từ gốc tới đỉnh đang đứng
    vector<int> path, it(head);                 // it[u]: con kế tiếp cần thăm của u
    path.reserve(n);
    auto answer = [&](int v) {                  // trả lời các câu hỏi của v
        for (int j = qhead[v]; j >= 0; j = qnxt[j])
            ans[j] = qk[j] < (int)path.size() ? path[path.size() - 1 - qk[j]] : -1;
    };
    path.push_back(1);
    answer(1);
    while (!path.empty()) {
        int u = path.back();
        if (it[u] < 0) { path.pop_back(); continue; }   // hết con: quay lui
        int v = it[u]; it[u] = nxt[v];
        path.push_back(v);
        answer(v);
    }
    for (int i = 0; i < q; i++) printf("%d\n", ans[i]);
    return 0;
}
