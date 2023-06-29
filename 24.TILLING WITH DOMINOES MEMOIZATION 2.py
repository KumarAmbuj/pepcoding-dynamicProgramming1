def findcount(n,m,dp):
    if n<m:
        return 1
    if n==m:
        return 2

    if dp[n]!=0:
        return dp[n]
    ans=0
    if n<=m:
        ans=findcount(n-1,m,dp)
    else:
        ans=findcount(n-1,m,dp)+findcount(n-m,m,dp)
    dp[n]=ans
    return dp[n]


def findways(n,m):
    dp=[0 for i in range(n+1)]

    ans = findcount(n,m,dp)
    print(ans)

findways(5,3)