#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
typedef array<array<ll, 2>, 2> Mat;
Mat mul(const Mat &A, const Mat &B) {
    Mat C = {};
    for (int i = 0; i < 2; i++) for (int j = 0; j < 2; j++)
        C[i][j] = (A[i][0] * B[0][j] + A[i][1] * B[1][j]) % MOD;
    return C;
}
int main() {
    if (fopen("LATGACH.INP", "r")) {
        freopen("LATGACH.INP", "r", stdin); freopen("LATGACH.OUT", "w", stdout);
    }
    int T; scanf("%d", &T);
    while (T--) {
        ll n; scanf("%lld", &n);
        Mat R = {{{1, 0}, {0, 1}}}, Q = {{{1, 1}, {1, 0}}};
        for (ll e = n; e; e >>= 1, Q = mul(Q, Q)) if (e & 1) R = mul(R, Q);
        printf("%lld\n", R[0][0]);                 // Q^n[0][0] = F(n+1) = số cách lát 2 x n
    }
}
