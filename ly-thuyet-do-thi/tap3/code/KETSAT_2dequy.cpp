#include <bits/stdc++.h>
using namespace std;

int b, k, N;
vector<int> ptr;
string out;

void euler(int u) {                             // Hierholzer đệ quy
    while (ptr[u] < b) {
        int d = ptr[u]++;
        euler((int)(((long long)u * b + d) % N));
        out.push_back('0' + d);
    }
}

int main() {
    if (fopen("KETSAT.INP", "r")) {
        freopen("KETSAT.INP", "r", stdin);
        freopen("KETSAT.OUT", "w", stdout);
    }
    scanf("%d %d", &b, &k);
    N = 1;
    for (int i = 0; i < k - 1; i++) N *= b;
    ptr.assign(N, 0);
    euler(0);
    reverse(out.begin(), out.end());
    string ans = string(k - 1, '0') + out;
    printf("%d\n%s\n", (int)ans.size(), ans.c_str());
    return 0;
}
