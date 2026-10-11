#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("DOMINO.INP","r")){freopen("DOMINO.INP","r",stdin);freopen("DOMINO.OUT","w",stdout);}
    int n; scanf("%d",&n);
    vector<int> A(n+1),B(n+1); vector<vector<int>> g(7); vector<int> deg(7,0);
    for(int i=1;i<=n;i++){scanf("%d %d",&A[i],&B[i]);g[A[i]].push_back(i);g[B[i]].push_back(i);deg[A[i]]++;deg[B[i]]++;}
    int s=-1,odd=0; for(int v=0;v<7;v++) if(deg[v]%2){odd++; if(s<0) s=v;}
    if(odd!=0&&odd!=2){puts("NO");return 0;}
    if(s<0) s=A[1];
    vector<char> used(n+1,0); vector<int> it(7,0);
    vector<pair<int,int>> st={{s,0}}; vector<pair<int,int>> path; // (đỉnh, quân dùng để tới)
    while(!st.empty()){int u=st.back().first;
        while(it[u]<(int)g[u].size()&&used[g[u][it[u]]]) it[u]++;
        if(it[u]==(int)g[u].size()){path.push_back(st.back());st.pop_back();}
        else{int id=g[u][it[u]++];used[id]=1;int v=A[id]^B[id]^u;st.push_back({v,id});}
    }
    if((int)path.size()!=n+1){puts("NO");return 0;}
    reverse(path.begin(),path.end());
    for(int i=1;i<=n;i++){int from=path[i-1].first,id=path[i].second; printf("%d %c\n",id,A[id]==from?'+':'-');}
}
