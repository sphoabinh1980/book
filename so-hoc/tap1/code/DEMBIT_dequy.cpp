#include <bits/stdc++.h>
using namespace std;

typedef unsigned __int128 u128;

u128 f(long long n) {             // tổng số bit 1 của 0, 1, ..., n
    if (n <= 0) return 0;
    int k = 63 - __builtin_clzll(n);  // bit cao nhất: 2^k <= n < 2^(k+1)
    long long p = 1LL << k;
    // 0..p-1 có k · 2^(k-1) bit 1; p..n có (n - p + 1) bit cao nhất,
    // phần còn lại của p..n giống hệt 0..n-p
    return (u128)k * (p / 2) + (n - p + 1) + f(n - p);
}

void inso(u128 x) {
    if (x >= 10) inso(x / 10);
    putchar('0' + (int)(x % 10));
}

int main() {
    if (fopen("DEMBIT.INP", "r")) {
        freopen("DEMBIT.INP", "r", stdin);
        freopen("DEMBIT.OUT", "w", stdout);
    }
    long long n;
    cin >> n;
    inso(f(n));
    putchar('\n');
    return 0;
}
