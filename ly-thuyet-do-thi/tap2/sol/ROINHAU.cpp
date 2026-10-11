#include <bits/stdc++.h>
using namespace std;
#include "flow.h"
int main(){
    if(fopen("ROINHAU.INP","r")){freopen("ROINHAU.INP","r",stdin);freopen("ROINHAU.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m); Dinic D(n); vector<int> U(m+1),V(m+1),id(m+1);
    for(int i=1;i<=m;i++){scanf("%d %d",&U[i],&V[i]);id[i]=D.add(U[i],V[i],1);}
    int k=D.maxflow(1,n);
    vector<vector<int>> out(n+1); // các cung có luồng
    for(int i=1;i<=m;i++) if(D.e[id[i]].cap==0) out[U[i]].push_back(i);
    vector<int> ptr(n+1,0);
    printf("%d\n",k);
    for(int r=0;r<k;r++){
        vector<int> path={1}; vector<int> pos(n+1,-1); pos[1]=0; int u=1;
        while(u!=n){int e=out[u][ptr[u]++]; int v=V[e];
            if(pos[v]>=0){ while((int)path.size()>pos[v]+1){pos[path.back()]=-1;path.pop_back();} }
            else {pos[v]=path.size(); path.push_back(v);}
            u=v;}
        printf("%d",(int)path.size()); for(int x:path) printf(" %d",x); printf("\n");
    }
}
