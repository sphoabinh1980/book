#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("PTTS.INP", "r")) {
        freopen("PTTS.INP", "r", stdin);
        freopen("PTTS.OUT", "w", stdout);
    }
    int q;
    cin >> q;
    while (q--) {
        int n;
        cin >> n;
        cout << n << " =";
        bool dau = true;
        for (int d = 2; (long long)d * d <= n; d++) {   // thử chia tới √n
            if (n % d) continue;
            int e = 0;
            while (n % d == 0) n /= d, e++;  // chia hết mức có thể
            cout << (dau ? " " : " * ") << d;
            if (e > 1) cout << "^" << e;
            dau = false;
        }
        if (n > 1) cout << (dau ? " " : " * ") << n;  // phần còn lại là SNT
        cout << "\n";
    }
    return 0;
}
