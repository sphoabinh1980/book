#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll m;

// trả về cặp (F(n), F(n + 1)) mod m
pair<ll, ll> fib(ll n) {
    if (n == 0) return {0, 1 % m};
    pair<ll, ll> p = fib(n / 2);         // (F(k), F(k + 1)), k = n / 2
    ll a = p.first, b = p.second;
    ll c = a * ((2 * b - a + m) % m) % m;    // F(2k) = F(k)(2F(k+1) - F(k))
    ll d = (a * a + b * b) % m;              // F(2k+1) = F(k)^2 + F(k+1)^2
    if (n % 2 == 0) return {c, d};
    return {d, (c + d) % m};
}

int main() {
    if (fopen("FIBO.INP", "r")) {
        freopen("FIBO.INP", "r", stdin);
        freopen("FIBO.OUT", "w", stdout);
    }
    ll n;
    cin >> n >> m;
    cout << fib(n).first << "\n";
    return 0;
}
