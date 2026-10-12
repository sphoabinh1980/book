#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool laNT(ll n) {                           // thử ước tới √n (Bài 5)
    if (n < 2) return false;
    for (ll d = 2; d * d <= n; d++)
        if (n % d == 0) return false;
    return true;
}

int main() {
    if (fopen("SANGDOAN.INP", "r")) {
        freopen("SANGDOAN.INP", "r", stdin);
        freopen("SANGDOAN.OUT", "w", stdout);
    }
    ll L, R;
    cin >> L >> R;
    vector<ll> kq;
    for (ll x = L; x <= R; x++)             // kiểm tra riêng từng số
        if (laNT(x)) kq.push_back(x);
    cout << kq.size() << "\n";
    for (size_t i = 0; i < kq.size(); i++)
        cout << kq[i] << (i + 1 < kq.size() ? " " : "\n");
    return 0;
}
