#include <bits/stdc++.h>
using namespace std;

// n có phải số nguyên tố không? Chỉ thử các ước 6k ± 1 không vượt quá √n
bool laNT(long long n) {
    if (n < 2) return false;                // 0 và 1 không nguyên tố
    if (n < 4) return true;                 // 2 và 3
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6)   // i = 5, 11, 17, ...
        if (n % i == 0 || n % (i + 2) == 0) return false;
    return true;
}

int main() {
    if (fopen("KTNT.INP", "r")) {
        freopen("KTNT.INP", "r", stdin);
        freopen("KTNT.OUT", "w", stdout);
    }
    int q;
    cin >> q;
    while (q--) {
        long long n;
        cin >> n;
        cout << (laNT(n) ? "YES" : "NO") << "\n";
    }
    return 0;
}
