def findminmoves(jumps,n):
    dp=[0 for i in range(n+1)]

    dp[0]=0

    for i in range(1,len(dp)):
        mn=99

        for j in range(len(jumps)):
            if i-jumps[j]>=0:
                mn=min(mn,dp[i-jumps[j]])

        dp[i]=mn+1
    print(dp[n])

jumps=[1,2,3]
n=10
findminmoves(jumps,n)