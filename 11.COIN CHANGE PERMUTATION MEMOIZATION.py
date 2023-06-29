def coinchange(n,coins,dp):
    if n==0:
        return 1
    if dp[n]!=0:
        return dp[n]
    if n<0:
        return 0
    ans=0
    for i in range(len(coins)):
        ans+=coinchange(n-coins[i],coins,dp)
    dp[n]=ans
    return dp[n]

def findcoinchange(coins,n):
    dp=[0 for i in range(n+1)]
    dp[0]=1

    ans=coinchange(n,coins,dp)
    print(ans)

coins=[2,3,5]
findcoinchange(coins,7)