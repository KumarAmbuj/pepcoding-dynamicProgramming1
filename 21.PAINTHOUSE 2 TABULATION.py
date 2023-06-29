def findminsum(arr):
    dp=[[0 for j in range(len(arr[0]))] for j in range(len(arr))]

    for i in range(len(arr[0])):
        dp[0][i]=arr[0][i]


    for i in range(1,len(arr)):
        for j in range(len(arr[0])):

            mn=99

            for k in range(len(dp[0])):

                if k==j:
                    continue
                mn=min(mn,dp[i-1][k])

            dp[i][j]=mn+arr[i][j]

    mn=99
    for i in range(len(dp[0])):
        mn=min(mn,dp[len(arr)-1][i])

    print(mn)

arr=[[1,5,7,2,1,4],
     [5,8,4,3,6,1],
     [3,2,4,7,2,3],
     [1,2,4,9,1,7]]
findminsum(arr)