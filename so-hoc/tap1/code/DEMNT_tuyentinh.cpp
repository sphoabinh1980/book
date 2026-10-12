#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DEMNT.INP", "r")) {
        freopen("DEMNT.INP", "r", stdin);
        freopen("DEMNT.OUT", "w", stdout);
    }
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    vector<int> a(q), b(q);
    int N = 1;
    for (int i = 0; i < q; i++) {
        cin >> a[i] >> b[i];
        N = max(N, b[i]);
    }
    vector<int> lp(N + 1, 0), pr;           // lp[x]: ước NT nhỏ nhất của x
    for (int i = 2; i <= N; i++) {
        if (lp[i] == 0) { lp[i] = i; pr.push_back(i); }
        // gạch i · p với mọi SNT p ≤ lp[i]: mỗi hợp số bị gạch đúng 1 lần
        for (int p : pr) {
            if (p > lp[i] || (long long)i * p > N) break;
            lp[i * p] = p;
        }
    }
    vector<int> c(N + 1, 0);
    for (int x = 1; x <= N; x++) c[x] = c[x - 1] + (x > 1 && lp[x] == x);
    for (int i = 0; i < q; i++)
        cout << c[b[i]] - c[a[i] - 1] << "\n";
    return 0;
}
