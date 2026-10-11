#include <bits/stdc++.h>
using namespace std;
vector<int> p; int f(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
int main(){
    if(fopen("NETVE.INP","r")){freopen("NETVE.INP","r",stdin);freopen("NETVE.OUT","w",stdout);}
    int T; scanf("%d",&T);
    while(T--){int n,m; scanf("%d %d",&n,&m);
        p.resize(n+1); iota(p.begin(),p.end(),0); vector<int> deg(n+1,0);
        for(int i=0;i<m;i++){int u,v;scanf("%d %d",&u,&v);deg[u]++;deg[v]++;p[f(u)]=f(v);}
        int odd=0,root=-1; bool ok=true;
        for(int v=1;v<=n;v++) if(deg[v]){ odd+=deg[v]%2; if(root<0) root=f(v); else if(f(v)!=root) ok=false; }
        puts(ok&&(odd==0||odd==2)?"YES":"NO");
    }
}
