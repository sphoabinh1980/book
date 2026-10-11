#include <bits/stdc++.h>
using namespace std;
#include "scc.h"
int main(){
    if(fopen("TINDON.INP","r")){freopen("TINDON.INP","r",stdin);freopen("TINDON.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    vector<vector<int>> g(n+1); vector<pair<int,int>> e(m);
    for(auto&x:e){scanf("%d %d",&x.first,&x.second);g[x.first].push_back(x.second);}
    vector<int> comp; int c=tarjan(n,g,comp);
    vector<int> in(c,0); for(auto&x:e) if(comp[x.first]!=comp[x.second]) in[comp[x.second]]++;
    printf("%d\n",(int)count(in.begin(),in.end(),0));
}
