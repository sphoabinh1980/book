#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("GIAITHUA.INP", "r")) {
        freopen("GIAITHUA.INP", "r", stdin);
        freopen("GIAITHUA.OUT", "w", stdout);
    }
    int n;
    cin >> n;
    unsigned long long f = 1;    // chỉ đúng khi n <= 20
    for (int i = 2; i <= n; i++)
        f *= i;                  // từ 21! trở đi: tràn số, sai âm thầm
    cout << f << "\n";
    return 0;
}
