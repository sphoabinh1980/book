#include <bits/stdc++.h>
using namespace std;
vector<int> p;
int f(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
int main(){
    if(fopen("GIENGONG.INP","r")){freopen("GIENGONG.INP","r",stdin);freopen("GIENGONG.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    vector<array<int,3>> e;
    for(int i=1;i<=n;i++){int a;scanf("%d",&a);e.push_back({a,0,i});}
    for(int i=0;i<m;i++){int u,v,c;scanf("%d %d %d",&u,&v,&c);e.push_back({c,u,v});}
    sort(e.begin(),e.end()); p.resize(n+1); iota(p.begin(),p.end(),0);
    long long tot=0;
    for(auto&x:e){int u=f(x[1]),v=f(x[2]); if(u!=v){p[u]=v;tot+=x[0];}}
    printf("%lld\n",tot);
}
