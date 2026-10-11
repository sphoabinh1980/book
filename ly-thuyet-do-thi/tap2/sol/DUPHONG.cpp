#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("DUPHONG.INP","r")){freopen("DUPHONG.INP","r",stdin);freopen("DUPHONG.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    vector<vector<int>> g(n+1);
    for(int i=0;i<m;i++){int u,v;scanf("%d %d",&u,&v);g[u].push_back(v);g[v].push_back(u);}
    vector<int> comp(n+1,0); vector<long long> sz(1,0); int k=0;
    for(int s=1;s<=n;s++) if(!comp[s]){
        k++; sz.push_back(0); vector<int> st={s}; comp[s]=k;
        while(!st.empty()){int u=st.back();st.pop_back();sz[k]++;
            for(int v:g[u]) if(!comp[v]){comp[v]=k;st.push_back(v);}}
    }
    for(int v=1;v<=n;v++) printf("%lld%c",sz[comp[v]],v==n?'\n':' ');
    long long pairs=0; for(int i=1;i<=k;i++) pairs+=sz[i]*(sz[i]-1)/2;
    vector<long long> s(sz.begin()+1,sz.end()); sort(s.rbegin(),s.rend());
    long long best=pairs+(k>=2?s[0]*s[1]:0);
    printf("%lld\n%lld\n",pairs,best);
}
