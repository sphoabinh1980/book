#include <bits/stdc++.h>
using namespace std;
vector<int> p,w; // w[x]: chênh lệch phe giữa x và cha
pair<int,int> f(int x){ // trả về (gốc, chẵn lẻ từ x tới gốc), không đệ quy
    int r=x,par=0; while(p[r]!=r){par^=w[r];r=p[r];}
    int cur=x,acc=par; while(p[cur]!=cur){int nx=p[cur],wc=w[cur];p[cur]=r;w[cur]=acc;acc^=wc;cur=nx;}
    return {r,par};
}
int main(){
    if(fopen("HAIPHE.INP","r")){freopen("HAIPHE.INP","r",stdin);freopen("HAIPHE.OUT","w",stdout);}
    int n,m; scanf("%d %d",&n,&m);
    p.resize(n+1); w.assign(n+1,0); iota(p.begin(),p.end(),0);
    for(int i=1;i<=m;i++){int a,b,t;scanf("%d %d %d",&a,&b,&t);
        auto [ra,pa]=f(a); auto [rb,pb]=f(b);
        if(ra==rb){ if((pa^pb)!=t){printf("%d\n",i);return 0;} }
        else {p[ra]=rb; w[ra]=pa^pb^t;}
    }
    printf("0\n");
}
