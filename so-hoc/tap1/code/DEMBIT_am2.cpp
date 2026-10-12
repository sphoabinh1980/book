#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("COSOAM2.INP", "r")) {
        freopen("COSOAM2.INP", "r", stdin);
        freopen("COSOAM2.OUT", "w", stdout);
    }
    long long n;                  // |n| <= 10^18, có thể âm
    cin >> n;
    string s;
    while (n != 0) {
        long long r = n % (-2);   // C++: r thuộc {-1, 0, 1}
        n /= -2;
        if (r < 0) {              // sửa số dư âm: r += 2, thương tăng 1
            r += 2;
            n += 1;
        }
        s.push_back('0' + r);
    }
    if (s.empty()) s = "0";
    reverse(s.begin(), s.end());
    cout << s << "\n";
    return 0;
}
