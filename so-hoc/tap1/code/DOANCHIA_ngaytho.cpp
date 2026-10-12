#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DOANCHIA.INP", "r")) {
        freopen("DOANCHIA.INP", "r", stdin);
        freopen("DOANCHIA.OUT", "w", stdout);
    }
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long k;
    cin >> n >> k;
    vector<long long> a(n);
    for (auto &x : a) cin >> x;
    long long ans = 0;
    for (int l = 0; l < n; l++) {
        long long s = 0;              // tổng a[l..r]
        for (int r = l; r < n; r++) {
            s += a[r];
            if (s % k == 0) ans++;    // đúng cả khi s âm
        }
    }
    cout << ans << "\n";
    return 0;
}
