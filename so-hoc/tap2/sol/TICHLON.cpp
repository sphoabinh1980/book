#include <bits/stdc++.h>
using namespace std;
const int B = 10000;                                            // cơ số 10^4
vector<long long> parse(const string& s) {                      // xâu chữ số -> mảng ô đảo ngược
    vector<long long> v;
    for (int e = s.size(); e > 0; e -= 4) {
        int st = max(0, e - 4); v.push_back(stoi(s.substr(st, e - st)));
    }
    return v;
}
int main() {
    if (fopen("TICHLON.INP", "r")) {
        freopen("TICHLON.INP", "r", stdin); freopen("TICHLON.OUT", "w", stdout);
    }
    ios::sync_with_stdio(false);
    string a, b; cin >> a >> b;
    bool neg = false;
    if (a[0] == '-') { neg = !neg; a.erase(0, 1); }
    if (b[0] == '-') { neg = !neg; b.erase(0, 1); }
    vector<long long> x = parse(a), y = parse(b), c(x.size() + y.size() + 1, 0);
    for (size_t i = 0; i < x.size(); i++) {
        long long xi = x[i];
        if (!xi) continue;
        long long* ci = c.data() + i;
        for (size_t j = 0; j < y.size(); j++) ci[j] += xi * y[j];   // cộng dồn, dồn nhớ sau
    }
    for (size_t k = 0; k + 1 < c.size(); k++) { c[k + 1] += c[k] / B; c[k] %= B; }  // dồn nhớ
    while (c.size() > 1 && c.back() == 0) c.pop_back();
    if (c.size() == 1 && c[0] == 0) neg = false;                // tích bằng 0: không in "-0"
    string out = neg ? "-" : "";
    out += to_string(c.back());
    char buf[8];
    for (int k = (int)c.size() - 2; k >= 0; k--) { sprintf(buf, "%04lld", c[k]); out += buf; }
    cout << out << '\n';
}
