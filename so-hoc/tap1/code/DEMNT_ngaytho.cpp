#include <bits/stdc++.h>
using namespace std;

bool laNT(int n) {                          // thử ước tới √n (Bài 5)
    if (n < 2) return false;
    for (int d = 2; (long long)d * d <= n; d++)
        if (n % d == 0) return false;
    return true;
}

int main() {
    if (fopen("DEMNT.INP", "r")) {
        freopen("DEMNT.INP", "r", stdin);
        freopen("DEMNT.OUT", "w", stdout);
    }
    int q;
    cin >> q;
    while (q--) {
        int a, b, dem = 0;
        cin >> a >> b;
        for (int x = a; x <= b; x++)        // kiểm tra lại từng số
            if (laNT(x)) dem++;
        cout << dem << "\n";
    }
    return 0;
}
