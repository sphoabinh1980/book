#include <bits/stdc++.h>
using namespace std;
const int N=2001;
bitset<N> r[N];
int main(){
    if(fopen("XEPHANG.INP","r")){freopen("XEPHANG.INP","r",stdin);freopen("XEPHANG.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    for(int i=0;i<m;i++){int a,b;scanf("%d %d",&a,&b);r[a][b]=1;}
    for(int k=1;k<=n;k++) for(int i=1;i<=n;i++) if(r[i][k]) r[i]|=r[k];
    vector<int> ans;
    for(int v=1;v<=n;v++){int c=r[v].count(); for(int u=1;u<=n;u++) if(r[u][v]) c++; if(c==n-1) ans.push_back(v);}
    printf("%d\n",(int)ans.size());
    for(size_t i=0;i<ans.size();i++) printf("%d%c",ans[i],i+1==ans.size()?'\n':' ');
}
