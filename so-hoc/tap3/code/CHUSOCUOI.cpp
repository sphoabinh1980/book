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
        string a, b;                        // số rất lớn: đọc vào xâu
        cin >> a >> b;
        int x = a.back() - '0';             // a mod 10 = chữ số cuối
        if (b == "0") { puts("1"); continue; }   // a^0 = 1
        int e = 0;                          // e = b mod 4 (Horner)
        for (char c : b) e = (e * 10 + (c - '0')) % 4;
        if (e == 0) e = 4;                  // b chia hết 4: dùng mũ 4
        int r = 1;
        for (int i = 0; i < e; i++) r = r * x % 10;
        printf("%d\n", r);
    }
    return 0;
}
