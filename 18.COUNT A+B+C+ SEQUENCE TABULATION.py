def findcount(s):
    n=len(s)
    a=[0 for i in range(n)]
    ab=[0 for i in range(n)]
    abc=[0 for i in range(n)]


    for i in range(n):
        if s[i]=='a':
           if i==0:
               a[i]=1
           else:
               a[i]=2*a[i-1]+1
               ab[i]=ab[i-1]
               abc[i]=abc[i-1]

        elif s[i]=='b':
            if i>0:
                a[i]=a[i-1]
                ab[i]=2*ab[i-1]+a[i]
                abc[i]=abc[i-1]

        elif s[i]=='c':
            if i>0:
                a[i]=a[i-1]
                ab[i]=ab[i-1]
                abc[i]=2*abc[i-1]+ab[i]

    print(abc[n-1])

s='abcabc'
findcount(s)