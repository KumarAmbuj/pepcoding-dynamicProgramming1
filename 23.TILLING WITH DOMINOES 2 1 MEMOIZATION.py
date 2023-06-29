def findcount(n,dp):
    if n==1:
        return 1
    if n==2:
        return 2

    if dp[n]!=0:
        return dp[n]

    ans=findcount(n-1,dp)+findcount(n-2,dp)
    dp[n]=ans
    return dp[n]

def findways(n):
    dp=[0 for i in range(n+1)]
    dp[1]=1
    dp[2]=2

    ans=findcount(n,dp)
    print(ans)

findways(5)