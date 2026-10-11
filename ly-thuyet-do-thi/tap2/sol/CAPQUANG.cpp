#include <bits/stdc++.h>
using namespace std;
const int LG=17;
int main(){
    if(fopen("CAPQUANG.INP","r")){freopen("CAPQUANG.INP","r",stdin);freopen("CAPQUANG.OUT","w",stdout);}
    int n,q; scanf("%d %d",&n,&q);
    vector<vector<pair<int,int>>> g(n+1);
    for(int i=1;i<n;i++){int u,v,c;scanf("%d %d %d",&u,&v,&c);g[u].push_back({v,c});g[v].push_back({u,c});}
    vector<array<int,LG+1>> up(n+1),mn(n+1); vector<int> dep(n+1,-1);
    dep[1]=0; up[1].fill(1); mn[1].fill(INT_MAX); vector<int> st={1};
    while(!st.empty()){int u=st.back();st.pop_back();
        for(auto [v,c]:g[u]) if(dep[v]<0){dep[v]=dep[u]+1;up[v][0]=u;mn[v][0]=c;
            for(int j=1;j<=LG;j++){up[v][j]=up[up[v][j-1]][j-1];mn[v][j]=min(mn[v][j-1],mn[up[v][j-1]][j-1]);}
            st.push_back(v);}}
    while(q--){int u,v;scanf("%d %d",&u,&v); int r=INT_MAX; if(dep[u]<dep[v]) swap(u,v);
        for(int j=LG;j>=0;j--) if(dep[u]-(1<<j)>=dep[v]){r=min(r,mn[u][j]);u=up[u][j];}
        if(u!=v){for(int j=LG;j>=0;j--) if(up[u][j]!=up[v][j]){r=min({r,mn[u][j],mn[v][j]});u=up[u][j];v=up[v][j];}
            r=min({r,mn[u][0],mn[v][0]});}
        printf("%d\n",r);}
}
