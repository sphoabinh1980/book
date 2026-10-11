#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    if (fopen("BAYRE.INP", "r")) {
        freopen("BAYRE.INP", "r", stdin);
        freopen("BAYRE.OUT", "w", stdout);
    }
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    vector<int> U(m), V(m);
    vector<ll> C(m);
    for (int i = 0; i < m; i++) scanf("%d %d %lld", &U[i], &V[i], &C[i]);
    const ll INF = LLONG_MAX / 4;
    vector<ll> d(n + 1, INF);                   // d sau lượt i: giá rẻ nhất dùng <= i chuyến
    d[1] = 0;
    for (int it = 0; it < k; it++) {
        vector<ll> nd = d;                      // chỉ nới lỏng từ kết quả của lượt trước
        for (int i = 0; i < m; i++)
            if (d[U[i]] < INF && d[U[i]] + C[i] < nd[V[i]]) nd[V[i]] = d[U[i]] + C[i];
        if (nd == d) break;                     // không còn thay đổi: dừng sớm
        d = nd;
    }
    printf("%lld\n", d[n] >= INF ? -1 : d[n]);
    return 0;
}
