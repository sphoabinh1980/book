#include <bits/stdc++.h>
using namespace std;
int main(){
    if(fopen("BATTAY.INP","r")){freopen("BATTAY.INP","r",stdin);freopen("BATTAY.OUT","w",stdout);}
    int n; scanf("%d",&n);
    long long s=0,mx=0;
    for(int i=0;i<n;i++){long long d;scanf("%lld",&d);s+=d;mx=max(mx,d);}
    if(s%2!=0||mx>s-mx) printf("-1\n"); else printf("%lld\n",s/2);
}
