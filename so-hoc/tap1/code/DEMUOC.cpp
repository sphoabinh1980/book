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
    for (long long d = 1; d * d <= n; d++)      // chỉ duyệt d ≤ √n
        if (n % d == 0) {
            long long e = n / d;                // ước "bạn đôi" của d
            cnt++; sum += d;
            if (e != d) { cnt++; sum += e; }    // n chính phương: d = e
        }
    cout << cnt << " " << sum << "\n";
    return 0;
}
