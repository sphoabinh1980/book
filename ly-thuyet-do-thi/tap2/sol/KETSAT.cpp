#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("KETSAT.INP","r")){freopen("KETSAT.INP","r",stdin);freopen("KETSAT.OUT","w",stdout);}
    int b,k; scanf("%d %d",&b,&k);
    int N=1; for(int i=0;i<k-1;i++) N*=b;      // số đỉnh: các xâu độ dài k-1
    vector<int> ptr(N,0); vector<pair<int,int>> st={{0,-1}}; string out;
    while(!st.empty()){auto [u,c]=st.back();
        if(ptr[u]<b){int d=ptr[u]++; st.push_back({(int)(((long long)u*b+d)%N),d});}
        else{st.pop_back(); if(c>=0) out.push_back('0'+c);}
    }
    reverse(out.begin(),out.end());
    string ans=string(k-1,'0')+out;
    printf("%d\n%s\n",(int)ans.size(),ans.c_str());
}
