#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("SANGDOAN.INP", "r")) {
        freopen("SANGDOAN.INP", "r", stdin);
        freopen("SANGDOAN.OUT", "w", stdout);
    }
    ll L, R;
    cin >> L >> R;
    ll S = sqrtl(R);                        // S = ⌊√R⌋, chỉnh lại cho chắc
    while (S * S > R) S--;
    while ((S + 1) * (S + 1) <= R) S++;
    // Bước 1: sàng Eratosthenes thường cho các số ≤ √R
    vector<char> hop(S + 1, 0);
    vector<ll> ps;
    for (ll i = 2; i <= S; i++)
        if (!hop[i]) {
            ps.push_back(i);
            for (ll j = i * i; j <= S; j += i) hop[j] = 1;
        }
    // Bước 2: gạch bội của từng p trong [L, R]; số x ứng với ô x − L
    vector<char> gach(R - L + 1, 0);
    for (ll p : ps) {
        ll st = max(p * p, (L + p - 1) / p * p);    // bội đầu tiên cần gạch
        for (ll j = st; j <= R; j += p) gach[j - L] = 1;
    }
    if (L == 1) gach[0] = 1;                // 1 không phải số nguyên tố
    vector<ll> kq;
    for (ll x = L; x <= R; x++)
        if (!gach[x - L]) kq.push_back(x);
    cout << kq.size() << "\n";
    for (size_t i = 0; i < kq.size(); i++)
        cout << kq[i] << (i + 1 < kq.size() ? " " : "\n");
    return 0;
}
