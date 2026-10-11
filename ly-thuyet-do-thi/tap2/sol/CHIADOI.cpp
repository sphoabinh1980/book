#include <bits/stdc++.h>
using namespace std;
const int MX=100001;
int main(){
    if(fopen("CHIADOI.INP","r")){freopen("CHIADOI.INP","r",stdin);freopen("CHIADOI.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    vector<vector<int>> g(n+1);
    for(int i=0;i<m;i++){int u,v;scanf("%d %d",&u,&v);g[u].push_back(v);g[v].push_back(u);}
    vector<int> col(n+1,-1); vector<int> diffs;
    for(int s=1;s<=n;s++) if(col[s]<0){
        int c[2]={0,0}; col[s]=0; vector<int> q={s};
        for(size_t h=0;h<q.size();h++){int u=q[h];c[col[u]]++;
            for(int v:g[u]){ if(col[v]<0){col[v]=col[u]^1;q.push_back(v);} else if(col[v]==col[u]){printf("-1\n");return 0;} }}
        diffs.push_back(abs(c[0]-c[1]));
    }
    // chọn dấu cho mỗi hiệu để tổng có trị tuyệt đối nhỏ nhất: subset sum
    int S=0; for(int d:diffs) S+=d;
    map<int,int> cnt; for(int d:diffs) if(d) cnt[d]++;
    vector<int> items;
    for(auto [d,c]:cnt){int k=1; while(c>0){int t=min(k,c); items.push_back(d*t); c-=t; k*=2;}}
    bitset<MX> b; b[0]=1;
    for(int x:items) b|=b<<x;
    int best=S;
    for(int x=0;x<=S;x++) if(b[x]) best=min(best,abs(S-2*x));
    printf("%d\n",best);
}
