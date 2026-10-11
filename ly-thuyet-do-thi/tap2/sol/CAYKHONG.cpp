#include <bits/stdc++.h>
using namespace std;
vector<int> p;
int f(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
int main(){
    if(fopen("CAYKHONG.INP","r")){freopen("CAYKHONG.INP","r",stdin);freopen("CAYKHONG.OUT","w",stdout);}
    int T; scanf("%d",&T);
    while(T--){
        int n,m; scanf("%d %d",&n,&m);
        p.assign(n+1,0); iota(p.begin(),p.end(),0);
        int k=n;
        for(int i=0;i<m;i++){int u,v;scanf("%d %d",&u,&v);u=f(u);v=f(v);if(u!=v){p[u]=v;k--;}}
        printf("%lld\n",(long long)m-n+2LL*k-1);
    }
}
