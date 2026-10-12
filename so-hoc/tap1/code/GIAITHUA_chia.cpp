#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CHIANHO.INP", "r")) {
        freopen("CHIANHO.INP", "r", stdin);
        freopen("CHIANHO.OUT", "w", stdout);
    }
    string s;
    long long b;                   // chia số lớn s cho số nhỏ b <= 10^9
    cin >> s >> b;
    string q;                      // thương, tính từ chữ số cao nhất
    long long r = 0;               // số dư của phần đầu (như Bài 1)
    for (char ch : s) {
        r = r * 10 + (ch - '0');
        q.push_back('0' + r / b);  // r < 10 · b nên r / b là một chữ số
        r %= b;
    }
    size_t k = 0;
    while (k + 1 < q.size() && q[k] == '0') k++;   // bỏ số 0 ở đầu
    cout << q.substr(k) << " " << r << "\n";
    return 0;
}
