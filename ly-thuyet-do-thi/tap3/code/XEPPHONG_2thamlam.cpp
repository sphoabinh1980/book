#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("XEPPHONG.INP", "r")) {
        freopen("XEPPHONG.INP", "r", stdin);
        freopen("XEPPHONG.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    vector<char> busy(m + 1, 0);
    int ans = 0;
    for (int i = 1; i <= n; i++) {              // mỗi thí sinh lấy phòng trống đầu tiên trong danh sách
        int k; scanf("%d", &k);
        bool placed = false;
        while (k--) {
            int p; scanf("%d", &p);
            if (!placed && !busy[p]) { busy[p] = 1; placed = true; ans++; }
        }
    }
    printf("%d\n", ans);
    return 0;
}
