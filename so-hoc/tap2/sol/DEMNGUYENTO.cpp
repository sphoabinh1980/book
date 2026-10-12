#include <bits/stdc++.h>
using namespace std;
const int N = 10000000;
int main() {
    if (fopen("DEMNGUYENTO.INP", "r")) {
        freopen("DEMNGUYENTO.INP", "r", stdin); freopen("DEMNGUYENTO.OUT", "w", stdout);
    }
    vector<char> gach(N + 1, 0); gach[0] = gach[1] = 1;
    for (long long p = 2; p * p <= N; p++)
        if (!gach[p]) for (long long j = p * p; j <= N; j += p) gach[j] = 1;
    vector<int> c(N + 1, 0), pr;                   // c[x] = π(x); pr = danh sách số nguyên tố
    for (int x = 1; x <= N; x++) {
        c[x] = c[x - 1] + !gach[x];
        if (!gach[x]) pr.push_back(x);
    }
    int q; scanf("%d", &q);
    string out;
    while (q--) {
        int t, x; scanf("%d %d", &t, &x);
        out += to_string(t == 1 ? c[x] : pr[x - 1]) + '\n';   // loại 2: số nguyên tố thứ x
    }
    fputs(out.c_str(), stdout);
}
