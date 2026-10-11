#include <bits/stdc++.h>
using namespace std;
#include "scc.h"
int main(){
    if(fopen("KHOBAU.INP","r")){freopen("KHOBAU.INP","r",stdin);freopen("KHOBAU.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    vector<long long> a(n+1); for(int i=1;i<=n;i++) scanf("%lld",&a[i]);
    vector<vector<int>> g(n+1); vector<pair<int,int>> e(m);
    for(auto&x:e){scanf("%d %d",&x.first,&x.second);g[x.first].push_back(x.second);}
    vector<int> comp; int c=tarjan(n,g,comp);
    vector<long long> w(c,0); for(int v=1;v<=n;v++) w[comp[v]]+=a[v];
    vector<vector<int>> h(c); for(auto&x:e) if(comp[x.first]!=comp[x.second]) h[comp[x.first]].push_back(comp[x.second]);
    // Tarjan đánh số thành phần theo thứ tự tô pô ngược: cung đi từ số lớn sang số nhỏ
    vector<long long> best(c,LLONG_MIN); int s=comp[1]; best[s]=w[s]; long long ans=0;
    for(int x=s;x>=0;x--) if(best[x]!=LLONG_MIN){ans=max(ans,best[x]); for(int y:h[x]) best[y]=max(best[y],best[x]+w[y]);}
    printf("%lld\n",ans);
}
