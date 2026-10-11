#include <bits/stdc++.h>
using namespace std;
vector<int> p,sz;
int f(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
int main(){
    if(fopen("MANGBANBE.INP","r")){freopen("MANGBANBE.INP","r",stdin);freopen("MANGBANBE.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    p.resize(n+1); sz.assign(n+1,1); iota(p.begin(),p.end(),0);
    int cnt=n,best=1;
    while(m--){int u,v;scanf("%d %d",&u,&v);u=f(u);v=f(v);
        if(u!=v){if(sz[u]<sz[v])swap(u,v);p[v]=u;sz[u]+=sz[v];cnt--;best=max(best,sz[u]);}
        printf("%d %d\n",cnt,best);}
}
