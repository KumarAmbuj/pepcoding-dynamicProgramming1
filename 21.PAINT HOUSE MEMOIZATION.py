def minsum(i,j,arr,dp):
    if i==0:
        return arr[0][j]

    if dp[i][j]!=0:
        return dp[i][j]
    mn=99
    for k in range(len(dp[0])):
        if j==k:
            continue
        mn=min(mn,minsum(i-1,k,arr,dp))
    dp[i][j]=mn+arr[i][j]
    return dp[i][j]


def findminsum(arr):
    dp=[[0 for j in range(len(arr[0]))] for i in range(len(arr))]
    n=len(arr)
    mn=99

    for i in range(len(dp[0])):
        dp[0][i]=arr[0][i]


    for i in range(len(arr[0])):
        mn=min(mn,minsum(n-1,i,arr,dp))
    print(mn)
    for i in range(len(dp)):
        print(dp[i])
arr=[[1,5,7,2,1,4],
     [5,8,4,3,6,1],
     [3,2,4,7,2,3],
     [1,2,4,9,1,7]]
findminsum(arr)