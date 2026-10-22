#include <bits/stdc++.h>
using namespace std;
int n, k;
long long target, cnt;
vector<long long> a, g;
void Try(int i, int used) {
    if (i == n) {
        if (used == k) cnt++;
        return;
    }
    if (n - i < k - used) return;
    for (int j = 0; j < used; j++) {
        if (g[j] + a[i] > target) continue;
        g[j] += a[i];
        Try(i + 1, used);
        g[j] -= a[i];
    }
    if (used < k) {
        g[used] = a[i];
        Try(i + 1, used + 1);
        g[used] = 0;
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    if (fopen("XEPDEU.INP", "r")) {
        freopen("XEPDEU.INP", "r", stdin);
        freopen("XEPDEU.OUT", "w", stdout);
    }
    cin >> n >> k;
    a.resize(n);
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sum += a[i];
    }
    if (sum % k != 0) {
        cout << 0 << '\n';
        return 0;
    }
    target = sum / k;
    sort(a.begin(), a.end(), greater<long long>());
    if (a[0] > target) {
        cout << 0 << '\n';
        return 0;
    }
    g.assign(k, 0);
    Try(0, 0);
    cout << cnt << '\n';
}