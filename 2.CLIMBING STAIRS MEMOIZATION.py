def findtotalways(n,jumps,dp):
    if n==0:
        return 1
    if n<0:
        return 0

    if dp[n]!=0:
        return dp[n]

    ans=0

    for j in range(len(jumps)):
        ans+=findtotalways(n-jumps[j],jumps,dp)

    dp[n]=ans
    return ans

def findways(jumps,n):
    dp=[0 for i in range(n+1)]
    dp[0]=1
    ans=findtotalways(n,jumps,dp)

    print(ans)

jumps=[1,2,3]
n=6
findways(jumps,n)