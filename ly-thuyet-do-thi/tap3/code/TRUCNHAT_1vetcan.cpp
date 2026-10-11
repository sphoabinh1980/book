#include <bits/stdc++.h>
using namespace std;

int n, d;
vector<int> a, b;
vector<vector<int>> can, day;

bool pick(int j, int from);

bool go(int j) {                                // xếp lần lượt từng ngày
    if (j > d) return true;
    return pick(j, 0);
}

bool pick(int j, int from) {                    // chọn thêm người cho ngày j (vét cạn tổ hợp)
    if ((int)day[j].size() == b[j]) return go(j + 1);
    for (int x = from; x < (int)can[j].size(); x++) {
        int i = can[j][x];
        if (a[i] == 0) continue;
        a[i]--; day[j].push_back(i);
        if (pick(j, x + 1)) return true;
        a[i]++; day[j].pop_back();
    }
    return false;
}

int main() {
    if (fopen("TRUCNHAT.INP", "r")) {
        freopen("TRUCNHAT.INP", "r", stdin);
        freopen("TRUCNHAT.OUT", "w", stdout);
    }
    scanf("%d %d", &n, &d);
    a.resize(n + 1); b.resize(d + 1); can.resize(d + 1); day.resize(d + 1);
    for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
    for (int j = 1; j <= d; j++) scanf("%d", &b[j]);
    for (int i = 1; i <= n; i++) { int k; scanf("%d", &k); while (k--) { int j; scanf("%d", &j); can[j].push_back(i); } }
    if (!go(1)) { printf("NO\n"); return 0; }
    printf("YES\n");
    for (int j = 1; j <= d; j++) {
        for (int i : day[j]) printf("%d ", i);
        printf("\n");
    }
    return 0;
}
