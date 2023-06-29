def findmoves(n,jumps,dp):
    if n==0:
        return 0
    if n<0:
        return 999
    if dp[n]!=0:
        return dp[n]

    mn=99

    for j in range(len(jumps)):
        mn=min(mn,findmoves(n-jumps[j],jumps,dp))

    dp[n]=mn+1
    return dp[n]


def findminmoves(jumps,n):
    dp=[0 for i in  range(n+1)]

    ans=findmoves(n,jumps,dp)

    print(ans)
jumps=[1,2,3]
n=10
findminmoves(jumps,n)