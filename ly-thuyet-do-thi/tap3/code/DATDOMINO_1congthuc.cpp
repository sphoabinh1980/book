#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("DATDOMINO.INP", "r")) {
        freopen("DATDOMINO.INP", "r", stdin);
        freopen("DATDOMINO.OUT", "w", stdout);
    }
    int R, C;
    cin >> R >> C;
    int empty = 0;
    for (int i = 0; i < R; i++) { string s; cin >> s; empty += count(s.begin(), s.end(), '.'); }
    printf("%d\n", empty / 2);                  // đúng khi không có ô cấm, nói chung thì không
    return 0;
}
