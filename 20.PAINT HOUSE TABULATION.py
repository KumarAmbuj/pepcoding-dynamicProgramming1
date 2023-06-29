def findminsum(arr):
    n=len(arr)
    dp=[[0 for j in range(3)] for i in range(n)]

    dp[0][0]=arr[0][0]
    dp[0][1]=arr[0][1]
    dp[0][2]=arr[0][2]

    for i in range(1,len(arr)):
        dp[i][0]=min(dp[i-1][1],dp[i-1][2])+arr[i][0]
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])+arr[i][1]
        dp[i][2]=min(dp[i-1][0],dp[i-1][1])+arr[i][2]

    ans=min(dp[n-1][0],dp[n-1][1],dp[n-1][2])
    print(ans)
    
arr=[[1,5,7],
     [5,8,4],
     [3,2,9],
     [1,2,4]]
findminsum(arr)