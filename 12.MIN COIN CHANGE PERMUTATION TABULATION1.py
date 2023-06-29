def findminchange(coins,n):
    dp=[0 for i in range(n+1)]

    for i in range(1,len(dp)):
        mn=99
        for j in range(len(coins)):

            if i>=coins[j]:
                mn=min(mn,dp[i-coins[j]])
        dp[i]=mn+1

    print(dp[n])

coins=[2,3,5]
findminchange(coins,11)