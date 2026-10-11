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
    const int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};   // N E S W
    const string H = "NESW";
    // trạng thái (x, y, k): ở ô (x, y), quay mặt hướng k; mã hóa (x * C + y) * 4 + k
    vector<int> d((size_t)R * C * 4, INT_MAX);
    deque<int> q;
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            if (a[i][j] == 'S') {
                int id = (i * C + j) * 4 + H.find(h);
                d[id] = 0; q.push_back(id);
            }
    while (!q.empty()) {
        int id = q.front(); q.pop_front();
        int k = id % 4, x = id / 4 / C, y = id / 4 % C, c = d[id];
        if (a[x][y] == 'T') { printf("%d\n", c); return 0; }
        int u = x + dx[k], v = y + dy[k];
        if (u >= 0 && u < R && v >= 0 && v < C && a[u][v] != '#') {
            int id2 = (u * C + v) * 4 + k;      // tiến: trọng số 0, đẩy vào ĐẦU
            if (c < d[id2]) { d[id2] = c; q.push_front(id2); }
        }
        for (int t : {(k + 1) % 4, (k + 3) % 4}) {
            int id2 = (x * C + y) * 4 + t;      // xoay: trọng số 1, đẩy vào CUỐI
            if (c + 1 < d[id2]) { d[id2] = c + 1; q.push_back(id2); }
        }
    }
    printf("-1\n");
    return 0;
}
