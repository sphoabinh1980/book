#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("FIBO.INP", "r")) {
        freopen("FIBO.INP", "r", stdin);
        freopen("FIBO.OUT", "w", stdout);
    }
    long long n, m;
    cin >> n >> m;
    long long a = 0, b = 1 % m;          // a = F(i), b = F(i + 1), i = 0
    for (long long i = 0; i < n; i++) {  // n lần: tịnh tiến i -> i + 1
        long long c = (a + b) % m;
        a = b;
        b = c;
    }
    cout << a << "\n";
    return 0;
}
