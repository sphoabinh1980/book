#include <bits/stdc++.h>
using namespace std;
const int N = 10000000, MOD = 1000000007;
int spf[N + 1], cnt[N + 1];                        // cnt[p] = số phần tử đạt số mũ lớn nhất của p
unsigned char mx[N + 1];                           // mx[p] = số mũ lớn nhất của p trong dãy
int main() {
    if (fopen("BCNNDAY.INP", "r")) {
        freopen("BCNNDAY.INP", "r", stdin); freopen("BCNNDAY.OUT", "w", stdout);
    }
    int n; scanf("%d", &n);
    vector<int> a(n);
    int M = 1;
    for (int &x : a) { scanf("%d", &x); M = max(M, x); }
    for (long long i = 2; i <= M; i++)             // sàng ước nguyên tố nhỏ nhất tới max a_i
        if (!spf[i]) {
            spf[i] = i;
            if (i * i <= M) for (long long j = i * i; j <= M; j += i) if (!spf[j]) spf[j] = i;
        }
    auto phantich = [&](int x, vector<pair<int, int>> &f) {
        f.clear();
        while (x > 1) {
            int p = spf[x], e = 0;
            while (x % p == 0) x /= p, e++;
            f.push_back({p, e});
        }
    };
    vector<pair<int, int>> f;
    for (int x : a) {
        phantich(x, f);
        for (auto &pe : f) {
            int p = pe.first, e = pe.second;
            if (e > mx[p]) mx[p] = e, cnt[p] = 1;
            else if (e == mx[p]) cnt[p]++;
        }
    }
    long long L = 1;
    for (int p = 2; p <= M; p++)
        for (int k = 0; k < mx[p]; k++) L = L * p % MOD;
    int can = 0;              // a_i cần thiết: là phần tử DUY NHẤT đạt mx[p] với một p nào đó
    for (int x : a) {
        phantich(x, f);
        bool ok = false;
        for (auto &pe : f) if (pe.second == mx[pe.first] && cnt[pe.first] == 1) ok = true;
        can += ok;
    }
    printf("%lld\n%d\n", L, can);
}
