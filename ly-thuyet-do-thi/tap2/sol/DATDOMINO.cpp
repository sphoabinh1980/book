#include <bits/stdc++.h>
using namespace std;
// Hopcroft-Karp: ô trắng (i+j chẵn) bên trái, ô đen bên phải
int main(){
    if(fopen("DATDOMINO.INP","r")){freopen("DATDOMINO.INP","r",stdin);freopen("DATDOMINO.OUT","w",stdout);}
    int R,C; cin>>R>>C; vector<string> a(R); for(auto&s:a) cin>>s;
    int N=R*C; vector<vector<int>> g(N);
    const int dx[4]={-1,1,0,0},dy[4]={0,0,-1,1};
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) if(a[i][j]=='.'&&(i+j)%2==0)
        for(int d=0;d<4;d++){int u=i+dx[d],v=j+dy[d]; if(u>=0&&u<R&&v>=0&&v<C&&a[u][v]=='.') g[i*C+j].push_back(u*C+v);}
    vector<int> ml(N,-1),mr(N,-1),dist(N);
    auto bfs=[&](){queue<int> q; bool found=false;
        for(int u=0;u<N;u++){ if(ml[u]<0){dist[u]=0;q.push(u);} else dist[u]=-1; }
        while(!q.empty()){int u=q.front();q.pop(); for(int v:g[u]){int w=mr[v]; if(w<0) found=true; else if(dist[w]<0){dist[w]=dist[u]+1;q.push(w);}}}
        return found;};
    function<bool(int)> dfs=[&](int u){ for(int v:g[u]){int w=mr[v]; if(w<0||(dist[w]==dist[u]+1&&dfs(w))){ml[u]=v;mr[v]=u;return true;}} dist[u]=-1; return false;};
    int ans=0; while(bfs()) for(int u=0;u<N;u++) if(ml[u]<0&&!g[u].empty()&&dfs(u)) ans++;
    printf("%d\n",ans);
}
