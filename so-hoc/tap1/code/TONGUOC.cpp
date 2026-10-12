#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TONGUOC.INP", "r")) {
        freopen("TONGUOC.INP", "r", stdin);
        freopen("TONGUOC.OUT", "w", stdout);
    }
    long long n;
    cin >> n;
    long long s = 0;
    for (long long i = 1, j; i <= n; i = j + 1) {
        long long q = n / i;       // giá trị chung của cả khối
        j = n / q;                 // chỉ số lớn nhất có n / j == q
        s += q * (j - i + 1);      // khối [i, j] góp q * (độ dài khối)
    }
    cout << s << "\n";
    return 0;
}
