def findcount(n,k,dp):
    if k==1:
        return 1
    if n==k:
        return 1
    if k>n:
        return 0
    if dp[k][n]!=0:
        return dp[k][n]

    ans=k*findcount(n-1,k,dp)+findcount(n-1,k-1,dp)

    dp[k][n]=ans
    return dp[k][n]

def findways(n,k):
    dp=[[0 for i in range(n+1)] for j in range(k+1)]

    ans=findcount(n,k,dp)
    for i in range(len(dp)):
        print(dp[i])
    print(ans)

findways(5,3)