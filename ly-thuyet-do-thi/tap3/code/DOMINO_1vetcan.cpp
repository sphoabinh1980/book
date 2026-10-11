#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> A, B, ord, sg;
vector<char> used;

bool go(int last, int k) {                      // đã đặt k quân, nửa phải của quân cuối là last
    if (k == n) return true;
    for (int i = 1; i <= n; i++) if (!used[i])
        for (int f = 0; f < 2; f++) {           // f = 0: đặt +, f = 1: xoay ngược
            int l = f ? B[i] : A[i], r = f ? A[i] : B[i];
            if (k > 0 && l != last) continue;
            used[i] = 1; ord[k] = i; sg[k] = f;
            if (go(r, k + 1)) return true;
            used[i] = 0;
        }
    return false;
}

int main() {
    if (fopen("DOMINO.INP", "r")) {
        freopen("DOMINO.INP", "r", stdin);
        freopen("DOMINO.OUT", "w", stdout);
    }
    scanf("%d", &n);
    A.resize(n + 1); B.resize(n + 1); ord.resize(n); sg.resize(n); used.assign(n + 1, 0);
    for (int i = 1; i <= n; i++) scanf("%d %d", &A[i], &B[i]);
    if (!go(-1, 0)) { puts("NO"); return 0; }
    for (int k = 0; k < n; k++) printf("%d %c\n", ord[k], sg[k] ? '-' : '+');
    return 0;
}
