#include <bits/stdc++.h>
using namespace std;

const int N = 2005;
bitset<N> a[N];

int main() {
    if (fopen("TAMGIAC.INP", "r")) {
        freopen("TAMGIAC.INP", "r", stdin);
        freopen("TAMGIAC.OUT", "w", stdout);
    }
    int n, m;
    scanf("%d %d", &n, &m);
    if (n >= N) { printf("0\n"); return 0; }   // ma trận 1e5 x 1e5 không vừa bộ nhớ
    vector<pair<int,int>> e(m);
    for (auto &[u, v] : e) {
        scanf("%d %d", &u, &v);
        a[u][v] = a[v][u] = 1;
    }
    long long cnt = 0;
    for (auto [u, v] : e) cnt += (a[u] & a[v]).count();   // số bạn chung của u và v
    printf("%lld\n", cnt / 3);             // mỗi tam giác được đếm ở cả ba cạnh
    return 0;
}
