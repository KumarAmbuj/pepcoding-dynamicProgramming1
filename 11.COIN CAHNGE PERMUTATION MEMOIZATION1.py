def coinchange(n,coins,dp):
    if n==0:
        return 1
    if n<0:
        return 0
    if dp[n]!=0:
        return dp[n]

    ans=0
    for coin in coins:
        ans+=coinchange(n-coin,coins,dp)
    dp[n]=ans
    return dp[n]



def findcoinchange(coins,n):
    dp=[0 for i in range(n+1)]
    dp[0]=1

    ans=coinchange(n,coins,dp)

    print(ans)

coins=[2,3,5]
findcoinchange(coins,7)
findcoinchange(coins,10)