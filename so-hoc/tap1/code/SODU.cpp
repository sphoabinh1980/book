#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("SODU.INP", "r")) {
        freopen("SODU.INP", "r", stdin);
        freopen("SODU.OUT", "w", stdout);
    }
    string s;               // N dài tới 10^6 chữ số: đọc vào xâu
    long long m;
    cin >> s >> m;
    long long r = 0;        // r = (phần đầu đã đọc của N) mod m
    for (char c : s)
        r = (r * 10 + (c - '0')) % m;   // thêm một chữ số bên phải
    cout << r << "\n";
    return 0;
}
