#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TONGUOC.INP", "r")) {
        freopen("TONGUOC.INP", "r", stdin);
        freopen("TONGUOC.OUT", "w", stdout);
    }
    long long n;
    cin >> n;
    long long r = sqrtl(n);                // r = phần nguyên của căn n
    while (r * r > n) r--;                 // sửa sai số làm tròn
    while ((r + 1) * (r + 1) <= n) r++;
    long long s = 0;
    for (long long i = 1; i <= r; i++) s += n / i;
    cout << 2 * s - r * r << "\n";         // đếm cặp (i, j), i * j <= n
    return 0;
}
