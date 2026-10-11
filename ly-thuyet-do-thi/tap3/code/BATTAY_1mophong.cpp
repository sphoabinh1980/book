#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("BATTAY.INP", "r")) {
        freopen("BATTAY.INP", "r", stdin);
        freopen("BATTAY.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    priority_queue<long long> pq;          // số lần bắt tay còn thiếu của từng bạn
    long long cnt = 0;
    for (int i = 0; i < n; i++) {
        long long d;
        scanf("%lld", &d);
        if (d > 0) pq.push(d);
    }
    // Mỗi bước: hai bạn còn thiếu nhiều nhất bắt tay nhau một lần
    while (pq.size() >= 2) {
        long long a = pq.top(); pq.pop();
        long long b = pq.top(); pq.pop();
        cnt++;
        if (a > 1) pq.push(a - 1);
        if (b > 1) pq.push(b - 1);
    }
    if (!pq.empty()) printf("-1\n");       // còn đúng một bạn chưa đủ
    else printf("%lld\n", cnt);
    return 0;
}
