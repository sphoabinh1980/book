#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("PTTS.INP", "r")) {
        freopen("PTTS.INP", "r", stdin);
        freopen("PTTS.OUT", "w", stdout);
    }
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    vector<int> a(q);
    int N = 2;
    for (int i = 0; i < q; i++) {
        cin >> a[i];
        N = max(N, a[i]);
    }
    vector<int> spf(N + 1, 0);              // ước nguyên tố nhỏ nhất
    for (long long i = 2; i <= N; i++)
        if (spf[i] == 0) {                  // i nguyên tố
            spf[i] = i;
            for (long long j = i * i; j <= N; j += i)
                if (spf[j] == 0) spf[j] = i;    // i là SNT đầu tiên gạch j
        }
    for (int i = 0; i < q; i++) {
        int n = a[i];
        cout << n << " =";
        bool dau = true;
        while (n > 1) {
            int p = spf[n], e = 0;          // p chắc chắn là ước nguyên tố
            while (n % p == 0) n /= p, e++;
            cout << (dau ? " " : " * ") << p;
            if (e > 1) cout << "^" << e;
            dau = false;
        }
        cout << "\n";
    }
    return 0;
}
