#include <bits/stdc++.h>
using namespace std;

// thử mọi ước d từ 2 tới n − 1: đúng nhưng rất chậm
bool laNT(long long n) {
    if (n < 2) return false;
    for (long long d = 2; d < n; d++)
        if (n % d == 0) return false;       // tìm thấy ước thật sự
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
