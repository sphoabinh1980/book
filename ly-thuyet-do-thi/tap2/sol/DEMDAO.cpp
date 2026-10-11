#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("DEMDAO.INP","r")){freopen("DEMDAO.INP","r",stdin);freopen("DEMDAO.OUT","w",stdout);}
    int R,C; cin>>R>>C; vector<string> a(R); for(auto&s:a) cin>>s;
    const int dx[4]={-1,1,0,0},dy[4]={0,0,-1,1};
    int cnt=0,best=0; vector<pair<int,int>> st;
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) if(a[i][j]=='#'){
        cnt++; int area=0; a[i][j]='x'; st.push_back({i,j});
        while(!st.empty()){
            auto [x,y]=st.back(); st.pop_back(); area++;
            for(int d=0;d<4;d++){int u=x+dx[d],v=y+dy[d];
                if(u>=0&&u<R&&v>=0&&v<C&&a[u][v]=='#'){a[u][v]='x';st.push_back({u,v});}}
        }
        best=max(best,area);
    }
    printf("%d %d\n",cnt,best);
}
