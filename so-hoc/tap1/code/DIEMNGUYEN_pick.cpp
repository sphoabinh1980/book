#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    if (fopen("PICK.INP", "r")) {
        freopen("PICK.INP", "r", stdin);
        freopen("PICK.OUT", "w", stdout);
    }
    int n;
    cin >> n;                         // đa giác n đỉnh, liệt kê theo thứ tự
    vector<long long> x(n), y(n);
    for (int i = 0; i < n; i++) cin >> x[i] >> y[i];
    long long S2 = 0, B = 0;          // S2 = 2 lần diện tích
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;          // cạnh nối đỉnh i với đỉnh i + 1
        S2 += x[i] * y[j] - x[j] * y[i];          // công thức dây giày
        B += gcd(llabs(x[j] - x[i]), llabs(y[j] - y[i]));
    }
    S2 = llabs(S2);
    long long I = (S2 - B + 2) / 2;   // Pick: S = I + B/2 - 1
    cout << S2 / 2 << (S2 % 2 ? ".5" : "") << " " << B << " " << I << "\n";
    return 0;
}
