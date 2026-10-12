#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
void print128(unsigned __int128 x) {               // in số 128 bit: tách từng chữ số
    char s[45]; int k = 0;
    do { s[k++] = '0' + (int)(x % 10); x /= 10; } while (x);
    while (k) putchar(s[--k]);
}
int main() {
    if (fopen("CATGACH.INP", "r")) {
        freopen("CATGACH.INP", "r", stdin); freopen("CATGACH.OUT", "w", stdout);
    }
    int T; scanf("%d", &T);
    while (T--) {
        ull a, b; scanf("%llu %llu", &a, &b);
        ull g = __gcd(a, b);
        printf("%llu ", g);
        print128((unsigned __int128)(a / g) * (b / g));   // có thể tới 10^36
        putchar('\n');
    }
}
