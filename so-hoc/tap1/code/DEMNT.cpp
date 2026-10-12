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
    int N = 1;                              // chỉ cần sàng tới max b
    for (int i = 0; i < q; i++) {
        cin >> a[i] >> b[i];
        N = max(N, b[i]);
    }
    vector<char> gach(N + 1, 0);        // gach[x] = 1: x không nguyên tố
    gach[0] = gach[1] = 1;
    for (long long p = 2; p * p <= N; p++)
        if (!gach[p])                       // p nguyên tố: gạch bội từ p^2
            for (long long j = p * p; j <= N; j += p) gach[j] = 1;
    vector<int> c(N + 1, 0);                // c[x] = số SNT trong [1, x]
    for (int x = 1; x <= N; x++) c[x] = c[x - 1] + !gach[x];
    for (int i = 0; i < q; i++)
        cout << c[b[i]] - c[a[i] - 1] << "\n";
    return 0;
}
