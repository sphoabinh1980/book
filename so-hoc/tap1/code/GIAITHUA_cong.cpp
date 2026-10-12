#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CONGLON.INP", "r")) {
        freopen("CONGLON.INP", "r", stdin);
        freopen("CONGLON.OUT", "w", stdout);
    }
    string s, t;
    cin >> s >> t;                  // hai số tự nhiên rất dài
    vector<int> a, b, c;            // chữ số đảo ngược: a[0] hàng đơn vị
    for (int i = (int)s.size() - 1; i >= 0; i--) a.push_back(s[i] - '0');
    for (int i = (int)t.size() - 1; i >= 0; i--) b.push_back(t[i] - '0');
    int nho = 0;
    for (size_t i = 0; i < max(a.size(), b.size()) || nho; i++) {
        int x = nho;
        if (i < a.size()) x += a[i];
        if (i < b.size()) x += b[i];
        c.push_back(x % 10);        // x <= 9 + 9 + 1 = 19
        nho = x / 10;               // nhớ 0 hoặc 1
    }
    for (int i = (int)c.size() - 1; i >= 0; i--) cout << c[i];
    cout << "\n";
    return 0;
}
