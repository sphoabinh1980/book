#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("BUTRU.INP", "r")) {
        freopen("BUTRU.INP", "r", stdin);
        freopen("BUTRU.OUT", "w", stdout);
    }
    long long n;
    int k;
    cin >> n >> k;
    vector<long long> a(k);
    for (auto &x : a) cin >> x;
    // L[S] = lcm các a[i] với i thuộc tập con S, hoặc n + 1 nếu > n
    vector<long long> L(1 << k);
    L[0] = 1;
    long long ans = 0;
    for (int S = 1; S < (1 << k); S++) {
        int i = __builtin_ctz(S);          // phần tử nhỏ nhất của S
        long long x = L[S & (S - 1)];      // lcm của S khi bỏ i đi
        if (x > n) L[S] = n + 1;           // đã vượt n thì mãi vượt n
        else {
            long long y = x / __gcd(x, a[i]);
            // y * a[i] > n  <=>  y > n / a[i]: so sánh trước khi nhân
            L[S] = (y > n / a[i]) ? n + 1 : y * a[i];
        }
        long long cnt = n / L[S];          // số bội của L[S] trong [1, n]
        if (__builtin_popcount(S) % 2 == 1) ans += cnt;
        else ans -= cnt;
    }
    cout << ans << "\n";
    return 0;
}
