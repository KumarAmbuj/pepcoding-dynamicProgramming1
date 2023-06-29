def mincoinchange(n,coins,dp):
    if n==0:
        return 0
    
    if dp[n]!=0:
        return dp[n]

    mn=99

    for coin in coins:
        if coin<=n:
            mn=min(mn,mincoinchange(n-coin,coins,dp))
    dp[n]=mn+1
    return dp[n]

def findmincoin(coins,n):
    dp=[0 for i in range(n+1)]

    ans=mincoinchange(n,coins,dp)
    print(ans)

coins=[2,3,5]

findmincoin(coins,111)