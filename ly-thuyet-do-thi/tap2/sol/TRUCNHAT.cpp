#include <bits/stdc++.h>
using namespace std;
#include "flow.h"
int main(){
    if(fopen("TRUCNHAT.INP","r")){freopen("TRUCNHAT.INP","r",stdin);freopen("TRUCNHAT.OUT","w",stdout);}
    int n,d; scanf("%d %d",&n,&d);
    int s=n+d+1,t=n+d+2; Dinic D(t);
    vector<int> a(n+1),b(d+1); long long need=0;
    for(int i=1;i<=n;i++){scanf("%d",&a[i]);D.add(s,i,a[i]);}
    for(int j=1;j<=d;j++){scanf("%d",&b[j]);D.add(n+j,t,b[j]);need+=b[j];}
    vector<array<int,3>> e;
    for(int i=1;i<=n;i++){int k;scanf("%d",&k);while(k--){int j;scanf("%d",&j);e.push_back({i,j,D.add(i,n+j,1)});}}
    if(D.maxflow(s,t)!=need){printf("NO\n");return 0;}
    vector<vector<int>> day(d+1);
    for(auto&x:e) if(D.e[x[2]].cap==0) day[x[1]].push_back(x[0]);
    printf("YES\n");
    for(int j=1;j<=d;j++){sort(day[j].begin(),day[j].end()); for(size_t i=0;i<day[j].size();i++) printf("%d%c",day[j][i],i+1==day[j].size()?'\n':' '); if(day[j].empty()) printf("\n");}
}
