def findcoinchange(coins,n):

    dp=[0 for i in range(n+1)]
    dp[0]=1

    for coin in coins:
        for i in range(coin,len(dp)):
            dp[i]+=dp[i-coin]
    print(dp[n])

coins=[2,3,5]
n=10
findcoinchange(coins,n)