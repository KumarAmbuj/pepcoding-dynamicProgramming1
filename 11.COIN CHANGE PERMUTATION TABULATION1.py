def findcoinchange(coins,n):
    dp=[0 for i in range(n+1)]
    dp[0]=1

    for i in range(1,len(dp)):
        ans=0

        for coin in coins:

            if i>=coin:
                ans+=dp[i-coin]
        dp[i]=ans

    print(dp[n])

coins=[2,3,5]
findcoinchange(coins,10)

coins=[2,3,5]
findcoinchange(coins,7)