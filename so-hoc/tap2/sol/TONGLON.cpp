#include <bits/stdc++.h>
using namespace std;
// So sánh giá trị tuyệt đối của hai xâu chữ số (không có số 0 thừa ở đầu)
int cmpAbs(const string& x, const string& y) {
    if (x.size() != y.size()) return x.size() < y.size() ? -1 : 1;
    return x < y ? -1 : (x > y ? 1 : 0);
}
string add(const string& x, const string& y) {               // |x| + |y|
    string r; int i = x.size() - 1, j = y.size() - 1, c = 0;
    while (i >= 0 || j >= 0 || c) {
        int t = c + (i >= 0 ? x[i--] - '0' : 0) + (j >= 0 ? y[j--] - '0' : 0);
        r += char('0' + t % 10); c = t / 10;                   // số nhớ chỉ là 0 hoặc 1
    }
    reverse(r.begin(), r.end()); return r;
}
string sub(const string& x, const string& y) {               // |x| - |y| với |x| >= |y|
    string r; int i = x.size() - 1, j = y.size() - 1, b = 0;
    while (i >= 0) {
        int t = x[i--] - '0' - b - (j >= 0 ? y[j--] - '0' : 0);
        b = t < 0; if (b) t += 10;                             // mượn 1 từ hàng kế tiếp
        r += char('0' + t);
    }
    while (r.size() > 1 && r.back() == '0') r.pop_back();     // xóa các số 0 thừa ở đầu
    reverse(r.begin(), r.end()); return r;
}
int main() {
    if (fopen("TONGLON.INP", "r")) {
        freopen("TONGLON.INP", "r", stdin); freopen("TONGLON.OUT", "w", stdout);
    }
    ios::sync_with_stdio(false);
    string a, b; cin >> a >> b;
    bool na = a[0] == '-', nb = b[0] == '-';
    if (na) a.erase(0, 1);
    if (nb) b.erase(0, 1);
    string r; bool neg;
    if (na == nb) { r = add(a, b); neg = na; }                 // cùng dấu: cộng trị tuyệt đối
    else {
        int c = cmpAbs(a, b);
        if (c >= 0) { r = sub(a, b); neg = na; } else { r = sub(b, a); neg = nb; }
    }
    if (r == "0") neg = false;                                 // không in "-0"
    cout << (neg ? "-" : "") << r << '\n';
}
