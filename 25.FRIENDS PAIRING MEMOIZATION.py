def friendpairing(n,dp):
    if n==1:
        return 1
    if n==2:
        return 2

    if dp[n]!=0:
        return dp[n]

    ans=friendpairing(n-1,dp)+(n-1)*friendpairing(n-2,dp)
    dp[n]=ans
    return dp[n]

def findpairing(n):
    dp=[0 for i in range(n+1)]

    ans=friendpairing(n,dp)
    print(ans)

findpairing(4)