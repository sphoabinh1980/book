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
    vector<long long> cnt(k, 0);  // cnt[d]: số tổng tiền tố có dư d
    cnt[0] = 1;                   // S[0] = 0 (tiền tố rỗng)
    long long s = 0, ans = 0;     // s = S[r] mod k, luôn trong [0, k)
    for (int r = 1; r <= n; r++) {
        long long a;
        cin >> a;
        s = ((s + a) % k + k) % k;    // số dư không âm (Bài 1)
        ans += cnt[s];            // ghép với mọi S[l - 1] cùng số dư
        cnt[s]++;
    }
    cout << ans << "\n";
    return 0;
}
