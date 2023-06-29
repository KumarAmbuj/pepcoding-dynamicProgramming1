def findways(n,m):
    dp=[0 for i in range(n+1)]
    dp[1]=1
    for i in range(2,len(dp)):
        if i<m:
            dp[i]=1
        elif i==m:
            dp[i]=2
        else:
            dp[i]=dp[i-1]+dp[i-m]
    print(dp[n])

findways(5,3)