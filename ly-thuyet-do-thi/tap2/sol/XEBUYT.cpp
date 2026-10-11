#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
struct E{int v; ll w,a,p,b;};
int main(){
    if(fopen("XEBUYT.INP","r")){freopen("XEBUYT.INP","r",stdin);freopen("XEBUYT.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    vector<vector<E>> g(n+1);
    for(int i=0;i<m;i++){int u,v; ll w,a,p,b; scanf("%d %d %lld %lld %lld %lld",&u,&v,&w,&a,&p,&b); g[u].push_back({v,w,a,p,b});}
    vector<ll> d(n+1,LLONG_MAX); d[1]=0;
    priority_queue<pair<ll,int>,vector<pair<ll,int>>,greater<>> pq; pq.push({0,1});
    while(!pq.empty()){auto [t,u]=pq.top();pq.pop(); if(t!=d[u]) continue;
        for(auto&e:g[u]){
            ll dep = t<=e.a ? e.a : e.a+(t-e.a+e.p-1)/e.p*e.p;
            if(dep>e.b) continue;
            if(dep+e.w<d[e.v]){d[e.v]=dep+e.w;pq.push({d[e.v],e.v});}
        }}
    printf("%lld\n",d[n]==LLONG_MAX?-1:d[n]);
}
