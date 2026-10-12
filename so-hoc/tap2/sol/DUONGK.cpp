#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
const ull MOD = 1000000007, M2 = MOD * MOD;
int n;
ull P[60][50][50];                                 // P[j] = A^(2^j)
int main() {
    if (fopen("DUONGK.INP", "r")) {
        freopen("DUONGK.INP", "r", stdin); freopen("DUONGK.OUT", "w", stdout);
    }
    int m, q; scanf("%d %d %d", &n, &m, &q);
    for (int i = 0; i < m; i++) { int u, v; scanf("%d %d", &u, &v); P[0][u - 1][v - 1] = 1; }
    for (int j = 1; j < 60; j++)                   // bình phương liên tiếp: 59 phép nhân ma trận
        for (int a = 0; a < n; a++) for (int c = 0; c < n; c++) {
            ull s = 0;
            for (int b = 0; b < n; b++) {
                s += P[j - 1][a][b] * P[j - 1][b][c];
                if (s >= M2) s -= M2;           // giữ s < 2·MOD², không tràn
            }
            P[j][a][c] = s % MOD;
        }
    while (q--) {
        int s, t; ull K; scanf("%d %d %llu", &s, &t, &K);
        vector<ull> row(n, 0), nr(n);              // vectơ hàng: số đường đi từ s tới từng đỉnh
        row[s - 1] = 1;
        for (int j = 0; j < 60; j++) if (K >> j & 1) {   // row <- row · A^(2^j): chỉ O(n^2)
            for (int c = 0; c < n; c++) {
                ull x = 0;
                for (int b = 0; b < n; b++) { x += row[b] * P[j][b][c]; if (x >= M2) x -= M2; }
                nr[c] = x % MOD;
            }
            row = nr;
        }
        printf("%llu\n", row[t - 1]);
    }
}
