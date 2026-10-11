#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("CHUYENDOI.INP","r")){freopen("CHUYENDOI.INP","r",stdin);freopen("CHUYENDOI.OUT","w",stdout);}
    int n; scanf("%d",&n);
    vector<vector<int>> g(n+1);
    vector<pair<int,int>> e;
    for(int i=1;i<=n;i++) for(int j=1;j<=n;j++){int x;scanf("%d",&x); if(x){g[i].push_back(j); if(i<j) e.push_back({i,j});}}
    printf("%d\n",(int)e.size());
    for(auto&p:e) printf("%d %d\n",p.first,p.second);
    for(int i=1;i<=n;i++){printf("%d",(int)g[i].size()); for(int v:g[i]) printf(" %d",v); printf("\n");}
}
