#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("ROBOTXOAY.INP", "r")) {
        freopen("ROBOTXOAY.INP", "r", stdin);
        freopen("ROBOTXOAY.OUT", "w", stdout);
    }
    int R, C; char h;
    cin >> R >> C >> h;
    vector<string> a(R);
    for (auto &s : a) cin >> s;
    const int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};
    string H = "NESW";
    vector<int> d((size_t)R * C * 4, INT_MAX);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;   // Dijkstra trên trạng thái
    for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) if (a[i][j] == 'S') { int id = (i * C + j) * 4 + H.find(h); d[id] = 0; pq.push({0, id}); }
    while (!pq.empty()) {
        auto [c, id] = pq.top(); pq.pop();
        if (c != d[id]) continue;
        int k = id % 4, x = id / 4 / C, y = id / 4 % C;
        if (a[x][y] == 'T') { printf("%d\n", c); return 0; }
        int u = x + dx[k], v = y + dy[k];
        if (u >= 0 && u < R && v >= 0 && v < C && a[u][v] != '#') {
            int id2 = (u * C + v) * 4 + k;
            if (c < d[id2]) { d[id2] = c; pq.push({c, id2}); }
        }
        for (int t : {(k + 1) % 4, (k + 3) % 4}) {
            int id2 = (x * C + y) * 4 + t;
            if (c + 1 < d[id2]) { d[id2] = c + 1; pq.push({c + 1, id2}); }
        }
    }
    printf("-1\n");
    return 0;
}
