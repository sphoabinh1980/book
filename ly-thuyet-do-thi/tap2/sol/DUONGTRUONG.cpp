#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    if(fopen("DUONGTRUONG.INP","r")){freopen("DUONGTRUONG.INP","r",stdin);freopen("DUONGTRUONG.OUT","w",stdout);}
    int n,m,s; scanf("%d %d %d",&n,&m,&s);
    vector<vector<pair<int,int>>> g(n+1);
    for(int i=0;i<m;i++){int u,v,w;scanf("%d %d %d",&u,&v,&w);g[u].push_back({v,w});}
    vector<ll> d(n+1,LLONG_MAX); d[s]=0;
    priority_queue<pair<ll,int>,vector<pair<ll,int>>,greater<>> pq; pq.push({0,s});
    while(!pq.empty()){auto [du,u]=pq.top();pq.pop(); if(du!=d[u]) continue;
        for(auto [v,w]:g[u]) if(d[u]+w<d[v]){d[v]=d[u]+w;pq.push({d[v],v});}}
    for(int v=1;v<=n;v++) printf("%lld%c",d[v]==LLONG_MAX?-1:d[v],v==n?'\n':' ');
}
