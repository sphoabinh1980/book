#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
typedef array<array<ll, 3>, 3> Mat;
Mat mul(const Mat &A, const Mat &B) {
    Mat C = {};
    for (int i = 0; i < 3; i++) for (int l = 0; l < 3; l++) if (A[i][l])
        for (int j = 0; j < 3; j++) C[i][j] = (C[i][j] + A[i][l] * B[l][j]) % MOD;
    return C;
}
// trạng thái v = (f[x], f[x-1], f[x-2]); đi thêm d bậc: v <- T^d · v
array<ll, 3> go(array<ll, 3> v, ll d) {
    Mat R = {{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}}, T = {{{1, 1, 1}, {1, 0, 0}, {0, 1, 0}}};
    for (; d; d >>= 1, T = mul(T, T)) if (d & 1) R = mul(R, T);
    array<ll, 3> w = {0, 0, 0};
    for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) w[i] = (w[i] + R[i][j] * v[j]) % MOD;
    return w;
}
int main() {
    if (fopen("TRIBO.INP", "r")) {
        freopen("TRIBO.INP", "r", stdin); freopen("TRIBO.OUT", "w", stdout);
    }
    ll n; int K; scanf("%lld %d", &n, &K);
    vector<ll> b(K);
    for (auto &x : b) scanf("%lld", &x);
    sort(b.begin(), b.end());                      // các bậc hỏng không cho theo thứ tự
    array<ll, 3> v = {1, 0, 0}; ll x = 0;          // f[0] = 1 (đứng ở chân cầu thang)
    for (ll y : b) { v = go(v, y - x); v[0] = 0; x = y; }   // không được đứng trên bậc hỏng
    v = go(v, n - x);
    printf("%lld\n", v[0]);
}
