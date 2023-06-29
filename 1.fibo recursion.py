def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1


    ans=fibo(n-1)+fibo(n-2)
    print(n,ans)
    return ans

def findfibo(n):



    ans=fibo(n)
    print(ans)

findfibo(6)


