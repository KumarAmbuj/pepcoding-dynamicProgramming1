def findminchange(n,coins,dp):
    if n==0:
        return 0
    if n<0:
        return 99
    if dp[n]!=0:
        return dp[n]
    mn=99
    for coin in coins:
        mn=min(mn,findminchange(n-coin,coins,dp))
    dp[n]=mn+1
    return dp[n]


def findcoinchange(coins,n):
    dp=[0 for i in range(n+1)]

    ans=findminchange(n,coins,dp)
    print(ans)

coins=[2,3,5]
findcoinchange(coins,111)