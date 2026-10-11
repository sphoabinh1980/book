#include <bits/stdc++.h>
using namespace std;
#include "flow.h"
int main(){
    if(fopen("DUONGONG.INP","r")){freopen("DUONGONG.INP","r",stdin);freopen("DUONGONG.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m); Dinic D(n); vector<int> U(m+1),V(m+1);
    for(int i=1;i<=m;i++){long long c;scanf("%d %d %lld",&U[i],&V[i],&c);D.add(U[i],V[i],c);}
    long long F=D.maxflow(1,n);
    vector<char> S(n+1,0); S[1]=1; vector<int> st={1};
    while(!st.empty()){int u=st.back();st.pop_back(); for(int id:D.g[u]) if(D.e[id].cap>0&&!S[D.e[id].to]){S[D.e[id].to]=1;st.push_back(D.e[id].to);}}
    vector<int> cut; for(int i=1;i<=m;i++) if(S[U[i]]&&!S[V[i]]) cut.push_back(i);
    printf("%lld\n%d\n",F,(int)cut.size());
    for(size_t i=0;i<cut.size();i++) printf("%d%c",cut[i],i+1==cut.size()?'\n':' ');
}
