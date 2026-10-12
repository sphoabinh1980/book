#include <bits/stdc++.h>
using namespace std;

const long long B = 1000000000;   // cơ số 10^9: mỗi ô giữ 9 chữ số

int main() {
    if (fopen("GIAITHUA.INP", "r")) {
        freopen("GIAITHUA.INP", "r", stdin);
        freopen("GIAITHUA.OUT", "w", stdout);
    }
    int n;
    cin >> n;
    vector<long long> a(1, 1);    // a[0] là khối 9 chữ số thấp nhất
    for (int x = 2; x <= n; x++) {
        long long c = 0;          // số nhớ, luôn nhỏ hơn x
        for (size_t i = 0; i < a.size(); i++) {
            long long t = a[i] * x + c;   // < 10^9 · 2001: vừa long long
            a[i] = t % B;
            c = t / B;
        }
        if (c > 0) a.push_back(c);        // c < x < B: đúng một ô mới
    }
    printf("%lld", a.back());             // khối đầu: không in số 0 thừa
    for (int i = (int)a.size() - 2; i >= 0; i--)
        printf("%09lld", a[i]);           // các khối sau: đủ 9 chữ số
    printf("\n");
    return 0;
}
