#include <bits/stdc++.h>
using namespace std;
#include "scc.h"
int main(){
    if(fopen("TUYENCHON.INP","r")){freopen("TUYENCHON.INP","r",stdin);freopen("TUYENCHON.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    // đỉnh 2i-1: "nhận i", đỉnh 2i: "loại i"
    auto node=[&](int x){return x>0? 2*x-1 : 2*(-x);};
    auto neg=[&](int v){return v%2? v+1 : v-1;};
    vector<vector<int>> g(2*n+1);
    for(int i=0;i<m;i++){int x,y;scanf("%d %d",&x,&y);int a=node(x),b=node(y);g[neg(a)].push_back(b);g[neg(b)].push_back(a);}
    vector<int> comp; tarjan(2*n,g,comp);
    string s(n,'0');
    for(int i=1;i<=n;i++){ if(comp[2*i-1]==comp[2*i]){printf("NO\n");return 0;}
        s[i-1]= comp[2*i-1]<comp[2*i] ? '1':'0'; }
    printf("YES\n%s\n",s.c_str());
}
