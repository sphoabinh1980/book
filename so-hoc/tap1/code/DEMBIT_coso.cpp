#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DOICOSO.INP", "r")) {
        freopen("DOICOSO.INP", "r", stdin);
        freopen("DOICOSO.OUT", "w", stdout);
    }
    long long n;
    int b;                        // 2 <= b <= 36
    cin >> n >> b;
    const string D = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string s;
    do {
        s.push_back(D[n % b]);    // chữ số hàng thấp nhất
        n /= b;                   // bỏ hàng thấp nhất
    } while (n > 0);              // do-while: n = 0 vẫn in "0"
    reverse(s.begin(), s.end());  // các chữ số sinh ra theo thứ tự ngược
    cout << s << "\n";
    return 0;
}
