#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("TAMGIAC.INP","r")){freopen("TAMGIAC.INP","r",stdin);freopen("TAMGIAC.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    vector<int> eu(m),ev(m),deg(n+1);
    for(int i=0;i<m;i++){scanf("%d %d",&eu[i],&ev[i]);deg[eu[i]]++;deg[ev[i]]++;}
    auto less_=[&](int a,int b){return deg[a]<deg[b]||(deg[a]==deg[b]&&a<b);};
    vector<vector<int>> g(n+1);
    for(int i=0;i<m;i++){int a=eu[i],b=ev[i]; if(less_(a,b)) g[a].push_back(b); else g[b].push_back(a);}
    vector<int> mark(n+1,0);
    long long cnt=0;
    for(int u=1;u<=n;u++){
        for(int v:g[u]) mark[v]=u;
        for(int v:g[u]) for(int w:g[v]) if(mark[w]==u) cnt++;
    }
    printf("%lld\n",cnt);
}
