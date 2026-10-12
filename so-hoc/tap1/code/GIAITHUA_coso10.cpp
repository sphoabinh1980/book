#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("GIAITHUA.INP", "r")) {
        freopen("GIAITHUA.INP", "r", stdin);
        freopen("GIAITHUA.OUT", "w", stdout);
    }
    int n;
    cin >> n;
    vector<int> a(1, 1);     // a[0] là chữ số hàng đơn vị; ban đầu a = 1
    for (int x = 2; x <= n; x++) {
        int c = 0;           // số nhớ
        for (size_t i = 0; i < a.size(); i++) {
            int t = a[i] * x + c;
            a[i] = t % 10;   // chữ số giữ lại
            c = t / 10;      // phần nhớ sang hàng kế tiếp
        }
        while (c > 0) {      // số nhớ cuối cùng thành các chữ số mới
            a.push_back(c % 10);
            c /= 10;
        }
    }
    for (int i = (int)a.size() - 1; i >= 0; i--) cout << a[i];
    cout << "\n";
    return 0;
}
