def knapsack(cap,wts,value,dp):
    if cap==0:
        return 0

    if dp[cap]!=0:
        return dp[cap]
    mx=0
    for i in range(len(value)):
        if cap>=wts[i]:
            mx=max(mx,knapsack(cap-wts[i],wts,value,dp)+value[i])
    dp[cap]=mx
    return dp[cap]


def findknapsack(wts,value,cap):

    dp=[0 for i in range(cap+1)]

    ans=knapsack(cap,wts,value,dp)
    print(ans)

wts=[2,5,1,3,4]
values=[15,14,10,45,30]
findknapsack(wts,values,7)
