def findways(jumps,n):
    dp=[0 for i in range(n+1)]
    dp[0]=1

    for i in range(1,n+1):
        ans=0

        for j in range(len(jumps)):
            if jumps[j]<=i:
                ans+=dp[i-jumps[j]]
        dp[i]=ans
    print(dp[n])
jumps=[1,2,3]
n=6
findways(jumps,n)