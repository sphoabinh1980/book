#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("VIETLIEN.INP", "r")) {
        freopen("VIETLIEN.INP", "r", stdin);
        freopen("VIETLIEN.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    int r = 0, p = 10 % m, nxt = 10;        // SAI: r * p có thể vượt 2^31
    for (int i = 1; i <= n; i++) {
        if (i == nxt) { p = p * 10 % m; nxt *= 10; }
        r = (r * p + i % m) % m;
    }
    printf("%d\n", r);
    return 0;
}
