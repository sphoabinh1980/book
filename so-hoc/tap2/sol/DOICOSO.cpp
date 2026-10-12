#include <bits/stdc++.h>
using namespace std;
int val(char ch) { return isdigit(ch) ? ch - '0' : ch - 'A' + 10; }
int main() {
    if (fopen("DOICOSO.INP", "r")) {
        freopen("DOICOSO.INP", "r", stdin); freopen("DOICOSO.OUT", "w", stdout);
    }
    int q; scanf("%d", &q);
    const char* DIG = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char s[128];
    while (q--) {
        int a, b; scanf("%d %d %s", &a, &b, s);
        unsigned long long v = 0;
        for (char* p = s; *p; p++) v = v * a + val(*p);        // Horner: cơ số a -> giá trị
        string r;
        do { r += DIG[v % b]; v /= b; } while (v > 0);          // chia liên tiếp; v = 0 vẫn in "0"
        reverse(r.begin(), r.end());
        puts(r.c_str());
    }
}
