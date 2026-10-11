#include <bits/stdc++.h>
using namespace std;
const int MOD=1e9+7;
int main(){
    if(fopen("DEMLOTRINH.INP","r")){freopen("DEMLOTRINH.INP","r",stdin);freopen("DEMLOTRINH.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    vector<vector<int>> g(n+1),rg(n+1);
    for(int i=0;i<m;i++){int u,v;scanf("%d %d",&u,&v);g[u].push_back(v);rg[v].push_back(u);}
    auto reach=[&](int s,vector<vector<int>>&G){vector<char> vis(n+1,0);vector<int> st={s};vis[s]=1;
        while(!st.empty()){int u=st.back();st.pop_back();for(int v:G[u]) if(!vis[v]){vis[v]=1;st.push_back(v);}} return vis;};
    auto A=reach(1,g),B=reach(n,rg);
    if(!A[n]){printf("0\n");return 0;}
    vector<int> in(n+1,0); int tot=0;
    for(int u=1;u<=n;u++) if(A[u]&&B[u]){tot++; for(int v:g[u]) if(A[v]&&B[v]) in[v]++;}
    vector<long long> f(n+1,0); f[1]=1; queue<int> q; q.push(1); int done=0;
    if(in[1]){printf("-1\n");return 0;}
    while(!q.empty()){int u=q.front();q.pop();done++;
        for(int v:g[u]) if(A[v]&&B[v]){f[v]=(f[v]+f[u])%MOD; if(--in[v]==0) q.push(v);}}
    if(done<tot) printf("-1\n"); else printf("%lld\n",f[n]);
}
