#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CHUKI.INP", "r")) {
        freopen("CHUKI.INP", "r", stdin);
        freopen("CHUKI.OUT", "w", stdout);
    }
    long long x, c, m;            // x[i+1] = (x[i]^2 + c) mod m
    cin >> x >> c >> m;           // m <= 10^6, 0 <= x, c < m
    vector<int> first(m, -1);     // first[v]: chỉ số đầu tiên có x[i] = v
    for (int i = 0;; i++) {
        if (first[x] != -1) {     // gặp lại một giá trị: đã vào vòng
            int mu = first[x], lam = i - first[x];
            cout << mu << " " << lam << "\n";
            break;
        }
        first[x] = i;
        x = (x * x + c) % m;
    }
    return 0;
}
