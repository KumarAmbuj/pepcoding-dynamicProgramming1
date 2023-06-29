def findknapsack(values,wts,cap):
    dp=[[0 for j in range(cap+1)] for i in range(len(wts)+1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):

            if i==0 and j==0:
                dp[i][j]=0
            elif i==0:
                dp[i][j]=0
            elif j==0:
                dp[i][j]=0
            else:
                if j<wts[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-wts[i-1]]+values[i-1])
    print(dp[len(values)][cap])

wts=[2,5,1,3,4]
values=[15,14,10,45,30]
findknapsack(values,wts,7)
