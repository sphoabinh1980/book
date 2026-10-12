#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("SODU.INP", "r")) {
        freopen("SODU.INP", "r", stdin);
        freopen("SODU.OUT", "w", stdout);
    }
    string s;
    long long m;
    cin >> s >> m;
    unsigned long long N = 0;    // dựng lại cả số N rồi mới chia
    for (char c : s) N = N * 10 + (c - '0');  // tràn khi N > 19 chữ số!
    cout << N % m << "\n";
    return 0;
}
