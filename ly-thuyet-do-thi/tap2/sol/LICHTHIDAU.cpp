#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    if(fopen("LICHTHIDAU.INP","r")){freopen("LICHTHIDAU.INP","r",stdin);freopen("LICHTHIDAU.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    // cạnh x -> y trọng số c nghĩa là d[y] >= d[x] + c (đường đi dài nhất)
    vector<array<ll,3>> e;
    for(int i=0;i<m;i++){int t,a,b; ll c; scanf("%d %d %d %lld",&t,&a,&b,&c);
        if(t==1) e.push_back({b,a,c}); else e.push_back({a,b,-c});}
    vector<ll> d(n+1,1);
    for(int it=0;it<=n;it++){
        bool ch=false;
        for(auto&x:e) if(d[x[0]]+x[2]>d[x[1]]){d[x[1]]=d[x[0]]+x[2];ch=true;}
        if(!ch){for(int v=1;v<=n;v++) printf("%lld%c",d[v],v==n?'\n':' ');return 0;}
    }
    printf("-1\n");
}
