#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("BUTRU.INP", "r")) {
        freopen("BUTRU.INP", "r", stdin);
        freopen("BUTRU.OUT", "w", stdout);
    }
    long long n;
    int k;
    cin >> n >> k;
    vector<long long> a(k);
    for (auto &x : a) cin >> x;
    long long ans = 0;
    for (long long x = 1; x <= n; x++)     // xét từng số trong [1, n]
        for (int i = 0; i < k; i++)
            if (x % a[i] == 0) {           // x là bội của a[i]
                ans++;
                break;                     // đếm x đúng một lần
            }
    cout << ans << "\n";
    return 0;
}
