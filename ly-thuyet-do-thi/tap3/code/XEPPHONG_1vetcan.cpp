#include <bits/stdc++.h>
using namespace std;

int n, m, best = 0;
vector<vector<int>> g;
vector<char> busy;

void go(int i, int cnt) {                       // xét thí sinh i, đã xếp được cnt người
    if (cnt + (n - i + 1) <= best) return;      // có xếp hết số còn lại cũng không hơn
    if (i > n) { best = cnt; return; }
    for (int p : g[i]) if (!busy[p]) {          // xếp i vào phòng p
        busy[p] = 1; go(i + 1, cnt + 1); busy[p] = 0;
    }
    go(i + 1, cnt);                             // hoặc không xếp i
}

int main() {
    if (fopen("XEPPHONG.INP", "r")) {
        freopen("XEPPHONG.INP", "r", stdin);
        freopen("XEPPHONG.OUT", "w", stdout);
    }
    scanf("%d %d", &n, &m);
    g.resize(n + 1); busy.assign(m + 1, 0);
    for (int i = 1; i <= n; i++) { int k; scanf("%d", &k); g[i].resize(k); for (int &x : g[i]) scanf("%d", &x); }
    go(1, 0);
    printf("%d\n", best);
    return 0;
}
