#include <bits/stdc++.h>
#define ll long long
using namespace std;
int m,u,r;
int v[200],t[200],f[200];
int dp[200][400][200];
int main()
{
    freopen("CAU4.INP","r",stdin);
    freopen("CAU4.OUT","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin>>m>>u>>r;
    for (int i=1;i<=r;i++)
    {
        cin>>v[i]>>t[i]>>f[i];
    }
    for (int i=1;i<=r;i++) dp[i][0][0]=0;
    for (int i=1;i<=m;i++) dp[0][i][0]=0;
    for (int i=1;i<=u;i++) dp[0][0][i]=0;
    for (int i=1;i<=r;i++)
        for (int j=1;j<=m;j++)
            for (int k=1;k<=u;k++)
    {
        if (j<t[i]) dp[i][j][k]=dp[i-1][j][k];
        else if (k<f[i]) dp[i][j][k]=dp[i-1][j][k];
        else dp[i][j][k]=max(dp[i-1][j][k],dp[i-1][j-t[i]][k-f[i]] + v[i]);
    }
    cout<<dp[r][m][u];
}
