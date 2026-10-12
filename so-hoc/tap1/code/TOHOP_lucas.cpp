#include <bits/stdc++.h>
using namespace std;
long long p;
vector<long long> f, inf;   // giai thừa và nghịch đảo, chỉ tới p - 1

long long power(long long a, long long b) {
    long long r = 1;
    a %= p;
    while (b > 0) {
        if (b & 1) r = r * a % p;
        a = a * a % p;
        b >>= 1;
    }
    return r;
}

long long Csmall(long long n, long long k) {   // 0 <= n < p
    if (k > n) return 0;
    return f[n] * inf[k] % p * inf[n - k] % p;
}

int main() {
    if (fopen("TOHOP.INP", "r")) {
        freopen("TOHOP.INP", "r", stdin);
        freopen("TOHOP.OUT", "w", stdout);
    }
    long long n, k;
    cin >> n >> k >> p;          // n, k <= 10^18; p nguyên tố <= 10^6
    f.assign(p, 1);
    inf.assign(p, 1);
    for (long long i = 1; i < p; i++) f[i] = f[i - 1] * i % p;
    inf[p - 1] = power(f[p - 1], p - 2);
    for (long long i = p - 1; i >= 1; i--) inf[i - 1] = inf[i] * i % p;
    long long r = (k <= n) ? 1 : 0;
    while (r && (n > 0 || k > 0)) {  // tách chữ số cơ số p của n, k
        r = r * Csmall(n % p, k % p) % p;
        n /= p;
        k /= p;
    }
    cout << r << "\n";
    return 0;
}
