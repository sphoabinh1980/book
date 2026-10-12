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
        long long a, b;
        cin >> a >> b;
        long long r = 1;
        for (long long i = 0; i < b; i++)   // nhân b lần, giữ chữ số cuối
            r = r * (a % 10) % 10;
        printf("%lld\n", r);
    }
    return 0;
}
