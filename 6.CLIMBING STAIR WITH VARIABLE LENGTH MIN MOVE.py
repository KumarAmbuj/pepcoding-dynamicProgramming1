def findminmoves(jumps,n):
    dp=[None for i in range(n+1)]
    dp[n]=0
    for i in range(n-1,-1,-1):
        mn=999
        for j in range(1,jumps[i]+1):

            if i+j<len(dp):

                if dp[i+j]!=None:

                    mn=min(mn,dp[i+j])
        if mn!=999:
            dp[i]=mn+1
        else:
            dp[i]=None
    print(dp[0])

jumps=[3,3,0,2,2,3,0]
n=6
findminmoves(jumps,n)

jumps=[3,2,4,2,0,2,3,1,2,2]
n=10
findminmoves(jumps,n)