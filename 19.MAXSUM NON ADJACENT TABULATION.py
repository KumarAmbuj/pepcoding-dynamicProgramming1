def findmaxsum(arr):
    inc=arr[0]
    exc=0

    for i in range(1,len(arr)):
        ninc=exc+arr[i]
        nexc=max(inc,exc)

        inc=ninc
        exc=nexc

    ans=max(inc,exc)
    print(ans)

arr=[5,10,10,100,5,6]
findmaxsum(arr)