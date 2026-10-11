#include <bits/stdc++.h>
using namespace std;
const int LG=17;
vector<int> p;
int f(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
int main(){
    if(fopen("ITDOC.INP","r")){freopen("ITDOC.INP","r",stdin);freopen("ITDOC.OUT","w",stdout);}
    int n,m,q; scanf("%d %d %d",&n,&m,&q);
    vector<array<int,3>> e(m); for(auto&x:e) scanf("%d %d %d",&x[1],&x[2],&x[0]);
    sort(e.begin(),e.end()); p.resize(n+1); iota(p.begin(),p.end(),0);
    vector<vector<pair<int,int>>> g(n+1);
    for(auto&x:e){int u=f(x[1]),v=f(x[2]); if(u!=v){p[u]=v; g[x[1]].push_back({x[2],x[0]}); g[x[2]].push_back({x[1],x[0]});}}
    vector<array<int,LG+1>> up(n+1),mx(n+1); vector<int> dep(n+1,-1),root(n+1);
    for(int s=1;s<=n;s++) if(dep[s]<0){
        dep[s]=0; up[s].fill(s); mx[s].fill(0); root[s]=s; vector<int> st={s};
        while(!st.empty()){int u=st.back();st.pop_back();
            for(auto [v,w]:g[u]) if(dep[v]<0){dep[v]=dep[u]+1;root[v]=s;up[v][0]=u;mx[v][0]=w;
                for(int j=1;j<=LG;j++){up[v][j]=up[up[v][j-1]][j-1];mx[v][j]=max(mx[v][j-1],mx[up[v][j-1]][j-1]);}
                st.push_back(v);}}
    }
    while(q--){int u,v;scanf("%d %d",&u,&v);
        if(root[u]!=root[v]){printf("-1\n");continue;}
        int r=0; if(dep[u]<dep[v]) swap(u,v);
        for(int j=LG;j>=0;j--) if(dep[u]-(1<<j)>=dep[v]){r=max(r,mx[u][j]);u=up[u][j];}
        if(u!=v){for(int j=LG;j>=0;j--) if(up[u][j]!=up[v][j]){r=max({r,mx[u][j],mx[v][j]});u=up[u][j];v=up[v][j];}
            r=max({r,mx[u][0],mx[v][0]});}
        printf("%d\n",r);}
}
