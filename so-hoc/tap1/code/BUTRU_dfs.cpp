#include <bits/stdc++.h>
using namespace std;
long long n, ans = 0;
int k;
vector<long long> a;

// đã chọn một tập con có lcm = l, dấu sg; thử thêm a[j] với j >= i
void dfs(int i, long long l, int sg) {
    for (int j = i; j < k; j++) {
        long long y = l / __gcd(l, a[j]);
        if (y > n / a[j]) continue;        // lcm > n: cắt cả nhánh
        long long nl = y * a[j];
        ans += sg * (n / nl);
        dfs(j + 1, nl, -sg);
    }
}

int main() {
    if (fopen("BUTRU.INP", "r")) {
        freopen("BUTRU.INP", "r", stdin);
        freopen("BUTRU.OUT", "w", stdout);
    }
    cin >> n >> k;
    a.resize(k);
    for (auto &x : a) cin >> x;
    sort(a.begin(), a.end());
    a.erase(unique(a.begin(), a.end()), a.end());  // bỏ số trùng
    k = a.size();
    dfs(0, 1, 1);
    cout << ans << "\n";
    return 0;
}
