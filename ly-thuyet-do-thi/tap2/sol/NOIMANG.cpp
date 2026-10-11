#include <bits/stdc++.h>
using namespace std;
vector<int> p;
int f(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
int main(){
    if(fopen("NOIMANG.INP","r")){freopen("NOIMANG.INP","r",stdin);freopen("NOIMANG.OUT","w",stdout);}
    int n,k,m; scanf("%d %d %d",&n,&k,&m);
    p.resize(n+1); iota(p.begin(),p.end(),0); int cnt=n;
    for(int i=0;i<k;i++){int u,v;scanf("%d %d",&u,&v);u=f(u);v=f(v);if(u!=v){p[u]=v;cnt--;}}
    vector<array<int,3>> e(m); for(auto&x:e) scanf("%d %d %d",&x[1],&x[2],&x[0]);
    sort(e.begin(),e.end()); long long tot=0;
    for(auto&x:e){int u=f(x[1]),v=f(x[2]); if(u!=v){p[u]=v;cnt--;tot+=x[0];}}
    printf("%lld\n",cnt==1?tot:-1LL);
}
