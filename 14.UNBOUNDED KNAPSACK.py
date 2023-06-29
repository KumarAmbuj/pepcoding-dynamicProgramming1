def findknapsack(wts,value,cap):
    dp=[0 for i in range(cap+1)]

    for i in range(1,len(dp)):
        mx=0
        for j in range(len(value)):

            if i>=wts[j]:

                if mx<dp[i-wts[j]]+value[j]:
                    mx=dp[i-wts[j]]+value[j]
        dp[i]=mx

    print(dp[cap])

wts=[2,5,1,3,4]
values=[15,14,10,45,30]
findknapsack(wts,values,7)
