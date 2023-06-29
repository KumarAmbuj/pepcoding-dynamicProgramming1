def coinchange(coins,n):
    dp=[0 for i in range(n+1)]
    dp[0]=1

    for j in range(len(coins)):
        for i in range(coins[j],len(dp)):
            dp[i]=dp[i]+dp[i-coins[j]]
    print(dp[n])

coins=[2,3,5]
n=10
coinchange(coins,n)