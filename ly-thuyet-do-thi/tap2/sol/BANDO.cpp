#include <bits/stdc++.h>
using namespace std;
int R,C,K; vector<string> a;
const int dx[4]={-1,1,0,0},dy[4]={0,0,-1,1};
bool in(int x,int y){return x>=0&&x<R&&y>=0&&y<C;}
int good(int x,int y){
    if(a[x][y]!='.') return 0;
    int c=0; for(int d=0;d<4;d++){int u=x+dx[d],v=y+dy[d]; if(in(u,v)&&a[u][v]=='.') c++;}
    return c==K;
}
int main(){
    if(fopen("BANDO.INP","r")){freopen("BANDO.INP","r",stdin);freopen("BANDO.OUT","w",stdout);}
    int q; cin>>R>>C>>K>>q; a.resize(R);
    for(auto&s:a) cin>>s;
    long long cnt=0;
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) cnt+=good(i,j);
    printf("%lld\n",cnt);
    while(q--){
        int x,y; scanf("%d %d",&x,&y); x--; y--;
        vector<pair<int,int>> cells={{x,y}};
        for(int d=0;d<4;d++) if(in(x+dx[d],y+dy[d])) cells.push_back({x+dx[d],y+dy[d]});
        for(auto&c:cells) cnt-=good(c.first,c.second);
        a[x][y]=(a[x][y]=='.'?'#':'.');
        for(auto&c:cells) cnt+=good(c.first,c.second);
        printf("%lld\n",cnt);
    }
}
