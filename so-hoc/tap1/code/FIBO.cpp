#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef array<array<ll, 2>, 2> Mat;      // ma trận 2 x 2
ll m;

Mat mul(const Mat &A, const Mat &B) {    // A * B, mọi phần tử mod m
    Mat C;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)      // mỗi tích < 10^18, tổng < 2*10^18
            C[i][j] = (A[i][0] * B[0][j] + A[i][1] * B[1][j]) % m;
    return C;
}

int main() {
    if (fopen("FIBO.INP", "r")) {
        freopen("FIBO.INP", "r", stdin);
        freopen("FIBO.OUT", "w", stdout);
    }
    ll n;
    cin >> n >> m;
    Mat R = {{{1 % m, 0}, {0, 1 % m}}};  // R = I (ma trận đơn vị)
    Mat M = {{{1, 1}, {1, 0}}};          // M = Q^(2^t) ở lượt thứ t
    while (n > 0) {                      // lũy thừa nhanh như Bài 9
        if (n & 1) R = mul(R, M);
        M = mul(M, M);
        n >>= 1;
    }
    cout << R[0][1] << "\n";             // Q^n = [[F(n+1), F(n)], ...]
    return 0;
}
