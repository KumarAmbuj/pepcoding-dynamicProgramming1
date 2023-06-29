def findmax(i,j,arr,m,n,dp):
    if j==n-1:
        dp[i][j]=arr[i][j]
        return dp[i][j]
    if dp[i][j]!=0:
        return dp[i][j]

    if i==0:
        dp[i][j]=max(findmax(i,j+1,arr,m,n,dp),findmax(i+1,j+1,arr,m,n,dp))+arr[i][j]

    elif i==m-1:
        dp[i][j]=max(findmax(i-1,j+1,arr,m,n,dp),findmax(i,j+1,arr,m,n,dp))+arr[i][j]

    else:
        dp[i][j]=max(findmax(i-1,j+1,arr,m,n,dp),findmax(i,j+1,arr,m,n,dp),findmax(i+1,j+1,arr,m,n,dp))+arr[i][j]

    return dp[i][j]


def fun(arr):
    m=len(arr)
    n=len(arr[0])

    dp=[[0 for j in range(n)] for i in range(n)]

    ans=0
    for i in range(m):
        ans=max(ans,findmax(i,0,arr,m,n,dp))
    print(ans)

arr=[[0,1,4,2,8,2],
     [4,3,6,5,0,4],
     [1,2,4,1,4,6],
     [2,0,7,3,2,2],
     [3,1,5,9,2,4],
     [2,7,0,8,5,1]]

fun(arr)