def findknapsack(wts,values,cap):
    dp=[[ 0 for j in range(cap+1)] for i in range(len(values)+1)]

    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):

            if j<wts[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-wts[i-1]]+values[i-1])
    print(dp[len(values)][cap])

wts=[2,5,1,3,4]
values=[15,14,10,45,30]

findknapsack(wts,values,7)