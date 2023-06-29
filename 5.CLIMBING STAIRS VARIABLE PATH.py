def findtotalmoves(jumps,n):
    dp=[None for i in range(n+1)]

    dp[n]=1


    for i in range(n-1,-1,-1):
        ans=0

        for j in range(1,jumps[i]+1):

            if i+j<len(dp):

                if dp[i+j]!=None:
                    ans+=dp[i+j]

        if ans!=0:
            dp[i]=ans
    print(dp[0])

jumps=[3,3,0,2,2,3,0]
n=6
findtotalmoves(jumps,n)
