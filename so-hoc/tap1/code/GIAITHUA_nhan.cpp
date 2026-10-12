#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("NHANLON.INP", "r")) {
        freopen("NHANLON.INP", "r", stdin);
        freopen("NHANLON.OUT", "w", stdout);
    }
    string s, t;
    cin >> s >> t;
    int L1 = s.size(), L2 = t.size();
    vector<long long> c(L1 + L2, 0);   // tích có không quá L1 + L2 chữ số
    for (int i = 0; i < L1; i++)
        for (int j = 0; j < L2; j++)   // chữ số hàng 10^i nhân hàng 10^j
            c[i + j] += (s[L1 - 1 - i] - '0') * (t[L2 - 1 - j] - '0');
    for (int k = 0; k + 1 < L1 + L2; k++) {   // dồn nhớ một lượt
        c[k + 1] += c[k] / 10;
        c[k] %= 10;
    }
    int k = L1 + L2 - 1;
    while (k > 0 && c[k] == 0) k--;    // bỏ các số 0 thừa ở đầu
    for (; k >= 0; k--) cout << c[k];
    cout << "\n";
    return 0;
}
