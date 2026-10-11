#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n,m; vector<vector<pair<int,int>>> g;
vector<ll> dij(int s){
    vector<ll> d(n+1,LLONG_MAX); d[s]=0;
    priority_queue<pair<ll,int>,vector<pair<ll,int>>,greater<>> pq; pq.push({0,s});
    while(!pq.empty()){auto [du,u]=pq.top();pq.pop(); if(du!=d[u]) continue;
        for(auto [v,w]:g[u]) if(d[u]+w<d[v]){d[v]=d[u]+w;pq.push({d[v],v});}}
    return d;
}
int main(){
    if(fopen("NUTGIAO.INP","r")){freopen("NUTGIAO.INP","r",stdin);freopen("NUTGIAO.OUT","w",stdout);}
    scanf("%d %d",&n,&m); g.assign(n+1,{});
    vector<array<int,3>> e(m);
    for(auto&x:e){scanf("%d %d %d",&x[0],&x[1],&x[2]);g[x[0]].push_back({x[1],x[2]});g[x[1]].push_back({x[0],x[2]});}
    auto d1=dij(1),dn=dij(n); ll D=d1[n];
    auto on=[&](int v){return d1[v]!=LLONG_MAX&&dn[v]!=LLONG_MAX&&d1[v]+dn[v]==D;};
    vector<ll> val; for(int v=1;v<=n;v++) if(on(v)) val.push_back(d1[v]);
    sort(val.begin(),val.end());
    map<ll,int> cntv; for(ll x:val) cntv[x]++;
    val.erase(unique(val.begin(),val.end()),val.end());
    int K=val.size(); vector<int> cover(K+1,0);
    for(auto&x:e) for(int t=0;t<2;t++){
        int a=t?x[1]:x[0], b=t?x[0]:x[1];
        if(on(a)&&on(b)&&d1[a]+x[2]+dn[b]==D){
            int l=upper_bound(val.begin(),val.end(),d1[a])-val.begin();
            int r=lower_bound(val.begin(),val.end(),d1[b])-val.begin();
            if(l<r){cover[l]++;cover[r]--;}
        }
    }
    vector<int> ans; int c=0;
    vector<char> okv(K);
    for(int i=0;i<K;i++){c+=cover[i]; okv[i]=(c==0&&cntv[val[i]]==1);}
    for(int v=1;v<=n;v++) if(on(v)){int i=lower_bound(val.begin(),val.end(),d1[v])-val.begin(); if(okv[i]) ans.push_back(v);}
    printf("%d\n",(int)ans.size());
    for(size_t i=0;i<ans.size();i++) printf("%d%c",ans[i],i+1==ans.size()?'\n':' ');
}
