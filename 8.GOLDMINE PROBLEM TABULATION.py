def findmax(arr):
    m=len(arr)
    n=len(arr[0])

    dp=[[0 for j in range(n)] for i in range(m)]

    for i in range(m):
        dp[i][n-1]=arr[i][n-1]

    for j in range(n-2,-1,-1):
        for i in range(0,m):

            if i==0:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j+1])+arr[i][j]


            elif i==m-1:
                dp[i][j]=max(dp[i-1][j],dp[i][j+1])+arr[i][j]
            else:
                dp[i][j]=max(dp[i-1][j+1],dp[i][j+1],dp[i+1][j])+arr[i][j]

    ans=0
    for i in range(m):
        ans=max(ans,dp[i][0])
    print(ans)


arr=[[0,1,4,2,8,2],
     [4,3,6,5,0,4],
     [1,2,4,1,4,6],
     [2,0,7,3,2,2],
     [3,1,5,9,2,4],
     [2,7,0,8,5,1]]

findmax(arr)