#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("KETSAT.INP", "r")) {
        freopen("KETSAT.INP", "r", stdin);
        freopen("KETSAT.OUT", "w", stdout);
    }
    int b, k;
    scanf("%d %d", &b, &k);
    // đồ thị de Bruijn: đỉnh = xâu k-1 chữ số (viết như số hệ b), N = b^(k-1) đỉnh;
    // từ đỉnh u, bấm chữ số d đi tới đỉnh (u*b + d) mod N. Mỗi cạnh là một mã k chữ số.
    int N = 1;
    for (int i = 0; i < k - 1; i++) N *= b;
    vector<int> ptr(N, 0);                      // chữ số tiếp theo chưa dùng ở mỗi đỉnh
    vector<pair<int,int>> st = {{0, -1}};       // (đỉnh, chữ số vừa bấm để tới)
    string out;
    while (!st.empty()) {                       // Hierholzer không đệ quy
        auto [u, c] = st.back();
        if (ptr[u] < b) {
            int d = ptr[u]++;
            st.push_back({(int)(((long long)u * b + d) % N), d});
        } else {
            st.pop_back();
            if (c >= 0) out.push_back('0' + c);
        }
    }
    reverse(out.begin(), out.end());
    string ans = string(k - 1, '0') + out;      // bắt đầu ở đỉnh 00...0
    printf("%d\n%s\n", (int)ans.size(), ans.c_str());
    return 0;
}
