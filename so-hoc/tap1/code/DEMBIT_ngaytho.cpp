#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DEMBIT.INP", "r")) {
        freopen("DEMBIT.INP", "r", stdin);
        freopen("DEMBIT.OUT", "w", stdout);
    }
    long long n;
    cin >> n;
    long long s = 0;              // tổng số bit 1 của 1..n
    for (long long i = 1; i <= n; i++) {
        long long x = i;
        while (x > 0) {           // đếm bit 1 của i: xét từng bit
            s += x & 1;           // bit thấp nhất
            x >>= 1;              // bỏ bit thấp nhất
        }
    }
    cout << s << "\n";
    return 0;
}
