#include <bits/stdc++.h>
using namespace std;
const int N = 10000000;
int main() {
    if (fopen("SINHDOI.INP", "r")) {
        freopen("SINHDOI.INP", "r", stdin); freopen("SINHDOI.OUT", "w", stdout);
    }
    vector<char> gach(N + 3, 0); gach[0] = gach[1] = 1;
    for (long long p = 2; p * p <= N + 2; p++)
        if (!gach[p]) for (long long j = p * p; j <= N + 2; j += p) gach[j] = 1;
    vector<int> t(N + 1, 0);                       // t[x] = số p ≤ x mà p và p + 2 cùng nguyên tố
    for (int x = 1; x <= N; x++) t[x] = t[x - 1] + (!gach[x] && !gach[x + 2]);
    int q; scanf("%d", &q);
    string out;
    while (q--) {
        int a, b; scanf("%d %d", &a, &b);
        int r = b - 2 >= a ? t[b - 2] - t[a - 1] : 0;   // cần a ≤ p và p + 2 ≤ b
        out += to_string(r) + '\n';
    }
    fputs(out.c_str(), stdout);
}
