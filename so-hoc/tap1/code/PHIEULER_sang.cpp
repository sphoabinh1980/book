#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("SANGPHI.INP", "r")) {
        freopen("SANGPHI.INP", "r", stdin);
        freopen("SANGPHI.OUT", "w", stdout);
    }
    int N;
    scanf("%d", &N);
    vector<int> phi(N + 1);
    for (int i = 0; i <= N; i++) phi[i] = i;
    for (int p = 2; p <= N; p++)
        if (phi[p] == p)                    // chưa bị sửa: p nguyên tố
            for (int j = p; j <= N; j += p)
                phi[j] -= phi[j] / p;       // nhân φ(j) với (1 - 1/p)
    for (int i = 1; i <= N; i++) printf("%d ", phi[i]);
    printf("\n");
    return 0;
}
