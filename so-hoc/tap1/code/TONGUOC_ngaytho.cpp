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
    for (long long i = 1; i <= n; i++)
        s += n / i;                // số bội của i trong [1, n]
    cout << s << "\n";
    return 0;
}
