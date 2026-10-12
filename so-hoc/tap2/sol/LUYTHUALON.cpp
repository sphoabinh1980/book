#include <bits/stdc++.h>
using namespace std;
const long long B = 1000000000;                                 // mỗi ô giữ 9 chữ số
int main() {
    if (fopen("LUYTHUALON.INP", "r")) {
        freopen("LUYTHUALON.INP", "r", stdin); freopen("LUYTHUALON.OUT", "w", stdout);
    }
    long long a; int b; scanf("%lld %d", &a, &b);
    vector<long long> d = {1};                                  // d[0] là ô thấp nhất; a^0 = 1
    for (int it = 0; it < b; it++) {
        long long c = 0;
        for (size_t i = 0; i < d.size(); i++) {
            long long t = d[i] * a + c;                         // t < 10^18 + 10^9: vừa long long
            d[i] = t % B; c = t / B;
        }
        if (c) d.push_back(c);                                  // c < a <= B: thêm nhiều nhất một ô
        while (d.size() > 1 && d.back() == 0) d.pop_back();     // a = 0: kết quả là 0
    }
    printf("%lld", d.back());
    for (int i = (int)d.size() - 2; i >= 0; i--) printf("%09lld", d[i]);   // đủ 9 chữ số
    printf("\n");
}
