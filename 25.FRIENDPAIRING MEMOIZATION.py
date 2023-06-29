def findpairing(n,dp):
    if n==1:
        return 1
    if n==2:
        return 2

    if dp[n]!=0:
        return dp[n]

    ans=findpairing(n-1,dp)+(n-1)*findpairing(n-2,dp)
    dp[n]=ans
    return dp[n]

def friendpairing(n):
    dp=[0 for i in range(n+1)]

    ans=findpairing(n,dp)
    print(ans)

friendpairing(4)

