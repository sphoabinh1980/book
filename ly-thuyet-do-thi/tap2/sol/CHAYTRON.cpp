#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("CHAYTRON.INP","r")){freopen("CHAYTRON.INP","r",stdin);freopen("CHAYTRON.OUT","w",stdout);}
    int R,C; cin>>R>>C; vector<string> a(R); for(auto&s:a) cin>>s;
    const int INF=INT_MAX, dx[4]={-1,1,0,0},dy[4]={0,0,-1,1};
    vector<vector<int>> f(R,vector<int>(C,INF)),p(R,vector<int>(C,-1));
    deque<pair<int,int>> q;
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) if(a[i][j]=='F'){f[i][j]=0;q.push_back({i,j});}
    while(!q.empty()){auto [x,y]=q.front();q.pop_front();
        for(int d=0;d<4;d++){int u=x+dx[d],v=y+dy[d];
            if(u>=0&&u<R&&v>=0&&v<C&&a[u][v]!='#'&&f[u][v]==INF){f[u][v]=f[x][y]+1;q.push_back({u,v});}}}
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) if(a[i][j]=='J'){p[i][j]=0;q.push_back({i,j});}
    while(!q.empty()){auto [x,y]=q.front();q.pop_front();
        if(x==0||y==0||x==R-1||y==C-1){printf("%d\n",p[x][y]+1);return 0;}
        for(int d=0;d<4;d++){int u=x+dx[d],v=y+dy[d];
            if(a[u][v]!='#'&&p[u][v]<0&&f[u][v]>p[x][y]+1){p[u][v]=p[x][y]+1;q.push_back({u,v});}}}
    printf("-1\n");
}
