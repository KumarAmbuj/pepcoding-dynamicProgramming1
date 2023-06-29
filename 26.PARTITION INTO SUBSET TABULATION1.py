def findways(n,k):
    dp=[[0 for i in range(n+1)] for j in range(k+1)]

    for i in range(1,len(dp)):
        for j in range(len(dp[0])):

            if i==1:
                dp[i][j]=1

            elif i==j:
                dp[i][j]=1

            elif i>j:
                dp[i][j]=0

            elif i<j:
                dp[i][j]=i*dp[i][j-1]+dp[i-1][j-1]

    print(dp[k][n])

findways(5,3)