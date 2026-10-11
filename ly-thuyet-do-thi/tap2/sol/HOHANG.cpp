#include <bits/stdc++.h>
using namespace std;
const int LG=18;
int main(){
    if(fopen("HOHANG.INP","r")){freopen("HOHANG.INP","r",stdin);freopen("HOHANG.OUT","w",stdout);}
    int n; scanf("%d",&n);
    vector<int> par(n+1); vector<vector<int>> ch(n+1); int root=0;
    for(int i=1;i<=n;i++){scanf("%d",&par[i]); if(par[i]) ch[par[i]].push_back(i); else root=i;}
    vector<array<int,LG+1>> up(n+1); vector<int> dep(n+1,0);
    vector<int> st={root}; up[root].fill(root);
    while(!st.empty()){int u=st.back();st.pop_back();
        for(int v:ch[u]){dep[v]=dep[u]+1;up[v][0]=u;for(int j=1;j<=LG;j++)up[v][j]=up[up[v][j-1]][j-1];st.push_back(v);}}
    int q; scanf("%d",&q);
    while(q--){int u,v;scanf("%d %d",&u,&v); int diff=abs(dep[u]-dep[v]);
        if(dep[u]<dep[v]) swap(u,v);
        for(int j=LG;j>=0;j--) if(dep[u]-(1<<j)>=dep[v]) u=up[u][j];
        if(u!=v){for(int j=LG;j>=0;j--) if(up[u][j]!=up[v][j]){u=up[u][j];v=up[v][j];} u=up[u][0];}
        printf("%d %d\n",u,diff);}
}
