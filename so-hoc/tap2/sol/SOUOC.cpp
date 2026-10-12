#include <bits/stdc++.h>
using namespace std;
const int N = 10000000;
int spf[N + 1];
int main() {
    if (fopen("SOUOC.INP", "r")) {
        freopen("SOUOC.INP", "r", stdin); freopen("SOUOC.OUT", "w", stdout);
    }
    for (long long i = 2; i <= N; i++)             // sàng ước nguyên tố nhỏ nhất
        if (!spf[i]) {
            spf[i] = i;                            // i nguyên tố
            if (i * i <= N) for (long long j = i * i; j <= N; j += i) if (!spf[j]) spf[j] = i;
        }
    int q; scanf("%d", &q);
    string out;
    while (q--) {
        int n; scanf("%d", &n);
        long long d = 1, s = 1;
        while (n > 1) {
            int p = spf[n], e = 0; long long pk = 1, sum = 1;
            while (n % p == 0) { n /= p; e++; pk *= p; sum += pk; }   // sum = 1 + p + ... + p^e
            d *= e + 1; s *= sum;
        }
        out += to_string(d) + ' ' + to_string(s) + '\n';
    }
    fputs(out.c_str(), stdout);
}
