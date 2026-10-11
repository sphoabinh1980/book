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
    vector<int> U(m), V(m); vector<ll> C(m);
    for (int i = 0; i < m; i++) scanf("%d %d %lld", &U[i], &V[i], &C[i]);
    const ll INF = LLONG_MAX / 4;
    vector<ll> d(n + 1, INF);
    d[1] = 0;
    for (int it = 0; it < k; it++)              // LỖI: nới lỏng ngay trên d, không sao chép
        for (int i = 0; i < m; i++)
            if (d[U[i]] < INF && d[U[i]] + C[i] < d[V[i]]) d[V[i]] = d[U[i]] + C[i];
    printf("%lld\n", d[n] >= INF ? -1 : d[n]);
    return 0;
}
