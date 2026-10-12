#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CHUSOCUOI.INP", "r")) {
        freopen("CHUSOCUOI.INP", "r", stdin);
        freopen("CHUSOCUOI.OUT", "w", stdout);
    }
    int T;
    cin >> T;
    while (T--) {
        unsigned long long a, b;            // chỉ chứa được số ≤ 1,8·10^19
        cin >> a >> b;
        if (b == 0) { puts("1"); continue; }
        int x = a % 10, e = b % 4;
        if (e == 0) e = 4;
        int r = 1;
        for (int i = 0; i < e; i++) r = r * x % 10;
        printf("%d\n", r);
    }
    return 0;
}
