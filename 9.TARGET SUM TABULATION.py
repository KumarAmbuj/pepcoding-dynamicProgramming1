def targetsum(arr,target):
    dp=[[False for j in range(target+1)] for i in range(len(arr)+1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):

            if i==0 and j==0:
                dp[i][j]=True
            elif i==0:
                dp[i][j]=False
            elif j==0:
                dp[i][j]=True

            else:
                if j<arr[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]

    print(dp[len(arr)][target])

arr=[4,2,7,1,3]
target=10
targetsum(arr,target)