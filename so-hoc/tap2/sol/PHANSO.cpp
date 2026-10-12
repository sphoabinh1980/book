#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
    if (fopen("PHANSO.INP", "r")) {
        freopen("PHANSO.INP", "r", stdin); freopen("PHANSO.OUT", "w", stdout);
    }
    int q; scanf("%d", &q);
    vector<int> L(q), R(q); int N = 1;
    for (int i = 0; i < q; i++) { scanf("%d %d", &L[i], &R[i]); N = max(N, R[i]); }
    vector<int> phi(N + 1);
    for (int i = 0; i <= N; i++) phi[i] = i;
    for (int p = 2; p <= N; p++)
        if (phi[p] == p)                    // p nguyên tố: nhân (1 - 1/p) vào mọi bội
            for (int j = p; j <= N; j += p) phi[j] -= phi[j] / p;
    vector<ll> S(N + 1, 0);                 // S[b] = số phân số tối giản trong (0, 1) có mẫu <= b
    for (int b = 2; b <= N; b++) S[b] = S[b - 1] + phi[b];
    for (int i = 0; i < q; i++) printf("%lld\n", S[R[i]] - S[L[i] - 1]);
}
