#include <bits/stdc++.h>
using namespace std;

const int MX = 100001;

int main() {
    if (fopen("CHIADOI.INP", "r")) {
        freopen("CHIADOI.INP", "r", stdin);
        freopen("CHIADOI.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        g[u].push_back(v); g[v].push_back(u);
    }
    // Bước 1: tô hai màu từng thành phần bằng BFS, ghi lại hiệu |a - b|
    vector<int> col(n + 1, -1), diffs;
    for (int s = 1; s <= n; s++) {
        if (col[s] >= 0) continue;
        int c[2] = {0, 0};
        col[s] = 0;
        vector<int> q = {s};
        for (size_t h = 0; h < q.size(); h++) {
            int u = q[h];
            c[col[u]]++;
            for (int v : g[u]) {
                if (col[v] < 0) { col[v] = col[u] ^ 1; q.push_back(v); }
                else if (col[v] == col[u]) { printf("-1\n"); return 0; }   // chu trình lẻ
            }
        }
        diffs.push_back(abs(c[0] - c[1]));
    }
    // Bước 2: chia các hiệu thành hai nhóm có tổng gần nhau nhất (tổng tập con)
    int S = 0;
    for (int d : diffs) S += d;
    map<int,int> cnt;                       // gộp các hiệu bằng nhau
    for (int d : diffs) if (d) cnt[d]++;
    bitset<MX> can;
    can[0] = 1;
    for (auto [d, c] : cnt)                 // tách c bản sao thành 1, 2, 4, ... bản
        for (int k = 1; c > 0; k *= 2) {
            int t = min(k, c);
            can |= can << (d * t);
            c -= t;
        }
    int best = S;
    for (int x = 0; x <= S; x++) if (can[x]) best = min(best, abs(S - 2 * x));
    printf("%d\n", best);
    return 0;
}
