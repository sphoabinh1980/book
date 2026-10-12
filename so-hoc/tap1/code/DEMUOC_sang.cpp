#include <bits/stdc++.h>
using namespace std;

// Số ước và tổng ước của MỌI số 1..N bằng "sàng điều hòa"
int main() {
    int N;
    cin >> N;
    vector<int> cnt(N + 1, 0);
    vector<long long> sum(N + 1, 0);
    for (int d = 1; d <= N; d++)        // d là ước của d, 2d, 3d, ...
        for (int k = d; k <= N; k += d)
            cnt[k]++, sum[k] += d;
    for (int k = 1; k <= N; k++)
        cout << k << ": " << cnt[k] << " " << sum[k] << "\n";
    return 0;
}
