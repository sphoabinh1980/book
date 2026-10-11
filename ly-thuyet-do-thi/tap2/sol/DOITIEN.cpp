#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("DOITIEN.INP","r")){freopen("DOITIEN.INP","r",stdin);freopen("DOITIEN.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    vector<int> U(m),V(m); vector<double> W(m);
    for(int i=0;i<m;i++){double r;scanf("%d %d %lf",&U[i],&V[i],&r);W[i]=-log(r);}
    vector<double> d(n+1,0);
    bool neg=false;
    for(int it=0;it<n;it++){
        bool ch=false;
        for(int i=0;i<m;i++) if(d[U[i]]+W[i]<d[V[i]]-1e-9){d[V[i]]=d[U[i]]+W[i];ch=true;}
        if(!ch) break;
        if(it==n-1) neg=true;
    }
    puts(neg?"YES":"NO");
}
