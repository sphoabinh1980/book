struct DSU {
    vector<int> p, sz;
    DSU(int n) : p(n + 1), sz(n + 1, 1) { iota(p.begin(), p.end(), 0); }
    int root(int x) {                           // nén đường đi kiểu "nhảy hai bậc"
        while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
        return x;
    }
    bool unite(int a, int b) {                  // trả về false nếu a, b đã cùng nhóm
        a = root(a); b = root(b);
        if (a == b) return false;
        if (sz[a] < sz[b]) swap(a, b);          // treo cây nhỏ vào cây lớn
        p[b] = a; sz[a] += sz[b];
        return true;
    }
};
