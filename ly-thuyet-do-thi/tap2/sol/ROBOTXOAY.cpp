#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("ROBOTXOAY.INP","r")){freopen("ROBOTXOAY.INP","r",stdin);freopen("ROBOTXOAY.OUT","w",stdout);}
    int R,C; char h; cin>>R>>C>>h; vector<string> a(R); for(auto&s:a) cin>>s;
    const int dx[4]={-1,0,1,0},dy[4]={0,1,0,-1}; // N E S W
    string H="NESW";
    vector<int> d((size_t)R*C*4,INT_MAX);
    deque<array<int,3>> q;
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) if(a[i][j]=='S'){int k=H.find(h); d[(i*C+j)*4+k]=0; q.push_back({i,j,k});}
    while(!q.empty()){
        auto [x,y,k]=q.front(); q.pop_front(); int cur=d[(x*C+y)*4+k];
        if(a[x][y]=='T'){printf("%d\n",cur);return 0;}
        int u=x+dx[k],v=y+dy[k];
        if(u>=0&&u<R&&v>=0&&v<C&&a[u][v]!='#'&&d[(u*C+v)*4+k]>cur){d[(u*C+v)*4+k]=cur;q.push_front({u,v,k});}
        for(int t:{(k+1)%4,(k+3)%4}) if(d[(x*C+y)*4+t]>cur+1){d[(x*C+y)*4+t]=cur+1;q.push_back({x,y,t});}
    }
    printf("-1\n");
}
