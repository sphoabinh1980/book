#include <bits/stdc++.h>
using namespace std;

int b, k, total, P;                             // total = b^k mã; P = b^(k-1)
vector<char> seen;
string s;

bool go(int code, int cnt) {                    // code: k chữ số cuối; cnt: số mã đã gặp
    if (cnt == total) return true;
    for (int d = 0; d < b; d++) {               // thử bấm thêm chữ số d
        int nc = (code % P) * b + d;
        if (seen[nc]) continue;
        seen[nc] = 1; s.push_back('0' + d);
        if (go(nc, cnt + 1)) return true;
        seen[nc] = 0; s.pop_back();             // quay lui
    }
    return false;
}

int main() {
    if (fopen("KETSAT.INP", "r")) {
        freopen("KETSAT.INP", "r", stdin);
        freopen("KETSAT.OUT", "w", stdout);
    }
    scanf("%d %d", &b, &k);
    total = 1;
    for (int i = 0; i < k; i++) total *= b;
    P = total / b;
    seen.assign(total, 0);
    s = string(k, '0'); seen[0] = 1;            // bắt đầu bằng mã 00...0
    go(0, 1);
    printf("%d\n%s\n", (int)s.size(), s.c_str());
    return 0;
}
