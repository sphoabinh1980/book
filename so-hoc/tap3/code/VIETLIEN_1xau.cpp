#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("VIETLIEN.INP", "r")) {
        freopen("VIETLIEN.INP", "r", stdin);
        freopen("VIETLIEN.OUT", "w", stdout);
    }
    long long n, m;
    scanf("%lld %lld", &n, &m);
    string s;                               // viết hẳn cả xâu ra
    for (long long i = 1; i <= n; i++) s += to_string(i);
    long long r = 0;                        // rồi lấy dư như bài SODU
    for (char c : s) r = (r * 10 + (c - '0')) % m;
    printf("%lld\n", r);
    return 0;
}
