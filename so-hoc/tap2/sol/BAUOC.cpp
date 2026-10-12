#include <bits/stdc++.h>
using namespace std;
int main() {
    if (fopen("BAUOC.INP", "r")) {
        freopen("BAUOC.INP", "r", stdin); freopen("BAUOC.OUT", "w", stdout);
    }
    const int B = 10000;                           // 10^4 = căn bậc ba của 10^12
    vector<char> gach(B + 1, 0); vector<int> pr;
    for (int p = 2; p <= B; p++) if (!gach[p]) {
        pr.push_back(p);
        for (int j = p * p; j <= B; j += p) gach[j] = 1;
    }
    int n; scanf("%d", &n);
    while (n--) {
        long long a; scanf("%lld", &a);
        int cnt = 0;
        for (int p : pr) {                         // bóc hết các thừa số nguyên tố ≤ 10^4
            if ((long long)p * p > a) break;       // a = 1 hoặc nguyên tố: không còn p^2 nào
            if (a % p) continue;
            int e = 0;
            while (a % p == 0) a /= p, e++;
            if (e >= 2) cnt++;                     // p^2 là một "số ba ước" chia hết a
        }
        // phần còn lại a: mọi ước nguyên tố > 10^4 nên a = 1, q, q·r hoặc q^2
        long long s = sqrtl((long double)a);
        while (s * s > a) s--;
        while ((s + 1) * (s + 1) <= a) s++;
        if (a > 1 && s * s == a) cnt++;
        printf("%d\n", cnt);
    }
}
