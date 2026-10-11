#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("BANCHUNG.INP","r")){freopen("BANCHUNG.INP","r",stdin);freopen("BANCHUNG.OUT","w",stdout);}
    int n,m,q; scanf("%d %d %d",&n,&m,&q);
    vector<vector<int>> g(n+1);
    for(int i=0;i<m;i++){int u,v;scanf("%d %d",&u,&v);g[u].push_back(v);g[v].push_back(u);}
    for(int i=1;i<=n;i++) sort(g[i].begin(),g[i].end());
    map<pair<int,int>,int> memo;
    while(q--){
        int u,v; scanf("%d %d",&u,&v);
        if(g[u].size()>g[v].size()||(g[u].size()==g[v].size()&&u>v)) swap(u,v);
        auto key=make_pair(u,v);
        auto it=memo.find(key);
        if(it==memo.end()){
            int c=0;
            for(int x:g[u]) if(binary_search(g[v].begin(),g[v].end(),x)) c++;
            it=memo.insert({key,c}).first;
        }
        printf("%d\n",it->second);
    }
}
