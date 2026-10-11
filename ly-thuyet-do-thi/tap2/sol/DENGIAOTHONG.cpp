#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("DENGIAOTHONG.INP","r")){freopen("DENGIAOTHONG.INP","r",stdin);freopen("DENGIAOTHONG.OUT","w",stdout);}
    int n,m,P; cin>>n>>m>>P;
    vector<string> s(n+1); for(int i=1;i<=n;i++) cin>>s[i];
    vector<vector<int>> g(n+1);
    for(int i=0;i<m;i++){int u,v;cin>>u>>v;g[u].push_back(v);g[v].push_back(u);}
    vector<int> d((size_t)(n+1)*P,-1);
    deque<pair<int,int>> q; d[1*P+0]=0; q.push_back({1,0});
    while(!q.empty()){
        auto [u,r]=q.front(); q.pop_front(); int t=d[u*P+r];
        if(u==n){printf("%d\n",t);return 0;}
        int r2=(r+1)%P;
        auto go=[&](int v){ if(d[v*P+r2]<0){d[v*P+r2]=t+1;q.push_back({v,r2});} };
        go(u);                              // đứng chờ 1 phút
        if(s[u][r]=='1') for(int v:g[u]) go(v); // đèn xanh: đi sang nút kề
    }
    printf("-1\n");
}
