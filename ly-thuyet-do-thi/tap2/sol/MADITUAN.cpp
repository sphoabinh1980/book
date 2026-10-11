#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("MADITUAN.INP","r")){freopen("MADITUAN.INP","r",stdin);freopen("MADITUAN.OUT","w",stdout);}
    int N,sx,sy,Q; scanf("%d %d %d %d",&N,&sx,&sy,&Q);
    vector<int> d((size_t)N*N,-1);
    const int dx[8]={1,2,2,1,-1,-2,-2,-1},dy[8]={2,1,-1,-2,-2,-1,1,2};
    vector<int> q; q.reserve((size_t)N*N);
    auto id=[&](int x,int y){return (x-1)*N+(y-1);};
    d[id(sx,sy)]=0; q.push_back(id(sx,sy));
    for(size_t h=0;h<q.size();h++){
        int x=q[h]/N+1,y=q[h]%N+1;
        for(int k=0;k<8;k++){int u=x+dx[k],v=y+dy[k];
            if(u>=1&&u<=N&&v>=1&&v<=N&&d[id(u,v)]<0){d[id(u,v)]=d[q[h]]+1;q.push_back(id(u,v));}}
    }
    while(Q--){int x,y;scanf("%d %d",&x,&y);printf("%d\n",d[id(x,y)]);}
}
