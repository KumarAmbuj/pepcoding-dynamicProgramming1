def findmoves(n,jumps,dp):
    if n==0:
        return 0
    if n<0:
        return -10
    if dp[n]!=0:
        return dp[n]

    mx=0
    for j in range(len(jumps)):
        mx=max(mx,findmoves(n-jumps[j],jumps,dp))
    dp[n]=mx+1
    return dp[n]

def findmaxmoves(jumps,n):
    dp=[0 for i in range(n+1)]
    dp[0]=0

    ans=findmoves(n,jumps,dp)
    print(ans)


jumps=[1,2,3]
findmaxmoves(jumps,10)