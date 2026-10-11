#include <bits/stdc++.h>
using namespace std;

vector<int> p;
int root(int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }

int main() {
    if (fopen("ITDOC.INP", "r")) {
        freopen("ITDOC.INP", "r", stdin);
        freopen("ITDOC.OUT", "w", stdout);
    }
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    vector<array<int,3>> e(m);
    for (auto &x : e) scanf("%d %d %d", &x[1], &x[2], &x[0]);
    sort(e.begin(), e.end());
    while (q--) {
        int s, t;
        scanf("%d %d", &s, &t);
        if (s == t) { printf("0\n"); continue; }
        p.assign(n + 1, 0); iota(p.begin(), p.end(), 0);
        int ans = -1;
        for (auto &x : e) {                     // thêm dần cạnh theo độ dốc tăng dần
            p[root(x[1])] = root(x[2]);
            if (root(s) == root(t)) { ans = x[0]; break; }
        }
        printf("%d\n", ans);
    }
    return 0;
}
