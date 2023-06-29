def fibo(n,dp):
    if n==0:
        return 0
    if n==1:
        return 1
    if dp[n]!=0:
        return dp[n]

    ans=fibo(n-1,dp)+fibo(n-2,dp)
    print(n,ans)
    dp[n]=ans
    return ans

def findfibo(n):

    dp=[0 for i in range(n+1)]
    dp[0]=0
    dp[1]=1

    ans=fibo(n,dp)
    print(ans)

findfibo(6)


