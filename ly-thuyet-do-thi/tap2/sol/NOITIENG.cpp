#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("NOITIENG.INP","r")){freopen("NOITIENG.INP","r",stdin);freopen("NOITIENG.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    vector<pair<int,int>> e(m);
    for(auto&p:e) scanf("%d %d",&p.first,&p.second);
    sort(e.begin(),e.end()); e.erase(unique(e.begin(),e.end()),e.end());
    vector<int> in(n+1),out(n+1);
    for(auto&p:e){out[p.first]++;in[p.second]++;}
    int ans=-1;
    for(int v=1;v<=n;v++) if(in[v]==n-1&&out[v]==0) ans=v;
    printf("%d\n",ans);
}
