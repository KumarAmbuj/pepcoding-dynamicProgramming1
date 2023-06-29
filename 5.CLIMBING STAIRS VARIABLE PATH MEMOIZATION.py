def findtotalmoves(i,jumps,n,dp):
    if i==n:
        return 1
    if i>n:
        return 0
    if dp[i]!=0:
        return dp[i]

    ans=0

    for j in range(1,jumps[i]+1):
        k=findtotalmoves(i+j,jumps,n,dp)
        if k!=None:
            ans+=k
    if ans!=0:
      dp[i]=ans
    else:
        dp[i]=None
    return dp[i]

def findtotal(jumps,n):
    dp=[0 for i in range(n+1)]
    dp[n]=1
    ans=findtotalmoves(0,jumps,n,dp)
    print(ans)
    print(dp)
jumps=[3,3,0,2,2,3,0]
n=6
findtotal(jumps,n)