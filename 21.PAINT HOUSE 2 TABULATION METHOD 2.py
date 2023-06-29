def findminsum(arr):
    dp=[[0 for j in range(len(arr[0]))] for i in range(len(arr))]

    fmin=99
    smin=99

    for i in range(len(arr[0])):
        dp[0][i]=arr[0][i]

        if dp[0][i]<=fmin:
            smin=fmin
            fmin=dp[0][i]
        elif dp[0][i]<smin:
            smin=dp[0][i]

    for i in range(1,len(arr)):
        nfmin=99
        nsmin=99
        for j in range(len(arr[0])):

            if dp[i-1][j]==fmin:
                dp[i][j]=smin+arr[i][j]
            else:
                dp[i][j]=fmin+arr[i][j]

            if dp[i][j]<=nfmin:
                nsmin=nfmin
                nfmin=dp[i][j]

            elif dp[i][j]<smin:
                nsmin=dp[i][j]
        fmin=nfmin
        smin=nsmin
    print(fmin)

    for i in range(len(dp)):
        print(dp[i])

arr=[[1,5,7,2,1,4],
     [5,8,4,3,6,1],
     [3,2,4,7,2,3],
     [1,2,4,9,1,7]]
findminsum(arr)




