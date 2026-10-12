#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<vector<ll>> Mat;
ll m;

Mat mul(const Mat &A, const Mat &B) {    // nhân ma trận bất kì, mod m
    int r = A.size(), t = B.size(), c = B[0].size();
    Mat C(r, vector<ll>(c, 0));
    for (int i = 0; i < r; i++)
        for (int l = 0; l < t; l++)
            for (int j = 0; j < c; j++)
                C[i][j] = (C[i][j] + A[i][l] * B[l][j]) % m;
    return C;
}

Mat power(Mat A, ll e) {                 // A^e, A vuông
    int k = A.size();
    Mat R(k, vector<ll>(k, 0));
    for (int i = 0; i < k; i++) R[i][i] = 1 % m;
    while (e > 0) {
        if (e & 1) R = mul(R, A);
        A = mul(A, A);
        e >>= 1;
    }
    return R;
}

int main() {
    if (fopen("FIBO.INP", "r")) {
        freopen("FIBO.INP", "r", stdin);
        freopen("FIBO.OUT", "w", stdout);
    }
    int k;
    ll n;
    cin >> k >> n >> m;
    // f(i) = c1 f(i-1) + c2 f(i-2) + ... + ck f(i-k)
    vector<ll> c(k), f(k);
    for (auto &x : c) cin >> x;
    for (auto &x : f) cin >> x;          // f(0), f(1), ..., f(k-1)
    Mat T(k, vector<ll>(k, 0));          // ma trận đồng hành
    for (int j = 0; j < k; j++) T[0][j] = c[j] % m;
    for (int i = 1; i < k; i++) T[i][i - 1] = 1 % m;
    Mat v(k, vector<ll>(1));             // v = (f(k-1), ..., f(1), f(0))
    for (int i = 0; i < k; i++) v[i][0] = f[k - 1 - i] % m;
    v = mul(power(T, n), v);             // v = (f(n+k-1), ..., f(n))
    cout << v[k - 1][0] << "\n";
    return 0;
}
