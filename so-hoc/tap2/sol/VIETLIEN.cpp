#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("VIETLIEN.INP", "r")) {
        freopen("VIETLIEN.INP", "r", stdin);
        freopen("VIETLIEN.OUT", "w", stdout);
    }
    long long n, m; scanf("%lld %lld", &n, &m);
    long long r = 0, p = 10 % m, nxt = 10;        // p = 10^(số chữ số của i) mod m
    for (long long i = 1; i <= n; i++) {
        if (i == nxt) { p = p * 10 % m; nxt *= 10; }
        r = (r * p + i % m) % m;                   // viết thêm i vào bên phải
    }
    printf("%lld\n", r);
}
