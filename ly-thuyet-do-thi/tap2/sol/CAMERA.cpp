#include <bits/stdc++.h>
using namespace std;
int R,C; vector<vector<int>> g; vector<int> mr,ml,vis; int stamp=0;
bool kuhn(int u){ for(int v:g[u]) if(vis[v]!=stamp){vis[v]=stamp; if(!mr[v]||kuhn(mr[v])){mr[v]=u;ml[u]=v;return true;}} return false;}
int main(){
    if(fopen("CAMERA.INP","r")){freopen("CAMERA.INP","r",stdin);freopen("CAMERA.OUT","w",stdout);}
    int K; scanf("%d %d %d",&R,&C,&K); g.resize(R+1); mr.assign(C+1,0); ml.assign(R+1,0); vis.assign(C+1,0);
    for(int i=0;i<K;i++){int r,c;scanf("%d %d",&r,&c);g[r].push_back(c);}
    int t=0; for(int r=1;r<=R;r++){stamp++; if(kuhn(r)) t++;}
    // König: Z = các đỉnh tới được từ hàng chưa ghép theo đường đan xen
    vector<char> zr(R+1,0),zc(C+1,0); queue<int> q;
    for(int r=1;r<=R;r++) if(!ml[r]){zr[r]=1;q.push(r);}
    while(!q.empty()){int r=q.front();q.pop(); for(int c:g[r]) if(!zc[c]){zc[c]=1; int r2=mr[c]; if(r2&&!zr[r2]){zr[r2]=1;q.push(r2);}}}
    printf("%d\n",t);
    for(int r=1;r<=R;r++) if(!zr[r]) printf("H %d\n",r);
    for(int c=1;c<=C;c++) if(zc[c]) printf("C %d\n",c);
}
