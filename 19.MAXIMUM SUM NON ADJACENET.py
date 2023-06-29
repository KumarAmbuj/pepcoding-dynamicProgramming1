def findmaxsum(arr):
    inc=[0 for i in range(len(arr))]
    exc=[0 for i in range(len(arr))]

    inc[0]=arr[0]
    for i in range(1,len(arr)):
        inc[i]=exc[i-1]+arr[i]
        exc[i]=max(inc[i-1],exc[i-1])

    ans=max(inc[len(arr)-1],exc[len(arr)-1])

    print(ans)

arr=[5,10,10,100,5,6]
findmaxsum(arr)