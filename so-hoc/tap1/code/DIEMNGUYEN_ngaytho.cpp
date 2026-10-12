#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DIEMNGUYEN.INP", "r")) {
        freopen("DIEMNGUYEN.INP", "r", stdin);
        freopen("DIEMNGUYEN.OUT", "w", stdout);
    }
    long long x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    if (x1 == x2) {                   // đoạn thẳng đứng (hoặc một điểm)
        cout << llabs(y2 - y1) + 1 << "\n";
        return 0;
    }
    if (x1 > x2) {                    // cho x1 < x2
        swap(x1, x2);
        swap(y1, y2);
    }
    long long dx = x2 - x1, dy = y2 - y1, cnt = 0;
    for (long long x = x1; x <= x2; x++)
        // y = y1 + (x - x1) · dy / dx nguyên <=> dx | (x - x1) · dy
        if ((x - x1) * dy % dx == 0) cnt++;
    cout << cnt << "\n";
    return 0;
}
