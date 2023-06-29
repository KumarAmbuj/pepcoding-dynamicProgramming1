def findmoves(i,jumps,n,dp):
    if i==n:
        return 0
    if i>n:
        return 99
    if dp[i]!=0:
        return dp[i]
    mn=99
    for j in range(1,jumps[i]+1):

        k=findmoves(i+j,jumps,n,dp)

        if k!=None:

            mn=min(mn,k)
    if mn!=99:
        dp[i]=mn+1
    else:
        dp[i]=None
    return dp[i]



def findminmoves(jumps,n):
    dp=[0 for i in range(n+1)]
    dp[n]=0

    ans=findmoves(0,jumps,n,dp)

    print(ans)

jumps=[3,3,0,2,2,3,0]
n=6
findminmoves(jumps,n)

jumps=[3,2,4,2,0,2,3,1,2,2]
n=10
findminmoves(jumps,n)