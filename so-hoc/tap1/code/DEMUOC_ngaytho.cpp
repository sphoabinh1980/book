#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DEMUOC.INP", "r")) {
        freopen("DEMUOC.INP", "r", stdin);
        freopen("DEMUOC.OUT", "w", stdout);
    }
    long long n;
    cin >> n;
    long long cnt = 0, sum = 0;
    for (long long d = 1; d <= n; d++)          // thử mọi số từ 1 tới n
        if (n % d == 0) { cnt++; sum += d; }
    cout << cnt << " " << sum << "\n";
    return 0;
}
