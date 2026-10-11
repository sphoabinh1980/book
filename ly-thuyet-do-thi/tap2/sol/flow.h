// Dinic, cạnh 2i là cạnh xuôi, 2i+1 là cạnh ngược
struct Dinic{
    struct E{int to; long long cap;};
    int n; std::vector<E> e; std::vector<std::vector<int>> g; std::vector<int> lv,it;
    Dinic(int n):n(n),g(n+1),lv(n+1),it(n+1){}
    int add(int u,int v,long long c){e.push_back({v,c});g[u].push_back(e.size()-1);e.push_back({u,0});g[v].push_back(e.size()-1);return e.size()-2;}
    bool bfs(int s,int t){std::fill(lv.begin(),lv.end(),-1);lv[s]=0;std::queue<int> q;q.push(s);
        while(!q.empty()){int u=q.front();q.pop();for(int id:g[u]) if(e[id].cap>0&&lv[e[id].to]<0){lv[e[id].to]=lv[u]+1;q.push(e[id].to);}}
        return lv[t]>=0;}
    long long dfs(int u,int t,long long f){ if(u==t) return f;
        for(int&i=it[u];i<(int)g[u].size();i++){int id=g[u][i],v=e[id].to;
            if(e[id].cap>0&&lv[v]==lv[u]+1){long long d=dfs(v,t,std::min(f,e[id].cap)); if(d>0){e[id].cap-=d;e[id^1].cap+=d;return d;}}}
        return 0;}
    long long maxflow(int s,int t){long long F=0; while(bfs(s,t)){std::fill(it.begin(),it.end(),0); while(long long f=dfs(s,t,LLONG_MAX)) F+=f;} return F;}
};
