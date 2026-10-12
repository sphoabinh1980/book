#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("NGHICHDAO.INP", "r")) {
        freopen("NGHICHDAO.INP", "r", stdin);
        freopen("NGHICHDAO.OUT", "w", stdout);
    }
    int n;
    ll p;                               // p nguyên tố, p > n
    scanf("%d %lld", &n, &p);
    vector<ll> inv(n + 1);
    inv[1] = 1;
    for (int i = 2; i <= n; i++)        // p = (p/i)·i + p%i, với p%i < i
        inv[i] = (p - p / i) * inv[p % i] % p;
    for (int i = 1; i <= n; i++) printf("%lld ", inv[i]);
    printf("\n");
    return 0;
}
