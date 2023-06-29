def mincost(i,j,arr,m,n,dp):
    if dp[i][j]!=0:
        return dp[i][j]

    if i==m-1:
        dp[i][j]=mincost(i,j+1,arr,m,n,dp)+arr[i][j]
    elif j==n-1:
        dp[i][j]=mincost(i+1,j,arr,m,n,dp)+arr[i][j]

    else:
        dp[i][j]=min(mincost(i+1,j,arr,m,n,dp),mincost(i,j+1,arr,m,n,dp))+arr[i][j]


    return dp[i][j]



def findmincost(arr):
    m=len(arr)
    n=len(arr[0])

    dp=[[0 for j in range(n)] for i in range(m)]

    dp[m-1][n-1]=arr[m-1][n-1]


    ans=mincost(0,0,arr,m,n,dp)
    print(ans)

arr=[[3,4,0,6],
     [7,2,4,6],
     [3,1,2,7],
     [5,9,8,2]]

findmincost(arr)

arr=[[2,8,4,1,6,4,2],
     [6,0,9,5,3,8,5],
     [1,4,3,4,0,6,5],
     [6,4,7,3,4,6,1],
     [1,0,3,7,1,2,7],
     [1,5,3,2,3,0,9],
     [2,2,5,1,9,8,2]]

findmincost(arr)
