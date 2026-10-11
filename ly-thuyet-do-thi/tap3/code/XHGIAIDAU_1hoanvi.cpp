#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("XHGIAIDAU.INP", "r")) {
        freopen("XHGIAIDAU.INP", "r", stdin);
        freopen("XHGIAIDAU.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<pair<int,int>> e(m);
    for (auto &x : e) scanf("%d %d", &x.first, &x.second);
    vector<int> p(n), pos(n + 1), found;
    iota(p.begin(), p.end(), 1);
    int cnt = 0;
    do {                                        // thử mọi bảng xếp hạng
        for (int i = 0; i < n; i++) pos[p[i]] = i;
        bool ok = true;
        for (auto &x : e) if (pos[x.first] > pos[x.second]) { ok = false; break; }
        if (ok) { cnt++; found = p; if (cnt > 1) break; }
    } while (next_permutation(p.begin(), p.end()));
    if (cnt == 0) printf("-1\n");
    else if (cnt > 1) printf("0\n");
    else for (int i = 0; i < n; i++) printf("%d%c", found[i], i == n - 1 ? '\n' : ' ');
    return 0;
}
