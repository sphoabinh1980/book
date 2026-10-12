#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll LIM = 1000000000000000000LL, INF = LIM + 1;    // INF: "vượt 10^18"
ll lcm2(ll x, ll y) {                              // BCNN có "bão hòa" tại INF
    if (x == INF || y == INF) return INF;
    ll v = x / __gcd(x, y);
    return v > LIM / y ? INF : v * y;
}
struct Seg { ll v; int lo, hi; };                  // lcm(t[l..r]) = v với mọi l trong [lo, hi]
int main() {
    if (fopen("DENNHAY.INP", "r")) { freopen("DENNHAY.INP", "r", stdin); freopen("DENNHAY.OUT", "w", stdout); }
    int n, q; scanf("%d %d", &n, &q);
    vector<ll> t(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &t[i]);
    vector<int> ql(q), qr(q), ord(q);
    for (int i = 0; i < q; i++) scanf("%d %d", &ql[i], &qr[i]), ord[i] = i;
    sort(ord.begin(), ord.end(), [&](int x, int y) { return qr[x] < qr[y]; });
    vector<ll> res(q);
    vector<Seg> cur, nxt;                          // các đoạn theo l giảm dần, v tăng dần
    int j = 0;
    for (int r = 1; r <= n; r++) {
        nxt.clear(); nxt.push_back({t[r], r, r});
        for (auto &s : cur) {
            ll w = lcm2(s.v, t[r]);
            if (w == nxt.back().v) nxt.back().lo = s.lo;   // gộp các đoạn cùng giá trị
            else nxt.push_back({w, s.lo, s.hi});
        }
        swap(cur, nxt);                            // cur có không quá ~62 đoạn
        for (; j < q && qr[ord[j]] == r; j++) {
            int l = ql[ord[j]];
            for (auto &s : cur) if (s.lo <= l) { res[ord[j]] = s.v; break; }
        }
    }
    for (int i = 0; i < q; i++) printf("%lld\n", res[i] == INF ? -1LL : res[i]);
}
