#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("BIENAP.INP","r")){freopen("BIENAP.INP","r",stdin);freopen("BIENAP.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    vector<vector<pair<int,int>>> g(n+1);
    for(int i=1;i<=m;i++){int u,v;scanf("%d %d",&u,&v);g[u].push_back({v,i});g[v].push_back({u,i});}
    vector<int> num(n+1,0),low(n+1,0),pe(n+1,0),it(n+1,0),cnt(n+1,0); int timer=0;
    vector<int> st={1}; num[1]=low[1]=++timer;
    while(!st.empty()){int u=st.back();
        if(it[u]<(int)g[u].size()){auto [v,id]=g[u][it[u]++]; if(id==pe[u]) continue;
            if(num[v]) low[u]=min(low[u],num[v]); else {num[v]=low[v]=++timer;pe[v]=id;st.push_back(v);} }
        else {st.pop_back(); if(!st.empty()){int p=st.back(); low[p]=min(low[p],low[u]); if(low[u]>=num[p]) cnt[p]++;}}
    }
    vector<pair<int,int>> ans;
    for(int v=1;v<=n;v++){int parts= v==1? cnt[v] : cnt[v]+1; if(parts>=2) ans.push_back({v,parts});}
    printf("%d\n",(int)ans.size());
    for(auto [v,c]:ans) printf("%d %d\n",v,c);
}
