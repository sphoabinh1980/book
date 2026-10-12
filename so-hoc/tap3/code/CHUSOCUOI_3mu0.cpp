#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("CHUSOCUOI.INP", "r")) {
        freopen("CHUSOCUOI.INP", "r", stdin);
        freopen("CHUSOCUOI.OUT", "w", stdout);
    }
    int T;
    cin >> T;
    while (T--) {
        string a, b;
        cin >> a >> b;
        int x = a.back() - '0', e = 0;
        for (char c : b) e = (e * 10 + (c - '0')) % 4;
        int r = 1;                          // SAI: b ≡ 0 (mod 4) cho r = 1
        for (int i = 0; i < e; i++) r = r * x % 10;
        printf("%d\n", r);
    }
    return 0;
}
