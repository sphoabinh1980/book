#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// a^b mod m bằng đệ quy: a^b = (a^(b/2))^2, nhân thêm a nếu b lẻ
ll power(ll a, ll b, ll m) {
    if (b == 0) return 1 % m;
    ll h = power(a, b / 2, m);              // h = a^(b/2) mod m
    ll r = (__int128)h * h % m;
    if (b % 2 == 1) r = (__int128)r * (a % m) % m;
    return r;
}

int main() {
    if (fopen("LUYTHUA.INP", "r")) {
        freopen("LUYTHUA.INP", "r", stdin);
        freopen("LUYTHUA.OUT", "w", stdout);
    }
    ll a, b, m;
    cin >> a >> b >> m;
    cout << power(a, b, m) << "\n";
    return 0;
}
