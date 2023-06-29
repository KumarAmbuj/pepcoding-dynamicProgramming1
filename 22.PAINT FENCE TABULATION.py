def findcount(n,k):
    same=[0 for i in range(n+1)]
    diff=[0 for i in range(n+1)]
    total=[0 for i in range(n+1)]
    
    same[2]=k
    diff[2]=k*(k-1)
    total[2]=same[2]+diff[2]

    for i in range(3,n+1):
        same[i]=diff[i-1]
        diff[i]=total[i-1]*(k-1)
        total[i]=same[i]+diff[i]

    print(total[n])
findcount(5,3)