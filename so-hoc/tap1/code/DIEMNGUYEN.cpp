#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {   // Euclid (Bài 3)
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    if (fopen("DIEMNGUYEN.INP", "r")) {
        freopen("DIEMNGUYEN.INP", "r", stdin);
        freopen("DIEMNGUYEN.OUT", "w", stdout);
    }
    long long x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    long long dx = llabs(x2 - x1), dy = llabs(y2 - y1);
    cout << gcd(dx, dy) + 1 << "\n";   // gcd(0, 0) = 0: đoạn suy biến
    return 0;
}
