// Tarjan không đệ quy: trả về comp[v] (đánh số theo thứ tự tô pô ngược) và số thành phần
inline int tarjan(int n,const std::vector<std::vector<int>>&g,std::vector<int>&comp){
    std::vector<int> num(n+1,0),low(n+1,0),it(n+1,0),stk; std::vector<char> on(n+1,0);
    comp.assign(n+1,-1); int timer=0,c=0;
    for(int s=1;s<=n;s++) if(!num[s]){
        std::vector<int> cs={s}; num[s]=low[s]=++timer; stk.push_back(s); on[s]=1;
        while(!cs.empty()){int u=cs.back();
            if(it[u]<(int)g[u].size()){int v=g[u][it[u]++];
                if(!num[v]){num[v]=low[v]=++timer;stk.push_back(v);on[v]=1;cs.push_back(v);}
                else if(on[v]) low[u]=std::min(low[u],num[v]);}
            else {cs.pop_back(); if(!cs.empty()) low[cs.back()]=std::min(low[cs.back()],low[u]);
                if(low[u]==num[u]){while(true){int w=stk.back();stk.pop_back();on[w]=0;comp[w]=c;if(w==u)break;} c++;}}
        }
    }
    return c;
}
