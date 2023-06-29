def findmaxmoves(jumps,n):
    dp=[0 for i in range(n+1)]

    dp[0]=0

    for i in range(1,len(dp)):
        mx=0

        for j in range(len(jumps)):

            if i-jumps[j]>=0:

                mx=max(mx,dp[i-jumps[j]])
        dp[i]=mx+1

    print(dp[n])

jumps=[1,2,3]
findmaxmoves(jumps,10)