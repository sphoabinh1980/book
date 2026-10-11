#include <bits/stdc++.h>
using namespace std;
// Trả lời offline bằng DFS không đệ quy: khi đứng ở v, ngăn xếp đường đi chứa đúng các tổ tiên của v.
int main(){
    if(fopen("CAPK.INP","r")){freopen("CAPK.INP","r",stdin);freopen("CAPK.OUT","w",stdout);}
    int n,q; scanf("%d %d",&n,&q);
    vector<int> head(n+1,-1),nxt(n+1);
    for(int i=2;i<=n;i++){int p;scanf("%d",&p);nxt[i]=head[p];head[p]=i;}
    vector<int> qk(q),qh(n+1,-1),qn(q),ans(q);
    for(int i=0;i<q;i++){int v;scanf("%d %d",&v,&qk[i]);qn[i]=qh[v];qh[v]=i;}
    vector<int> path; path.reserve(n); vector<int> it(n+1);
    path.push_back(1); for(int i=1;i<=n;i++) it[i]=head[i];
    for(int j=qh[1];j>=0;j=qn[j]) ans[j]= qk[j]<(int)path.size()? path[path.size()-1-qk[j]] : -1;
    while(!path.empty()){
        int u=path.back();
        if(it[u]<0){path.pop_back();continue;}
        int v=it[u]; it[u]=nxt[v]; path.push_back(v);
        for(int j=qh[v];j>=0;j=qn[j]) ans[j]= qk[j]<(int)path.size()? path[path.size()-1-qk[j]] : -1;
    }
    for(int i=0;i<q;i++) printf("%d\n",ans[i]);
}
