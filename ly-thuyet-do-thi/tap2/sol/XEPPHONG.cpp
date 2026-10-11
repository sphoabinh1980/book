#include <bits/stdc++.h>
using namespace std;
int n,m; vector<vector<int>> g; vector<int> mt,vis; int stamp=0;
bool kuhn(int u){ for(int v:g[u]) if(vis[v]!=stamp){vis[v]=stamp; if(!mt[v]||kuhn(mt[v])){mt[v]=u;return true;}} return false;}
int main(){
    if(fopen("XEPPHONG.INP","r")){freopen("XEPPHONG.INP","r",stdin);freopen("XEPPHONG.OUT","w",stdout);}
    scanf("%d %d",&n,&m); g.resize(n+1); mt.assign(m+1,0); vis.assign(m+1,0);
    for(int i=1;i<=n;i++){int k;scanf("%d",&k);g[i].resize(k);for(int&x:g[i])scanf("%d",&x);}
    int ans=0; for(int i=1;i<=n;i++){stamp++; if(kuhn(i)) ans++;}
    printf("%d\n",ans);
}
